---
name: "rar-cowork-cookbook-report-identify-common-issues"
description: "Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_common_issues", "rar_sha256": "bed4a6a93672f813464f6cf5f888aeff1b34312f63eaffd09bb8c48822209310", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 bed4a6a93672f813…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_common_issues_agent.py` first:

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
    "version": '2.0.1',
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
