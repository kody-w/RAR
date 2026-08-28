---
name: "rar-cowork-cookbook-ppt-exec-purchase-project-materials"
description: "Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_purchase_project_materials", "rar_sha256": "f1026d771ac3e1cc1744edebabea409575e145a0fbdb6660e1314730b161a305", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_purchase_project_materials`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_purchase_project_materials_agent.py` and in the RCI capsule.

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
