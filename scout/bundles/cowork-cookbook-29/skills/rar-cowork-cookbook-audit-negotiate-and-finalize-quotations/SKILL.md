---
name: "rar-cowork-cookbook-audit-negotiate-and-finalize-quotations"
description: "Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_negotiate_and_finalize_quotations", "rar_sha256": "e053e88e67016e8c17a7fc5a9de243b9e46cf82257bd80ad0412d885a33a7b7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_negotiate_and_finalize_quotations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-negotiate-and-finalize-quotations:7f75d6e47300c5b65881ebf453c1950fa50bc08600b8054a2bc1a30b112e211a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_negotiate_and_finalize_quotations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_negotiate_and_finalize_quotations_agent.py` is
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

Negotiate and finalize quotations Completeness Audit — Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 e053e88e67016e8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 audit_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 audit_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Completeness Audit — Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_negotiate_and_finalize_quotations',
    "version": '2.0.0',
    "display_name": 'Negotiate and finalize quotations Completeness Audit',
    "description": 'Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '98a0da8dd8ea1a49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditNegotiateAndFinalizeQuotations(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditNegotiateAndFinalizeQuotations'
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
    print(AuditNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
