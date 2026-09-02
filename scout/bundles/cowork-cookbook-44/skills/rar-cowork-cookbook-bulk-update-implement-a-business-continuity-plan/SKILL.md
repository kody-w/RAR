---
name: "rar-cowork-cookbook-bulk-update-implement-a-business-continuity-plan"
description: "Applies a bulk field update across implement a business continuity plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_implement_a_business_continuity_plan", "rar_sha256": "e9dd7dfcce22a6a5ec768771107354fcedafbaaa6b0d040b5ef950f3ddc2c40a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_implement_a_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-implement-a-business-continuity-plan:06ba78ec2fa6e970263a55dab36dcc4497b177db149c0c7cef575425b9de2d9a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_implement_a_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_implement_a_business_continuity_plan_agent.py` is
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
