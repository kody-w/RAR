---
name: "rar-cowork-cookbook-teams-update-perform-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions", "rar_sha256": "f15ba935843ea51ebc2ee9f2082acbce6f48c32f06d54299877e4ca59462121c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_perform_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Perform corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 f15ba935843ea51e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions',
    "version": '2.0.0',
    "display_name": 'Perform corrective and preventative actions Teams Channel Update',
    "description": 'Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b991b2cc8e6a5545',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePerformCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePerformCorrectiveAndPreventativeActions'
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
    print(TeamsUpdatePerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
