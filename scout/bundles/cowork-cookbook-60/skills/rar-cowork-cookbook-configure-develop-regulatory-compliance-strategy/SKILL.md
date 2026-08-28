---
name: "rar-cowork-cookbook-configure-develop-regulatory-compliance-strategy"
description: "Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_regulatory_compliance_strategy", "rar_sha256": "9dd93520dac6a823cbbd5e1462fba825057dda0fa0eac9df16c3491f918ac4f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_regulatory_compliance_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_regulatory_compliance_strategy_agent.py` and in the RCI capsule.

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

Develop regulatory compliance strategy Configuration Bulk Setup — Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 9dd93520dac6a823…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_regulatory_compliance_strategy_agent.py` first:

```bash
python3 configure_develop_regulatory_compliance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_regulatory_compliance_strategy_agent.py   # or on stdin
python3 configure_develop_regulatory_compliance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop regulatory compliance strategy Configuration Bulk Setup — Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_regulatory_compliance_strategy',
    "version": '2.0.1',
    "display_name": 'Develop regulatory compliance strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-regulatory-compliance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-regulatory-compliance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'effff201bcc252a4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-regulatory-compliance-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-develop-regulatory-compliance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopRegulatoryComplianceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopRegulatoryComplianceStrategy'
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
    print(ConfigureDevelopRegulatoryComplianceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
