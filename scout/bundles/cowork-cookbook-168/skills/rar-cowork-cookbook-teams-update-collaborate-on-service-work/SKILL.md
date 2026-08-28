---
name: "rar-cowork-cookbook-teams-update-collaborate-on-service-work"
description: "Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_collaborate_on_service_work", "rar_sha256": "cca9db411eadb5deb4f97ac018433f4b1731647ca6ec182c5ace8c3d462e109d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 cca9db411eadb5de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_collaborate_on_service_work_agent.py` first:

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
    "version": '2.0.0',
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
