from pathlib import Path
import csv
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
evaluation = json.loads((ROOT / 'evaluation.json').read_text())
skills = {s['id']: s for s in evaluation}
routing = json.loads((ROOT / 'workflow-routing.json').read_text())
alternatives = json.loads((ROOT / 'dropped-alternatives.json').read_text())

kept = {s['id'] for s in evaluation if s['decision'] == 'Keep'}
dropped = {s['id'] for s in evaluation if s['decision'] == 'Drop'}
assert len(routing) == len(kept) == 42
assert len(alternatives) == len(dropped) == 8
assert {r['id'] for r in routing} == kept
assert {a['dropped_id'] for a in alternatives} == dropped
for a in alternatives:
    assert set(a['replacement_ids']) <= kept
    assert all(a.get(k) for k in ['reason', 'use_instead', 'minimum_output', 'reconsider'])

def link(identifier):
    return f"[{skills[identifier]['skill']}][s{identifier}]"

def escape(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')

def resolve_ids(text):
    return re.sub(r'\b(0[1-9]|[1-4][0-9]|50)\b', lambda m: link(m.group(1)), text)

alt_table = [
    '| Dropped skill and trial | Why it was dropped | Retained alternative and expected output | When the original may be useful |',
    '|---|---|---|---|',
]
for a in alternatives:
    identifier = a['dropped_id']
    replacement_links = ', '.join(link(i) for i in a['replacement_ids'])
    replacement = f"{replacement_links}. {a['use_instead']} **Deliver:** {a['minimum_output']}"
    alt_table.append(f"| {link(identifier)} · [trial](results/{identifier}.md) | {escape(a['reason'])} | {escape(replacement)} | {escape(a['reconsider'])} |")

catalog = []
for stage in dict.fromkeys(r['stage'] for r in routing):
    catalog += [f'**{stage}**', '', '| Skill and trial | Use when | Produce | Handoff |', '|---|---|---|---|']
    for r in routing:
        if r['stage'] != stage:
            continue
        identifier = r['id']
        catalog.append(f"| {link(identifier)} · [trial](results/{identifier}.md) | {escape(r['trigger'])} | {escape(r['output'])} | {escape(resolve_ids(r['handoff']))} |")
    catalog.append('')

definitions = '\n'.join(f"[s{s['id']}]: {s['source_url']}" for s in evaluation)
template = (ROOT / 'workflow-overview.md').read_text()
report = (template.replace('{{ALTERNATIVES_TABLE}}', '\n'.join(alt_table))
          .replace('{{ROUTING_CATALOG}}', '\n'.join(catalog))
          .replace('{{SOURCE_DEFINITIONS}}', definitions))
assert '{{' not in report
used = set(re.findall(r'\]\[s(\d{2})\]', report))
defined = set(re.findall(r'^\[s(\d{2})\]:', report, re.M))
assert used == defined == set(skills)
for target in re.findall(r'\]\(([^)]+)\)', report):
    if not target.startswith(('http:', 'https:', '#')):
        assert (ROOT / target.split('#')[0]).is_file(), target
assert all((ROOT / s['result_path']).is_file() for s in evaluation)

(ROOT / 'WORKFLOW-REPORT.md').write_text(report)
diagram = re.search(r'```mermaid\n(.*?)\n```', report, re.S).group(1)
(ROOT / 'skill-workflow.mmd').write_text(diagram + '\n')

routing_csv = []
for r in routing:
    skill = skills[r['id']]
    resolved_handoff = re.sub(r'\b(0[1-9]|[1-4][0-9]|50)\b', lambda m: skills[m.group(1)]['skill'], r['handoff'])
    routing_csv.append({
        'id': r['id'], 'stage': r['stage'], 'skill': skill['skill'],
        'trigger': r['trigger'], 'required_output': r['output'], 'handoff': resolved_handoff,
        'source_url': skill['source_url'], 'trial_evidence': skill['result_path'],
    })
alternative_csv = []
for a in alternatives:
    identifier = a['dropped_id']
    alternative_csv.append({
        'dropped_skill': skills[identifier]['skill'], 'reason': a['reason'],
        'replacement_skills': '; '.join(skills[i]['skill'] for i in a['replacement_ids']),
        'how_to_use_alternatives': a['use_instead'], 'minimum_output': a['minimum_output'],
        'when_to_reconsider_original': a['reconsider'], 'trial_evidence': skills[identifier]['result_path'],
    })
for filename, rows in [('workflow-routing.csv', routing_csv), ('dropped-alternatives.csv', alternative_csv)]:
    with (ROOT / filename).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

bundle = ROOT / 'staff-engineer-workflow-report.zip'
with zipfile.ZipFile(bundle, 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in ['WORKFLOW-REPORT.md', 'workflow-routing.csv', 'dropped-alternatives.csv',
                 'workflow-routing.json', 'dropped-alternatives.json', 'skill-workflow.mmd',
                 'REPORT.md', 'METHOD.md', 'manifest.json', 'judgments.json', 'evaluation.json',
                 'staff-engineer-skills-evidence.zip']:
        archive.write(ROOT / name, name)
    for folder in ['results', 'trials']:
        for path in sorted((ROOT / folder).iterdir()):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT))
with zipfile.ZipFile(bundle) as archive:
    assert archive.testzip() is None

print(json.dumps({
    'report': str(ROOT / 'WORKFLOW-REPORT.md'), 'retained_skills_routed': len(routing),
    'dropped_skills_with_alternatives': len(alternatives), 'source_links_checked': len(defined),
    'report_words_approx': len(report.split()), 'bundle_bytes': bundle.stat().st_size,
    'validation': 'All retained/dropped coverage, retained-only replacements, evidence paths, reference links and ZIP integrity passed.'
}, indent=2))
