---
name: "rar-cowork-cookbook-bulk-update-receive-service-requests"
description: "Applies a bulk field update across receive service requests records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_service_requests", "rar_sha256": "ca6c0578cfb0cab88c5d907e7df1b7f4bdae096ba48d051c3af23f1805afd1e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_receive_service_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-receive-service-requests:83bc75bf019c384654731bfb6e9550b3577659e4f2ce22c3d1a33ca9fc1cd74b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_receive_service_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_receive_service_requests_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 ca6c0578cfb0cab8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_service_requests_agent.py` first:

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
    "version": '2.0.0',
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
