---
name: "rar-cowork-cookbook-demo-data-plan-production"
description: "Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_production", "rar_sha256": "255c03ce65162253941b8f466a4c8a3368af1b65c79963c66432d888574aea84", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_plan_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-plan-production:de26f4e879633475a2ed93885245cbccd17ea906e5f8aa4563b3b8dadcaddf25", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_plan_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_plan_production_agent.py` is
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

Plan production Demo Data Generator — Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_production_agent.py` and embedded as the fenced Python below (sha256 255c03ce65162253…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_production_agent.py` first:

```bash
python3 demo_data_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_production_agent.py   # or on stdin
python3 demo_data_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Demo Data Generator — Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_production',
    "version": '2.0.0',
    "display_name": 'Plan production Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8672439d2d608843',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataPlanProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProduction'
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
    print(DemoDataPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
