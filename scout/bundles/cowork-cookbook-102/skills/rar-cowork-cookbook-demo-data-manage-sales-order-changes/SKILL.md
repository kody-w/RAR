---
name: "rar-cowork-cookbook-demo-data-manage-sales-order-changes"
description: "Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_sales_order_changes", "rar_sha256": "f34ec43c30352746082bcfee8389ae926218787aee501069342513d5353df6ba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_sales_order_changes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_sales_order_changes_agent.py` and in the RCI capsule.

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

Manage sales order changes Demo Data Generator — Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 f34ec43c30352746…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_sales_order_changes_agent.py` first:

```bash
python3 demo_data_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_sales_order_changes_agent.py   # or on stdin
python3 demo_data_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Demo Data Generator — Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_sales_order_changes',
    "version": '2.0.1',
    "display_name": 'Manage sales order changes Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd2a39f6956d20e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManageSalesOrderChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSalesOrderChanges'
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
    print(DemoDataManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
