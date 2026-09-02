---
name: "rar-cowork-cookbook-bulk-update-plan-loads"
description: "Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_loads", "rar_sha256": "cab322941a7308494e94717f00f6c55a0f65f79c877c5734152b49aeff2bd0d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-loads:67dc6807988fe118cb5525f2bc83e64832465f126a4cc2044ebf489cf1b69343", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_loads_agent.py` is
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

Plan loads Bulk Field Update — Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_loads_agent.py` and embedded as the fenced Python below (sha256 cab322941a730849…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_loads_agent.py` first:

```bash
python3 bulk_update_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_loads_agent.py   # or on stdin
python3 bulk_update_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Bulk Field Update — Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_loads',
    "version": '2.0.0',
    "display_name": 'Plan loads Bulk Field Update',
    "description": 'Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c52fc0dfeaab27da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanLoads'
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
    print(BulkUpdatePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
