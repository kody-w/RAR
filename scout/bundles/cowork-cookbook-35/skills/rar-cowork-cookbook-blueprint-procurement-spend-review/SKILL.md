---
name: "rar-cowork-cookbook-blueprint-procurement-spend-review"
description: "Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_procurement_spend_review", "rar_sha256": "9d3d0c28e76bc98b6f369e0dcfc9993a94261391cfab5e3155e2323c5d804892", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "source_to_pay", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_procurement_spend_review`. The original RAPP
agent is preserved byte-for-byte in `blueprint_procurement_spend_review_agent.py` and in the RCI capsule.

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

Procurement Spend & Supplier Risk Blueprint — Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-procurement-spend-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_procurement_spend_review_agent.py` and embedded as the fenced Python below (sha256 9d3d0c28e76bc98b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_procurement_spend_review_agent.py` first:

```bash
python3 blueprint_procurement_spend_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_procurement_spend_review_agent.py   # or on stdin
python3 blueprint_procurement_spend_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procurement Spend & Supplier Risk Blueprint — Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-procurement-spend-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_procurement_spend_review',
    "version": '2.0.1',
    "display_name": 'Procurement Spend & Supplier Risk Blueprint',
    "description": 'Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'source_to_pay', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-procurement-spend-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-procurement-spend-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c0999a13d944789',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'source-to-pay/blueprint-procurement-spend-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.529, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintProcurementSpendReview(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintProcurementSpendReview'
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
    print(BlueprintProcurementSpendReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
