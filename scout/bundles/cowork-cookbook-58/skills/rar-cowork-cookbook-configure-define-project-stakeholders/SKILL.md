---
name: "rar-cowork-cookbook-configure-define-project-stakeholders"
description: "Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_project_stakeholders", "rar_sha256": "e7ec55021bf3bd97c8c7b975ac43cd0149599a4da92ec7d27bad2024ca53c502", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `configure_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Configuration Bulk Setup — Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 e7ec55021bf3bd97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_project_stakeholders_agent.py` first:

```bash
python3 configure_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_project_stakeholders_agent.py   # or on stdin
python3 configure_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Configuration Bulk Setup — Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_project_stakeholders',
    "version": '2.0.1',
    "display_name": 'Define project stakeholders Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0794b831574d11bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineProjectStakeholders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProjectStakeholders'
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
    print(ConfigureDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
