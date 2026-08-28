---
name: "rar-cowork-cookbook-ppt-exec-plan-service-operations"
description: "Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_operations", "rar_sha256": "b384cfc5e105df8da2fb09beb0b2553d18fdfaf29c5a8536fef647fc120f3484", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_operations`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_operations_agent.py` and in the RCI capsule.

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

Plan service operations Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 b384cfc5e105df8d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_operations_agent.py` first:

```bash
python3 ppt_exec_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_operations_agent.py   # or on stdin
python3 ppt_exec_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_operations',
    "version": '2.0.1',
    "display_name": 'Plan service operations Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8036b1d6842fba05',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPlanServiceOperations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceOperations'
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
    print(PptExecPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
