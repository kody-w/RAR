---
name: "rar-cowork-cookbook-configure-reimburse-workers-for-expenses"
description: "Applies a bulk configuration change to reimburse workers for expenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reimburse_workers_for_expenses", "rar_sha256": "e256cfe4b94508187e25193d962e2672eb4d49f01910826294f366cb3e3933d5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
