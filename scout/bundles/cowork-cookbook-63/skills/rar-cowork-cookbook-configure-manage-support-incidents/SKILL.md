---
name: "rar-cowork-cookbook-configure-manage-support-incidents"
description: "Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_support_incidents", "rar_sha256": "859dd4614bbd00581a8b2dce695b440c6d6f656d797d87dc5da4d9067dbb2bf3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_support_incidents`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_support_incidents_agent.py` and in the RCI capsule.

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

Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 859dd4614bbd0058…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_support_incidents_agent.py` first:

```bash
python3 configure_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_support_incidents_agent.py   # or on stdin
python3 configure_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Configuration Bulk Setup — Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_support_incidents',
    "version": '2.0.1',
    "display_name": 'Manage support incidents Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage support incidents from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '654bffc250c9f16d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSupportIncidents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupportIncidents'
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
    print(ConfigureManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
