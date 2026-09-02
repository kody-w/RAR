---
name: "rar-cowork-cookbook-teams-update-make-payments-on-asset-leases"
description: "Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_make_payments_on_asset_leases", "rar_sha256": "5ade59413d24f6c421ae395e1f8d5c921775b5e04f299b9c0dd0d134f5f94e07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_make_payments_on_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-make-payments-on-asset-leases:b4bd052f282b7ce92b09cae8f4b53a1553a55886e8c2940ee1fc9b2a4defc001", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_make_payments_on_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_make_payments_on_asset_leases_agent.py` is
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

Make payments on asset leases Teams Channel Update — Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 5ade59413d24f6c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_make_payments_on_asset_leases_agent.py` first:

```bash
python3 teams_update_make_payments_on_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_make_payments_on_asset_leases_agent.py   # or on stdin
python3 teams_update_make_payments_on_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Make payments on asset leases Teams Channel Update — Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_make_payments_on_asset_leases',
    "version": '2.0.0',
    "display_name": 'Make payments on asset leases Teams Channel Update',
    "description": 'Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-make-payments-on-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c08a907c4fe7f32e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/make-payments-on-asset-leases'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-make-payments-on-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateMakePaymentsOnAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMakePaymentsOnAssetLeases'
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
    print(TeamsUpdateMakePaymentsOnAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
