---
name: "rar-cowork-cookbook-adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct upsell, cross sell or repeat sale prompt status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "362fdab08ace77b4bddc4deb4a3278dc84ee8b754d28ec2e586d1b847b0b28d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt:50472229c8043731b574f6109d0e594cb1744a0233c02187a9bf06517a00f550", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
