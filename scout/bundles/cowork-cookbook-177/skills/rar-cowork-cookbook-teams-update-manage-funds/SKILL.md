---
name: "rar-cowork-cookbook-teams-update-manage-funds"
description: "Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_funds", "rar_sha256": "66ef40b093afa2e525725f7a0fba25d1bab12b72370f6f892d794e5f9448f610", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_funds`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_funds_agent.py` and in the RCI capsule.

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

Manage funds Teams Channel Update — Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_funds_agent.py` and embedded as the fenced Python below (sha256 66ef40b093afa2e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_funds_agent.py` first:

```bash
python3 teams_update_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_funds_agent.py   # or on stdin
python3 teams_update_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Teams Channel Update — Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_funds',
    "version": '2.0.1',
    "display_name": 'Manage funds Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f50c9c1a091e1bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateManageFunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageFunds'
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
    print(TeamsUpdateManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
