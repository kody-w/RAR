---
name: "rar-cowork-cookbook-audit-develop-loyalty-programs"
description: "Audits develop loyalty programs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_loyalty_programs", "rar_sha256": "ee0591a3b080ea51744e7eaa27e2f99404ee87ebea596ac69e050148c3b41f3d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_loyalty_programs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-loyalty-programs:94f4b41e605e1e1c03c4a4637886bb4e94ed8c43e5390b6681ffe182b19c7934", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_loyalty_programs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_loyalty_programs_agent.py` is
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

Develop loyalty programs Completeness Audit — Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 ee0591a3b080ea51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_loyalty_programs_agent.py` first:

```bash
python3 audit_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_loyalty_programs_agent.py   # or on stdin
python3 audit_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Completeness Audit — Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_loyalty_programs',
    "version": '2.0.0',
    "display_name": 'Develop loyalty programs Completeness Audit',
    "description": 'Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e5bdf08f586dda6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopLoyaltyPrograms(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLoyaltyPrograms'
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
    print(AuditDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
