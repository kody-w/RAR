---
name: "rar-cowork-cookbook-bulk-update-implement-a-business-continuity-plan"
description: "Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_implement_a_business_continuity_plan", "rar_sha256": "dead08aa77c85d94d17fb788222ac6ce09373e93f96a2a83941af6b396591ba5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_implement_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_implement_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Implement a business continuity plan Bulk Field Update — Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 dead08aa77c85d94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 bulk_update_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 bulk_update_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Bulk Field Update — Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_implement_a_business_continuity_plan',
    "version": '2.0.1',
    "display_name": 'Implement a business continuity plan Bulk Field Update',
    "description": 'Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f55b89221827f797',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateImplementABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateImplementABusinessContinuityPlan'
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
    print(BulkUpdateImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
