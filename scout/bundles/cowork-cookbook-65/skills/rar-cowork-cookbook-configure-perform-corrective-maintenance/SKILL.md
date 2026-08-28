---
name: "rar-cowork-cookbook-configure-perform-corrective-maintenance"
description: "Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_perform_corrective_maintenance", "rar_sha256": "df5e82680e7ad84014431dea0d94d12df57c8e162a67743ed9e9edcedd1b7e02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 df5e82680e7ad840…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_perform_corrective_maintenance_agent.py` first:

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
    "version": '2.0.0',
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
