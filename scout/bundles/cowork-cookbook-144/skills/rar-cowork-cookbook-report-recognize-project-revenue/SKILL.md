---
name: "rar-cowork-cookbook-report-recognize-project-revenue"
description: "Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_recognize_project_revenue", "rar_sha256": "e92a4114ad9c11d58a75e14a0a9b1a22a23aad351296b5d13f9f73674bf813aa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_recognize_project_revenue`. The original RAPP
agent is preserved byte-for-byte in `report_recognize_project_revenue_agent.py` and in the RCI capsule.

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

Recognize project revenue Summary Report — Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 e92a4114ad9c11d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_recognize_project_revenue_agent.py` first:

```bash
python3 report_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_recognize_project_revenue_agent.py   # or on stdin
python3 report_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Summary Report — Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_recognize_project_revenue',
    "version": '2.0.1',
    "display_name": 'Recognize project revenue Summary Report',
    "description": 'Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '208e8ac554e6b3cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportRecognizeProjectRevenue(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecognizeProjectRevenue'
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
    print(ReportRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
