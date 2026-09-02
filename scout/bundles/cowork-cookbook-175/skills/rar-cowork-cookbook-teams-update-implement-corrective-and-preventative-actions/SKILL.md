---
name: "rar-cowork-cookbook-teams-update-implement-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions", "rar_sha256": "8d7e5168551170eb6ca849571a7f6fbb8bc08565beea34a085738bb5063bc46f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_implement_corrective_and_preventative_actions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-implement-corrective-and-preventative-actions:bc2397aa2a0fc26ff74c636fccfc885fc1e73152007b67f548bb48cdd2105899", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_implement_corrective_and_preventative_actions_agent.py` is
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
