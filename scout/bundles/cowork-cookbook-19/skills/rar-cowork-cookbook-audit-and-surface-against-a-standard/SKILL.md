---
name: "rar-cowork-cookbook-audit-and-surface-against-a-standard"
description: "Apply a brand guide, naming convention, compliance policy, or quality standard across dozens of files - without manually reviewing each one and without risking accidental changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_and_surface_against_a_standard", "rar_sha256": "451d4d8183d19ad8bcd8db61b032ca203d7cbcac77f4af04a1411d8e18741510", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_and_surface_against_a_standard_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-and-surface-against-a-standard:3847c8f161753dbb2ff84c877e98c077a8e246d57a2014b3601751de6d6423e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "work_management", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_and_surface_against_a_standard`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_and_surface_against_a_standard_agent.py` is
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
