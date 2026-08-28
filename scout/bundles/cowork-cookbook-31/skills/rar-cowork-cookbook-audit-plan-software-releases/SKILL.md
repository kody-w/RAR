---
name: "rar-cowork-cookbook-audit-plan-software-releases"
description: "Audits plan software releases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_software_releases", "rar_sha256": "3c7d27afea4dc8ff6e59f26bb4c700894147082fac614b344ea1f3df43e77a67", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Completeness Audit — Audits plan software releases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 3c7d27afea4dc8ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_software_releases_agent.py` first:

```bash
python3 audit_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_software_releases_agent.py   # or on stdin
python3 audit_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Completeness Audit — Audits plan software releases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_software_releases',
    "version": '2.0.1',
    "display_name": 'Plan software releases Completeness Audit',
    "description": 'Audits plan software releases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db58985f95eacef6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditPlanSoftwareReleases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanSoftwareReleases'
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
    print(AuditPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
