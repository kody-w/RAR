---
name: "rar-cowork-cookbook-teams-update-maintain-budgets"
description: "Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_maintain_budgets", "rar_sha256": "3da1cf735128989adfa2cf821354ff3f53152e615f12e597428b3b511b95e074", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_maintain_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-maintain-budgets:8146627056bdba2ad011d54e6cf41d46e849f6d9393156bc0bc27c1329c12bfc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_maintain_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_maintain_budgets_agent.py` is
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

Maintain budgets Teams Channel Update — Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 3da1cf735128989a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_maintain_budgets_agent.py` first:

```bash
python3 teams_update_maintain_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_maintain_budgets_agent.py   # or on stdin
python3 teams_update_maintain_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain budgets Teams Channel Update — Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_maintain_budgets',
    "version": '2.0.0',
    "display_name": 'Maintain budgets Teams Channel Update',
    "description": 'Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-maintain-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-maintain-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2bbc80abd783a3bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/maintain-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-maintain-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateMaintainBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMaintainBudgets'
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
    print(TeamsUpdateMaintainBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
