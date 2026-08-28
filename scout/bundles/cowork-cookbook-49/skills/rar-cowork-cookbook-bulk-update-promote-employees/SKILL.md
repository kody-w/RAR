---
name: "rar-cowork-cookbook-bulk-update-promote-employees"
description: "Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_promote_employees", "rar_sha256": "32132bac31e527bd24a4491d9a2e4f7eab47666d20baf5cdfeb565f2602d8e3c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_promote_employees`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_promote_employees_agent.py` and in the RCI capsule.

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

Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_promote_employees_agent.py` and embedded as the fenced Python below (sha256 32132bac31e527bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_promote_employees_agent.py` first:

```bash
python3 bulk_update_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_promote_employees_agent.py   # or on stdin
python3 bulk_update_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_promote_employees',
    "version": '2.0.0',
    "display_name": 'Promote employees Bulk Field Update',
    "description": 'Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '328b39f8330ede27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePromoteEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePromoteEmployees'
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
    print(BulkUpdatePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
