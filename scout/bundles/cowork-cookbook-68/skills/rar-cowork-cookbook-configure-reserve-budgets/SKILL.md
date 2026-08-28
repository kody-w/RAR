---
name: "rar-cowork-cookbook-configure-reserve-budgets"
description: "Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reserve_budgets", "rar_sha256": "c4ca6d877f1a051c379953e06d6a5fd41796bb9801a491940631e43e75054f04", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reserve_budgets`. The original RAPP
agent is preserved byte-for-byte in `configure_reserve_budgets_agent.py` and in the RCI capsule.

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

Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 c4ca6d877f1a051c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reserve_budgets_agent.py` first:

```bash
python3 configure_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reserve_budgets_agent.py   # or on stdin
python3 configure_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reserve_budgets',
    "version": '2.0.1',
    "display_name": 'Reserve budgets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b36e23b46df8ccb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReserveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReserveBudgets'
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
    print(ConfigureReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
