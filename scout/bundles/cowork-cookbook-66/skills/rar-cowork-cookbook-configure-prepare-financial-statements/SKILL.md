---
name: "rar-cowork-cookbook-configure-prepare-financial-statements"
description: "Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prepare_financial_statements", "rar_sha256": "128a81cb766ad2a1f8c08381ad45d04e7dc1570aa5c7571525ba44579a4a6b2e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_prepare_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `configure_prepare_financial_statements_agent.py` and in the RCI capsule.

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

Prepare financial statements Configuration Bulk Setup — Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 128a81cb766ad2a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prepare_financial_statements_agent.py` first:

```bash
python3 configure_prepare_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prepare_financial_statements_agent.py   # or on stdin
python3 configure_prepare_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare financial statements Configuration Bulk Setup — Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prepare-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prepare_financial_statements',
    "version": '2.0.1',
    "display_name": 'Prepare financial statements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-prepare-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prepare-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7dc8afc1f7a92fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-financial-statements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-prepare-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePrepareFinancialStatements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrepareFinancialStatements'
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
    print(ConfigurePrepareFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
