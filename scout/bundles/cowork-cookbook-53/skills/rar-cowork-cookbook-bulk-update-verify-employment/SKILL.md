---
name: "rar-cowork-cookbook-bulk-update-verify-employment"
description: "Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_verify_employment", "rar_sha256": "686a90ea78109ae335afbd3fa4d6a8f073fb400256ad6af77cc7c7c34075b67f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_verify_employment`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_verify_employment_agent.py` and in the RCI capsule.

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

Verify employment Bulk Field Update — Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-verify-employment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_verify_employment_agent.py` and embedded as the fenced Python below (sha256 686a90ea78109ae3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_verify_employment_agent.py` first:

```bash
python3 bulk_update_verify_employment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_verify_employment_agent.py   # or on stdin
python3 bulk_update_verify_employment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Verify employment Bulk Field Update — Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-verify-employment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_verify_employment',
    "version": '2.0.1',
    "display_name": 'Verify employment Bulk Field Update',
    "description": 'Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-verify-employment',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-verify-employment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07ec40a8d17f22d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/verify-employment'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-verify-employment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateVerifyEmployment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateVerifyEmployment'
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
    print(BulkUpdateVerifyEmployment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
