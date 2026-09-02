---
name: "rar-cowork-cookbook-customer-relationship-health-check"
description: "Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_relationship_health_check", "rar_sha256": "8b42b6eb45afa21932d15734e422dd0316e3e50f7dc2fb2b525541a4c7acdabb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "customer_relationship_health_check_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/customer-relationship-health-check:3dcbe65b7e8087d5393f5d52a8928a6952cdb13cea42c747135385db451aa039", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/customer_relationship_health_check`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `customer_relationship_health_check_agent.py` is
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

Customer Relationship Health Check — Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-relationship-health-check
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_relationship_health_check_agent.py` and embedded as the fenced Python below (sha256 8b42b6eb45afa219…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_relationship_health_check_agent.py` first:

```bash
python3 customer_relationship_health_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_relationship_health_check_agent.py   # or on stdin
python3 customer_relationship_health_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Relationship Health Check — Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-relationship-health-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_relationship_health_check',
    "version": '2.0.0',
    "display_name": 'Customer Relationship Health Check',
    "description": 'Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'customer-relationship-health-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-relationship-health-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec768a5a495ba82f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-relationship-health-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.375, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:check'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CustomerRelationshipHealthCheck(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerRelationshipHealthCheck'
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
    print(CustomerRelationshipHealthCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
