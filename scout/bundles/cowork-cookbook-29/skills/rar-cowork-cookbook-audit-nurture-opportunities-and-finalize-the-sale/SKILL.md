---
name: "rar-cowork-cookbook-audit-nurture-opportunities-and-finalize-the-sale"
description: "Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "34fcf9159ef5fbf0cf17f634d81a9ee43be45e816d10c7fe753eaf49395a923b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_nurture_opportunities_and_finalize_the_sale_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-nurture-opportunities-and-finalize-the-sale:792d5ef6bc6a92275592d894ebe3a730dea4ab3128bdbfadc054c5b6e7cb3592", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_nurture_opportunities_and_finalize_the_sale_agent.py` is
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

Nurture opportunities and finalize the sale Completeness Audit — Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 34fcf9159ef5fbf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_nurture_opportunities_and_finalize_the_sale_agent.py` first:

```bash
python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py   # or on stdin
python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture opportunities and finalize the sale Completeness Audit — Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale',
    "version": '2.0.0',
    "display_name": 'Nurture opportunities and finalize the sale Completeness Audit',
    "description": 'Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-nurture-opportunities-and-finalize-the-sale',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '71e73d36a83634a8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-nurture-opportunities-and-finalize-the-sale', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditNurtureOpportunitiesAndFinalizeTheSale(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditNurtureOpportunitiesAndFinalizeTheSale'
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
    print(AuditNurtureOpportunitiesAndFinalizeTheSale().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
