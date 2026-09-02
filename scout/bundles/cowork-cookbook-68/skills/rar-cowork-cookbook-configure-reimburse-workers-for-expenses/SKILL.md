---
name: "rar-cowork-cookbook-configure-reimburse-workers-for-expenses"
description: "Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reimburse_workers_for_expenses", "rar_sha256": "e256cfe4b94508187e25193d962e2672eb4d49f01910826294f366cb3e3933d5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_reimburse_workers_for_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-reimburse-workers-for-expenses:d17fdfee90353fd37887b972e87ea96c16b21bd3d478bb011c329e9018b1e22a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_reimburse_workers_for_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_reimburse_workers_for_expenses_agent.py` is
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

Reimburse workers for expenses Configuration Bulk Setup — Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 e256cfe4b9450818…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reimburse_workers_for_expenses_agent.py` first:

```bash
python3 configure_reimburse_workers_for_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reimburse_workers_for_expenses_agent.py   # or on stdin
python3 configure_reimburse_workers_for_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reimburse workers for expenses Configuration Bulk Setup — Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reimburse_workers_for_expenses',
    "version": '2.0.0',
    "display_name": 'Reimburse workers for expenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reimburse-workers-for-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reimburse-workers-for-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c3fe141a69fd5a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/reimburse-workers-for-expenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-reimburse-workers-for-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReimburseWorkersForExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReimburseWorkersForExpenses'
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
    print(ConfigureReimburseWorkersForExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
