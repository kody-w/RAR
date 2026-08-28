---
name: "rar-cowork-cookbook-audit-plan-software-releases"
description: "Audits plan software releases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_software_releases", "rar_sha256": "b1f797744fab019436c3ecad95931457ffe642b32b9517947867a98e192e4e4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 b1f797744fab0194…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_software_releases_agent.py` first:

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
    "version": '2.0.0',
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
