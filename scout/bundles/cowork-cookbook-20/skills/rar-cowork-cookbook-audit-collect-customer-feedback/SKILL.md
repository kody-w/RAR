---
name: "rar-cowork-cookbook-audit-collect-customer-feedback"
description: "Audits collect customer feedback records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_collect_customer_feedback", "rar_sha256": "d983142857aa1b1f99f2b4ee56dc7013db5397f3d0e3ba761ec66e8a43896f4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 d983142857aa1b1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_collect_customer_feedback_agent.py` first:

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
    "version": '2.0.0',
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
