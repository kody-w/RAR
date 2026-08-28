---
name: "rar-cowork-cookbook-bulk-update-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "6f96a815442bea9e2f747b64b80cffa6cf695176267bfd6e29cf2341b481356f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` and embedded as the fenced Python below (sha256 6f96a815442bea9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` first:

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
    "version": '2.0.0',
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
