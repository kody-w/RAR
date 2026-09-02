---
name: "rar-cowork-cookbook-demo-data-forecast-cash-flow"
description: "Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_cash_flow", "rar_sha256": "f0a6f1df0475af160714b3f1916858e094ed5305e22996303c45dce701426667", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_forecast_cash_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-forecast-cash-flow:5766bdebd33fd24d5924c1591f997abdc38973410e8c6a7f4a9e82be3ec0e642", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_forecast_cash_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_forecast_cash_flow_agent.py` is
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

Forecast cash flow Demo Data Generator — Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 f0a6f1df0475af16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_cash_flow_agent.py` first:

```bash
python3 demo_data_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_forecast_cash_flow_agent.py   # or on stdin
python3 demo_data_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Demo Data Generator — Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_forecast_cash_flow',
    "version": '2.0.0',
    "display_name": 'Forecast cash flow Demo Data Generator',
    "description": 'Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd828a9f6ae88ed63',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataForecastCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataForecastCashFlow'
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
    print(DemoDataForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
