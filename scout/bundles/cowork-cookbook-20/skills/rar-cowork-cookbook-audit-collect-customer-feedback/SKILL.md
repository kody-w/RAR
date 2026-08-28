---
name: "rar-cowork-cookbook-audit-collect-customer-feedback"
description: "Audits collect customer feedback records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_collect_customer_feedback", "rar_sha256": "b696492cece7b91a2865dfbb40a48339ea876df1b3144ab1beb741e794e390fd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `audit_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Completeness Audit — Audits collect customer feedback records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 b696492cece7b91a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_collect_customer_feedback_agent.py` first:

```bash
python3 audit_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_collect_customer_feedback_agent.py   # or on stdin
python3 audit_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Completeness Audit — Audits collect customer feedback records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_collect_customer_feedback',
    "version": '2.0.1',
    "display_name": 'Collect customer feedback Completeness Audit',
    "description": 'Audits collect customer feedback records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ada539dbc4ed7ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditCollectCustomerFeedback(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCollectCustomerFeedback'
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
    print(AuditCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
