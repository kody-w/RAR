---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "48843aa159ca7a02aebbc259496476dc6c4e7aeb87efc227372c9fd55711cd84", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
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
