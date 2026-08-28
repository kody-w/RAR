---
name: "rar-cowork-cookbook-bulk-update-define-project-scope"
description: "Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_project_scope", "rar_sha256": "db8e39485f277aeef0eb11000579cb477d69b807379e1eed812f79f7de1ccb1b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_project_scope`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_project_scope_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 db8e39485f277aee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_project_scope_agent.py` first:

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
    "version": '2.0.1',
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
