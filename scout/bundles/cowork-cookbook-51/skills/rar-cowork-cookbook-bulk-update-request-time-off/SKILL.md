---
name: "rar-cowork-cookbook-bulk-update-request-time-off"
description: "Applies a bulk field update across request time off records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_request_time_off", "rar_sha256": "64ff28444b0b78e7b4e96681901c14f6f6ba490283d001f668029d830c7c8296", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_request_time_off_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-request-time-off:fa5e8ddbfb855ffa930607153aa776cc23ed98874baa1994239445cf9ecc3001", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_request_time_off`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_request_time_off_agent.py` is
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

Request time off Bulk Field Update — Applies a bulk field update across request time off records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-request-time-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_request_time_off_agent.py` and embedded as the fenced Python below (sha256 64ff28444b0b78e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_request_time_off_agent.py` first:

```bash
python3 bulk_update_request_time_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_request_time_off_agent.py   # or on stdin
python3 bulk_update_request_time_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request time off Bulk Field Update — Applies a bulk field update across request time off records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-request-time-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_request_time_off',
    "version": '2.0.0',
    "display_name": 'Request time off Bulk Field Update',
    "description": 'Applies a bulk field update across request time off records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-request-time-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-request-time-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92f369987815abc0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-time-off'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-request-time-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRequestTimeOff(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRequestTimeOff'
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
    print(BulkUpdateRequestTimeOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
