---
name: "rar-cowork-cookbook-teams-update-define-asset-accounting-books"
description: "Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_asset_accounting_books", "rar_sha256": "069fe25b58d4b964b7aac6e877fdc0c4b1ec223aec5f7567ac8a66caad1feb3b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Teams Channel Update — Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 069fe25b58d4b964…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_asset_accounting_books_agent.py` first:

```bash
python3 teams_update_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_asset_accounting_books_agent.py   # or on stdin
python3 teams_update_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Teams Channel Update — Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_asset_accounting_books',
    "version": '2.0.1',
    "display_name": 'Define asset accounting books Teams Channel Update',
    "description": 'Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66ee95ac0d59aaef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineAssetAccountingBooks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAssetAccountingBooks'
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
    print(TeamsUpdateDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
