---
name: "rar-cowork-cookbook-teams-update-analyze-financial-statements"
description: "Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_financial_statements", "rar_sha256": "45614052fe1778c05a8735a74d3ccd617ca6e4c56cf7f102681be2c88b85022b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_financial_statements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-financial-statements:c9a17179f3aa12be20614c48f1542f353b7ecd545cb4fe9b8062c969ae1c2ff0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_financial_statements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_financial_statements_agent.py` is
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

Analyze financial statements Teams Channel Update — Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 45614052fe1778c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_financial_statements_agent.py` first:

```bash
python3 teams_update_analyze_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_financial_statements_agent.py   # or on stdin
python3 teams_update_analyze_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze financial statements Teams Channel Update — Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_financial_statements',
    "version": '2.0.0',
    "display_name": 'Analyze financial statements Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60ca8f82f98e1b1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-financial-statements'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-analyze-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateAnalyzeFinancialStatements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeFinancialStatements'
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
    print(TeamsUpdateAnalyzeFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
