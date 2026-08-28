---
name: "rar-cowork-cookbook-bulk-update-implement-a-business-continuity-plan"
description: "Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_implement_a_business_continuity_plan", "rar_sha256": "e9dd7dfcce22a6a5ec768771107354fcedafbaaa6b0d040b5ef950f3ddc2c40a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 e9dd7dfcce22a6a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_implement_a_business_continuity_plan_agent.py` first:

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
    "version": '2.0.0',
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
