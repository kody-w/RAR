---
name: "rar-cowork-cookbook-configure-plan-projects"
description: "Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_projects", "rar_sha256": "aac6b33a0290b7e8ad59ce0150d41ff1139c808be6a93488322f20399259df37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_projects_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-projects:21232af69ff37ee41bc70a7d2431842e364d477f2df9b42b4ce5fb5371771c83", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_projects`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_projects_agent.py` is
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

Plan projects Configuration Bulk Setup — Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_projects_agent.py` and embedded as the fenced Python below (sha256 aac6b33a0290b7e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_projects_agent.py` first:

```bash
python3 configure_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_projects_agent.py   # or on stdin
python3 configure_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Configuration Bulk Setup — Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_projects',
    "version": '2.0.0',
    "display_name": 'Plan projects Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42eeaf215e578e2d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-projects'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanProjects(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjects'
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
    print(ConfigurePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
