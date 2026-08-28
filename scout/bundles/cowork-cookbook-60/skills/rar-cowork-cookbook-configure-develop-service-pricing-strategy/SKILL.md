---
name: "rar-cowork-cookbook-configure-develop-service-pricing-strategy"
description: "Applies a bulk configuration change to develop service pricing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_service_pricing_strategy", "rar_sha256": "6fbbdeb09521633953e164619f50e80b1f68c10a10d71e3b5e9852ef0461d3f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 6fbbdeb095216339…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_service_pricing_strategy_agent.py` first:

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
    "version": '2.0.1',
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
