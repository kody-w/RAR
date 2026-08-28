---
name: "rar-cowork-cookbook-opportunity-slip-risk-analysis"
description: "Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/opportunity_slip_risk_analysis", "rar_sha256": "2a5441efdb6c225cf16f8df58424947276087fe20ae9322d54572edee99fad47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/opportunity_slip_risk_analysis`. The original RAPP
agent is preserved byte-for-byte in `opportunity_slip_risk_analysis_agent.py` and in the RCI capsule.

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

Opportunity Slip-Risk Analysis — Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `opportunity_slip_risk_analysis_agent.py` and embedded as the fenced Python below (sha256 2a5441efdb6c225c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `opportunity_slip_risk_analysis_agent.py` first:

```bash
python3 opportunity_slip_risk_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 opportunity_slip_risk_analysis_agent.py   # or on stdin
python3 opportunity_slip_risk_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Opportunity Slip-Risk Analysis — Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/opportunity_slip_risk_analysis',
    "version": '2.0.1',
    "display_name": 'Opportunity Slip-Risk Analysis',
    "description": 'Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'opportunity-slip-risk-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/opportunity-slip-risk-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd47a601792a90804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/opportunity-slip-risk-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class OpportunitySlipRiskAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OpportunitySlipRiskAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(OpportunitySlipRiskAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
