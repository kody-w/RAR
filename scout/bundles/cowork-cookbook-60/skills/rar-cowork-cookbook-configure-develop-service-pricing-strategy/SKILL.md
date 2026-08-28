---
name: "rar-cowork-cookbook-configure-develop-service-pricing-strategy"
description: "Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_service_pricing_strategy", "rar_sha256": "7f1b7e50a0e1d3b01323f5a6dc111a9211b09f7e19425cd0a20d6af570d4c8d8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_service_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_service_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop service pricing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 7f1b7e50a0e1d3b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_service_pricing_strategy_agent.py` first:

```bash
python3 configure_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_service_pricing_strategy_agent.py   # or on stdin
python3 configure_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_service_pricing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop service pricing strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd4570be27fcd7514',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopServicePricingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopServicePricingStrategy'
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
    print(ConfigureDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
