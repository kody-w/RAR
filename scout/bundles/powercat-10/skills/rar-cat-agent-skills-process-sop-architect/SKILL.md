---
name: "rar-cat-agent-skills-process-sop-architect"
description: "Turn process notes and transcripts into an editable SOP, process map, RACI, control register, improvement backlog, and polished PowerPoint briefing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/process_sop_architect", "rar_sha256": "c3e86bfb91394e7c5d71411fab845e334b0ee2dd85a93e1fbaad9fe40ba07bc4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Parag Dessai", "tags": ["process_improvement", "sop", "operations", "powerpoint", "productivity"]}
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
