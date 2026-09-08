---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "a3ce3929b7708296679c21b8f9a0e58efd70e3cf3c18c6d5e465ed6585c7c3b1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
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
