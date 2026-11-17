"""Validate preserved evidence and proposed configuration syntax without a network."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def read_json(name):
    return json.loads((ROOT / name).read_text())

def main():
    ids = {f"{i:02}" for i in range(1, 51)}
    manifest = read_json("manifest.json")
    evaluation = read_json("evaluation.json")
    hashes = read_json("artifact-hashes.json")
    judgments = read_json("judgments.json")
    for rows in [manifest, evaluation, hashes, judgments]:
        assert len(rows) == 50 and {r["id"] for r in rows} == ids
    assert Counter(r["decision"] for r in evaluation) == {"Keep": 42, "Drop": 8}
    for row in hashes:
        for folder, suffix, field in [("trials", "json", "scenario_sha256"), ("results", "md", "result_sha256")]:
            path = ROOT / folder / f"{row['id']}.{suffix}"
            assert hashlib.sha256(path.read_bytes()).hexdigest() == row[field], path
    kept = {r["id"] for r in evaluation if r["decision"] == "Keep"}
    dropped = ids - kept
    routing = read_json("workflow-routing.json")
    alternatives = read_json("dropped-alternatives.json")
    assert len(routing) == 42 and {r["id"] for r in routing} == kept
    assert len(alternatives) == 8 and {r["dropped_id"] for r in alternatives} == dropped
    assert all(set(r["replacement_ids"]) <= kept for r in alternatives)
    subprocess.run([sys.executable, str(ROOT / "agent-stack" / "build.py"), "--check"], check=True)
    checked_links = 0
    for p in ROOT.rglob("*.md"):
        if any(part in {"sources", ".git"} for part in p.relative_to(ROOT).parts):
            continue
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text()):
            if re.match(r"(?:https?://|mailto:|#)", target):
                continue
            target = target.split("#")[0]
            # Trial outputs can quote hypothetical code paths; only validate
            # navigational links in authored reports and agent documentation.
            if "results" in p.relative_to(ROOT).parts:
                continue
            assert (p.parent / target).exists(), (p, target)
            checked_links += 1
    print(f"OK: 50 scenarios/results match original hashes; 42 kept/8 dropped; routing complete; generated adapters match role and skill bindings; {checked_links} local links resolve.")
    print("This validates archival integrity and syntax, not skill efficacy or host compatibility.")

if __name__ == "__main__":
    main()
