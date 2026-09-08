---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "9d5aac2ba3712657aade17d943de5d4935e122c800e3919e3c9202506154441b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_formatter`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_formatter_agent.py` and in the RCI capsule.

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

SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_formatter_agent.py` and embedded as the fenced Python below (sha256 9d5aac2ba3712657…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_formatter_agent.py` first:

```bash
python3 sharepoint_list_formatter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_formatter_agent.py   # or on stdin
python3 sharepoint_list_formatter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_formatter',
    "version": '3.0.2',
    "display_name": 'SharePoint List Formatter',
    "description": 'Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.',
    "author": 'Mathias Salomonsen',
    "tags": ['sharepoint', 'microsoft_365', 'productivity', 'tables', 'data'],
    "category": 'pipeline',
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
        "upstream_slug": 'sharepoint-list-formatter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '081ee2e4c6d01a36',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class SharepointListFormatter(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListFormatter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(SharepointListFormatter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
