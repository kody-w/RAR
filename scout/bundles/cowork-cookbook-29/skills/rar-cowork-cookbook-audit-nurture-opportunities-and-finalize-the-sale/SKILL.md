---
name: "rar-cowork-cookbook-audit-nurture-opportunities-and-finalize-the-sale"
description: "Audits nurture opportunities and finalize the sale records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "1e5ebec5a0278513300d0509346091acf6bcc09dbf3e51616ec025fb101cf25a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 1e5ebec5a0278513…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_nurture_opportunities_and_finalize_the_sale_agent.py` first:

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
    "version": '2.0.1',
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
