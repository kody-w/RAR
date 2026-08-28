---
name: "rar-cowork-cookbook-configure-plan-workforce-development"
description: "Applies a bulk configuration change to plan workforce development from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_development", "rar_sha256": "223c6790d831777b8d3d3baeaf75fdeaed412e2becf23fb3fddd6c0cc537c3d4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_development_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 223c6790d831777b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_development_agent.py` first:

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
    "version": '2.0.1',
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
