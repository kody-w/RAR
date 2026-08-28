---
name: "rar-cowork-cookbook-configure-develop-marketing-strategy"
description: "Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_marketing_strategy", "rar_sha256": "634d9655c241bc422de78f608f1ad056285a49bf01e0fcd91a03991eed4ce671", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_marketing_strategy`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_marketing_strategy_agent.py` and in the RCI capsule.

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

Develop marketing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 634d9655c241bc42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_marketing_strategy_agent.py` first:

```bash
python3 configure_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_marketing_strategy_agent.py   # or on stdin
python3 configure_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Configuration Bulk Setup — Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_marketing_strategy',
    "version": '2.0.1',
    "display_name": 'Develop marketing strategy Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90d014260935b4b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopMarketingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopMarketingStrategy'
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
    print(ConfigureDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
