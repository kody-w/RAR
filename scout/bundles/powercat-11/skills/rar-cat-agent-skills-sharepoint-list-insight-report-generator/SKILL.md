---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "29a7c49ea3bc92bfb00f7b609f89aff2c1d0b85e5e6323b8e64c38353388513e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_insight_report_generator_agent.py` and embedded as the fenced Python below (sha256 29a7c49ea3bc92bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_insight_report_generator_agent.py` first:

```bash
python3 sharepoint_list_insight_report_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_insight_report_generator_agent.py   # or on stdin
python3 sharepoint_list_insight_report_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/sharepoint_list_insight_report_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sharepoint_list_insight_report_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/sharepoint_list_insight_report_generator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
