---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "1ff5ecc58626978dfa6177c233f43cb7f545aec0fd3025735830c380f44b8564", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_test_planner`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_test_planner_agent.py` and in the RCI capsule.

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

Copilot Studio Test Planner — Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner
  Upstream author: Elliot Margot
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_test_planner_agent.py` and embedded as the fenced Python below (sha256 1ff5ecc58626978d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_test_planner_agent.py` first:

```bash
python3 copilot_studio_test_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_test_planner_agent.py   # or on stdin
python3 copilot_studio_test_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_test_planner_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_test_planner_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_test_planner/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Copilot Studio Test Planner — Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_test_planner',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Test Planner',
    "description": 'Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.',
    "author": 'Elliot Margot',
    "tags": ['qa', 'eval', 'regression', 'agent'],
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
        "upstream_slug": 'copilot-studio-test-planner',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ddaf3694d8c2a432',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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


class CopilotStudioTestPlanner(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTestPlanner'
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
    print(CopilotStudioTestPlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
