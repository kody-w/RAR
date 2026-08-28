---
name: "rar-cowork-cookbook-blueprint-credit-and-collections-review"
description: "Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_credit_and_collections_review", "rar_sha256": "56bcdc20a1870820b0c53ed54e8319581617fc8ce58a93c03d5501bc88bbe0ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "order_to_cash", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_credit_and_collections_review`. The original RAPP
agent is preserved byte-for-byte in `blueprint_credit_and_collections_review_agent.py` and in the RCI capsule.

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

Credit & Collections Review Blueprint — Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_credit_and_collections_review_agent.py` and embedded as the fenced Python below (sha256 56bcdc20a1870820…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_credit_and_collections_review_agent.py` first:

```bash
python3 blueprint_credit_and_collections_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_credit_and_collections_review_agent.py   # or on stdin
python3 blueprint_credit_and_collections_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Credit & Collections Review Blueprint — Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_credit_and_collections_review',
    "version": '2.0.0',
    "display_name": 'Credit & Collections Review Blueprint',
    "description": 'Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'order_to_cash', 'advanced', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'blueprint-credit-and-collections-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba11a05153ec0c31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': '2026-08-20', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'order-to-cash/blueprint-credit-and-collections-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.474, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintCreditAndCollectionsReview(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintCreditAndCollectionsReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintCreditAndCollectionsReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
