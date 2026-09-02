---
name: "rar-cowork-cookbook-teams-update-perform-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions", "rar_sha256": "f15ba935843ea51ebc2ee9f2082acbce6f48c32f06d54299877e4ca59462121c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_perform_corrective_and_preventative_actions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-perform-corrective-and-preventative-actions:b0df6da80eaa3e6010d7ce7baca378f7f72909bf3c8118d44c84100bc69c3832", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_perform_corrective_and_preventative_actions_agent.py` is
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
