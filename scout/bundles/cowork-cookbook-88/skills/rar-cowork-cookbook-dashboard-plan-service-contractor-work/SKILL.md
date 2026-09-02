---
name: "rar-cowork-cookbook-dashboard-plan-service-contractor-work"
description: "Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_service_contractor_work", "rar_sha256": "4ccfdfd861dba22ecb679a535ce4ab0be29d3473d2fdf52a969b5bdab9675808", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_plan_service_contractor_work_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-plan-service-contractor-work:2a98ad7796cbfa622ba71846214dbd32c2533861f970180c96a9da90ea4a035c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_plan_service_contractor_work`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_plan_service_contractor_work_agent.py` is
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

Plan service contractor work Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 4ccfdfd861dba22e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_service_contractor_work_agent.py` first:

```bash
python3 dashboard_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_service_contractor_work_agent.py   # or on stdin
python3 dashboard_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_service_contractor_work',
    "version": '2.0.0',
    "display_name": 'Plan service contractor work Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan service contractor work - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c792b35c80a9877e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardPlanServiceContractorWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanServiceContractorWork'
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
    print(DashboardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
