---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "6f807e260a523b863fa68d29d0842a44b896e321b4ead0fe36cb7bb773d713d4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scrollytelling_data_agent.py` and embedded as the fenced Python below (sha256 6f807e260a523b86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scrollytelling_data_agent.py` first:

```bash
python3 scrollytelling_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scrollytelling_data_agent.py   # or on stdin
python3 scrollytelling_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/scrollytelling_data_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/scrollytelling_data_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/scrollytelling_data/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
