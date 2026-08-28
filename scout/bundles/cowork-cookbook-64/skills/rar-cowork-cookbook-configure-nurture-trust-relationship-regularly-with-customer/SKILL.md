---
name: "rar-cowork-cookbook-configure-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "7c5fc72f6631cf00ac0e3f645fda1a28589be2bbedca70a752e6ec7ebf4fb5b7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 7c5fc72f6631cf00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_nurture_trust_relationship_regularly_with_customer_agent.py` first:

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
    "version": '2.0.0',
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
