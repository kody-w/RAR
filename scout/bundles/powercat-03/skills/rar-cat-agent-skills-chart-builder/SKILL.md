---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "f4ed638b191940f09a2bf01dde7ab052dbca6fba9627b2bfb957f3de8ffa0917", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/chart_builder`. The original RAPP
agent is preserved byte-for-byte in `chart_builder_agent.py` and in the RCI capsule.

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

Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chart_builder_agent.py` and embedded as the fenced Python below (sha256 f4ed638b191940f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chart_builder_agent.py` first:

```bash
python3 chart_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chart_builder_agent.py   # or on stdin
python3 chart_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/chart_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/chart_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/chart_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/chart_builder',
    "version": '3.0.2',
    "display_name": 'Chart Builder',
    "description": 'Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.',
    "author": 'Adi Leibowitz',
    "tags": ['data', 'charts', 'matplotlib', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'chart-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#chart-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f32fa164a482da33',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.4, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ChartBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ChartBuilder'
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
    print(ChartBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
