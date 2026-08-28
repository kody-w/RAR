---
name: "rar-cowork-cookbook-customer-relationship-health-check"
description: "Scores the accounts you own for relationship health using contact coverage, engagement recency, and open-pipeline signals."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_relationship_health_check", "rar_sha256": "f3f5151c240257dc22ab50ddfe86ef50e7cc6c986d813e88a43fa0f7c53cb57a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_relationship_health_check_agent.py` and embedded as the fenced Python below (sha256 f3f5151c240257dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_relationship_health_check_agent.py` first:

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
    "version": '2.0.1',
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
