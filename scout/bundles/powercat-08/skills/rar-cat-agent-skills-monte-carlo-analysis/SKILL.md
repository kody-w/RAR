---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "33b7c20af7270399ddff663b9d1f2e284248d5d4d316cf53a57fb526dbaaadc0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `monte_carlo_analysis_agent.py` and embedded as the fenced Python below (sha256 33b7c20af7270399…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `monte_carlo_analysis_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
