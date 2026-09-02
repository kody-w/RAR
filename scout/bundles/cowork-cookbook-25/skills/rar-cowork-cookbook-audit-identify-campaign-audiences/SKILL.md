---
name: "rar-cowork-cookbook-audit-identify-campaign-audiences"
description: "Audits identify campaign audiences records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_campaign_audiences", "rar_sha256": "a05b699d8699abf20a652bc09125a60567f156caab3136c9084cf2ca3942290e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_identify_campaign_audiences_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-identify-campaign-audiences:da7f3d486dee3008089e8fa5b3d854ecafb3c0c6bb27c0732ddb96716e2c0ff5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_identify_campaign_audiences`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_identify_campaign_audiences_agent.py` is
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
