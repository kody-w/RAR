---
name: "rar-cowork-cookbook-dashboard-plan-marketing-campaigns"
description: "Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_marketing_campaigns", "rar_sha256": "fd72db42b1d1288f2cf8eff00ec5f530a2a9418c57e76e8cf669b805df3d00a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_marketing_campaigns_agent.py` and in the RCI capsule.

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

Plan marketing campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 fd72db42b1d1288f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_marketing_campaigns_agent.py` first:

```bash
python3 dashboard_plan_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_marketing_campaigns_agent.py   # or on stdin
python3 dashboard_plan_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan marketing campaigns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_marketing_campaigns',
    "version": '2.0.0',
    "display_name": 'Plan marketing campaigns Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-plan-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fcb8c9de4b3bbaf9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-marketing-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-marketing-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanMarketingCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanMarketingCampaigns'
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
    print(DashboardPlanMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
