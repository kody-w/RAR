---
name: "rar-cowork-cookbook-ppt-exec-plan-service-operations"
description: "Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_operations", "rar_sha256": "2b1e9c5d6d0f0d806f3f11f789ab17d6caf570c4a78bfb1c04f17858e4283cfa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 2b1e9c5d6d0f0d80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_operations_agent.py` first:

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
    "version": '2.0.0',
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
