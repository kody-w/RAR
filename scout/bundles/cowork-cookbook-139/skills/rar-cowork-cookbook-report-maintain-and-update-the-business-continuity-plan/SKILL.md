---
name: "rar-cowork-cookbook-report-maintain-and-update-the-business-continuity-plan"
description: "Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan", "rar_sha256": "6d8f363a42beee90b9cfb4870c85cff111be52d920c73496205645c505a0792c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Summary Report — Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 6d8f363a42beee90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 report_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 report_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Summary Report — Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Maintain and update the business continuity plan Summary Report',
    "description": 'Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'deb6979754c5f54d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainAndUpdateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
