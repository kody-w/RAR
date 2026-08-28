---
name: "rar-cowork-cookbook-ppt-exec-develop-sales-pricing-strategy"
description: "Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy", "rar_sha256": "384a89f9a0a7fe409389a953734fc41bfd2448b6c78824685a0dff7fd798d062", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_sales_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop sales pricing strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 384a89f9a0a7fe40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_sales_pricing_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_sales_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_sales_pricing_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_sales_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales pricing strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy',
    "version": '2.0.1',
    "display_name": 'Develop sales pricing strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-sales-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '911a101f3fbfd1c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-pricing-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-develop-sales-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopSalesPricingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopSalesPricingStrategy'
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
    print(PptExecDevelopSalesPricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
