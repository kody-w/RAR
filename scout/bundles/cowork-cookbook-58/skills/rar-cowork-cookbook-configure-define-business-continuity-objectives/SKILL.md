---
name: "rar-cowork-cookbook-configure-define-business-continuity-objectives"
description: "Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_business_continuity_objectives", "rar_sha256": "6db96d63a916cfd6bde5760b95defba133987f1698e9a4e210f6f776b8964aa2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_business_continuity_objectives`. The original RAPP
agent is preserved byte-for-byte in `configure_define_business_continuity_objectives_agent.py` and in the RCI capsule.

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

Define business continuity objectives Configuration Bulk Setup — Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 6db96d63a916cfd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_business_continuity_objectives_agent.py` first:

```bash
python3 configure_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_business_continuity_objectives_agent.py   # or on stdin
python3 configure_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Configuration Bulk Setup — Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_business_continuity_objectives',
    "version": '2.0.0',
    "display_name": 'Define business continuity objectives Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5545c1055898def6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineBusinessContinuityObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineBusinessContinuityObjectives'
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
    print(ConfigureDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
