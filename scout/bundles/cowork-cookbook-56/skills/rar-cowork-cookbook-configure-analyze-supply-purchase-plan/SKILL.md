---
name: "rar-cowork-cookbook-configure-analyze-supply-purchase-plan"
description: "Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_supply_purchase_plan", "rar_sha256": "03cb649f8861ce49bf29c69c13f84f3df43451dc7ec3e20b9bdbef69c2aad429", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_supply_purchase_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_supply_purchase_plan_agent.py` and in the RCI capsule.

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

Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 03cb649f8861ce49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_supply_purchase_plan_agent.py` first:

```bash
python3 configure_analyze_supply_purchase_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_supply_purchase_plan_agent.py   # or on stdin
python3 configure_analyze_supply_purchase_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_supply_purchase_plan',
    "version": '2.0.1',
    "display_name": 'Analyze supply purchase plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-supply-purchase-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa9f366ed2966660',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/analyze-supply-purchase-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-supply-purchase-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeSupplyPurchasePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSupplyPurchasePlan'
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
    print(ConfigureAnalyzeSupplyPurchasePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
