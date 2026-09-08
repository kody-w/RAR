---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "a88c23f9363dafc9f717b4b7d41fbb028c2b909e8dd95bf7fed54e962955dcd5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
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
