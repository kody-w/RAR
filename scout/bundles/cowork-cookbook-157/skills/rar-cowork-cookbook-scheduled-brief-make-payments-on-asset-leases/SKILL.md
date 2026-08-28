---
name: "rar-cowork-cookbook-scheduled-brief-make-payments-on-asset-leases"
description: "Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases", "rar_sha256": "1c78691b663c6bf2f95a4ebc88a987c3d066e3a2e19a3e66e2be877056b4a13f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_make_payments_on_asset_leases_agent.py` and in the RCI capsule.

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

Make payments on asset leases Scheduled Email Brief — Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 1c78691b663c6bf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_make_payments_on_asset_leases_agent.py` first:

```bash
python3 scheduled_brief_make_payments_on_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_make_payments_on_asset_leases_agent.py   # or on stdin
python3 scheduled_brief_make_payments_on_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Make payments on asset leases Scheduled Email Brief — Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases',
    "version": '2.0.1',
    "display_name": 'Make payments on asset leases Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-make-payments-on-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f2bc24ae3f35ed92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/make-payments-on-asset-leases'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-make-payments-on-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefMakePaymentsOnAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMakePaymentsOnAssetLeases'
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
    print(ScheduledBriefMakePaymentsOnAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
