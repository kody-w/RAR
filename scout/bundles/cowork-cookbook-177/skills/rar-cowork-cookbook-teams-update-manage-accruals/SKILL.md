---
name: "rar-cowork-cookbook-teams-update-manage-accruals"
description: "Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_accruals", "rar_sha256": "0634902fb7ba457eeea18575c68304f36184799511838abc187527876a892d97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 0634902fb7ba457e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_accruals_agent.py` first:

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
    "version": '2.0.0',
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
