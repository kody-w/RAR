---
name: "rar-cowork-cookbook-bulk-update-define-project-scope"
description: "Applies a bulk field update across define project scope records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_project_scope", "rar_sha256": "49e6e39cf4cd3fb2dd61bbd043c72ee82ec66d72151fdf6211862fdbfa3db917", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
