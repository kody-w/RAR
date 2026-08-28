---
name: "rar-cowork-cookbook-bulk-update-develop-project-approval-processes"
description: "Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_project_approval_processes", "rar_sha256": "134e47199fddcac91a511e9d53856bb2ee6c799752c10d3342557fdb844e563b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_project_approval_processes`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_project_approval_processes_agent.py` and in the RCI capsule.

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

Develop project approval processes Bulk Field Update — Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 134e47199fddcac9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_project_approval_processes_agent.py` first:

```bash
python3 bulk_update_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_project_approval_processes_agent.py   # or on stdin
python3 bulk_update_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Bulk Field Update — Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_project_approval_processes',
    "version": '2.0.1',
    "display_name": 'Develop project approval processes Bulk Field Update',
    "description": 'Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b371396b4d942e03',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopProjectApprovalProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopProjectApprovalProcesses'
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
    print(BulkUpdateDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
