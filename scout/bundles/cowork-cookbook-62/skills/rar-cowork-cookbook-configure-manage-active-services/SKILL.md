---
name: "rar-cowork-cookbook-configure-manage-active-services"
description: "Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_active_services", "rar_sha256": "5baf97248777d8f72f580eb1f6b918d2ceb31d0996bfd34cf1002dfb9e48ffa0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_active_services`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_active_services_agent.py` and in the RCI capsule.

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

Manage active services Configuration Bulk Setup — Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-active-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 5baf97248777d8f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_active_services_agent.py` first:

```bash
python3 configure_manage_active_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_active_services_agent.py   # or on stdin
python3 configure_manage_active_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active services Configuration Bulk Setup — Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-active-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_active_services',
    "version": '2.0.1',
    "display_name": 'Manage active services Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-active-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-active-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a9a04eeeec809fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-active-services'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-manage-active-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageActiveServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageActiveServices'
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
    print(ConfigureManageActiveServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
