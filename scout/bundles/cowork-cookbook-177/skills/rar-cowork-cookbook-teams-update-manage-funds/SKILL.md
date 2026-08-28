---
name: "rar-cowork-cookbook-teams-update-manage-funds"
description: "Drafts a Teams channel post on manage funds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_funds", "rar_sha256": "b23791246a02810036702d0fe7bfd353509cf691347dc59d822d7cceed99282c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_funds_agent.py` and embedded as the fenced Python below (sha256 b23791246a028100…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_funds_agent.py` first:

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
    "version": '2.0.0',
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
