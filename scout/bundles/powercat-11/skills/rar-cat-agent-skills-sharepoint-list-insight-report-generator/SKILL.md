---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "1755e4d761977ef94e93304dc8d180edc0dc810f70e304a513ed4909b525f0d7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sharepoint_list_insight_report_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/sharepoint-list-insight-report-generator:f57f55540d4159213e06910ca4c489c6ffeac19488443ffa91e289202a7a89a8", "kind": "skill"}, "version": "2.0.0", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/sharepoint_list_insight_report_generator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sharepoint_list_insight_report_generator_agent.py` is
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

SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_insight_report_generator_agent.py` and embedded as the fenced Python below (sha256 1755e4d761977ef9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_insight_report_generator_agent.py` first:

```bash
python3 sharepoint_list_insight_report_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_insight_report_generator_agent.py   # or on stdin
python3 sharepoint_list_insight_report_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_insight_report_generator',
    "version": '2.0.0',
    "display_name": 'SharePoint List Insight Report Generator',
    "description": 'Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…',
    "author": 'Marco Rocca',
    "tags": ['sharepoint', 'microsoft_365', 'lists', 'report', 'html'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'sharepoint-list-insight-report-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '271bccfbe07e039e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class SharepointListInsightReportGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListInsightReportGenerator'
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
    print(SharepointListInsightReportGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
