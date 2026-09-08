---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "a3ce3929b7708296679c21b8f9a0e58efd70e3cf3c18c6d5e465ed6585c7c3b1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chart_builder_agent.py` and embedded as the fenced Python below (sha256 a3ce3929b7708296…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chart_builder_agent.py` first:

```bash
python3 chart_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chart_builder_agent.py   # or on stdin
python3 chart_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
