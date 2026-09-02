---
name: "rar-cowork-cookbook-demo-data-develop-sales-strategy"
description: "Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_sales_strategy", "rar_sha256": "572f16a9a27f32d7feafcc0e6c488a32f11070ffc039c5f27e748cf3742a5128", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_sales_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-sales-strategy:3218910eb073ed88cc556ace05b8b5bf967a7d05173569375355bb64dc27b4a8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_sales_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_sales_strategy_agent.py` is
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

Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 572f16a9a27f32d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_sales_strategy_agent.py` first:

```bash
python3 demo_data_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_sales_strategy_agent.py   # or on stdin
python3 demo_data_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_sales_strategy',
    "version": '2.0.0',
    "display_name": 'Develop sales strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a8d9b521b60094d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopSalesStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSalesStrategy'
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
    print(DemoDataDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
