---
name: "rar-cowork-cookbook-ppt-exec-purchase-project-materials"
description: "Generates an executive-ready PowerPoint deck on purchase project materials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_purchase_project_materials", "rar_sha256": "3b6ea48eae57056a6e14e415f9166db60e7bf2d286b93c2f3419a7e96967a381", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 3b6ea48eae57056a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_purchase_project_materials_agent.py` first:

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
    "version": '2.0.1',
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
