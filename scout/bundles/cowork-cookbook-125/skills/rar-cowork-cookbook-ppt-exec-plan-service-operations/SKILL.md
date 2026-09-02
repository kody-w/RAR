---
name: "rar-cowork-cookbook-ppt-exec-plan-service-operations"
description: "Generates an executive-ready PowerPoint deck on plan service operations status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_operations", "rar_sha256": "2b1e9c5d6d0f0d806f3f11f789ab17d6caf570c4a78bfb1c04f17858e4283cfa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_service_operations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-service-operations:6a94eec63905a89f384a705809418df6b8236f79ef7145ade5b386797ecda1df", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_service_operations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_service_operations_agent.py` is
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
