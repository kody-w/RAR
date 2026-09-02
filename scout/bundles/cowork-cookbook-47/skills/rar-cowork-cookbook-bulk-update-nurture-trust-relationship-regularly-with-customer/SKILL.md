---
name: "rar-cowork-cookbook-bulk-update-nurture-trust-relationship-regularly-with-customer"
description: "Applies a bulk field update across nurture trust relationship regularly with customer records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer", "rar_sha256": "6f96a815442bea9e2f747b64b80cffa6cf695176267bfd6e29cf2341b481356f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-nurture-trust-relationship-regularly-with-customer:cac3bfd65b0668fa76bfae797af883b9227d06be173b02bce922f46e92b4db0c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_nurture_trust_relationship_regularly_with_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_nurture_trust_relationship_regularly_with_customer_agent.py` is
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
