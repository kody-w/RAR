---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "2c9e627e44f3ee2fd57547d82642251701389b02ee2d6252532f8bfa9c6a15e7", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_knowledge_readiness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-studio-knowledge-readiness:5a9b2bea08577d04b59060f4969a631ad3fcf30d8e197149c572f0ee53527e3b", "kind": "skill"}, "version": "2.0.0", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_studio_knowledge_readiness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_knowledge_readiness_agent.py` is
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

Copilot Studio Knowledge Readiness — Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness
  Upstream author: Jay Padimiti
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_knowledge_readiness_agent.py` and embedded as the fenced Python below (sha256 2c9e627e44f3ee2f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_knowledge_readiness_agent.py` first:

```bash
python3 copilot_studio_knowledge_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_knowledge_readiness_agent.py   # or on stdin
python3 copilot_studio_knowledge_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Knowledge Readiness — Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness
  Upstream author: Jay Padimiti
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_knowledge_readiness',
    "version": '2.0.0',
    "display_name": 'Copilot Studio Knowledge Readiness',
    "description": 'Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review.',
    "author": 'Jay Padimiti',
    "tags": ['copilot_studio', 'knowledge', 'rag', 'sharepoint', 'dataverse', 'governance', 'readiness', 'assessment'],
    "category": 'integrations',
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
        "upstream_slug": 'copilot-studio-knowledge-readiness',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-knowledge-readiness',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd4fe7450b56dfe2a',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:assess', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CopilotStudioKnowledgeReadiness(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioKnowledgeReadiness'
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
    print(CopilotStudioKnowledgeReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
