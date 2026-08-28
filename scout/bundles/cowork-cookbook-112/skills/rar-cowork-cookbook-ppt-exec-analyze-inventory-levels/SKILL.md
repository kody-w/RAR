---
name: "rar-cowork-cookbook-ppt-exec-analyze-inventory-levels"
description: "Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_inventory_levels", "rar_sha256": "294935a699bdb6ac9b2c178bbf007dd5494ebee14496a0755d4b6dcd3704a671", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_inventory_levels_agent.py` and in the RCI capsule.

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

Analyze inventory levels Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 294935a699bdb6ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_inventory_levels_agent.py` first:

```bash
python3 ppt_exec_analyze_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_inventory_levels_agent.py   # or on stdin
python3 ppt_exec_analyze_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze inventory levels Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_inventory_levels',
    "version": '2.0.1',
    "display_name": 'Analyze inventory levels Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-analyze-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a1d6bb7764cb22fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/analyze-inventory-levels'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-analyze-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecAnalyzeInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeInventoryLevels'
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
    print(PptExecAnalyzeInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
