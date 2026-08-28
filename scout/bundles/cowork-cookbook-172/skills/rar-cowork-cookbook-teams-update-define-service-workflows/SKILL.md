---
name: "rar-cowork-cookbook-teams-update-define-service-workflows"
description: "Drafts a Teams channel post on define service workflows status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_workflows", "rar_sha256": "a2d15774f1516abd0ccfbd96a9aad2cab9e2f75d042794f7831cf8c64221efaf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 a2d15774f1516abd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_workflows_agent.py` first:

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
    "version": '2.0.0',
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
