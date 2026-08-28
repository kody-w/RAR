---
name: "rar-cowork-cookbook-audit-and-surface-against-a-standard"
description: "Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_and_surface_against_a_standard", "rar_sha256": "8358fa287655d5253a1b77fef154d6eaef5106a4ce8065ef09f0ee5639b8fee2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "work_management", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_and_surface_against_a_standard`. The original RAPP
agent is preserved byte-for-byte in `audit_and_surface_against_a_standard_agent.py` and in the RCI capsule.

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

Audit and surface against a standard — Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_and_surface_against_a_standard_agent.py` and embedded as the fenced Python below (sha256 8358fa287655d525…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_and_surface_against_a_standard_agent.py` first:

```bash
python3 audit_and_surface_against_a_standard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_and_surface_against_a_standard_agent.py   # or on stdin
python3 audit_and_surface_against_a_standard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit and surface against a standard — Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_and_surface_against_a_standard',
    "version": '2.0.1',
    "display_name": 'Audit and surface against a standard',
    "description": 'Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'work_management', 'advanced', 'read_only', 'analysis'],
    "category": 'analysis',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-and-surface-against-a-standard',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-and-surface-against-a-standard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a319565f3963a7d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/review-against-standards/audit-content-against-a-standard'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'work-management/audit-and-surface-against-a-standard', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.714, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAndSurfaceAgainstAStandard(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAndSurfaceAgainstAStandard'
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
    print(AuditAndSurfaceAgainstAStandard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
