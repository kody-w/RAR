---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "d859c727b6e268c23f6f7f423d0bc639d26deaef4653339360369ae84fae43e9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/monte_carlo_analysis`. The original RAPP
agent is preserved byte-for-byte in `monte_carlo_analysis_agent.py` and in the RCI capsule.

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

Monte Carlo Analysis — Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis
  Upstream author: Nazish Qasim
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `monte_carlo_analysis_agent.py` and embedded as the fenced Python below (sha256 d859c727b6e268c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `monte_carlo_analysis_agent.py` first:

```bash
python3 monte_carlo_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 monte_carlo_analysis_agent.py   # or on stdin
python3 monte_carlo_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monte Carlo Analysis — Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/monte_carlo_analysis',
    "version": '3.0.2',
    "display_name": 'Monte Carlo Analysis',
    "description": 'Run Monte Carlo simulations from natural-language risk inputs — triangular, normal, uniform, or log-normal — and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet.',
    "author": 'Nazish Qasim',
    "tags": ['monte_carlo', 'risk_assessment', 'python', 'simulation', 'matplotlib', 'charts', 'csv', 'analysis'],
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
        "upstream_slug": 'monte-carlo-analysis',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#monte-carlo-analysis',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8a9d6a293cabe5cc',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 1.0, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class MonteCarloAnalysis(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MonteCarloAnalysis'
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
    print(MonteCarloAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
