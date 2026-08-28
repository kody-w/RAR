---
name: "rar-cowork-cookbook-audit-and-surface-against-a-standard"
description: "Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_and_surface_against_a_standard", "rar_sha256": "451d4d8183d19ad8bcd8db61b032ca203d7cbcac77f4af04a1411d8e18741510", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "work_management", "advanced", "read_only", "analysis"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_and_surface_against_a_standard_agent.py` and embedded as the fenced Python below (sha256 451d4d8183d19ad8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_and_surface_against_a_standard_agent.py` first:

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
    "version": '2.0.0',
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
