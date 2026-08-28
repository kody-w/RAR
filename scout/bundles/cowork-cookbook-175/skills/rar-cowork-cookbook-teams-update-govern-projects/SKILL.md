---
name: "rar-cowork-cookbook-teams-update-govern-projects"
description: "Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_govern_projects", "rar_sha256": "7a9b14d6ca4e87cf1e821f47442187ff14ca2b2f3a5029cb77dd35ab3f4c5e80", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_govern_projects`. The original RAPP
agent is preserved byte-for-byte in `teams_update_govern_projects_agent.py` and in the RCI capsule.

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

Govern projects Teams Channel Update — Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_govern_projects_agent.py` and embedded as the fenced Python below (sha256 7a9b14d6ca4e87cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_govern_projects_agent.py` first:

```bash
python3 teams_update_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_govern_projects_agent.py   # or on stdin
python3 teams_update_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Teams Channel Update — Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_govern_projects',
    "version": '2.0.1',
    "display_name": 'Govern projects Teams Channel Update',
    "description": 'Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '827f16cbc42daa00',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateGovernProjects(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateGovernProjects'
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
    print(TeamsUpdateGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
