---
name: "rar-cowork-cookbook-configure-take-inventory-on-software-licenses"
description: "Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_take_inventory_on_software_licenses", "rar_sha256": "2d42da4f2b4f70e2e3ab8f8493dfcf62023c0aa50b00922639ec86d44f1f97ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_take_inventory_on_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-take-inventory-on-software-licenses:d000ffd0eebd442d95a73c07f909cffb995fa0ef111ab106d4cf01327d16c451", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_take_inventory_on_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_take_inventory_on_software_licenses_agent.py` is
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

Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2d42da4f2b4f70e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 configure_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 configure_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_take_inventory_on_software_licenses',
    "version": '2.0.0',
    "display_name": 'Take inventory on software licenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fdc1cecb5ad3716',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTakeInventoryOnSoftwareLicenses'
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
    print(ConfigureTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
