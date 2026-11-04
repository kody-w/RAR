---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "1ff5ecc58626978dfa6177c233f43cb7f545aec0fd3025735830c380f44b8564", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
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
