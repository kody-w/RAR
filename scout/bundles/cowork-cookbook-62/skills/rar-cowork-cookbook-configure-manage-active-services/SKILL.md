---
name: "rar-cowork-cookbook-configure-manage-active-services"
description: "Applies a bulk configuration change to manage active services from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_active_services", "rar_sha256": "dc3af5aa61a369816fe7b29f689c8afcde5f22f92e7a0ac90eaa83e1baa523db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
