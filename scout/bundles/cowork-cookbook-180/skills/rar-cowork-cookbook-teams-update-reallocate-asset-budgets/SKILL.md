---
name: "rar-cowork-cookbook-teams-update-reallocate-asset-budgets"
description: "Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reallocate_asset_budgets", "rar_sha256": "cb27ce3ccd3a95169fe48c27d89fd8dbe6835f71288a5f312bbf6767be08ab4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_reallocate_asset_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_reallocate_asset_budgets_agent.py` and in the RCI capsule.

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
