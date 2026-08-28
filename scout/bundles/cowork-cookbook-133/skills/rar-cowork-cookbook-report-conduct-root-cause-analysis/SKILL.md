---
name: "rar-cowork-cookbook-report-conduct-root-cause-analysis"
description: "Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_root_cause_analysis", "rar_sha256": "a66f5418fa672958ca11053c074e9c5f6aba888f1cf185aa95d5a69efab2e697", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 a66f5418fa672958…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_root_cause_analysis_agent.py` first:

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
    "version": '2.0.0',
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
