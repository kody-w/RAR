---
name: "rar-cowork-cookbook-audit-nurture-opportunities-and-finalize-the-sale"
description: "Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "34fcf9159ef5fbf0cf17f634d81a9ee43be45e816d10c7fe753eaf49395a923b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale`. The original RAPP
agent is preserved byte-for-byte in `audit_nurture_opportunities_and_finalize_the_sale_agent.py` and in the RCI capsule.

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
