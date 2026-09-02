---
name: "rar-cowork-cookbook-configure-receive-goods"
description: "Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_goods", "rar_sha256": "fe615efa546e693b7ed88e3b188b2cf364d1b858aeb89bd1785fd2b028414770", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_receive_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-receive-goods:e3f9e90c44615330c8aefb24be16f88651065cd26b973e98ca217cf6508e80f4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_receive_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_receive_goods_agent.py` is
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

Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_goods_agent.py` and embedded as the fenced Python below (sha256 fe615efa546e693b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_goods_agent.py` first:

```bash
python3 configure_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_goods_agent.py   # or on stdin
python3 configure_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Configuration Bulk Setup — Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_goods',
    "version": '2.0.0',
    "display_name": 'Receive goods Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to receive goods from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e20ccf7ee06717ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReceiveGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveGoods'
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
    print(ConfigureReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
