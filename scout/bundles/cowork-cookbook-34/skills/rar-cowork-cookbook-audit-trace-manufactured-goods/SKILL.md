---
name: "rar-cowork-cookbook-audit-trace-manufactured-goods"
description: "Audits trace manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_trace_manufactured_goods", "rar_sha256": "92dc48e4fe3bae684b2051e382520d06d0e102b881387496c4eff27b9112eb02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_trace_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_trace_manufactured_goods_agent.py` and in the RCI capsule.

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

Trace manufactured goods Completeness Audit — Audits trace manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-trace-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 92dc48e4fe3bae68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_trace_manufactured_goods_agent.py` first:

```bash
python3 audit_trace_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_trace_manufactured_goods_agent.py   # or on stdin
python3 audit_trace_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Trace manufactured goods Completeness Audit — Audits trace manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-trace-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_trace_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Trace manufactured goods Completeness Audit',
    "description": 'Audits trace manufactured goods records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-trace-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-trace-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95dd29c4d2ce3600',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/trace-manufactured-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-trace-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditTraceManufacturedGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTraceManufacturedGoods'
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
    print(AuditTraceManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
