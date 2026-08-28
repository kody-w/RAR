---
name: "rar-cowork-cookbook-configure-analyze-account-payable"
description: "Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_account_payable", "rar_sha256": "69b9ade47d1697304e635a4cf8b31cbe64c12e25808932f2716cdb71e6d8db51", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_account_payable`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_account_payable_agent.py` and in the RCI capsule.

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

Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 69b9ade47d169730…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_account_payable_agent.py` first:

```bash
python3 configure_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_account_payable_agent.py   # or on stdin
python3 configure_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Configuration Bulk Setup — Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_account_payable',
    "version": '2.0.1',
    "display_name": 'Analyze account payable Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze account payable from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1da31eed370b12ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeAccountPayable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAccountPayable'
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
    print(ConfigureAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
