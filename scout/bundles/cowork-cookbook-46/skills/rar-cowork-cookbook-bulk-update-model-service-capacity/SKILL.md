---
name: "rar-cowork-cookbook-bulk-update-model-service-capacity"
description: "Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_model_service_capacity", "rar_sha256": "9b5aef6958da45d47b43fb38a4ec833d33b7c19d193e7eb2d88b9c98bc64cd34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_model_service_capacity`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_model_service_capacity_agent.py` and in the RCI capsule.

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
