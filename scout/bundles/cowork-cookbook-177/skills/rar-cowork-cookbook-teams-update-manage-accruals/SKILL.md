---
name: "rar-cowork-cookbook-teams-update-manage-accruals"
description: "Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_accruals", "rar_sha256": "3d54660b6b5d8ccfcf48fa52407684a9ae0d3217b5c7eca6f9a4755e3d50ef24", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_accruals`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_accruals_agent.py` and in the RCI capsule.

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

Manage accruals Teams Channel Update — Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 3d54660b6b5d8ccf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_accruals_agent.py` first:

```bash
python3 teams_update_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_accruals_agent.py   # or on stdin
python3 teams_update_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Teams Channel Update — Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_accruals',
    "version": '2.0.1',
    "display_name": 'Manage accruals Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '006824224e9350fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateManageAccruals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageAccruals'
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
    print(TeamsUpdateManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
