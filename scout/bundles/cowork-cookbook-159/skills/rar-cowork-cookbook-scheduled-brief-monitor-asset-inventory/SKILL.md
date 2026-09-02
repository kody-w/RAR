---
name: "rar-cowork-cookbook-scheduled-brief-monitor-asset-inventory"
description: "Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_asset_inventory", "rar_sha256": "efed03c2a467f10a1207527ea480ebfb44633d25ab7693a9be439b1449cca6f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_monitor_asset_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-monitor-asset-inventory:6483a378c4f3c7d3df1d50eac1f4dfc8d145e944bbde39891c5944012ebb23f4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_monitor_asset_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_monitor_asset_inventory_agent.py` is
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

Monitor asset inventory Scheduled Email Brief — Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 efed03c2a467f10a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_asset_inventory_agent.py` first:

```bash
python3 scheduled_brief_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_asset_inventory_agent.py   # or on stdin
python3 scheduled_brief_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Scheduled Email Brief — Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_asset_inventory',
    "version": '2.0.0',
    "display_name": 'Monitor asset inventory Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b91b6bb99e310167',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefMonitorAssetInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorAssetInventory'
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
    print(ScheduledBriefMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
