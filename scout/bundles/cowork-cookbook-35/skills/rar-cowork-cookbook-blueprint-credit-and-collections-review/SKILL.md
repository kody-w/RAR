---
name: "rar-cowork-cookbook-blueprint-credit-and-collections-review"
description: "Paste this credit-and-collections workflow blueprint into Cowork and it ranks customers by credit exposure and overdue balance, then proposes a collections worklist."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_credit_and_collections_review", "rar_sha256": "af784f1123f8a3cf3a386a7ec2ca592cdd115fe41042240d2ac544e100463c05", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "order_to_cash", "advanced", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_credit_and_collections_review_agent.py` and embedded as the fenced Python below (sha256 af784f1123f8a3cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_credit_and_collections_review_agent.py` first:

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
    "version": '2.0.1',
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
