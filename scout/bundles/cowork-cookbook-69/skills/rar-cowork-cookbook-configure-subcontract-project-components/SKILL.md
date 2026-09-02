---
name: "rar-cowork-cookbook-configure-subcontract-project-components"
description: "Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_subcontract_project_components", "rar_sha256": "bc962d353717e50bad9485a5656b70bfd671135264065d1b709b0a879840c513", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_subcontract_project_components_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-subcontract-project-components:51db06ee3d78c93c39c8a5c9e4c9637655afefbaed508f530b7ed619b79f9926", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_subcontract_project_components`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_subcontract_project_components_agent.py` is
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

Subcontract project components Configuration Bulk Setup — Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 bc962d353717e50b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_subcontract_project_components_agent.py` first:

```bash
python3 configure_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_subcontract_project_components_agent.py   # or on stdin
python3 configure_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Configuration Bulk Setup — Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_subcontract_project_components',
    "version": '2.0.0',
    "display_name": 'Subcontract project components Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b6fbd4b5f094a21',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureSubcontractProjectComponents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureSubcontractProjectComponents'
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
    print(ConfigureSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
