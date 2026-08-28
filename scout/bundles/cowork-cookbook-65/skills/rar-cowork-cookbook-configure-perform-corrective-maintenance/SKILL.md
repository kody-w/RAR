---
name: "rar-cowork-cookbook-configure-perform-corrective-maintenance"
description: "Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_perform_corrective_maintenance", "rar_sha256": "a75fe52e47b2a17a5cbe2367fa816ad368873c5e05796ad5907752db5450744b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_perform_corrective_maintenance`. The original RAPP
agent is preserved byte-for-byte in `configure_perform_corrective_maintenance_agent.py` and in the RCI capsule.

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

Perform corrective maintenance Configuration Bulk Setup — Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 a75fe52e47b2a17a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_perform_corrective_maintenance_agent.py` first:

```bash
python3 configure_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_perform_corrective_maintenance_agent.py   # or on stdin
python3 configure_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Configuration Bulk Setup — Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_perform_corrective_maintenance',
    "version": '2.0.1',
    "display_name": 'Perform corrective maintenance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f2fbd3fbf95fa0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePerformCorrectiveMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePerformCorrectiveMaintenance'
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
    print(ConfigurePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
