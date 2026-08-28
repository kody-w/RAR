---
name: "rar-cowork-cookbook-bulk-update-receive-service-requests"
description: "Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_service_requests", "rar_sha256": "a20737692097e79203410dac3fa1b3cf121f09e06bf5431c9718ca87901ec834", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_service_requests`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_service_requests_agent.py` and in the RCI capsule.

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

Receive service requests Bulk Field Update — Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 a20737692097e792…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_service_requests_agent.py` first:

```bash
python3 bulk_update_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_service_requests_agent.py   # or on stdin
python3 bulk_update_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Bulk Field Update — Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_service_requests',
    "version": '2.0.1',
    "display_name": 'Receive service requests Bulk Field Update',
    "description": 'Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5f6f147a39f422d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReceiveServiceRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveServiceRequests'
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
    print(BulkUpdateReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
