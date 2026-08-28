---
name: "rar-cowork-cookbook-ppt-exec-analyze-inventory-levels"
description: "Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_inventory_levels", "rar_sha256": "86ff71eb286174a7f549b686342efd284cd0401592e95099c28aee24cf4106fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 86ff71eb286174a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_inventory_levels_agent.py` first:

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
    "version": '2.0.0',
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
