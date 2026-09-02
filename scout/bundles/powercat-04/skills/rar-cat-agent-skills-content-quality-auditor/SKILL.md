---
name: "rar-cat-agent-skills-content-quality-auditor"
description: "Score documents, pages, posts, or artefact libraries against a configurable quality rubric and recommend fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/content_quality_auditor", "rar_sha256": "884464387bc3f9da6f84ffad05a6432081cc32e356efba67a74c2d4a5ed0ed99", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "content_quality_auditor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/content-quality-auditor:48d71c12be10cbaef6cdfe37363c8092bfab5bb020097a24e48227a59e4d6842", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["content", "quality", "audit", "documents", "productivity", "governance"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/content_quality_auditor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `content_quality_auditor_agent.py` is
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
