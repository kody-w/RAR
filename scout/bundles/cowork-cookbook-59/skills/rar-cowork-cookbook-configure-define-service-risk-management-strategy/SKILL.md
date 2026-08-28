---
name: "rar-cowork-cookbook-configure-define-service-risk-management-strategy"
description: "Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_service_risk_management_strategy", "rar_sha256": "e42bc541f4d460c06dd988efb0a2926b41e6079a37ace353bc45fda171e7f80d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_service_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_define_service_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define service risk management strategy Configuration Bulk Setup — Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 e42bc541f4d460c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_service_risk_management_strategy_agent.py` first:

```bash
python3 configure_define_service_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_service_risk_management_strategy_agent.py   # or on stdin
python3 configure_define_service_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service risk management strategy Configuration Bulk Setup — Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_service_risk_management_strategy',
    "version": '2.0.0',
    "display_name": 'Define service risk management strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-service-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-service-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0dd5eda90df6d234',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-risk-management-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-define-service-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineServiceRiskManagementStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineServiceRiskManagementStrategy'
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
    print(ConfigureDefineServiceRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
