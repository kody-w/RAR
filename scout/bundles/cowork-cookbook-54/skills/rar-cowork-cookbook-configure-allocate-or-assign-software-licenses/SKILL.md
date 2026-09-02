---
name: "rar-cowork-cookbook-configure-allocate-or-assign-software-licenses"
description: "Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_or_assign_software_licenses", "rar_sha256": "ed3ffbddf793ec672f4f40a2a6e429aedce39b8a2cd24104735c03141beb581c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_allocate_or_assign_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-allocate-or-assign-software-licenses:c8a054caba9d4b94c0b3806263629afe48a9b622e917d0e7ce551dd4fbb082b7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_allocate_or_assign_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_allocate_or_assign_software_licenses_agent.py` is
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
