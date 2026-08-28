---
name: "rar-cowork-cookbook-configure-implement-application-lifecycle-management-alm-strategies"
description: "Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "f07d97b802c28ff831155463a6b26038fb9902fb0288445f677d49350e41aae8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 f07d97b802c28ff8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_application_lifecycle_management_alm_strategies_agent.py` first:

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
    "version": '2.0.0',
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
