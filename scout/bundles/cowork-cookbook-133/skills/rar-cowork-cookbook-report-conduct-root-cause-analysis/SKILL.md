---
name: "rar-cowork-cookbook-report-conduct-root-cause-analysis"
description: "Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_root_cause_analysis", "rar_sha256": "4a81c0f2e01dd9e91a9cc8a3e1da67c456dde2e137e0e51af50b384d204c63c6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_root_cause_analysis`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_root_cause_analysis_agent.py` and in the RCI capsule.

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

Conduct root cause analysis Summary Report — Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 4a81c0f2e01dd9e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_root_cause_analysis_agent.py` first:

```bash
python3 report_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_root_cause_analysis_agent.py   # or on stdin
python3 report_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Summary Report — Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_root_cause_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct root cause analysis Summary Report',
    "description": 'Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90fd871db10dde2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConductRootCauseAnalysis(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductRootCauseAnalysis'
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
    print(ReportConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
