---
name: "rar-cowork-cookbook-ppt-exec-design-warehouse-layout"
description: "Generates an executive-ready PowerPoint deck on design warehouse layout status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_design_warehouse_layout", "rar_sha256": "f31cb7d3d089354bfbc1df4865fb7b306de73724d65f325dcf42cb5dcca2a5a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_design_warehouse_layout_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-design-warehouse-layout:574b4a575a9f621e6adc6c3273fe4ead1a3e99e5ce38397dd1c8fd1807509f23", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_design_warehouse_layout`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_design_warehouse_layout_agent.py` is
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
