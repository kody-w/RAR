---
name: "rar-cowork-cookbook-opportunity-slip-risk-analysis"
description: "Scores your open opportunities for the risk of slipping past their estimated close date and produces a prioritized workbook of the ones that need attention."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/opportunity_slip_risk_analysis", "rar_sha256": "5ec0ee169f8e9f50c7da6cdd75315345e3414593e81afd40688f53f8b7a0e5fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "opportunity_slip_risk_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/opportunity-slip-risk-analysis:618df9345bb26c159819b290f699bf4bcd7ee0e05692cbaed7547220e8f53909", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/opportunity_slip_risk_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `opportunity_slip_risk_analysis_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
