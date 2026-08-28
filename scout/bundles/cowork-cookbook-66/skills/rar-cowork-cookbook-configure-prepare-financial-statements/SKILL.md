---
name: "rar-cowork-cookbook-configure-prepare-financial-statements"
description: "Applies a bulk configuration change to prepare financial statements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prepare_financial_statements", "rar_sha256": "17667df8f9b92a968d6cbb65f2d3ab69bbd00ee14cf33c50aa5cbe516b9c3fcb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 17667df8f9b92a96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prepare_financial_statements_agent.py` first:

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
    "version": '2.0.0',
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
