---
name: "rar-cowork-cookbook-scheduled-brief-cross-dock-produced-goods"
description: "Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_cross_dock_produced_goods", "rar_sha256": "b712b92dd19c5e28c4ea8624d895fc7ed8d3dfd14d3ff5ad1900efc6b88a148f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_cross_dock_produced_goods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_cross_dock_produced_goods_agent.py` and in the RCI capsule.

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

Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_cross_dock_produced_goods_agent.py` and embedded as the fenced Python below (sha256 b712b92dd19c5e28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_cross_dock_produced_goods_agent.py` first:

```bash
python3 scheduled_brief_cross_dock_produced_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_cross_dock_produced_goods_agent.py   # or on stdin
python3 scheduled_brief_cross_dock_produced_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock produced goods Scheduled Email Brief — Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_cross_dock_produced_goods',
    "version": '2.0.1',
    "display_name": 'Cross dock produced goods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing cross dock produced goods for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-cross-dock-produced-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-cross-dock-produced-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddff51b800003739',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/cross-dock-produced-goods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-cross-dock-produced-goods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCrossDockProducedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCrossDockProducedGoods'
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
    print(ScheduledBriefCrossDockProducedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
