---
name: "rar-cowork-cookbook-dashboard-update-work-order-details"
description: "Produces a self-contained interactive HTML dashboard for update work order details - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_update_work_order_details", "rar_sha256": "b428e2ada58b5cd5104959b79d2b9ceac83e6f8ca5c214ab824301132fd94175", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_update_work_order_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-update-work-order-details:3b31a0e4da2556796ef04dbd4cc48be9c298ab5440df1db691cc184d9110eed3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_update_work_order_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_update_work_order_details_agent.py` is
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
