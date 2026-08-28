---
name: "rar-cowork-cookbook-adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "362fdab08ace77b4bddc4deb4a3278dc84ee8b754d28ec2e586d1b847b0b28d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 362fdab08ace77b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

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
    "version": '2.0.0',
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
