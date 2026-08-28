---
name: "rar-cowork-cookbook-teams-update-define-service-workflows"
description: "Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_workflows", "rar_sha256": "7bf9e9a6cd654a81a4d4baec0f55d2d70221abc9849ac0ecff8e653190f4556a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_service_workflows`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_service_workflows_agent.py` and in the RCI capsule.

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

Define service workflows Teams Channel Update — Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 7bf9e9a6cd654a81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_workflows_agent.py` first:

```bash
python3 teams_update_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_service_workflows_agent.py   # or on stdin
python3 teams_update_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Teams Channel Update — Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_service_workflows',
    "version": '2.0.1',
    "display_name": 'Define service workflows Teams Channel Update',
    "description": 'Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57c6689ba0876cd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineServiceWorkflows(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineServiceWorkflows'
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
    print(TeamsUpdateDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
