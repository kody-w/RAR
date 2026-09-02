---
name: "rar-cowork-cookbook-ppt-exec-purchase-project-materials"
description: "Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_purchase_project_materials", "rar_sha256": "f1026d771ac3e1cc1744edebabea409575e145a0fbdb6660e1314730b161a305", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_purchase_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-purchase-project-materials:1e32b01d542f6a5d849c2103d665da2252e1e00c1e846d1142baf7ae68f57ce2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_purchase_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_purchase_project_materials_agent.py` is
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

Purchase project materials Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 f1026d771ac3e1cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_purchase_project_materials_agent.py` first:

```bash
python3 ppt_exec_purchase_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_purchase_project_materials_agent.py   # or on stdin
python3 ppt_exec_purchase_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase project materials Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_purchase_project_materials',
    "version": '2.0.0',
    "display_name": 'Purchase project materials Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-purchase-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4202ad671adb725',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/purchase-project-materials'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-purchase-project-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPurchaseProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPurchaseProjectMaterials'
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
    print(PptExecPurchaseProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
