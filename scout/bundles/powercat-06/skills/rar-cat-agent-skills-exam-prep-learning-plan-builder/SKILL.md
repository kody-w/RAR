---
name: "rar-cat-agent-skills-exam-prep-learning-plan-builder"
description: "Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/exam_prep_learning_plan_builder", "rar_sha256": "bd985899fe983b4f68a0f915ee19628c54d774f79167fafef7a7e2866cbe7fdb", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "4.0.3", "author": "Michael Heath", "tags": ["planning", "productivity", "learning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/exam_prep_learning_plan_builder`. The original RAPP
agent is preserved byte-for-byte in `exam_prep_learning_plan_builder_agent.py` and in the RCI capsule.

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

Exam Prep Learning Plan Builder — Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder
  Upstream author: Michael Heath
  Upstream version: 2.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `exam_prep_learning_plan_builder_agent.py` and embedded as the fenced Python below (sha256 bd985899fe983b4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `exam_prep_learning_plan_builder_agent.py` first:

```bash
python3 exam_prep_learning_plan_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 exam_prep_learning_plan_builder_agent.py   # or on stdin
python3 exam_prep_learning_plan_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/exam_prep_learning_plan_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/exam_prep_learning_plan_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/exam_prep_learning_plan_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Exam Prep Learning Plan Builder — Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder
  Upstream author: Michael Heath
  Upstream version: 2.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/exam_prep_learning_plan_builder',
    "version": '4.0.3',
    "display_name": 'Exam Prep Learning Plan Builder',
    "description": 'Build a personalized study plan app for an exam or certification: overview timeline, day-by-day schedule with a calendar picker, domain breakdown, one-click .ics download, and a notes tab to track confidence over time.',
    "author": 'Michael Heath',
    "tags": ['planning', 'productivity', 'learning'],
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
        "upstream_slug": 'exam-prep-learning-plan-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#exam-prep-learning-plan-builder',
        "upstream_version": '2.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'afe330883bb69ced',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.75, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:planning', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class ExamPrepLearningPlanBuilder(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ExamPrepLearningPlanBuilder'
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
    print(ExamPrepLearningPlanBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZOjSLblX2GiP1TWIzNYhFiyrc0GkARIAiEkBFJlWRaLs4hV7Kim/vs4CmVk1nvVr/uZzadRlWUIuH79rudcD+L3F6dtoqJ6+fyixl7kgBSRgdNELx9ffFB7VVw2cZHDp0Ibpz7iICWo6iJ30vgOfKRuWn9EytTJEacskaCoEPgVDE6GwK8eqJo4iD1nUvEZKTpQdTHokSbOQBrn4CPiO+Mnd/wEfyC1FwG/TQHSx00E9/GcFOS+UyFl7CWggrJF5sQ54lbASfyizz8iRQ4+eSl8jLzGXo1MN9PC8T9CGyZL86IBNdI4LtIUSFM5UM4r8iD2Qe6BhzUPS16hq5PFZQrql8+//PrxJYbfXz7//uKlTg1vvSzhU70C5RY4VR7noQ79fYQDVHAtvAihUDnCMObwGgYIxiGDt3wQIM+rDzVIg4/If/xH0jtVWP/8+UuOPD9fXqb/jDZHmghAU526gZH1nNJx4zRuxleET3tnrJEKNG2V19CzuqmgGa9vK79rKkrkH9OzD2+bvIag+fDlpYAmPDLw5eXnKStfXqp2+v46aSk//PyaFj2oPvz8XU/dulfgNZMyaPXr1+f1Uy0U/C4aB8jXg74Un3tVwItLAJX/4N/0eTP9qe4Zkq9vwh+K8iPy15onf/4B7X0rRBfq/Wu1MAZw5cvrtYjzD889Kpjf3IGJ/vDzP1MLC85L0rhu/i29v7wpjoAD0/7hGZKfPz7S9yuCPn171/nPt5265X/iCRT/tt17oP6Z7kdm/5PqqdPq91z+pbq/WoD+A/nln/r23y34iARfXhawwWGDOW4KPiO/P0rkl5/87zd/+vUPqPpfqjkUbeU9NHzNnDwOQN18/frLT/Xj9k+//vJTW8IqBk72ta3Sv9L5V3F97POnCD6lPvx5LdzfzJMcogry3kPI70X5v6o/XpETRED/+/36M/JjJ04fFJmc+LbpWwh+6MYa2vpDHH9++QMCTw69ab3HY4gff/sbAjG5KuoiaJCDV7QNAhM8YdZk/DGKawT+P6FGBWBc6xgG9ikH63/K8GRxESC//W+IwZ+cEOTNpzqJ07TGJsSDXQLKr+kT1R6l8dV9w7XfXpEj1FtUcRhDsEcMXte/5A8N055wYQ3BHOKUOzbgE2znT9MXBOLzb/9C89eHktdy/O0B0/Eb7BmiMkFeDQngdXLOikD+dMV7MArwWqg/LSAtIEEMofojdLou0g5C5hSIh1uIH0NQaYpqfOiGwfo8Kfvtt99cp46+5G8YPUPeeK3GoMC7OcinT9DoII3DqPmSAy8qkJ9+/+Mn5P8g/92qh/JpDx1SxTMV0ML1YachsLXaDIrBLMG8Qtx4pOL3P56xhWpySEEwcZAjwdtiWJoJ8L8F+iDzn8g5jbgABhgGNysLSKh5iMTNK6IEyLu9cNPp0UQNUVE3iA9KyJ2Q5kao1YHuvEcSciJSw/qrg/Ej0tbgsetvbuU8TMxgjzvNb4gq6pCIinQizupJTHBxkUMuT9/L4O0+VFL9VCPCNxWviDYVI1I6lVNGlfPcI3De8jJNCM/lUDkkadB/ySfCBVOoHp3xFh4oBCPjPVP6aco5pO8MwoBff9v7IeNMdHl80Gb1Ja+fVe9UUyq8ieVHJGxjf+KCvz9Lqo6KFg4zU/ymIQBqembBf2blUYMT7SMT7yPfiB+ZmB95Uj/ypSVxgkL+/x2MpiDwkmQsJf64XCBL7Wic35IDxZspiW+zIxxSHh4+GvH74PINnL5h9Jc8jWGlVePf3yQfKX3KvOFeW8HQGbzx0A99goZMeh/lPpVvVU2N4nzJv5EB9Ah5IB/MOMQG2DuTS982nJ5+szSCADBdfx8MHuVR+VNMYEkjZevCiCEBAL47RaSJqqlln0mGtQ+m9u0jOCT/ySsEaoclBvXDsENT4Y8+f4ROK6CbsGiCqsi+i8fTIAet8FsPWhuBCrwiFuy6qfJq2OpwGptkYBR+eqhCMgBjDE18j3AdOeWbMUWVfDPQgU1fx2H+Y/yfj753ycOSyXio0/GdBkayn0DbB8NbXt+tfGYKmjrV1luO/pzsp6fIj5z19y/5w8J3noC1mk50/0NoENimWf2oxAntaohYGXiWD6yDB7O/vpHzG/u/2/IZEfkjwr9B44PFkA/ZN358UKn555x8RqKmKevPGPYu9hrCJmrd17jA/gsl/m1qz4kEyk/fmOvT1MGfnsz1px3egvEZ+dOh6U8Sz7r8jJCv+CsxPdrG3qPDnp/PSJu/486HH74/8/bIC4Bdmz8AFdo1lWgN0eAxvBjge2KhNRAEmgme0xFy8jtXfROBhBVWIJyE37irniivhyz70A1D/yV/T/6zMaBjeTgRbV380LAP0oapfMvUO6fAR3kD9/anCS98HKrSyd0avHzO2zT9+JI7GfiXh6mJNWBxwtBNBzDYJuUEleBxBVsZGgjLsXlc/vl4unt8cdJXRHYm27/Lfgun2/rwkPJxAuVmOn9A4IQN/ga3kFjKNJ5QYTK8GcvJ0rdT1jSXvQ9t/3XfR+tCzPGLz1MHP9TDf99n5WmXt9PL45yZt/Bg+Ms0p0/OQlH44132/cztgpdf/8KM59j+T4yIJ/SY8OYNCID/F65AJRW4tZBS/cmM735936542+OPh3nN20n295dvgPHMynO2hOKwMz/VE6lixCsON4TXbwUGn/2Pp87neghwcOyBClyfY+csxwWAY2cuFdCsgwccMQeA4GiS9eaUzzBUwHAEzQROAALGYQDJ0rTnAibwXajvrUy/TpNDPNnkenhA0BzBQqDnXJKc0TgL8GDGTRpoMCOBz+I4/sPSBPbh09E3x6Yovg/AU0Ce/v7+4tIUlJSpWuHfPiKGnhxstnXHtYzmODsIGCeo8UqAG9l3X85b7kR3btt6lXIbqbw6ZMthT/LFMdyLpJDy2hLNTwIVH+dh3jocI8Q8H5bb+ujcDvmySU1PUI84hqF6VUlHygiw/J5j/HVWkn5ONaLBgdtNoE4SOVtZsb+htj6uoIcThNb5uFJSv6zVimWAKLdNgh+LdI0Chmq0tNvgON/QrBT0xna4xDPCkspldb6vfDKrT/igGRdxu76IA64ay3Hma3RB9442OMZRBLi/XQ6HMHVv2n2ngPlls6VI8+ZTtWBdNX+uKaJzGE2jvgTHxQDG5li3+pbdy7nnXu41s4qodkbNRZwUjJVeYhrQ+axmbXak/UAvmyZdjpvrObxfTMtZ+YslUx6iNIiC07pcHrWApOKZ3gxCn3s2Qx9oFq+tzFZMOhuyy5zQDwfRWatXHdu4e5d1uXgNcKmuKGUI/Ivq2NyxElWVL68LdWjmZwK2zG51Ot+0XTsMzprIVVHYUglmMtrs0s4zVw/qW1Jbpo5jl9sMIlxdNerVu9njZZOlh/zE1mwC0vFklY6jZot+1ndlmVPUOHgno9IqJaXubLdQGEw54xatu3dZT3WiNhaGEV3iG31fAWzDbERCNc/7M3ftzQ5dYst1Nj90rb8TJCXD1GDb0Fvp3NKLw4LfypaT4ma/wpfnqJZ9kTlX/rIjV7qlVLwAxq1u3grBArF9PB9WanYuCpKcp1JaD0m2yU8JzdX34IoN28Cx40ry8L1jE33UKh5ds4GnOjlKLqWZQV/cgMWC/iIs+QH01DWWl2fTZXBjOGbqZjsnjcjAUH8XzKyAz4Odf9SPGK+kteldmP3+bItSkmT75VLUlbVwspLjRralK3O0zsW+W8mZcat9Sj5UyxIXAbmZ5zRDmlh/0Jpb0S73FoMK90pR93BpvTz0yy68XOsRPxi3UU0aj1+jvOvJprO2w2YfEZf9nvWNeIEqvMQLq/A2hxGpr/yBopXaBs25vKxi9xQfvQVPoSjN+DSK7WYdhkbdgDZBN8OI2ahlq35vQqHwgEsEXoOAU/1hqZZelfv8HVtapQkcMpRcd+9sDFJysSLFM4cPpXS1MqQm1HDvHteHVbG3Nka9U7QkTZyClghZFNecUPIRhys3qYz2xfrW51xdErfdLL3QbiFanOy39dY38djR4qtyTO64BFZ0exbH4RSXIDlKhXYTxUTWjptUvkjVaWvMOysI90l2n62jKovWNtOY5bUmhpyM7tElIwdGUkZfKUp1VXoGp/VFSG5n4Z7nR2mxOsQ2DOwlRHHVErRRdIEmwDgxiZsf1wvdrtaFWbtbepPNnHxNLYT1wRAul2hlRrm43g3bnREajBmeItSXya7ppDZUEuvg4ZXb2nMsLMRLzltXcvAWRDEYBrPoEvzQUpqz0M1DdNcuIylKbUXPzpdVB4flEyqgxmolXURbX8hWKc2BbJN2OQ5zvpPUu+zQdZRoaW2fqTt29OutMBtr426GbBi6OcHHxzDxysGkjnFqlwPlZX1N7dj7qhp43oztGIzW9mjv+Cu7nN86+cgKcGjSTGM932LaACeIq6z4TJQQeqTes3W32VQgbpSdlC4h6hxZsBCosqfRSCgVD+MbSU66U7jfGq1XXBtzf1KXVUHPi1pslbSoave28y5axJh65xp3lkxXVLmjllcpSdf3eDvbAW5PHfbiGVvetq6AX6V1WrU80deB4KVZSs2U0i4qlwc4pahX53C7GUdpfc797M5KSe8B7tieTtQOuye3q43z1V07eA7Wt5V+Q8EAZz3UJs5bXVkE3PGYVrt0hXVqDKpTtOIOOEFcziea3QLLHth8rZCjVS0OfkxrYoUvAl7Qb4zXCD1l+RGLFjd1Vh9oWhlv+yNqLSuxJK1o5eAOv04PWHsPJOx0vXkSnG1vXHE27cbS+XsWHkN5Tsv5sOKP5gLzLSPGtvxihosaERRyUQUAjYIhKgS760FyJhSNyQ1DTl11Nx+p/SkX2y0QuUZcRZvryalUxSCHPt9vtrhrL0WCoDJjTIQtPXhRzy5HW5wPkqkxaXTVsNwpKayhzamI5+y501zc8TvtChZjL3Zme9bPquBaeXJhl6mJD6lHWlqcdQdNWahawXCznQl0ZS7ezT6ENbk7hFG8vdRNr4ZcP5xPLduzaXshN86VjFdS0RqObmMotwZYsJ07GNgGBVGFtmFFJ3kX+aFck1qBqoWcMWYhtKo1I5tQFA9os5lTWFpX9c29HDIiWNGbAj8tz/xqGWnxQAvFYGK7UbHiYGNck+sxvR0YOd0vsXVFF0cvTizTcd2eZaJ1cHHTXah7drho/dhIgLrbneNzXew59s6ejop5D2ycVLcz5ZDb6danBrKY8RW1LzxxQ2am3gs9GM9haYg9zhb4WmQcVD+UjHeiCM3ZJTu/VYWIv68HWUVlSKaosDTXHcv2JpU19LBIRlNgr6kRxKchj1Tx6jZEdhluqLZ3TvnBY/Coz+9kiw5WUadZIkLsA+MmzRdr8yocTHIcCjBwCipFi704v6xQ2UXrdbbmj/5e4gevNQ7nJg3YxTCvcVGYF/0KtMplHA4XvwWwr+O7HlH3WNrxoi8UJ/x0wwpf8DbO3oiDwqSbyLye5uimb6PT4XxqrkIslDt7hYLGTqmlK8eQAzfkiWrUWjD9ouKWaXOBxL6PL8RyE5aMFbWrxWZ5ckmRLT1Bs85HS9sM3nI+qqrg4JJ3HkOt2F7Pc/KmrOVDkvGFSTGq31ZhNIuLC3ZIeH8UyQPE+2I+hM0mznHugN7YML3fz8neAubxKNYb2bmM6zBT1JynvOS09hSGMuPZBpbX2Q43KMso1pK8c6dKiTcbzYss/JYt7NuZnQcbXbjtqgES0zoUNgIutrOOH2erkVek8XT3pJQ+DYcDvdwplOpZ9LjR3SOlddg4E40kVM6l5Cxlcrfo6riv/HxhE015Ndt7VujkyjXWtQorDJVR7mo2TX00+dRWvQWn8hQZnrqNV5eHJKHbXtQWsH172W3kxcI/1+FtiXHOxp8ft8XMw8u7eza1E1kXerUZ1H0ncWu9cjyxHOiTeeHveK55B9GgJc1D+2qsnF6bqwurEa3bHeOH8QBtEjTduDa9n23uciufTUfQKEGvsDOOx3yy9TBpKewXs8gp8Oq+TvJLcuaohDlbuidfPQE/eDFKZmQ0YO5S25xatGgTwttY9ysQlBUr25vZ5ZpW8ExFudHNGTzTpmlu0y7bkaE1zQTHKirG+O6ou7RdJYU7W1vX7SpaAan213xgsGlYGWkhLudriqnORg3DF2HZjrvE+OZce1kxxITA95Z/kywcdupm6BcaE1VpnxOk3Q6GPWizhVQ2vdShfIEmJINFu5LdaCERFc0ySr3WIfZzdHWdi9c05C0yAgqRkCtA+meuRMd5pp5Fm8wORbGkzy41JzMG7/JhX7LLc8WCNl/JsXqx587Jnkfj0IAbHcPimG3uguWsvWbdey26B7fYDfgt5xhYap1VXjfaCHOEzWLOEYl5UuwDLi4Xiyjqa1QXQBERtni2WpLsmWGZCGFe0hiFL46HW1Z1a4PCDc7kTNL0gySjXaM4VLRZ+DucT/vG9g+nkbCvaDoMtsdcxSBZV5tZtXA3zna3XLSY4S5C6nTyO4uwZvSVq9qLTtI4ZZNgGLZc3a048lKZzqgy8lBdW1012UgjSXjrGpgz6drF6bXrnSM1yEp7GWhzRx/bOprvyL7GGn+F36q6vVbabZVAQsU2CzizbVxlntuzQeogq4UAT8Va2goMVXckzjbSFeflBuXsch+wYG973KnzOYcdOceddVVeuyrK7pRTGaNS6DXFFhiWygSwd+50xW39Rlrb+549czhoOMUD7PY+HzsfjShX1E8x8P3bnTjdUjkc6G0uamM6Uofd+hat4JmmEJxN2DOX7rJSDkcVDi2jxw46bxgKU2biWRliea4OqGZxOk7WpCcz+fm2UfCbXTP0YqjPhrfP6oUBh4Bqloq74hKaHskpmW33MplkbkS6TLYgqYISBSXLqI5VW/gJyeJAYUG8KGQNR2lHzFcY2klJGcibcDWiqzXY6m3DXFtMsbbi2WeJVU/Q6Gpr6deYkGm0xU8y52JM1EQi728KQq55WDFHgkJXeM801e5qoefYEFPGNcF5kPHawSmVbAIwst21mN2G1GxZXZGugKQSMOPa1Qm9ZqYodoLtdmfWUuIgZhsCHjUavzZ2RaaxW1IZdoulH/F4siz3Oz6vpHoxcHBsc5VbCqqS6auDthWw9Zjd87HwBG/V8Fl+NcnretbTrngfNnkj81p+7FNXQIOlvh2LlGGr/M5wVFHDRsblW5RUd3uveGvCBrQum+Ge62/xuhj0S9Inlp8bZ3+5W3EWm51Wp3vb3ZdXhlXvVYhRYZ0Rs54MZK9ctQrJ5s5OivPMCJ2tcVQLmtFVZZwnSmHYGZFTCuuuPDfckVdn7nq4q90SVfGYorzqvEzL0cyNrtWGWsg4R+wi3e6dbsEZViCwsEWGGQ3i0PY3jiaFgUecDWnHDRZqiU6PpS5MvLqnZsd14VxHwgmJkYMB6sVix/szEBgrT4gGKuTHOugX83RnMNaeta/9fqN4GXrT2pGI7Zaw2qXJKtu9brDyGdUknMvsS7dmLH2943xiTgjjmWaBBGQca5yI2TcOzdDVWuZYg531xu7mumxgHGiQb3NjR1cri8SEOzbcr9t67Fqh6+aCh6aoWUcnv96dw+zKm9hhGeGNGRDdRSJsOV7Jx8ZzBom9zrsdtnRPStAaMlPuKT/VeKvfMEddrTRs3cf2Xdrfkuh03Yz5QbdFUMEZB4bitJsfa7RA01SGh+il6JJ8qNoVnNrORCRuG5wTrsuFY4cXTZRkVNzYRw+9qMqexT3aHs/HHqMk0iC2lwKFVLlLF2h3blUK3Wo3fIZnJImP3YLkS1sqGG1DD9kRJU7MakZ6gHFWLq9hQ5zrw16UEzkPO/e21NHaQ68LvDVI2tRJNGcjnd7ebVXGj+6pPdlRfVs0jKO3IwyYFt6XOzvYRTs6wQfRkoIVyTSZK5lzb5YEJcDPt9nNn9E22Dgkz4E8Sh2dEq9X1Sp2jnJUATfi6iKCs93RvRN8HefR2C6YsDmwVkOZTbWtZFNanGqv3KJaFXUZFjtL+jAjxgFw8LhUbByrpPt9sCN2aBuZaTVXb0rdNk5f6GttFkX3VTlo1ootyMQDHSNr28C7zxV5d0n3FkHutOtmR4b3RdC2TH/Lwa4DeX7uDrvNuRs6x9VvxA4sx8vYC+USvUV3RbS8BVmP47h20tMe64KBYAuJ3eCrQKNVhlilShv1+HrgmnabmDbp8NBiRZsZVdByPb3b6nZeVyFrW5y9DDaY2Y34OeUiSQ9WEqxTRjnExMY7g5WUbFY3Wm2jI2POMW7JHojGtLxjJMCzl29y0ux2w5vt3PeSFM138uyiJM0+3GnQ3kUVz9L6KNsrnFNunHrmlFjcW+n8uhQScieaIoiz8ybbrm1Cw2RqoWxWbjgE8rlsBo+l++3yPM+9HRNj5M5ud3OcHl2/IvmgKHFNYc/0dbc59vpJIFzKMWYE5m3t/gjkG7deEFzG6rMZH/Qn4cBI6lwhDwvUHV2667DTadnzp/6Au1gY+wN7l2CAgN5WhE/fqD2Na5V36VKM3IYt5E1DBfKcje9a45d+pQNKCeBhY9N7XRCSOV4pKmD33X0hryJGb501qXKonxwXYSHQQe4bQWek15PorY/tvOGora93ZRXpFHWrD/v9wmQgijV91vLjmrqVbaiqKenLXU9vnDa2vcaqr0vPH7ao3cPhVT8IkenrW6rIR9G4g8rboJS5vd8OxIztSdyhINb5GKlwW/1gzvIhmy2ShilP8/Z29RQ0Ta4cYFJ2xa0DdRC3gDrhW6h9XxVSK0dFd+3gMMEFQcfPWSnl594A8mrEeNs9bfKRPs2knIt8+RhcgpCqBBFi4iEdOXugdJZfX25mc+hnPM//4+Xjy/Tm5vn+5d/984zpF+D/z34P//Yr829vXh9vQIDjf37s9fnftujXjy+VF0N73l411GkbPn8x/59fNHz6F6/yptXj2x88TO+Hh+bbS6rGCac/Any8mplWvTzs9qf3m13cTEH5pm+y5vmKDxpBveKvs5c//i9YgKDZTikAAA== -->
