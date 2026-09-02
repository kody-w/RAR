---
name: "rar-cowork-cookbook-configure-reclaim-database-storage"
description: "Applies a bulk configuration change to reclaim database storage from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reclaim_database_storage", "rar_sha256": "9f7074b49cc54ad5d73d8e8cf77f6c340313a1b5a87715db87e6f88b159b6418", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_reclaim_database_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-reclaim-database-storage:2c0cd9d86938e7661996546fc1967332f852b35600863124f8bd7670e0ee0d8f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_reclaim_database_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_reclaim_database_storage_agent.py` is
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
