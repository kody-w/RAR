---
name: "rar-cowork-cookbook-scheduled-brief-record-fixed-asset-acquisitions"
description: "Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions", "rar_sha256": "5bde048d115c9fcc154e2ed451da0a53e673427ad04c0258d330ae482bb8c31c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_record_fixed_asset_acquisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-record-fixed-asset-acquisitions:cfea392d7838643eeff2926a4ba2a92b088a08195d54829f30045ad9570cb962", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_record_fixed_asset_acquisitions_agent.py` is
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

Record fixed asset acquisitions Scheduled Email Brief — Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 5bde048d115c9fcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_fixed_asset_acquisitions_agent.py` first:

```bash
python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py   # or on stdin
python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record fixed asset acquisitions Scheduled Email Brief — Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions',
    "version": '2.0.0',
    "display_name": 'Record fixed asset acquisitions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-record-fixed-asset-acquisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef20ab6fa49a7847',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-fixed-asset-acquisitions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-record-fixed-asset-acquisitions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefRecordFixedAssetAcquisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordFixedAssetAcquisitions'
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
    print(ScheduledBriefRecordFixedAssetAcquisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
