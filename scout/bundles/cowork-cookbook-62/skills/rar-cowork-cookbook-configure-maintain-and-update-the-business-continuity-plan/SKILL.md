---
name: "rar-cowork-cookbook-configure-maintain-and-update-the-business-continuity-plan"
description: "Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan", "rar_sha256": "620470dac2c3b06bd9fb6fa326cf0baeac659f36f5a9d13d7aab4075e12e133c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_maintain_and_update_the_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-maintain-and-update-the-business-continuity-plan:7cd8efd52cb2f0554b6b20798e517ce463caa9d5180d26c4b0b34ea1c4871a33", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_maintain_and_update_the_business_continuity_plan_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 620470dac2c3b06b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_and_update_the_business_continuity_plan_agent.py` first:

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
    "version": '2.0.0',
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
