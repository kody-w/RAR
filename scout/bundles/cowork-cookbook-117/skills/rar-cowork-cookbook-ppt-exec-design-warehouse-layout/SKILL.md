---
name: "rar-cowork-cookbook-ppt-exec-design-warehouse-layout"
description: "Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_design_warehouse_layout", "rar_sha256": "3bb97d0b6d5f37c069b1f48f4620b56857427e0752f68cf2d1a2ea31531de088", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_design_warehouse_layout`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_design_warehouse_layout_agent.py` and in the RCI capsule.

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

Design warehouse layout Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 3bb97d0b6d5f37c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_design_warehouse_layout_agent.py` first:

```bash
python3 ppt_exec_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_design_warehouse_layout_agent.py   # or on stdin
python3 ppt_exec_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_design_warehouse_layout',
    "version": '2.0.1',
    "display_name": 'Design warehouse layout Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00257d27be0947af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDesignWarehouseLayout(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDesignWarehouseLayout'
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
    print(PptExecDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
