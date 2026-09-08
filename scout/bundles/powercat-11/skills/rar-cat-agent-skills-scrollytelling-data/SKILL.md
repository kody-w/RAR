---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "a88c23f9363dafc9f717b4b7d41fbb028c2b909e8dd95bf7fed54e962955dcd5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/scrollytelling_data`. The original RAPP
agent is preserved byte-for-byte in `scrollytelling_data_agent.py` and in the RCI capsule.

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

Scrollytelling Data — Turns data into a scroll-driven HTML story.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#scrollytelling-data
  Upstream author: AndrewHessMSFT
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scrollytelling_data_agent.py` and embedded as the fenced Python below (sha256 a88c23f9363dafc9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scrollytelling_data_agent.py` first:

```bash
python3 scrollytelling_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scrollytelling_data_agent.py   # or on stdin
python3 scrollytelling_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrollytelling Data — Turns data into a scroll-driven HTML story.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#scrollytelling-data
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/scrollytelling_data',
    "version": '3.0.2',
    "display_name": 'Scrollytelling Data',
    "description": 'Turns data into a scroll-driven HTML story.',
    "author": 'AndrewHessMSFT',
    "tags": ['data', 'visualization', 'storytelling', 'reporting'],
    "category": 'pipeline',
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
        "upstream_slug": 'scrollytelling-data',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#scrollytelling-data',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '0b872fe30f38e4cf',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.8, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data', 'tag:reporting'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ScrollytellingData(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScrollytellingData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ScrollytellingData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
