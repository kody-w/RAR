---
name: "rar-cowork-cookbook-audit-identify-campaign-audiences"
description: "Audits identify campaign audiences records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_campaign_audiences", "rar_sha256": "185c768f479df8b65dcc8cc5f8a8a6e7c704dd10256d3f9c84b49b69b66ca9dd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

Identify campaign audiences Completeness Audit — Audits identify campaign audiences records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-campaign-audiences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 185c768f479df8b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_campaign_audiences_agent.py` first:

```bash
python3 audit_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_campaign_audiences_agent.py   # or on stdin
python3 audit_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Completeness Audit — Audits identify campaign audiences records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_campaign_audiences',
    "version": '2.0.1',
    "display_name": 'Identify campaign audiences Completeness Audit',
    "description": 'Audits identify campaign audiences records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9a00a5af868f2c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditIdentifyCampaignAudiences(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyCampaignAudiences'
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
    print(AuditIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
