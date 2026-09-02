---
name: "rar-cowork-cookbook-configure-define-service-risk-management-strategy"
description: "Applies a bulk configuration change to define service risk management strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_service_risk_management_strategy", "rar_sha256": "e42bc541f4d460c06dd988efb0a2926b41e6079a37ace353bc45fda171e7f80d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_service_risk_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-service-risk-management-strategy:483f0387504c937d891bf7fe4f511e65a923f2985b1f3bce8b3126320cf65fe2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_service_risk_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_service_risk_management_strategy_agent.py` is
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
