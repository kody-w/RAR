---
name: "rar-cowork-cookbook-dashboard-manage-store-operations"
description: "Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_store_operations", "rar_sha256": "c72beaf182392f7082a186ca26b39479914b852e61765b45bbe5bf5ab7c02004", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_store_operations`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_store_operations_agent.py` and in the RCI capsule.

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

Manage store operations Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 c72beaf182392f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_store_operations_agent.py` first:

```bash
python3 dashboard_manage_store_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_store_operations_agent.py   # or on stdin
python3 dashboard_manage_store_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage store operations Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_store_operations',
    "version": '2.0.1',
    "display_name": 'Manage store operations Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-store-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-store-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '218d35fed7c19591',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-store-operations'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-manage-store-operations', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageStoreOperations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageStoreOperations'
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
    print(DashboardManageStoreOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
