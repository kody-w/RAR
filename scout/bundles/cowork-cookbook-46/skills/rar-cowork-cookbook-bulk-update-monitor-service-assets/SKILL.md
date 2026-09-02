---
name: "rar-cowork-cookbook-bulk-update-monitor-service-assets"
description: "Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_service_assets", "rar_sha256": "04d4eb275a42eb84f67e8e0edf42fe84275759d315b1f84bcde2f96cdb27f6e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_monitor_service_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-monitor-service-assets:485f8da549836a9ee0be52192de1697aa6030088e62b9081697757e5700af5e9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_monitor_service_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_monitor_service_assets_agent.py` is
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

Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 04d4eb275a42eb84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_service_assets_agent.py` first:

```bash
python3 bulk_update_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_service_assets_agent.py   # or on stdin
python3 bulk_update_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Bulk Field Update — Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_service_assets',
    "version": '2.0.0',
    "display_name": 'Monitor service assets Bulk Field Update',
    "description": 'Applies a bulk field update across monitor service assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'bulk-update-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77eaeda621d19829',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorServiceAssets'
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
    print(BulkUpdateMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
