---
name: "rar-cowork-cookbook-dashboard-plan-service-contractor-work"
description: "Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_service_contractor_work", "rar_sha256": "4ccfdfd861dba22ecb679a535ce4ab0be29d3473d2fdf52a969b5bdab9675808", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_service_contractor_work`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_service_contractor_work_agent.py` and in the RCI capsule.

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

Plan service contractor work Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 4ccfdfd861dba22e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_service_contractor_work_agent.py` first:

```bash
python3 dashboard_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_service_contractor_work_agent.py   # or on stdin
python3 dashboard_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_service_contractor_work',
    "version": '2.0.0',
    "display_name": 'Plan service contractor work Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c792b35c80a9877e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanServiceContractorWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanServiceContractorWork'
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
    print(DashboardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
