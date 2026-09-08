---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "c915c29c6311ad09ee768d4267ba02b6fb91324750ffc62d9cc02c2cb6b5ea82", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_insight_report_generator`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_insight_report_generator_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_insight_report_generator_agent.py` and embedded as the fenced Python below (sha256 c915c29c6311ad09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_insight_report_generator_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
