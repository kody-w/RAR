---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "48843aa159ca7a02aebbc259496476dc6c4e7aeb87efc227372c9fd55711cd84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/idea_refiner`. The original RAPP
agent is preserved byte-for-byte in `idea_refiner_agent.py` and in the RCI capsule.

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

Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `idea_refiner_agent.py` and embedded as the fenced Python below (sha256 48843aa159ca7a02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `idea_refiner_agent.py` first:

```bash
python3 idea_refiner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 idea_refiner_agent.py   # or on stdin
python3 idea_refiner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/idea_refiner_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/idea_refiner_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/idea_refiner/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/idea_refiner',
    "version": '3.0.2',
    "display_name": 'Idea Refiner',
    "description": 'Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.',
    "author": 'Mathias Salomonsen',
    "tags": ['productivity', 'planning', 'decision_making', 'refinement', 'brainstorming'],
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
        "upstream_slug": 'idea-refiner',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#idea-refiner',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f0afbd6c6948a24e',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:planning', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class IdeaRefiner(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'IdeaRefiner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(IdeaRefiner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
