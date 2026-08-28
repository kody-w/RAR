---
name: "rar-cowork-cookbook-ppt-exec-develop-sales-pricing-strategy"
description: "Generates an executive-ready PowerPoint deck on develop sales pricing strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy", "rar_sha256": "7d381d19c23f443f9d77fd889f7f0a6a1ce93cae5fac230a9008c1f2458c44f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 7d381d19c23f443f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_sales_pricing_strategy_agent.py` first:

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
    "version": '2.0.0',
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
