---
name: "rar-cowork-cookbook-audit-determine-sales-targets"
description: "Audits determine sales targets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_determine_sales_targets", "rar_sha256": "17f88e729adb092ce193a45729f6f7d141570370b2b79c05efccb7be3a23c7d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_determine_sales_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-determine-sales-targets:238f241437d20b24321f7100cc998bfe95b64d390d2c3db4e7b825ada27fb8a8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_determine_sales_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_determine_sales_targets_agent.py` is
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

Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 17f88e729adb092c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_determine_sales_targets_agent.py` first:

```bash
python3 audit_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_determine_sales_targets_agent.py   # or on stdin
python3 audit_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_determine_sales_targets',
    "version": '2.0.0',
    "display_name": 'Determine sales targets Completeness Audit',
    "description": 'Audits determine sales targets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4437a045ed395fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDetermineSalesTargets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDetermineSalesTargets'
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
    print(AuditDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
