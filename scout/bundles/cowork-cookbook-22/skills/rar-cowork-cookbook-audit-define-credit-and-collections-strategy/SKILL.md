---
name: "rar-cowork-cookbook-audit-define-credit-and-collections-strategy"
description: "Audits define credit and collections strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_credit_and_collections_strategy", "rar_sha256": "9eafc1113aa4cf3cd77960dbbd65b3c05a8cb0de17b653d1031fb01fdef9d9e3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
