---
name: "rar-cowork-cookbook-opportunity-slip-risk-analysis"
description: "Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/opportunity_slip_risk_analysis", "rar_sha256": "5ec0ee169f8e9f50c7da6cdd75315345e3414593e81afd40688f53f8b7a0e5fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `opportunity_slip_risk_analysis_agent.py` and embedded as the fenced Python below (sha256 5ec0ee169f8e9f50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `opportunity_slip_risk_analysis_agent.py` first:

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
    "version": '2.0.0',
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
