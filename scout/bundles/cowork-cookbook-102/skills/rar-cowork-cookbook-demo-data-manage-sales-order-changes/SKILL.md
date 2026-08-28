---
name: "rar-cowork-cookbook-demo-data-manage-sales-order-changes"
description: "Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_sales_order_changes", "rar_sha256": "d54fee2e0b7cb32d4c44b517efc30ccd03fb72ea0fe3c657d7ff6cfda3769053", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 d54fee2e0b7cb32d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_sales_order_changes_agent.py` first:

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
    "version": '2.0.0',
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
