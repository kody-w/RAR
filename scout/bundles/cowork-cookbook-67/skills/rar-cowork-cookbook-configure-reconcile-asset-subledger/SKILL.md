---
name: "rar-cowork-cookbook-configure-reconcile-asset-subledger"
description: "Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_asset_subledger", "rar_sha256": "9830cd1711efac4ffca4524cc9cd41aedd36bd9a9216bd9a76ec58593dfa5049", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_reconcile_asset_subledger_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-reconcile-asset-subledger:a837628776207c15609381d3e385ffb4fe0d3f6015cbae29d9d1960e9d1c059d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_reconcile_asset_subledger`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_reconcile_asset_subledger_agent.py` is
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

Reconcile asset subledger Configuration Bulk Setup — Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 9830cd1711efac4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_asset_subledger_agent.py` first:

```bash
python3 configure_reconcile_asset_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_asset_subledger_agent.py   # or on stdin
python3 configure_reconcile_asset_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile asset subledger Configuration Bulk Setup — Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_asset_subledger',
    "version": '2.0.0',
    "display_name": 'Reconcile asset subledger Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reconcile-asset-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f60d19f06198b18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/reconcile-asset-subledger'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-reconcile-asset-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReconcileAssetSubledger(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileAssetSubledger'
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
    print(ConfigureReconcileAssetSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
