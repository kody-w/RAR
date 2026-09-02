---
name: "rar-cowork-cookbook-ppt-exec-develop-chart-of-accounts-strategy"
description: "Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy", "rar_sha256": "185904845c3fd992a72ad844de81e8344486010332ff62b9d4fc46c30b0d1fde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_chart_of_accounts_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-chart-of-accounts-strategy:6e5c6444e5e1484dc239e649822602f7f6d9dc5485fa67b2debd44a5d1539ef7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_chart_of_accounts_strategy_agent.py` is
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

Develop chart of accounts strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 185904845c3fd992…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy',
    "version": '2.0.0',
    "display_name": 'Develop chart of accounts strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c821606c5f0028d9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopChartOfAccountsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopChartOfAccountsStrategy'
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
    print(PptExecDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
