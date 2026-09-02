---
name: "rar-cowork-cookbook-configure-manage-active-services"
description: "Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_active_services", "rar_sha256": "dc3af5aa61a369816fe7b29f689c8afcde5f22f92e7a0ac90eaa83e1baa523db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_active_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-active-services:d0ff45e5d5ec5bf86461fcc90309cd727e7084a84ad2ca21a7ab69f7a9ee2252", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_active_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_active_services_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 dc3af5aa61a36981…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_active_services_agent.py` first:

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
    "version": '2.0.0',
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
