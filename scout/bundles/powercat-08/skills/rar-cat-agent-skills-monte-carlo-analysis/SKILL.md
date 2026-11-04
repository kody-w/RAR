---
name: "rar-cat-agent-skills-monte-carlo-analysis"
description: "Run Monte Carlo simulations from natural-language risk inputs \u2014 triangular, normal, uniform, or log-normal \u2014 and return percentiles, a histogram PNG, optional interactive HTML, and a downloadable results spreadsheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/monte_carlo_analysis", "rar_sha256": "f49b373bef4d20968b986d891cefaaffae7ff569a1388820214f144147ed06d5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["monte_carlo", "risk_assessment", "python", "simulation", "matplotlib", "charts", "csv", "analysis"]}
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
