---
name: "rar-cowork-cookbook-bulk-update-plan-fixed-assets"
description: "Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_fixed_assets", "rar_sha256": "73f37da8efd9cbc645818bcb830dace10aad44bd74b18e7aba1989e78332e14e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_fixed_assets_agent.py` and in the RCI capsule.

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

Plan fixed assets Bulk Field Update — Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 73f37da8efd9cbc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_fixed_assets_agent.py` first:

```bash
python3 bulk_update_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_fixed_assets_agent.py   # or on stdin
python3 bulk_update_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Bulk Field Update — Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Plan fixed assets Bulk Field Update',
    "description": 'Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cef2d87410fdc42f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanFixedAssets'
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
    print(BulkUpdatePlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
