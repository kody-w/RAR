---
name: "rar-cowork-cookbook-report-identify-common-issues"
description: "Builds a structured summary report of identify common issues activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_common_issues", "rar_sha256": "3738b2d30fc36fd3eb2ef9dff00bb5ad41f0eebb2126045a5782a82be888e25c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_identify_common_issues_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-identify-common-issues:92f59e4b5aa143ad5b204bb0c09473c26af5f961f15b3a3bbeef3724c5459b5a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_identify_common_issues`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_identify_common_issues_agent.py` is
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
