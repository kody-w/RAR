---
name: "rar-cowork-cookbook-bulk-update-manage-service-assets"
description: "Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_service_assets", "rar_sha256": "c399311498ab9e0ff2de1d8ae37256e0d0b5df8c4a37bb59f3e42e8b91a05978", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_service_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-service-assets:033f097d43aab3c3690b796f1c271ef0082dfbeaca54172ab3ea2ae889557e37", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_service_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_service_assets_agent.py` is
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
