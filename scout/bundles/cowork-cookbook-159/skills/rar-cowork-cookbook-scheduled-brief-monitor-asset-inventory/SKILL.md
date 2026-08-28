---
name: "rar-cowork-cookbook-scheduled-brief-monitor-asset-inventory"
description: "Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_asset_inventory", "rar_sha256": "f0b37c5332cf22e47ed05d99300d4dc4b2b7621d2bb7fa6ee17639472d31901c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 f0b37c5332cf22e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_asset_inventory_agent.py` first:

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
    "version": '2.0.1',
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
