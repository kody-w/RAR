---
name: "rar-cowork-cookbook-report-maintain-and-update-the-business-continuity-plan"
description: "Builds a structured summary report of maintain and update the business continuity plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan", "rar_sha256": "6d8f363a42beee90b9cfb4870c85cff111be52d920c73496205645c505a0792c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_maintain_and_update_the_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-maintain-and-update-the-business-continuity-plan:cfce72f1a7068eadd4947732be3d2e3a198f069c1cb19e3da5bf66ae6f279476", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_maintain_and_update_the_business_continuity_plan_agent.py` is
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
