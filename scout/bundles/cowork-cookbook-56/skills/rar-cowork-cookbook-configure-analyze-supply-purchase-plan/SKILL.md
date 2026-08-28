---
name: "rar-cowork-cookbook-configure-analyze-supply-purchase-plan"
description: "Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_supply_purchase_plan", "rar_sha256": "51e1d224aac770737b7d1f1a4ecc7c18ce9d3ed488076da7377df65431b66ae4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 51e1d224aac77073…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_supply_purchase_plan_agent.py` first:

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
    "version": '2.0.0',
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
