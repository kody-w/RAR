---
name: "rar-cowork-cookbook-teams-update-reallocate-asset-budgets"
description: "Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reallocate_asset_budgets", "rar_sha256": "cb27ce3ccd3a95169fe48c27d89fd8dbe6835f71288a5f312bbf6767be08ab4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_reallocate_asset_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-reallocate-asset-budgets:15db08a391ad5dc33fd7908c42e5fad8c4c60f8c40ca915ef11a759deafdc86c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_reallocate_asset_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_reallocate_asset_budgets_agent.py` is
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

Reallocate asset budgets Teams Channel Update — Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 cb27ce3ccd3a9516…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reallocate_asset_budgets_agent.py` first:

```bash
python3 teams_update_reallocate_asset_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_reallocate_asset_budgets_agent.py   # or on stdin
python3 teams_update_reallocate_asset_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reallocate asset budgets Teams Channel Update — Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_reallocate_asset_budgets',
    "version": '2.0.0',
    "display_name": 'Reallocate asset budgets Teams Channel Update',
    "description": 'Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-reallocate-asset-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c617514bcfdbf0bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/reallocate-asset-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-reallocate-asset-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateReallocateAssetBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReallocateAssetBudgets'
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
    print(TeamsUpdateReallocateAssetBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
