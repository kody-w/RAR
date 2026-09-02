---
name: "rar-cowork-cookbook-configure-purchase-assets"
description: "Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_purchase_assets", "rar_sha256": "5d1e1ec783be94e49c4613a21679b7bc49db282a1935545a46f3593ec5710de0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_purchase_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-purchase-assets:251bd54cdbe0607c04bfdcc0b4a55ec87b39ed13c0eb2a980956e2d201653a08", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_purchase_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_purchase_assets_agent.py` is
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

Purchase assets Configuration Bulk Setup — Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 5d1e1ec783be94e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_purchase_assets_agent.py` first:

```bash
python3 configure_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_purchase_assets_agent.py   # or on stdin
python3 configure_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Configuration Bulk Setup — Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_purchase_assets',
    "version": '2.0.0',
    "display_name": 'Purchase assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0238913c360410d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePurchaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePurchaseAssets'
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
    print(ConfigurePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
