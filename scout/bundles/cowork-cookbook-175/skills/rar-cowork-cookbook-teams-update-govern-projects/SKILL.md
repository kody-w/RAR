---
name: "rar-cowork-cookbook-teams-update-govern-projects"
description: "Drafts a Teams channel post on govern projects status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_govern_projects", "rar_sha256": "5cd034c0c57251db5a51e5b75293befecbf47976fac6ae22523cda2b55b584c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_govern_projects_agent.py` and embedded as the fenced Python below (sha256 5cd034c0c57251db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_govern_projects_agent.py` first:

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
    "version": '2.0.0',
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
