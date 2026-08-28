---
name: "rar-cowork-cookbook-configure-define-business-continuity-objectives"
description: "Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_business_continuity_objectives", "rar_sha256": "632a91031bfeddde77b9f2c2f8e696f8e0b122d17775d08b8f523e9209c9dfd2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 632a91031bfeddde…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_business_continuity_objectives_agent.py` first:

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
    "version": '2.0.1',
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
