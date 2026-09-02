---
name: "rar-cowork-cookbook-audit-manage-customer-collections"
description: "Audits manage customer collections records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_customer_collections", "rar_sha256": "6bc8c8d81f81166d6ad3208486bf287d59bb046ffce6c7bc483a3a8ad4d1c092", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_customer_collections_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-customer-collections:5f8df677e749127f78195f809896c32fe1f7965872a8a7774725587ea8fa9420", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_customer_collections`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_customer_collections_agent.py` is
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

Manage customer collections Completeness Audit — Audits manage customer collections records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 6bc8c8d81f81166d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_customer_collections_agent.py` first:

```bash
python3 audit_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_customer_collections_agent.py   # or on stdin
python3 audit_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Completeness Audit — Audits manage customer collections records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_customer_collections',
    "version": '2.0.0',
    "display_name": 'Manage customer collections Completeness Audit',
    "description": 'Audits manage customer collections records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd10b0e6ddeca0080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditManageCustomerCollections(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageCustomerCollections'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
