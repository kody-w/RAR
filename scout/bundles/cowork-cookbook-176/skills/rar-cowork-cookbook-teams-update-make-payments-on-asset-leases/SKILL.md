---
name: "rar-cowork-cookbook-teams-update-make-payments-on-asset-leases"
description: "Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_make_payments_on_asset_leases", "rar_sha256": "5ade59413d24f6c421ae395e1f8d5c921775b5e04f299b9c0dd0d134f5f94e07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_make_payments_on_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `teams_update_make_payments_on_asset_leases_agent.py` and in the RCI capsule.

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
