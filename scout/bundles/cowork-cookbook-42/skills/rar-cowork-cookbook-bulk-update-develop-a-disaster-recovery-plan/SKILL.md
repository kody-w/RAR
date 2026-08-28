---
name: "rar-cowork-cookbook-bulk-update-develop-a-disaster-recovery-plan"
description: "Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan", "rar_sha256": "f1975161d4148b7fd0c488b6c96b9fb0107264cabeb9fa917a00b894f8d430e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 f1975161d4148b7f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_a_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.0',
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
