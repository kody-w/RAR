---
name: "rar-cowork-cookbook-dashboard-update-work-order-details"
description: "Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_update_work_order_details", "rar_sha256": "b428e2ada58b5cd5104959b79d2b9ceac83e6f8ca5c214ab824301132fd94175", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 b428e2ada58b5cd5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_update_work_order_details_agent.py` first:

```bash
python3 dashboard_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_update_work_order_details_agent.py   # or on stdin
python3 dashboard_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_update_work_order_details',
    "version": '2.0.0',
    "display_name": 'Update work order details Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f47e979c0164e41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardUpdateWorkOrderDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardUpdateWorkOrderDetails'
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
    print(DashboardUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
