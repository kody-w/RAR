---
name: "rar-cowork-cookbook-report-analyze-safety-achievement"
description: "Builds a structured summary report of analyze safety achievement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_safety_achievement", "rar_sha256": "02d6c877547480ed1e4ef51aa4328599ab204e0357f29dd3201d222184cc6c54", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 02d6c877547480ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_safety_achievement_agent.py` first:

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
    "version": '2.0.1',
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
