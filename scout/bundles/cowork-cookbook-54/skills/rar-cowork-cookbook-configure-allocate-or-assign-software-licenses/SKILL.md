---
name: "rar-cowork-cookbook-configure-allocate-or-assign-software-licenses"
description: "Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_or_assign_software_licenses", "rar_sha256": "ed3ffbddf793ec672f4f40a2a6e429aedce39b8a2cd24104735c03141beb581c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_allocate_or_assign_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_allocate_or_assign_software_licenses_agent.py` and in the RCI capsule.

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

Allocate or assign software licenses Configuration Bulk Setup — Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 ed3ffbddf793ec67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_or_assign_software_licenses_agent.py` first:

```bash
python3 configure_allocate_or_assign_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_allocate_or_assign_software_licenses_agent.py   # or on stdin
python3 configure_allocate_or_assign_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate or assign software licenses Configuration Bulk Setup — Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_allocate_or_assign_software_licenses',
    "version": '2.0.0',
    "display_name": 'Allocate or assign software licenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-allocate-or-assign-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e21b2795dd2559e4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/allocate-or-assign-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-allocate-or-assign-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAllocateOrAssignSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAllocateOrAssignSoftwareLicenses'
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
    print(ConfigureAllocateOrAssignSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
