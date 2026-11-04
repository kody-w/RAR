---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "84d48403786831ecf324b56d1a8686cd7b9ea6797c0a356761ad9295533b4dda", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
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
