---
name: "rar-cowork-cookbook-configure-comply-with-customer-data-regulations"
description: "Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_comply_with_customer_data_regulations", "rar_sha256": "2a2378c0076b814c83c927bf1d2ba3d22cbe29633fd7e08068db8ae530788484", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_comply_with_customer_data_regulations`. The original RAPP
agent is preserved byte-for-byte in `configure_comply_with_customer_data_regulations_agent.py` and in the RCI capsule.

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

Comply with customer data regulations Configuration Bulk Setup — Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 2a2378c0076b814c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_comply_with_customer_data_regulations_agent.py` first:

```bash
python3 configure_comply_with_customer_data_regulations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_comply_with_customer_data_regulations_agent.py   # or on stdin
python3 configure_comply_with_customer_data_regulations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Comply with customer data regulations Configuration Bulk Setup — Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_comply_with_customer_data_regulations',
    "version": '2.0.1',
    "display_name": 'Comply with customer data regulations Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-comply-with-customer-data-regulations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-comply-with-customer-data-regulations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e808a3e8db0f3d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/comply-with-customer-data-regulations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-comply-with-customer-data-regulations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureComplyWithCustomerDataRegulations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureComplyWithCustomerDataRegulations'
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
    print(ConfigureComplyWithCustomerDataRegulations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
