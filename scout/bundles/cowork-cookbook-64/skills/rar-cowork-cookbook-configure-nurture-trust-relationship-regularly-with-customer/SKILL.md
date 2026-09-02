---
name: "rar-cowork-cookbook-configure-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk configuration change to nurture trust relationship regularly with customer from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "7c5fc72f6631cf00ac0e3f645fda1a28589be2bbedca70a752e6ec7ebf4fb5b7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_nurture_trust_relationship_regularly_with_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-nurture-trust-relationship-regularly-with-customer:6918970f20d7044a5ec895c59359e5763180e8f2997ac7f120947378f324fd2d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_nurture_trust_relationship_regularly_with_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_nurture_trust_relationship_regularly_with_customer_agent.py` is
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
