---
name: "rar-cowork-cookbook-scheduled-brief-record-fixed-asset-acquisitions"
description: "Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions", "rar_sha256": "5bde048d115c9fcc154e2ed451da0a53e673427ad04c0258d330ae482bb8c31c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_fixed_asset_acquisitions_agent.py` and in the RCI capsule.

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
