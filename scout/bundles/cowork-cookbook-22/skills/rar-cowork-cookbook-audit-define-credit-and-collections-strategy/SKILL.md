---
name: "rar-cowork-cookbook-audit-define-credit-and-collections-strategy"
description: "Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_credit_and_collections_strategy", "rar_sha256": "9eafc1113aa4cf3cd77960dbbd65b3c05a8cb0de17b653d1031fb01fdef9d9e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_credit_and_collections_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-credit-and-collections-strategy:4570dc323926e90ff159930b2434e553978218bdf3071e17d7b1c8c194c7f06d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_credit_and_collections_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_credit_and_collections_strategy_agent.py` is
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

Define credit and collections strategy Completeness Audit — Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 9eafc1113aa4cf3c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_credit_and_collections_strategy_agent.py` first:

```bash
python3 audit_define_credit_and_collections_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_credit_and_collections_strategy_agent.py   # or on stdin
python3 audit_define_credit_and_collections_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define credit and collections strategy Completeness Audit — Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_credit_and_collections_strategy',
    "version": '2.0.0',
    "display_name": 'Define credit and collections strategy Completeness Audit',
    "description": 'Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-define-credit-and-collections-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '496eb120648787b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-credit-and-collections-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-define-credit-and-collections-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineCreditAndCollectionsStrategy(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineCreditAndCollectionsStrategy'
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
    print(AuditDefineCreditAndCollectionsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
