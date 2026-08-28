---
name: "rar-cowork-cookbook-teams-update-make-payments-on-asset-leases"
description: "Drafts a Teams channel post on make payments on asset leases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_make_payments_on_asset_leases", "rar_sha256": "1872acf782ae72009f988f11222881f433ba2f9595dcc92d1c020b7d395ed22d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 1872acf782ae7200…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_make_payments_on_asset_leases_agent.py` first:

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
    "version": '2.0.1',
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
