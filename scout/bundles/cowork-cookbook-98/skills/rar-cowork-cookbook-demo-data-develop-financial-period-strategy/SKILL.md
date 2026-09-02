---
name: "rar-cowork-cookbook-demo-data-develop-financial-period-strategy"
description: "Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_financial_period_strategy", "rar_sha256": "f792f809cd025f62da0e42bb27ce13f907df0f6b989420c0f557b49523f4d00a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_financial_period_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-financial-period-strategy:3952dc95c9702f7995e3f2a29b5ded1a845395b1942a115980a399f5dc80c372", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_financial_period_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_financial_period_strategy_agent.py` is
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

Develop financial period strategy Demo Data Generator — Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 f792f809cd025f62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_financial_period_strategy_agent.py` first:

```bash
python3 demo_data_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_financial_period_strategy_agent.py   # or on stdin
python3 demo_data_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Demo Data Generator — Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_financial_period_strategy',
    "version": '2.0.0',
    "display_name": 'Develop financial period strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d86657c98515fb2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopFinancialPeriodStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopFinancialPeriodStrategy'
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
    print(DemoDataDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
