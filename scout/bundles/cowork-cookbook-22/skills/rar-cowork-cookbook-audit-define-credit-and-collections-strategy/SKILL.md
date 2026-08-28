---
name: "rar-cowork-cookbook-audit-define-credit-and-collections-strategy"
description: "Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_credit_and_collections_strategy", "rar_sha256": "881e5ce250b8c5729131a5b4628bc61521fe1037c5c75970d2713679fe0c3044", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_credit_and_collections_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_define_credit_and_collections_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 881e5ce250b8c572…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_credit_and_collections_strategy_agent.py` first:

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
    "version": '2.0.1',
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
