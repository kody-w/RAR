---
name: "rar-cowork-cookbook-configure-plan-workforce-capacity"
description: "Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_capacity", "rar_sha256": "13e224d96474cd4dbefc456b797c68181c70e2bd13e3088f8249a9b35890441f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_workforce_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-workforce-capacity:612fa745be3d4d5f0ea2802e8784c87a3352b071ac4bbe378bb8d843a2296901", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_workforce_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_workforce_capacity_agent.py` is
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

Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 13e224d96474cd4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_capacity_agent.py` first:

```bash
python3 configure_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_capacity_agent.py   # or on stdin
python3 configure_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_capacity',
    "version": '2.0.0',
    "display_name": 'Plan workforce capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-workforce-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aba204977e09b4b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-workforce-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanWorkforceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceCapacity'
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
    print(ConfigurePlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
