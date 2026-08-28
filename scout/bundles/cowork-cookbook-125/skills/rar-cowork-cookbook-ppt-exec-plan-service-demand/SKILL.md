---
name: "rar-cowork-cookbook-ppt-exec-plan-service-demand"
description: "Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_demand", "rar_sha256": "eaca461f6105b4ed21641defd623016cbceed94ad51713f01fed19a766f2d4c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_demand`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_demand_agent.py` and in the RCI capsule.

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

Plan service demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 eaca461f6105b4ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_demand_agent.py` first:

```bash
python3 ppt_exec_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_demand_agent.py   # or on stdin
python3 ppt_exec_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_demand',
    "version": '2.0.1',
    "display_name": 'Plan service demand Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44163428fdb76af7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPlanServiceDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceDemand'
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
    print(PptExecPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
