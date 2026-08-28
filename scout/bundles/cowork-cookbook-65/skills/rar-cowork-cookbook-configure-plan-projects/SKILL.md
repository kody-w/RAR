---
name: "rar-cowork-cookbook-configure-plan-projects"
description: "Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_projects", "rar_sha256": "77f9bf1b98e0c1837e9d88ab150606860b14fd8a6318fa460c07e818fe310024", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_projects`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_projects_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_projects_agent.py` and embedded as the fenced Python below (sha256 77f9bf1b98e0c183…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_projects_agent.py` first:

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
    "version": '2.0.1',
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
