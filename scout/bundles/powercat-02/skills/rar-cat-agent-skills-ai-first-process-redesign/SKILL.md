---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "e3d9ccd12cc26c79c1e294a7e0af59f2d7eb628d2366098ee45835223936c01b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.1.3", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_first_process_redesign`. The original RAPP
agent is preserved byte-for-byte in `ai_first_process_redesign_agent.py` and in the RCI capsule.

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

AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_first_process_redesign_agent.py` and embedded as the fenced Python below (sha256 e3d9ccd12cc26c79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_first_process_redesign_agent.py` first:

```bash
python3 ai_first_process_redesign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_first_process_redesign_agent.py   # or on stdin
python3 ai_first_process_redesign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/ai_first_process_redesign_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ai_first_process_redesign_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/ai_first_process_redesign/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_first_process_redesign',
    "version": '4.1.3',
    "display_name": 'AI-First Process Redesign',
    "description": 'Redesign your existing processes with AI-first thinking',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'process_improvement', 'agentic_workflow'],
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
        "upstream_slug": 'ai-first-process-redesign',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign',
        "upstream_version": '2.1.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ae3bcfad1b711034',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class AiFirstProcessRedesign(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiFirstProcessRedesign'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(AiFirstProcessRedesign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
