---
name: "rar-cowork-cookbook-teams-update-manage-project-knowledge-and-documentation"
description: "Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation", "rar_sha256": "05b0fc57ecb347ed4f1abd80b49d9a3854ef02dce1d465ee3861b3ff28794a9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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

Manage project knowledge and documentation Teams Channel Update — Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 05b0fc57ecb347ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 teams_update_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 teams_update_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Teams Channel Update — Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation',
    "version": '2.0.0',
    "display_name": 'Manage project knowledge and documentation Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f94cb2ce1850b932',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageProjectKnowledgeAndDocumentation'
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
    print(TeamsUpdateManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
