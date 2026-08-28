---
name: "rar-cowork-cookbook-configure-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "4123f5ee545297c7c93f4607fdaa1e925864b9b40011629e035e9aacb31857c5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer`. The original RAPP
agent is preserved byte-for-byte in `configure_nurture_trust_relationship_regularly_with_customer_agent.py` and in the RCI capsule.

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

Nurture trust relationship regularly with customer Configuration Bulk Setup — Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 4123f5ee545297c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_nurture_trust_relationship_regularly_with_customer_agent.py` first:

```bash
python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py   # or on stdin
python3 configure_nurture_trust_relationship_regularly_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture trust relationship regularly with customer Configuration Bulk Setup — Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer',
    "version": '2.0.1',
    "display_name": 'Nurture trust relationship regularly with customer Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-nurture-trust-relationship-regularly-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-nurture-trust-relationship-regularly-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0af5a5fd8a971020',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-nurture-trust-relationship-regularly-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureNurtureTrustRelationshipRegularlyWithCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureNurtureTrustRelationshipRegularlyWithCustomer'
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
    print(ConfigureNurtureTrustRelationshipRegularlyWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
