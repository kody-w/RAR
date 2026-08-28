---
name: "rar-cowork-cookbook-configure-reclaim-database-storage"
description: "Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reclaim_database_storage", "rar_sha256": "9f7074b49cc54ad5d73d8e8cf77f6c340313a1b5a87715db87e6f88b159b6418", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 9f7074b49cc54ad5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reclaim_database_storage_agent.py` first:

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
    "version": '2.0.0',
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
