---
name: "rar-cowork-cookbook-ppt-exec-design-warehouse-layout"
description: "Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_design_warehouse_layout", "rar_sha256": "f31cb7d3d089354bfbc1df4865fb7b306de73724d65f325dcf42cb5dcca2a5a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 f31cb7d3d089354b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_design_warehouse_layout_agent.py` first:

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
    "version": '2.0.0',
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
