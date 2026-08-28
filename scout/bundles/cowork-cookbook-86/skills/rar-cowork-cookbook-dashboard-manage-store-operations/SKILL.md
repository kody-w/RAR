---
name: "rar-cowork-cookbook-dashboard-manage-store-operations"
description: "Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_store_operations", "rar_sha256": "c099aee5776d0bba02f6a4350d88aa340f6d20cfab22a35e9bc0d044d20d9cf8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 c099aee5776d0bba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_store_operations_agent.py` first:

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
    "version": '2.0.0',
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
