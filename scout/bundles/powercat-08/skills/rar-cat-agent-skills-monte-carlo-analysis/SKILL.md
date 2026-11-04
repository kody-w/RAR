---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "f49b373bef4d20968b986d891cefaaffae7ff569a1388820214f144147ed06d5", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `monte_carlo_analysis_agent.py` and embedded as the fenced Python below (sha256 f49b373bef4d2096…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `monte_carlo_analysis_agent.py` first:

```bash
python3 monte_carlo_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 monte_carlo_analysis_agent.py   # or on stdin
python3 monte_carlo_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/monte_carlo_analysis_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/monte_carlo_analysis_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/monte_carlo_analysis/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
