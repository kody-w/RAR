---
name: "rar-cowork-cookbook-bulk-update-define-project-scope"
description: "Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_project_scope", "rar_sha256": "49e6e39cf4cd3fb2dd61bbd043c72ee82ec66d72151fdf6211862fdbfa3db917", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_project_scope_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-project-scope:a9629f54df0b5dd19833136fd6625f2087a56059317a5375bca3b228194cda4b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_project_scope`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_project_scope_agent.py` is
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

Define project scope Bulk Field Update — Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 49e6e39cf4cd3fb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_project_scope_agent.py` first:

```bash
python3 bulk_update_define_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_project_scope_agent.py   # or on stdin
python3 bulk_update_define_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project scope Bulk Field Update — Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_project_scope',
    "version": '2.0.0',
    "display_name": 'Define project scope Bulk Field Update',
    "description": 'Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd87e1df76f695430',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/define-project-scope'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-define-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProjectScope'
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
    print(BulkUpdateDefineProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
