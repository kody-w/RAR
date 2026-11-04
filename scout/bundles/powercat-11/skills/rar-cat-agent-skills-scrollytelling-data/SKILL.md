---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "6f807e260a523b863fa68d29d0842a44b896e321b4ead0fe36cb7bb773d713d4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
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
