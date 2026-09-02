---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "64d1835538128e525a1d912cc3140cda56f126332bd118ed0eeef34adf18b00f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "knowledge_corpus_curator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/knowledge-corpus-curator:f0575e685f239da56ffa30943e7f9bbbba25ad315ba8a2a9d1af0f2b1336da77", "kind": "skill"}, "version": "1.8.0", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/knowledge_corpus_curator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `knowledge_corpus_curator_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Knowledge Corpus Curator — Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator
  Upstream author: Doug Bellingeri
  Upstream version: 0.8.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `knowledge_corpus_curator_agent.py` and embedded as the fenced Python below (sha256 64d1835538128e52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `knowledge_corpus_curator_agent.py` first:

```bash
python3 knowledge_corpus_curator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 knowledge_corpus_curator_agent.py   # or on stdin
python3 knowledge_corpus_curator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Knowledge Corpus Curator — Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator
  Upstream author: Doug Bellingeri
  Upstream version: 0.8.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/knowledge_corpus_curator',
    "version": '1.8.0',
    "display_name": 'Knowledge Corpus Curator',
    "description": 'Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog.',
    "author": 'Doug Bellingeri',
    "tags": ['knowledge', 'sharepoint', 'governance', 'deduplication', 'documents', 'uploads', 'excel'],
    "category": 'productivity',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'knowledge-corpus-curator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#knowledge-corpus-curator',
        "upstream_version": '0.8.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '44b7b1e672580b5c',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class KnowledgeCorpusCurator(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'KnowledgeCorpusCurator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(KnowledgeCorpusCurator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
