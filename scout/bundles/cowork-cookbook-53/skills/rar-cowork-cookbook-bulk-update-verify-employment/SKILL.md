---
name: "rar-cowork-cookbook-bulk-update-verify-employment"
description: "Applies a bulk field update across verify employment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_verify_employment", "rar_sha256": "26f3dd39b1c8cfc4943bffbe33f9b4257900356f8f740d728e3d0b26186cb305", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_verify_employment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-verify-employment:17b079581a04a4f72bb3bb920573252a1a56024179a5ea549d62083769a9a364", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_verify_employment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_verify_employment_agent.py` is
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
