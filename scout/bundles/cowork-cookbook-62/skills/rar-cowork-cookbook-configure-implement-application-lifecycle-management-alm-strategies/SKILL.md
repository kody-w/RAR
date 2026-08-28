---
name: "rar-cowork-cookbook-configure-implement-application-lifecycle-management-alm-strategies"
description: "Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "608686e718c9f10c96dc2f46e8ad93c77d8d4637016741c4b04b53e7056167b4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies`. The original RAPP
agent is preserved byte-for-byte in `configure_implement_application_lifecycle_management_alm_strategies_agent.py` and in the RCI capsule.

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

Implement application lifecycle management (ALM) strategies Configuration Bulk Setup — Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 608686e718c9f10c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_application_lifecycle_management_alm_strategies_agent.py` first:

```bash
python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py   # or on stdin
python3 configure_implement_application_lifecycle_management_alm_strategies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement application lifecycle management (ALM) strategies Configuration Bulk Setup — Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies',
    "version": '2.0.1',
    "display_name": 'Implement application lifecycle management (ALM) strategies Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-implement-application-lifecycle-management-alm-strategies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-implement-application-lifecycle-management-alm-strategies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f1061a6954cdc7cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-application-lifecycle-management-alm-strategies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-implement-application-lifecycle-management-alm-strategies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureImplementApplicationLifecycleManagementAlmStrategies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureImplementApplicationLifecycleManagementAlmStrategies'
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
    print(ConfigureImplementApplicationLifecycleManagementAlmStrategies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
