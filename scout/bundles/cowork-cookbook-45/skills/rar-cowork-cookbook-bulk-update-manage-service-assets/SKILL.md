---
name: "rar-cowork-cookbook-bulk-update-manage-service-assets"
description: "Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_service_assets", "rar_sha256": "c399311498ab9e0ff2de1d8ae37256e0d0b5df8c4a37bb59f3e42e8b91a05978", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Bulk Field Update — Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 c399311498ab9e0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_service_assets_agent.py` first:

```bash
python3 bulk_update_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_service_assets_agent.py   # or on stdin
python3 bulk_update_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Bulk Field Update — Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_service_assets',
    "version": '2.0.0',
    "display_name": 'Manage service assets Bulk Field Update',
    "description": 'Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f87de82dc43074',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateManageServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageServiceAssets'
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
    print(BulkUpdateManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
