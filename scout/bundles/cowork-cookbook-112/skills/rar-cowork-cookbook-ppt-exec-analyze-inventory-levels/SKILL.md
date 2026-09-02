---
name: "rar-cowork-cookbook-ppt-exec-analyze-inventory-levels"
description: "Generates an executive-ready PowerPoint deck on analyze inventory levels status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_inventory_levels", "rar_sha256": "86ff71eb286174a7f549b686342efd284cd0401592e95099c28aee24cf4106fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_analyze_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-analyze-inventory-levels:7460fdd7c986661d6b59859fda703468039874868266c569c1242ac8db512de4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_analyze_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_analyze_inventory_levels_agent.py` is
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
