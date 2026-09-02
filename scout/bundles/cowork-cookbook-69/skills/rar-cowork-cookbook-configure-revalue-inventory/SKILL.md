---
name: "rar-cowork-cookbook-configure-revalue-inventory"
description: "Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_revalue_inventory", "rar_sha256": "b1decf0e7c6e25eb36c7d2a737a14e00b559deebde4ff1a57b7a05b80a88cf18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_revalue_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-revalue-inventory:88162c862dff9bb1bb318030b9227142862544baa41b0ce313a6d7fdf0e41508", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_revalue_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_revalue_inventory_agent.py` is
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

Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 b1decf0e7c6e25eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_revalue_inventory_agent.py` first:

```bash
python3 configure_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_revalue_inventory_agent.py   # or on stdin
python3 configure_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_revalue_inventory',
    "version": '2.0.0',
    "display_name": 'Revalue inventory Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e68eea6889435eca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureRevalueInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRevalueInventory'
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
    print(ConfigureRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
