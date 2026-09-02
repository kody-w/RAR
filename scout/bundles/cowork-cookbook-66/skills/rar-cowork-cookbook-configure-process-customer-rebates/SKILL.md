---
name: "rar-cowork-cookbook-configure-process-customer-rebates"
description: "Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_customer_rebates", "rar_sha256": "bee916b55162c3ade3b9c39a521b9f019e4aeda4412bf92278372360a8f92d50", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_process_customer_rebates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-process-customer-rebates:a094401266d3d6d7e0e27febb4c1b39bd4029d163a125b25641c1e1045e2d297", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_process_customer_rebates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_process_customer_rebates_agent.py` is
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

Process customer rebates Configuration Bulk Setup — Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 bee916b55162c3ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_customer_rebates_agent.py` first:

```bash
python3 configure_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_customer_rebates_agent.py   # or on stdin
python3 configure_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Configuration Bulk Setup — Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_customer_rebates',
    "version": '2.0.0',
    "display_name": 'Process customer rebates Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process customer rebates from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74fb36817befa894',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureProcessCustomerRebates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessCustomerRebates'
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
    print(ConfigureProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
