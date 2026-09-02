---
name: "rar-cowork-cookbook-scheduled-brief-make-payments-on-asset-leases"
description: "Schedulable morning-brief email summarizing make payments on asset leases for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases", "rar_sha256": "6e6bab2f2fc3d307f85d62d50c834bb69be780785e78b118e06bf9feb09f7780", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_make_payments_on_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-make-payments-on-asset-leases:c3a2437f66b65ae6fb2bbed7d4a3c649de8601ec3aa56ef11d36be3629e9fe45", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_make_payments_on_asset_leases_agent.py` is
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
