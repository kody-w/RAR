---
name: "rar-cowork-cookbook-configure-maintain-and-update-the-business-continuity-plan"
description: "Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan", "rar_sha256": "b1a09958d05644d7545532fa031a187d272d32bec0379ac927a8045a071d16bf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Configuration Bulk Setup — Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 b1a09958d05644d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Configuration Bulk Setup — Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan',
    "version": '2.0.1',
    "display_name": 'Maintain and update the business continuity plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '564455039af327eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainAndUpdateTheBusinessContinuityPlan'
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
    print(ConfigureMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
