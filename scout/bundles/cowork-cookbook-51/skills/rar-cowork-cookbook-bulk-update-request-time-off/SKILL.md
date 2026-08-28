---
name: "rar-cowork-cookbook-bulk-update-request-time-off"
description: "Applies a bulk field update across request time off records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_request_time_off", "rar_sha256": "db496373a448456ea924719576af598ff89e5ccadf401cf462c099f23229bb08", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_request_time_off_agent.py` and embedded as the fenced Python below (sha256 db496373a448456e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_request_time_off_agent.py` first:

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
    "version": '2.0.1',
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
