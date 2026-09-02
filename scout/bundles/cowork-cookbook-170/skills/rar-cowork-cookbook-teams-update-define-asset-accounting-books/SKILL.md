---
name: "rar-cowork-cookbook-teams-update-define-asset-accounting-books"
description: "Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_asset_accounting_books", "rar_sha256": "38085e691dee2f1a6c3c97c1d5bf9d74ba18709eb16bc6cd90e93a16e604ab8a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_asset_accounting_books_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-asset-accounting-books:dbf6c9c5a9fe219616ef4844a8af55279ff3e5dcd3690fe637f49dd10a8e662f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_asset_accounting_books`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_asset_accounting_books_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 38085e691dee2f1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_asset_accounting_books_agent.py` first:

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
    "version": '2.0.0',
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
