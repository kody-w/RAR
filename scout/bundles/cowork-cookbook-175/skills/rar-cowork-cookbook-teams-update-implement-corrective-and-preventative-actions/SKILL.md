---
name: "rar-cowork-cookbook-teams-update-implement-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions", "rar_sha256": "8d7e5168551170eb6ca849571a7f6fbb8bc08565beea34a085738bb5063bc46f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_implement_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Implement corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 8d7e5168551170eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_implement_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_implement_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_implement_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_implement_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions',
    "version": '2.0.0',
    "display_name": 'Implement corrective and preventative actions Teams Channel Update',
    "description": 'Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-implement-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6d303d7ee260640',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/implement-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-implement-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateImplementCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateImplementCorrectiveAndPreventativeActions'
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
    print(TeamsUpdateImplementCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
