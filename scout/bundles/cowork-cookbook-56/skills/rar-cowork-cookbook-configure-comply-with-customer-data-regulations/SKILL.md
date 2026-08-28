---
name: "rar-cowork-cookbook-configure-comply-with-customer-data-regulations"
description: "Applies a bulk configuration change to comply with customer data regulations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_comply_with_customer_data_regulations", "rar_sha256": "cf9e34d3926a81c890196bfed34cf267c2938088c0b536b674993b1339d73bf8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 cf9e34d3926a81c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_comply_with_customer_data_regulations_agent.py` first:

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
    "version": '2.0.0',
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
