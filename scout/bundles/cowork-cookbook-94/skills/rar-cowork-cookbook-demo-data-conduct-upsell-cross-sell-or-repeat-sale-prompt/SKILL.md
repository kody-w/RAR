---
name: "rar-cowork-cookbook-demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "da3c2683d8884bd2cde937e47c355e36a520bc63ca3e62cea0e5d4c6005eba20", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The original RAPP
agent is preserved byte-for-byte in `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and in the RCI capsule.

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

Conduct upsell, cross sell or repeat sale prompt Demo Data Generator — Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 da3c2683d8884bd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

```bash
python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py   # or on stdin
python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct upsell, cross sell or repeat sale prompt Demo Data Generator — Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt',
    "version": '2.0.0',
    "display_name": 'Conduct upsell, cross sell or repeat sale prompt Demo Data Generator',
    "description": 'Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed5828303285d798',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConductUpsellCrossSellOrRepeatSalePrompt(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConductUpsellCrossSellOrRepeatSalePrompt'
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
    print(DemoDataConductUpsellCrossSellOrRepeatSalePrompt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
