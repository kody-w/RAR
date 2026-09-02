---
name: "rar-cowork-cookbook-configure-implement-application-lifecycle-management-alm-strategies"
description: "Applies a bulk configuration change to implement application lifecycle management (ALM) strategies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "f07d97b802c28ff831155463a6b26038fb9902fb0288445f677d49350e41aae8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_implement_application_lifecycle_management_alm_strategies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-implement-application-lifecycle-management-alm-strategies:be1433e7d486e86b9f32b4bb28cd10e3844b8633dd145cb9a5bf5dc9c6cb04f8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_implement_application_lifecycle_management_alm_strategies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_implement_application_lifecycle_management_alm_strategies_agent.py` is
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
