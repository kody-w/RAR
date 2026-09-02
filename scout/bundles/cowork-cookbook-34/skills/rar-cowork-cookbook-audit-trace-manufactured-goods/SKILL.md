---
name: "rar-cowork-cookbook-audit-trace-manufactured-goods"
description: "Audits trace manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_trace_manufactured_goods", "rar_sha256": "92dc48e4fe3bae684b2051e382520d06d0e102b881387496c4eff27b9112eb02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_trace_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-trace-manufactured-goods:41ca4b91b7ab7be5412836a31d2fc4321e5b8c0d6e5ee2484eed4cefe966553f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_trace_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_trace_manufactured_goods_agent.py` is
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
