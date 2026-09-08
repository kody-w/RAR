---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "c915c29c6311ad09ee768d4267ba02b6fb91324750ffc62d9cc02c2cb6b5ea82", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
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
