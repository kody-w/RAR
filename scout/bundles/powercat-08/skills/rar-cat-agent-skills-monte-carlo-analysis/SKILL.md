---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "d859c727b6e268c23f6f7f423d0bc639d26deaef4653339360369ae84fae43e9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
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
