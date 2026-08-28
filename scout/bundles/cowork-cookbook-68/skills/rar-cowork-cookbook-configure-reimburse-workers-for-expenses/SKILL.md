---
name: "rar-cowork-cookbook-configure-reimburse-workers-for-expenses"
description: "Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reimburse_workers_for_expenses", "rar_sha256": "67eceaac68870b4012896f643844649d8617433b8d8965df61774759c24b2fe8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reimburse_workers_for_expenses`. The original RAPP
agent is preserved byte-for-byte in `configure_reimburse_workers_for_expenses_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 67eceaac68870b40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reimburse_workers_for_expenses_agent.py` first:

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
    "version": '2.0.1',
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
