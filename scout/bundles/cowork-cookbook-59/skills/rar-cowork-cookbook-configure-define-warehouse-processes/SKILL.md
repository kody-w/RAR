---
name: "rar-cowork-cookbook-configure-define-warehouse-processes"
description: "Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_warehouse_processes", "rar_sha256": "fb25b106b5db5f04494a18598ec9781f3b29882ae1e33b2ee78092e20f7a4196", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_warehouse_processes`. The original RAPP
agent is preserved byte-for-byte in `configure_define_warehouse_processes_agent.py` and in the RCI capsule.

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

Define warehouse processes Configuration Bulk Setup — Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 fb25b106b5db5f04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_warehouse_processes_agent.py` first:

```bash
python3 configure_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_warehouse_processes_agent.py   # or on stdin
python3 configure_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Configuration Bulk Setup — Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_warehouse_processes',
    "version": '2.0.0',
    "display_name": 'Define warehouse processes Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21dd1babf427783c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineWarehouseProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineWarehouseProcesses'
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
    print(ConfigureDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
