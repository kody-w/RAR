---
name: "rar-cowork-cookbook-audit-manage-service-pricing"
description: "Audits manage service pricing records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_service_pricing", "rar_sha256": "c3a49be07024e04f23e774b375ff80a61b2b6bd9cfbdbd82ecac8f503136a568", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_service_pricing`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_service_pricing_agent.py` and in the RCI capsule.

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

Manage service pricing Completeness Audit — Audits manage service pricing records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-service-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 c3a49be07024e04f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_service_pricing_agent.py` first:

```bash
python3 audit_manage_service_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_service_pricing_agent.py   # or on stdin
python3 audit_manage_service_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service pricing Completeness Audit — Audits manage service pricing records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-service-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_service_pricing',
    "version": '2.0.1',
    "display_name": 'Manage service pricing Completeness Audit',
    "description": 'Audits manage service pricing records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-service-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-service-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '54811aead14b2a7f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-service-pricing'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-manage-service-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditManageServicePricing(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageServicePricing'
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
    print(AuditManageServicePricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
