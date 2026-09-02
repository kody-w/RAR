---
name: "rar-cowork-cookbook-blueprint-procurement-spend-review"
description: "Paste this procurement-analysis workflow blueprint into Cowork and it profiles spend by vendor, flags concentration risk, and surfaces payable exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_procurement_spend_review", "rar_sha256": "6bd7ed4bcb1f27858f5e3b6fc5f3905bb51d1d419e2c76f43be10c8aeaae76d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blueprint_procurement_spend_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/blueprint-procurement-spend-review:75b4ea0a6987361c838c3f21e0e9df6c6fda93ff91bf459600212b44c198b836", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "source_to_pay", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/blueprint_procurement_spend_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blueprint_procurement_spend_review_agent.py` is
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
