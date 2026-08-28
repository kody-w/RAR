---
name: "rar-cowork-cookbook-teams-update-analyze-cash-flow"
description: "Drafts a Teams channel post on analyze cash flow status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_cash_flow", "rar_sha256": "08d4da8a274f3ddcb317f89e4c6fa7d36e1eaa607db55f2cfb6adb2a5fe93ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 08d4da8a274f3ddc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_cash_flow_agent.py` first:

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
    "version": '2.0.0',
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
