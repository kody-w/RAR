---
name: "rar-cowork-cookbook-customer-relationship-health-check"
description: "Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_relationship_health_check", "rar_sha256": "8b42b6eb45afa21932d15734e422dd0316e3e50f7dc2fb2b525541a4c7acdabb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_relationship_health_check`. The original RAPP
agent is preserved byte-for-byte in `customer_relationship_health_check_agent.py` and in the RCI capsule.

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
