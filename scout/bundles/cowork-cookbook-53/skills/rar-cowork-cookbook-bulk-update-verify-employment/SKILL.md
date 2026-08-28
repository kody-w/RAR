---
name: "rar-cowork-cookbook-bulk-update-verify-employment"
description: "Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_verify_employment", "rar_sha256": "26f3dd39b1c8cfc4943bffbe33f9b4257900356f8f740d728e3d0b26186cb305", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_verify_employment_agent.py` and embedded as the fenced Python below (sha256 26f3dd39b1c8cfc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_verify_employment_agent.py` first:

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
    "version": '2.0.0',
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
