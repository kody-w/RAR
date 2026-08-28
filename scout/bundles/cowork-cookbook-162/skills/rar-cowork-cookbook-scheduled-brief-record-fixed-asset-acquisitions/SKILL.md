---
name: "rar-cowork-cookbook-scheduled-brief-record-fixed-asset-acquisitions"
description: "Schedulable morning-brief email summarizing record fixed asset acquisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions", "rar_sha256": "8033636c2ba445df095a72c1512f1204e17f605918e451b4a4aa9ec31392d206", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 8033636c2ba445df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_fixed_asset_acquisitions_agent.py` first:

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
    "version": '2.0.1',
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
