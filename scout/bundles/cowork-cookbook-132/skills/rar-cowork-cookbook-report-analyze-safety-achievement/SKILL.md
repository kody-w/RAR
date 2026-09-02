---
name: "rar-cowork-cookbook-report-analyze-safety-achievement"
description: "Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_safety_achievement", "rar_sha256": "9d6fb5c743d9a0f955b270cc321b8e258f5d0525e53ab3932d95f164efca6354", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_analyze_safety_achievement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-analyze-safety-achievement:b2cdccee33dce685968aab29920b910e18e9f2fc43bed6af81f971a87ea23acf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_analyze_safety_achievement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_analyze_safety_achievement_agent.py` is
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

Analyze safety achievement Summary Report — Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-safety-achievement
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 9d6fb5c743d9a0f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_safety_achievement_agent.py` first:

```bash
python3 report_analyze_safety_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_safety_achievement_agent.py   # or on stdin
python3 report_analyze_safety_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze safety achievement Summary Report — Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-safety-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_safety_achievement',
    "version": '2.0.0',
    "display_name": 'Analyze safety achievement Summary Report',
    "description": 'Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-safety-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-safety-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c704cafbfb577e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-safety-achievement'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-analyze-safety-achievement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeSafetyAchievement(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeSafetyAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportAnalyzeSafetyAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
