---
name: "rar-cowork-cookbook-scheduled-brief-make-payments-on-asset-leases"
description: "Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases", "rar_sha256": "6e6bab2f2fc3d307f85d62d50c834bb69be780785e78b118e06bf9feb09f7780", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 6e6bab2f2fc3d307…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_make_payments_on_asset_leases_agent.py` first:

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
    "version": '2.0.0',
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
