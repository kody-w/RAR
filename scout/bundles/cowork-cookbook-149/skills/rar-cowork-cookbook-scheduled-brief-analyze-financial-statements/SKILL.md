---
name: "rar-cowork-cookbook-scheduled-brief-analyze-financial-statements"
description: "Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_financial_statements", "rar_sha256": "40d3a055881074c72cd6a4d5bfef8a10e59d222b34985058bb6d80ff5f647a57", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_financial_statements_agent.py` and in the RCI capsule.

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

Analyze financial statements Scheduled Email Brief — Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 40d3a055881074c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_financial_statements_agent.py` first:

```bash
python3 scheduled_brief_analyze_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_financial_statements_agent.py   # or on stdin
python3 scheduled_brief_analyze_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze financial statements Scheduled Email Brief — Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_financial_statements',
    "version": '2.0.1',
    "display_name": 'Analyze financial statements Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ccaecf3ed3c8bed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-financial-statements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-analyze-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefAnalyzeFinancialStatements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeFinancialStatements'
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
    print(ScheduledBriefAnalyzeFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
