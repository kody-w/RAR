---
name: "rar-cowork-cookbook-audit-identify-campaign-audiences"
description: "Audits identify campaign audiences records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_campaign_audiences", "rar_sha256": "a05b699d8699abf20a652bc09125a60567f156caab3136c9084cf2ca3942290e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 a05b699d8699abf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_campaign_audiences_agent.py` first:

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
    "version": '2.0.0',
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
