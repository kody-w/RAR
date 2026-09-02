---
name: "rar-cowork-cookbook-configure-release-goods-for-picking"
description: "Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_release_goods_for_picking", "rar_sha256": "e208ea5cd5b571c8e15369388a86f0c91e842436b19da84e2b4aee8ab37bb50b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_release_goods_for_picking_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-release-goods-for-picking:2e7f40dac9b18edf04f8f1dc6f2a2692730e9073380ff8f20c5680ca4ab980bd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_release_goods_for_picking`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_release_goods_for_picking_agent.py` is
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

Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 e208ea5cd5b571c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_release_goods_for_picking_agent.py` first:

```bash
python3 configure_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_release_goods_for_picking_agent.py   # or on stdin
python3 configure_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Configuration Bulk Setup — Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_release_goods_for_picking',
    "version": '2.0.0',
    "display_name": 'Release goods for picking Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to release goods for picking from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf924e23a2ff7814',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReleaseGoodsForPicking(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReleaseGoodsForPicking'
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
    print(ConfigureReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
