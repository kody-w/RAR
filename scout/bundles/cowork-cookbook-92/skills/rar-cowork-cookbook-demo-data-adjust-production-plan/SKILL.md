---
name: "rar-cowork-cookbook-demo-data-adjust-production-plan"
description: "Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_adjust_production_plan", "rar_sha256": "44e7c2e5bd36db3417edee3675d28801fff5107359eb988fb0ce049c57b57985", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_adjust_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-adjust-production-plan:0c3fab1f6a9db160e5ef877e50c53c7154a08d62affe5a6b3fa9aa2ae6479153", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_adjust_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_adjust_production_plan_agent.py` is
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

Adjust production plan Demo Data Generator — Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 44e7c2e5bd36db34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_adjust_production_plan_agent.py` first:

```bash
python3 demo_data_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_adjust_production_plan_agent.py   # or on stdin
python3 demo_data_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Demo Data Generator — Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_adjust_production_plan',
    "version": '2.0.0',
    "display_name": 'Adjust production plan Demo Data Generator',
    "description": 'Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd097dae42363ef4c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAdjustProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAdjustProductionPlan'
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
    print(DemoDataAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
