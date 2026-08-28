---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "884464387bc3f9da6f84ffad05a6432081cc32e356efba67a74c2d4a5ed0ed99", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/content_quality_auditor`. The original RAPP
agent is preserved byte-for-byte in `content_quality_auditor_agent.py` and in the RCI capsule.

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

Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `content_quality_auditor_agent.py` and embedded as the fenced Python below (sha256 884464387bc3f9da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `content_quality_auditor_agent.py` first:

```bash
python3 content_quality_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 content_quality_auditor_agent.py   # or on stdin
python3 content_quality_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Content Quality Auditor — Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#content-quality-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/content_quality_auditor',
    "version": '1.1.0',
    "display_name": 'Content Quality Auditor',
    "description": 'Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes.',
    "author": 'Simon Owen',
    "tags": ['content', 'quality', 'audit', 'documents', 'productivity', 'governance'],
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
        "upstream_slug": 'content-quality-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#content-quality-auditor',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b2eca5049c1ef246',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.636, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'tag:governance', 'tag:quality', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class ContentQualityAuditor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ContentQualityAuditor'
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
    print(ContentQualityAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
