---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "fc84cf7ea8d9f0a140a10a5f7199b9267aafff543fe973e715b2f8f476591f0a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.4.2", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/work_brief`. The original RAPP
agent is preserved byte-for-byte in `work_brief_agent.py` and in the RCI capsule.

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

Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_brief_agent.py` and embedded as the fenced Python below (sha256 fc84cf7ea8d9f0a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_brief_agent.py` first:

```bash
python3 work_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_brief_agent.py   # or on stdin
python3 work_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/work_brief',
    "version": '2.4.2',
    "display_name": 'Work Brief',
    "description": 'A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.',
    "author": 'Allan De Castro',
    "tags": ['productivity', 'automation', 'teams', 'email', 'calendar', 'briefing', 'multilingual'],
    "category": 'productivity',
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
        "upstream_slug": 'work-brief',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#work-brief',
        "upstream_version": '0.4.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '669d0b5ee44266f3',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WorkBrief(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkBrief'
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
    print(WorkBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
