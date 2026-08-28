---
name: "rar-cowork-cookbook-scheduled-brief-analyze-cash-flow"
description: "Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_cash_flow", "rar_sha256": "a286d191c2dcc6c823f92bd52949de4bd2fef6766629f1fefd47f37d7bcb2638", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_cash_flow_agent.py` and in the RCI capsule.

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

Analyze cash flow Scheduled Email Brief — Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 a286d191c2dcc6c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_cash_flow_agent.py` first:

```bash
python3 scheduled_brief_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_cash_flow_agent.py   # or on stdin
python3 scheduled_brief_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Scheduled Email Brief — Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_cash_flow',
    "version": '2.0.1',
    "display_name": 'Analyze cash flow Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d5af45add3c1286',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefAnalyzeCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeCashFlow'
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
    print(ScheduledBriefAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
