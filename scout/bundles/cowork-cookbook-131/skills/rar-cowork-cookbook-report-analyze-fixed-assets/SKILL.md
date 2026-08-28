---
name: "rar-cowork-cookbook-report-analyze-fixed-assets"
description: "Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_fixed_assets", "rar_sha256": "4f0592f4489a5241ec90188aff4d32770d26eee00017224f5b655cf0b78faa6a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_fixed_assets_agent.py` and in the RCI capsule.

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

Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 4f0592f4489a5241…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_fixed_assets_agent.py` first:

```bash
python3 report_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_fixed_assets_agent.py   # or on stdin
python3 report_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Summary Report — Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Analyze fixed assets Summary Report',
    "description": 'Builds a structured summary report of analyze fixed assets activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0faf53284b08fa6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportAnalyzeFixedAssets(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeFixedAssets'
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
    print(ReportAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
