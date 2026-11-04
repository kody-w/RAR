---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "3b957309d4ac4c7c604387d0814fd917c04feedd0f453bd24b110ea15152f1d2", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.4.2", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
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
