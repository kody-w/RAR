---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "c3e86bfb91394e7c5d71411fab845e334b0ee2dd85a93e1fbaad9fe40ba07bc4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.1.2", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/process_sop_architect`. The original RAPP
agent is preserved byte-for-byte in `process_sop_architect_agent.py` and in the RCI capsule.

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

Process & SOP Architect — Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#process-sop-architect
  Upstream author: Parag Dessai
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `process_sop_architect_agent.py` and embedded as the fenced Python below (sha256 c3e86bfb91394e7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `process_sop_architect_agent.py` first:

```bash
python3 process_sop_architect_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 process_sop_architect_agent.py   # or on stdin
python3 process_sop_architect_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/process_sop_architect_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/process_sop_architect_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/process_sop_architect/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Process & SOP Architect — Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#process-sop-architect
  Upstream author: Parag Dessai
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/process_sop_architect',
    "version": '3.1.2',
    "display_name": 'Process & SOP Architect',
    "description": 'Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing.',
    "author": 'Parag Dessai',
    "tags": ['process_improvement', 'sop', 'operations', 'powerpoint', 'productivity'],
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
        "upstream_slug": 'process-sop-architect',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#process-sop-architect',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3851098193863859',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ProcessSopArchitect(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProcessSopArchitect'
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
    print(ProcessSopArchitect().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
