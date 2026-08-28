---
name: "rar-cowork-cookbook-dashboard-manage-environmental-social-and-governance-esg-plan"
description: "Produces a self-contained interactive HTML dashboard for manage environmental, social, and governance (ESG) plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "cff3f6d1bc035ade4ad3b4ec6358534cb5656a4f1acfb27b9886bb5160d50f48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_environmental_social_and_governance_esg_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_environmental_social_and_governance_esg_plan_agent.py` and in the RCI capsule.

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
