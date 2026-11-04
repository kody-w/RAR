---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "3b957309d4ac4c7c604387d0814fd917c04feedd0f453bd24b110ea15152f1d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.4.2", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_brief_agent.py` and embedded as the fenced Python below (sha256 3b957309d4ac4c7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_brief_agent.py` first:

```bash
python3 work_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_brief_agent.py   # or on stdin
python3 work_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/work_brief_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/work_brief_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/work_brief/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
