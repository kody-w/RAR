---
name: "rar-cowork-cookbook-audit-manage-service-pricing"
description: "Audits manage service pricing records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_service_pricing", "rar_sha256": "9dd460e414e6072cf390aca002086fe1d075dff9415ad09fd80d3612d6e30b34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 9dd460e414e6072c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_service_pricing_agent.py` first:

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
    "version": '2.0.0',
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
