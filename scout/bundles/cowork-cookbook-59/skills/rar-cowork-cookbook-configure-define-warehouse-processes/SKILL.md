---
name: "rar-cowork-cookbook-configure-define-warehouse-processes"
description: "Applies a bulk configuration change to define warehouse processes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_warehouse_processes", "rar_sha256": "fb25b106b5db5f04494a18598ec9781f3b29882ae1e33b2ee78092e20f7a4196", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_warehouse_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-warehouse-processes:90a490c2ace575cfd205d991d491e9108f53f919074307e87d62ec52e009b519", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_warehouse_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_warehouse_processes_agent.py` is
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
