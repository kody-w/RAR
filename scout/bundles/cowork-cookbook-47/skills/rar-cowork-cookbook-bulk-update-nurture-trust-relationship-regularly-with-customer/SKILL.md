---
name: "rar-cowork-cookbook-bulk-update-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "0df661a81ce7be23db9f70ed5f167a2ae3c99ede005115933469c6801de08b4c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` and in the RCI capsule.

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

Nurture trust relationship regularly with customer Bulk Field Update — Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 0df661a81ce7be23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` first:

```bash
python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py   # or on stdin
python3 bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture trust relationship regularly with customer Bulk Field Update — Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer',
    "version": '2.0.1',
    "display_name": 'Nurture trust relationship regularly with customer Bulk Field Update',
    "description": 'Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-nurture-trust-relationship-regularly-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-nurture-trust-relationship-regularly-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'addcb409d2e93326',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-nurture-trust-relationship-regularly-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer'
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
    print(BulkUpdateNurtureTrustRelationshipRegularlyWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
