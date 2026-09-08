---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "fc84cf7ea8d9f0a140a10a5f7199b9267aafff543fe973e715b2f8f476591f0a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.4.2", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
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
