---
name: "rar-cowork-cookbook-audit-manage-service-pricing"
description: "Audits manage service pricing records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_service_pricing", "rar_sha256": "9dd460e414e6072cf390aca002086fe1d075dff9415ad09fd80d3612d6e30b34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_service_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-service-pricing:1709da08654c392476c218524b20d5a550b1beee88b2818d1df38adad4baef1b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_service_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_service_pricing_agent.py` is
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
