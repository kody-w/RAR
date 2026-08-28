---
name: "rar-cowork-cookbook-bulk-update-plan-fixed-assets"
description: "Applies a bulk field update across plan fixed assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_fixed_assets", "rar_sha256": "729154de8bf949e7665a0d8a75d52c717f5f49bebb3afe8e0832a281b11e5b38", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 729154de8bf949e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_fixed_assets_agent.py` first:

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
    "version": '2.0.0',
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
