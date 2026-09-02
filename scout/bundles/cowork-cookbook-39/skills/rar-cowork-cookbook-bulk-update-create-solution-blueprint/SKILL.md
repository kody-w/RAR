---
name: "rar-cowork-cookbook-bulk-update-create-solution-blueprint"
description: "Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_solution_blueprint", "rar_sha256": "b7c692f677651c9e1f0577def0e3e57cd4789adb313ca51d97a310f4cc70ac8e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_create_solution_blueprint_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-create-solution-blueprint:db3d564d53417f2161ee8bc6a8eac5cc4800bcdbf58fbb2610d4f500988017fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_create_solution_blueprint`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_create_solution_blueprint_agent.py` is
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

Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 b7c692f677651c9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_solution_blueprint_agent.py` first:

```bash
python3 bulk_update_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_solution_blueprint_agent.py   # or on stdin
python3 bulk_update_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_solution_blueprint',
    "version": '2.0.0',
    "display_name": 'Create solution blueprint Bulk Field Update',
    "description": 'Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b2fb15dd02960',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCreateSolutionBlueprint(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateSolutionBlueprint'
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
    print(BulkUpdateCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
