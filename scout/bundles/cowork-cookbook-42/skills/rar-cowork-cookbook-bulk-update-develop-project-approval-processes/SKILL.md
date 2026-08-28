---
name: "rar-cowork-cookbook-bulk-update-develop-project-approval-processes"
description: "Applies a bulk field update across develop project approval processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_project_approval_processes", "rar_sha256": "d8d26ca8ede4c587129003026c05d28be52c78c9eeca92e79f700c7e2680f5fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 d8d26ca8ede4c587…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_project_approval_processes_agent.py` first:

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
    "version": '2.0.0',
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
