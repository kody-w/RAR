---
name: "rar-cat-agent-skills-copilot-studio-knowledge-readiness"
description: "Assess whether an uploaded or exported document set is ready to power a Copilot Studio agent. Produces a corpus-based readiness score, prioritized cleanup backlog, chunking and metadata guidance, and a test-prompt suite, while calling out any evidence gaps that require live system review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_knowledge_readiness", "rar_sha256": "2c9e627e44f3ee2fd57547d82642251701389b02ee2d6252532f8bfa9c6a15e7", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Jay Padimiti", "tags": ["copilot_studio", "knowledge", "rag", "sharepoint", "dataverse", "governance", "readiness", "assessment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_knowledge_readiness`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_knowledge_readiness_agent.py` and in the RCI capsule.

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
