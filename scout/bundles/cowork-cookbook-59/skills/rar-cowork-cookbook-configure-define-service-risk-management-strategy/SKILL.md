---
name: "rar-cowork-cookbook-configure-define-service-risk-management-strategy"
description: "Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_service_risk_management_strategy", "rar_sha256": "6baf17864825d23b2527aec7174b8cf52c8e4a8ef806e8e20fc420a738613a82", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 6baf17864825d23b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_service_risk_management_strategy_agent.py` first:

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
    "version": '2.0.1',
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
