---
name: "rar-cowork-cookbook-adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "36d39c906c024337b72d37b8e8311551902eb0966e24663b9c0de62eb0da7ab4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and in the RCI capsule.

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

Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 36d39c906c024337…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

```bash
python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py   # or on stdin
python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt',
    "version": '2.0.1',
    "display_name": 'Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '105f197f2c7c8121',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt'
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
    print(AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
