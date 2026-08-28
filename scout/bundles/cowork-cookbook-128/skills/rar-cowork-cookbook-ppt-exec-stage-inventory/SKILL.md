---
name: "rar-cowork-cookbook-ppt-exec-stage-inventory"
description: "Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_stage_inventory", "rar_sha256": "54cbecffa56c1152b8b5bd05270d8fde844c810c0d64e083858fe0edc5633542", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_stage_inventory`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_stage_inventory_agent.py` and in the RCI capsule.

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

Stage inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 54cbecffa56c1152…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_stage_inventory_agent.py` first:

```bash
python3 ppt_exec_stage_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_stage_inventory_agent.py   # or on stdin
python3 ppt_exec_stage_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stage inventory Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-stage-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_stage_inventory',
    "version": '2.0.1',
    "display_name": 'Stage inventory Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-stage-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-stage-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7174ae9dcd7a9dde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/stage-inventory'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-stage-inventory', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecStageInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecStageInventory'
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
    print(PptExecStageInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
