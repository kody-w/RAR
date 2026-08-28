---
name: "rar-cowork-cookbook-bulk-update-develop-a-disaster-recovery-plan"
description: "Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan", "rar_sha256": "b5f9fa19ed026f7f4e97599edb4c662d7619240db3a4540012b408d699252a32", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_a_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Develop a disaster recovery plan Bulk Field Update — Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 b5f9fa19ed026f7f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_a_disaster_recovery_plan_agent.py` first:

```bash
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_a_disaster_recovery_plan_agent.py   # or on stdin
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a disaster recovery plan Bulk Field Update — Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan',
    "version": '2.0.1',
    "display_name": 'Develop a disaster recovery plan Bulk Field Update',
    "description": 'Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-a-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c336ff9fa34a3ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-disaster-recovery-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-a-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopADisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopADisasterRecoveryPlan'
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
    print(BulkUpdateDevelopADisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
