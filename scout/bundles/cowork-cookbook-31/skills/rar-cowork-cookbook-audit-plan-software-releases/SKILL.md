---
name: "rar-cowork-cookbook-audit-plan-software-releases"
description: "Audits plan software releases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_software_releases", "rar_sha256": "b1f797744fab019436c3ecad95931457ffe642b32b9517947867a98e192e4e4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-software-releases:68ea8492c1d6f9e544393fc17f7f72bd3f39dbf1313e2258eea71664703457b9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_software_releases_agent.py` is
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
