---
name: "rar-cowork-cookbook-demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates and creates realistic demo records for conduct upsell, cross sell or repeat sale prompt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "da3c2683d8884bd2cde937e47c355e36a520bc63ca3e62cea0e5d4c6005eba20", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt:b922cc045ae13a218875c0caadd8ff7f5d73ebee5d80f0899afd5fbde4ede955", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` is
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
