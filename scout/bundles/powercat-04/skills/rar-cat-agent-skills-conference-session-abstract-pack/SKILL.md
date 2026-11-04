---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "84d48403786831ecf324b56d1a8686cd7b9ea6797c0a356761ad9295533b4dda", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/conference_session_abstract_pack`. The original RAPP
agent is preserved byte-for-byte in `conference_session_abstract_pack_agent.py` and in the RCI capsule.

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

Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conference_session_abstract_pack_agent.py` and embedded as the fenced Python below (sha256 84d48403786831ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conference_session_abstract_pack_agent.py` first:

```bash
python3 conference_session_abstract_pack_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conference_session_abstract_pack_agent.py   # or on stdin
python3 conference_session_abstract_pack_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/conference_session_abstract_pack_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/conference_session_abstract_pack_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/conference_session_abstract_pack/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/conference_session_abstract_pack',
    "version": '2.1.2',
    "display_name": 'Conference Session Abstract Pack',
    "description": 'Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.',
    "author": 'Simon Owen',
    "tags": ['writing', 'conference', 'abstract', 'speaking', 'content', 'productivity'],
    "category": 'general',
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
        "upstream_slug": 'conference-session-abstract-pack',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '79b0788cb04dc619',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ConferenceSessionAbstractPack(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConferenceSessionAbstractPack'
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
    print(ConferenceSessionAbstractPack().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
