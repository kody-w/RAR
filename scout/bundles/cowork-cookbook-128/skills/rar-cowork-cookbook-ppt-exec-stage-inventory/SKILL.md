---
name: "rar-cowork-cookbook-ppt-exec-stage-inventory"
description: "Generates an executive-ready PowerPoint deck on stage inventory status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_stage_inventory", "rar_sha256": "769cdbcd4aaec60e3e2e2bd8926c7447af43a00a232c6f46af7647cf37ecab94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 769cdbcd4aaec60e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_stage_inventory_agent.py` first:

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
    "version": '2.0.0',
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
