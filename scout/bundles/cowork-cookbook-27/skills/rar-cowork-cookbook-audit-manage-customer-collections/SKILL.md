---
name: "rar-cowork-cookbook-audit-manage-customer-collections"
description: "Audits manage customer collections records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_customer_collections", "rar_sha256": "b452a24c1cee0f3e23d6132ce2ac0ccef211670a60ecf3d43d2cb12df12f48f6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_customer_collections_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 b452a24c1cee0f3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_customer_collections_agent.py` first:

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
    "version": '2.0.1',
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
