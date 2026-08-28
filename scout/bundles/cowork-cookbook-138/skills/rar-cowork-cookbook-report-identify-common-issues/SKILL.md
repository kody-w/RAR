---
name: "rar-cowork-cookbook-report-identify-common-issues"
description: "Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_common_issues", "rar_sha256": "3738b2d30fc36fd3eb2ef9dff00bb5ad41f0eebb2126045a5782a82be888e25c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_common_issues`. The original RAPP
agent is preserved byte-for-byte in `report_identify_common_issues_agent.py` and in the RCI capsule.

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

Identify common issues Summary Report — Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-common-issues
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 3738b2d30fc36fd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_common_issues_agent.py` first:

```bash
python3 report_identify_common_issues_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_common_issues_agent.py   # or on stdin
python3 report_identify_common_issues_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify common issues Summary Report — Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-common-issues
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_common_issues',
    "version": '2.0.0',
    "display_name": 'Identify common issues Summary Report',
    "description": 'Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-identify-common-issues',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-common-issues',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14bf3890351dc34d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/identify-common-issues'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-identify-common-issues', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIdentifyCommonIssues(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyCommonIssues'
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
    print(ReportIdentifyCommonIssues().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
