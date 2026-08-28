---
name: "rar-cowork-cookbook-teams-update-analyze-financial-statements"
description: "Drafts a Teams channel post on analyze financial statements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_financial_statements", "rar_sha256": "5a2ecbeed39dd392fe7d88319fc44b5de576952f946bf60304b5c06bc244fa59", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_financial_statements_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 5a2ecbeed39dd392…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_financial_statements_agent.py` first:

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
    "version": '2.0.1',
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
