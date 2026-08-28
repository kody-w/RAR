---
name: "rar-cowork-cookbook-scheduled-brief-analyze-financial-statements"
description: "Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_financial_statements", "rar_sha256": "09d4cfb68e47b85478b56d2f83d3c9b15fa5ebdbf937ad8f52fe963c3a775a7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 09d4cfb68e47b854…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_financial_statements_agent.py` first:

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
    "version": '2.0.0',
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
