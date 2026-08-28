---
name: "rar-cowork-cookbook-dashboard-plan-service-contractor-work"
description: "Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_service_contractor_work", "rar_sha256": "02c1e0293e1482df9988b4f93ffee913323cc8ae626a4e3d68e14e2d2a30c029", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 02c1e0293e1482df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_service_contractor_work_agent.py` first:

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
    "version": '2.0.1',
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
