---
name: "rar-cowork-cookbook-bulk-update-request-time-off"
description: "Applies a bulk field update across request time off records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_request_time_off", "rar_sha256": "64ff28444b0b78e7b4e96681901c14f6f6ba490283d001f668029d830c7c8296", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_request_time_off`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_request_time_off_agent.py` and in the RCI capsule.

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
