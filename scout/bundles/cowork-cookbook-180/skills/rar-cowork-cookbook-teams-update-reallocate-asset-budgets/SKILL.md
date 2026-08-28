---
name: "rar-cowork-cookbook-teams-update-reallocate-asset-budgets"
description: "Drafts a Teams channel post on reallocate asset budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reallocate_asset_budgets", "rar_sha256": "66dbadda92ce7b0fcbf86b22ee6d3ced7fcfa7cfc86c34c3257f7442fd573cd4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 66dbadda92ce7b0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reallocate_asset_budgets_agent.py` first:

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
    "version": '2.0.1',
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
