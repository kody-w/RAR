---
name: "rar-cowork-cookbook-configure-plan-workforce-development"
description: "Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_development", "rar_sha256": "c9120f25a701e6a60c67c89349f783f03ba384f7a2962c321c7a56fa87495135", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_workforce_development_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-workforce-development:4372cba24775bb9ef5cd8465bebdad3453b323111d94cdb655000afa7a010948", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_workforce_development`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_workforce_development_agent.py` is
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

Plan workforce development Configuration Bulk Setup — Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 c9120f25a701e6a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_development_agent.py` first:

```bash
python3 configure_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_development_agent.py   # or on stdin
python3 configure_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Configuration Bulk Setup — Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_development',
    "version": '2.0.0',
    "display_name": 'Plan workforce development Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f2f14dd7f2fb7d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanWorkforceDevelopment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceDevelopment'
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
    print(ConfigurePlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
