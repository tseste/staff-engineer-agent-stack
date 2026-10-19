from pathlib import Path
import csv
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'manifest.json').read_text())
judgments = {j['id']: j for j in json.loads((ROOT / 'judgments.json').read_text())}
fields = {j['id']: j for j in json.loads((ROOT / 'table-fields.json').read_text())}
assert len(manifest) == len(judgments) == len(fields) == 50
expected_ids = {f'{i:02}' for i in range(1, 51)}
assert {s['id'] for s in manifest} == set(judgments) == set(fields) == expected_ids
rows, integrity = [], []
for skill in manifest:
    identifier = skill['id']
    result = ROOT / 'results' / f'{identifier}.md'
    trial = ROOT / 'trials' / f'{identifier}.json'
    # Historical trial paths are preserved in the evidence manifest.
    source = ROOT / Path(skill['skill_path']).relative_to('/workspace/staff-skills')
    assert result.is_file() and len(result.read_text()) > 500, identifier
    assert trial.is_file() and source.is_file(), identifier
    judgment = judgments[identifier]
    assert len(judgment['scores']) == 5
    assert all(type(n) is int and 0 <= n <= 2 for n in judgment['scores'])
    score = sum(judgment['scores'])
    if judgment['decision'] == 'Keep':
        assert score >= 8
    rows.append({
        'id': identifier, 'skill': skill['name'], 'decision': judgment['decision'],
        'what_it_does': fields[identifier]['does'], 'how_it_helps': fields[identifier]['helps'],
        'score_out_of_10': score, 'reason': judgment['reason'],
        'trial_evidence': judgment['evidence'], 'drop_type': judgment.get('drop_type', ''),
        'source_url': skill['url'], 'source_commit': skill['commit'],
        'result_path': f'results/{identifier}.md', 'scenario_path': f'trials/{identifier}.json',
    })
    integrity.append({'id': identifier, **{
        label: hashlib.sha256(path.read_bytes()).hexdigest()
        for label, path in [('skill_sha256', source), ('scenario_sha256', trial), ('result_sha256', result)]
    }})

kept = [r for r in rows if r['decision'] == 'Keep']
dropped = [r for r in rows if r['decision'] == 'Drop']
assert len(kept) + len(dropped) == 50
with (ROOT / 'staff-engineer-skills.csv').open('w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
(ROOT / 'evaluation.json').write_text(json.dumps(rows, indent=2) + '\n')
(ROOT / 'artifact-hashes.json').write_text(json.dumps(integrity, indent=2) + '\n')

def escape(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')

report = [
    '# Staff engineer skill evaluation', '',
    f'**50 candidates evaluated; {len(kept)} kept, {len(dropped)} dropped.** Sources were pinned on 2026-10-18; evaluation completed on 2026-10-19.', '',
    'Each candidate received a fresh subagent with no inherited conversation, the original SKILL.md and local references, and one prewritten scenario. The parent reviewed the actual work product against prewritten expectations. Trial agents were instructed not to read grading criteria or other results.', '',
    '**Selection rule:** Score decision quality, evidence/uncertainty, tradeoffs/risk, concrete action, and proportionality from 0–2 each. Keep requires at least 8/10, no critical scenario omission, and distinct value in a general staff-engineer toolkit. Scores are subjective screening judgments. A passing result can still be dropped for redundancy or specialist-only scope.', '',
    '**Limits:** One qualitative scenario per skill, one parent evaluator, no no-skill baseline or statistical test, and no production implementation. These trials do not establish causal improvement over the underlying model, general effectiveness, or package security. Cases intentionally include situations where the right action is to avoid using a pattern. The readiness package lost on proportionality; the other drops concern core-toolkit fit or limited demonstrated added value, not demonstrated technical failure.', '',
    '**Persistence:** Kept means saved in this shortlist for selective use. No global installation, agent configuration change, or permanent behavioral change was performed. Interrupted agents with a complete saved work product were evaluated from that artifact; the missing trials were rerun in fresh agents.', '',
    '**Recommended starting set:** software-architecture, programming-principles, implementation-planning, product-shaping, systematic-debugging, verification-before-completion, receiving-code-review, and site-reliability-engineering.', '',
    '| # | Skill source | Decision | What it does | How it helps / trial finding |',
    '|---|---|---|---|---|',
]
for row in rows:
    report.append(f"| {row['id']} | [{row['skill']}]({row['source_url']}) | {row['decision']} | {escape(row['what_it_does'])} | {escape(row['how_it_helps'])} |")
report += ['', '## Evaluation evidence', '',
           'The linked work products contain the actual subagent responses, including assumptions, proposed checks, and limitations. Neither proposed tests nor scenario calculations are claims of production execution.', '',
           '| # | Skill | Score | Judgment | Evidence |', '|---|---|---|---|---|']
for row in rows:
    report.append(f"| {row['id']} | {row['skill']} | {row['score_out_of_10']}/10 | {escape(row['reason'])} | [{escape(row['trial_evidence'])}]({row['result_path']}) · [Scenario]({row['scenario_path']}) |")
report += ['', '## Source snapshots', '']
seen = set()
for skill in manifest:
    if skill['repository'] not in seen:
        seen.add(skill['repository'])
        report.append(f"- [{skill['repository']}](https://github.com/{skill['repository']}/tree/{skill['commit']}): `{skill['commit']}`")
report += ['', 'The manifest preserves source paths and prewritten expected behaviors. artifact-hashes.json records each skill, scenario, and work-product SHA-256 digest. Third-party source packages are not included in the evidence ZIP; source links identify the evaluated versions.', '']
(ROOT / 'REPORT.md').write_text('\n'.join(report))

shortlist = ['# Retained staff engineer skills', '',
             '42 selectively useful skills retained after scenario screening. This is an index, not an installation or unconditional activation policy.', '']
for row in kept:
    shortlist.append(f"- [{row['skill']}]({row['source_url']}): {row['what_it_does']} [Trial]({row['result_path']}).")
(ROOT / 'KEPT.md').write_text('\n'.join(shortlist) + '\n')

with zipfile.ZipFile(ROOT / 'staff-engineer-skills-evidence.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in ['REPORT.md', 'KEPT.md', 'METHOD.md', 'manifest.json', 'judgments.json',
                 'table-fields.json', 'evaluation.json', 'artifact-hashes.json', 'staff-engineer-skills.csv']:
        archive.write(ROOT / name, name)
    for folder in ['trials', 'results']:
        for path in sorted((ROOT / folder).iterdir()):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT))

print(json.dumps({'evaluated': len(rows), 'kept': len(kept), 'dropped': len(dropped),
                  'result_files': len(list((ROOT / 'results').glob('*.md'))),
                  'report': str(ROOT / 'REPORT.md'),
                  'csv': str(ROOT / 'staff-engineer-skills.csv'),
                  'bundle_bytes': (ROOT / 'staff-engineer-skills-evidence.zip').stat().st_size}, indent=2))
