---
name: "rar-cowork-cookbook-configure-plan-procurement"
description: "Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_procurement", "rar_sha256": "62015732cdd3494912ed4d479387f25b3c48af556bebfd368fab5d152c7ecf31", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_procurement`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_procurement_agent.py` and in the RCI capsule.

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

Plan procurement Configuration Bulk Setup — Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 62015732cdd34949…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_procurement_agent.py` first:

```bash
python3 configure_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_procurement_agent.py   # or on stdin
python3 configure_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Configuration Bulk Setup — Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_procurement',
    "version": '2.0.1',
    "display_name": 'Plan procurement Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec4ac3a0c0b91806',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanProcurement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProcurement'
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
    print(ConfigurePlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
