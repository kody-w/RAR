---
name: "rar-cowork-cookbook-bulk-update-model-service-capacity"
description: "Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_model_service_capacity", "rar_sha256": "9b5aef6958da45d47b43fb38a4ec833d33b7c19d193e7eb2d88b9c98bc64cd34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_model_service_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-model-service-capacity:1acedf3c156d8799846e43b5da754be16e9561e89be984af10eecc9a9ad8308f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_model_service_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_model_service_capacity_agent.py` is
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

Model service capacity Bulk Field Update — Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-model-service-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 9b5aef6958da45d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_model_service_capacity_agent.py` first:

```bash
python3 bulk_update_model_service_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_model_service_capacity_agent.py   # or on stdin
python3 bulk_update_model_service_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Model service capacity Bulk Field Update — Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-model-service-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_model_service_capacity',
    "version": '2.0.0',
    "display_name": 'Model service capacity Bulk Field Update',
    "description": 'Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-model-service-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-model-service-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12c4bbb97ae1b977',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/model-service-capacity'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-model-service-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateModelServiceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModelServiceCapacity'
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
    print(BulkUpdateModelServiceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
