---
name: "rar-cowork-cookbook-ppt-exec-plan-service-demand"
description: "Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_demand", "rar_sha256": "6ae6976e40f00d2607c0c1cf796cdf9a080cd75c9f1ef287d9ea0d0f10cf9050", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_service_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-service-demand:9ce6cd5bf6c40e691497b6a6bb0f90b3cebadc3c1300cda180e98e079aff5a41", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_service_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_service_demand_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 6ae6976e40f00d26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_demand_agent.py` first:

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
    "version": '2.0.0',
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
