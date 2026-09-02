---
name: "rar-cowork-cookbook-scheduled-brief-analyze-cash-flow"
description: "Schedulable morning-brief email summarizing analyze cash flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_cash_flow", "rar_sha256": "5cad100794689bb9a0ff2a8f979a2ad257c0014d3f56f73a6777410bc6fac048", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_cash_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-cash-flow:e9a7a79b62c7cb3311d5f4587acacb0e745bee6ab3814b78a6851a9e3dc20aab", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_cash_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_cash_flow_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 5cad100794689bb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_cash_flow_agent.py` first:

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
    "version": '2.0.0',
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
