---
name: "rar-cowork-cookbook-configure-reclaim-database-storage"
description: "Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reclaim_database_storage", "rar_sha256": "079d4fa6aa7e8caa5bfafc4bcc8f5549745fffcc4dd6efea744ceee002889ee1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reclaim_database_storage`. The original RAPP
agent is preserved byte-for-byte in `configure_reclaim_database_storage_agent.py` and in the RCI capsule.

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

Reclaim database storage Configuration Bulk Setup — Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reclaim-database-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 079d4fa6aa7e8caa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reclaim_database_storage_agent.py` first:

```bash
python3 configure_reclaim_database_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reclaim_database_storage_agent.py   # or on stdin
python3 configure_reclaim_database_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reclaim database storage Configuration Bulk Setup — Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reclaim-database-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reclaim_database_storage',
    "version": '2.0.1',
    "display_name": 'Reclaim database storage Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reclaim-database-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reclaim-database-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3150218b921c1054',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/reclaim-database-storage'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-reclaim-database-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReclaimDatabaseStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReclaimDatabaseStorage'
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
    print(ConfigureReclaimDatabaseStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
