---
name: "rar-cowork-cookbook-dashboard-plan-marketing-campaigns"
description: "Produces a self-contained interactive HTML dashboard for plan marketing campaigns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_marketing_campaigns", "rar_sha256": "fd72db42b1d1288f2cf8eff00ec5f530a2a9418c57e76e8cf669b805df3d00a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_plan_marketing_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-plan-marketing-campaigns:0b220208fd389b0b15b443760f488896e2a12505ba0f1c09d01a78ff43330c4b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_plan_marketing_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_plan_marketing_campaigns_agent.py` is
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
