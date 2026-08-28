---
name: "rar-cowork-cookbook-teams-update-analyze-cash-flow"
description: "Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_cash_flow", "rar_sha256": "6b6ecda0bb6a6b92b40400fa34ebd8e78a6bc0e02760e5d638b30d53cd5fe047", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_cash_flow_agent.py` and in the RCI capsule.

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

Analyze cash flow Teams Channel Update — Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 6b6ecda0bb6a6b92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_cash_flow_agent.py` first:

```bash
python3 teams_update_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_cash_flow_agent.py   # or on stdin
python3 teams_update_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Teams Channel Update — Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_cash_flow',
    "version": '2.0.1',
    "display_name": 'Analyze cash flow Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22b3cd7c29aa3333',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateAnalyzeCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeCashFlow'
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
    print(TeamsUpdateAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
