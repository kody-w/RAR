---
name: "rar-cowork-cookbook-ppt-exec-develop-chart-of-accounts-strategy"
description: "Generates an executive-ready PowerPoint deck on develop chart of accounts strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy", "rar_sha256": "185904845c3fd992a72ad844de81e8344486010332ff62b9d4fc46c30b0d1fde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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
