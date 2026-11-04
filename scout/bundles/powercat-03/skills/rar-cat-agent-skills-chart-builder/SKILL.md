---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "f4ed638b191940f09a2bf01dde7ab052dbca6fba9627b2bfb957f3de8ffa0917", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
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
