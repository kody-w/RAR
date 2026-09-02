---
name: "rar-cowork-cookbook-scheduled-brief-analyze-financial-statements"
description: "Schedulable morning-brief email summarizing analyze financial statements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_financial_statements", "rar_sha256": "09d4cfb68e47b85478b56d2f83d3c9b15fa5ebdbf937ad8f52fe963c3a775a7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_financial_statements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-financial-statements:6d732aaaf22ae89c42091fe70eca135a548c7f64b9d9000a1112bc1754fd05d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_financial_statements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_financial_statements_agent.py` is
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
