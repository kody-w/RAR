---
name: "rar-cowork-cookbook-report-analyze-safety-achievement"
description: "Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_safety_achievement", "rar_sha256": "9d6fb5c743d9a0f955b270cc321b8e258f5d0525e53ab3932d95f164efca6354", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_safety_achievement`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_safety_achievement_agent.py` and in the RCI capsule.

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
