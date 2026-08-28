---
name: "rar-cowork-cookbook-configure-receive-goods"
description: "Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_goods", "rar_sha256": "00e0ec9e8b41e4ea8b505c2ee51beed612410ce903d2ef0d420102d2cd40f407", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `configure_receive_goods_agent.py` and in the RCI capsule.

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

Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_goods_agent.py` and embedded as the fenced Python below (sha256 00e0ec9e8b41e4ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_goods_agent.py` first:

```bash
python3 configure_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_goods_agent.py   # or on stdin
python3 configure_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_goods',
    "version": '2.0.1',
    "display_name": 'Receive goods Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e20ccf7ee06717ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReceiveGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveGoods'
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
    print(ConfigureReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
