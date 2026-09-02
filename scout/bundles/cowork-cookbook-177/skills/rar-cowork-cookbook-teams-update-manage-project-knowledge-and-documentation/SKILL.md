---
name: "rar-cowork-cookbook-teams-update-manage-project-knowledge-and-documentation"
description: "Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation", "rar_sha256": "05b0fc57ecb347ed4f1abd80b49d9a3854ef02dce1d465ee3861b3ff28794a9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_project_knowledge_and_documentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-project-knowledge-and-documentation:469a18716ac3f35f4281f9a08965210d2010df495b119ebb30840f2581b43285", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_project_knowledge_and_documentation_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
