---
name: "rar-cowork-cookbook-demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "66d903cc2e26b599e355907576e389dc3a5afc482e1bfab45b08384102ab2c88", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 66d903cc2e26b599…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

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
    "version": '2.0.1',
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
