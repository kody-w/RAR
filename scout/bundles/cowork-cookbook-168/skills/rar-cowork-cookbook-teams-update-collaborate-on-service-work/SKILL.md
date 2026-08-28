---
name: "rar-cowork-cookbook-teams-update-collaborate-on-service-work"
description: "Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_collaborate_on_service_work", "rar_sha256": "d930bc248c9ff9eb3a87b32bc5eafe65f697dc1eaf87133df2b1f287eb256c43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_collaborate_on_service_work`. The original RAPP
agent is preserved byte-for-byte in `teams_update_collaborate_on_service_work_agent.py` and in the RCI capsule.

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

Collaborate on service work Teams Channel Update — Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 d930bc248c9ff9eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_collaborate_on_service_work_agent.py` first:

```bash
python3 teams_update_collaborate_on_service_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_collaborate_on_service_work_agent.py   # or on stdin
python3 teams_update_collaborate_on_service_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collaborate on service work Teams Channel Update — Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_collaborate_on_service_work',
    "version": '2.0.1',
    "display_name": 'Collaborate on service work Teams Channel Update',
    "description": 'Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-collaborate-on-service-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66657f82775bf626',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collaborate-on-service-work'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-collaborate-on-service-work', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCollaborateOnServiceWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCollaborateOnServiceWork'
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
    print(TeamsUpdateCollaborateOnServiceWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
