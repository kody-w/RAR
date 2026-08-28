---
name: "rar-cowork-cookbook-bulk-update-model-service-capacity"
description: "Applies a bulk field update across model service capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_model_service_capacity", "rar_sha256": "5c688e5504e32b1473c662d364988266da7fb1effefd0e89092c15b285feb00f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 5c688e5504e32b14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_model_service_capacity_agent.py` first:

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
    "version": '2.0.1',
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
