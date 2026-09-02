---
name: "rar-cowork-cookbook-dashboard-manage-environmental-social-and-governance-esg-plan"
description: "Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "cff3f6d1bc035ade4ad3b4ec6358534cb5656a4f1acfb27b9886bb5160d50f48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_environmental_social_and_governance_esg_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-environmental-social-and-governance-esg-plan:4c96cee8585f8cb740cd021cea9a332726da811afdc574505010dc43768555d4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` is
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

Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 cff3f6d1bc035ade…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 dashboard_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan',
    "version": '2.0.0',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '696fd3b7d6031bc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEnvironmentalSocialAndGovernanceEsgPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(DashboardManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
