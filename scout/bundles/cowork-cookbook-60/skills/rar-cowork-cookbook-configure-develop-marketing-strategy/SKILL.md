---
name: "rar-cowork-cookbook-configure-develop-marketing-strategy"
description: "Applies a bulk configuration change to develop marketing strategy from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_marketing_strategy", "rar_sha256": "297d66c6ee383af3e816e1df62d4804d0da1009980b4fd68390256d25b4e3f4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 297d66c6ee383af3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_marketing_strategy_agent.py` first:

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
    "version": '2.0.0',
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
