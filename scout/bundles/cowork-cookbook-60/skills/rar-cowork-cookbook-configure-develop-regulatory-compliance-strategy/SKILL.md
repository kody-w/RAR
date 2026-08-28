---
name: "rar-cowork-cookbook-configure-develop-regulatory-compliance-strategy"
description: "Applies a bulk configuration change to develop regulatory compliance strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_regulatory_compliance_strategy", "rar_sha256": "7412edc3616bb8dfca6a9129a0bc35eb50e9b4a233099a95ba5955c382173c19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 7412edc3616bb8df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_regulatory_compliance_strategy_agent.py` first:

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
    "version": '2.0.0',
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
