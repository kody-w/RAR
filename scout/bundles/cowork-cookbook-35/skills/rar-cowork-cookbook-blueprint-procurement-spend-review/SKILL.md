---
name: "rar-cowork-cookbook-blueprint-procurement-spend-review"
description: "Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_procurement_spend_review", "rar_sha256": "6bd7ed4bcb1f27858f5e3b6fc5f3905bb51d1d419e2c76f43be10c8aeaae76d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "source_to_pay", "advanced", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_procurement_spend_review_agent.py` and embedded as the fenced Python below (sha256 6bd7ed4bcb1f2785…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_procurement_spend_review_agent.py` first:

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
    "version": '2.0.0',
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
