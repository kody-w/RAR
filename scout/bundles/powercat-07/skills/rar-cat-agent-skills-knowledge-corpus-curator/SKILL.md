---
name: "rar-cat-agent-skills-knowledge-corpus-curator"
description: "Review uploaded knowledge-source files for duplication, redundancy, staleness, overlap, and potentially conflicting guidance, then produce an evidence-based curation backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/knowledge_corpus_curator", "rar_sha256": "64d1835538128e525a1d912cc3140cda56f126332bd118ed0eeef34adf18b00f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.8.0", "author": "Doug Bellingeri", "tags": ["knowledge", "sharepoint", "governance", "deduplication", "documents", "uploads", "excel"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/knowledge_corpus_curator`. The original RAPP
agent is preserved byte-for-byte in `knowledge_corpus_curator_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
