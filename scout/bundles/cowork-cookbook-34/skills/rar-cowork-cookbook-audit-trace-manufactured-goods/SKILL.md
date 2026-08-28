---
name: "rar-cowork-cookbook-audit-trace-manufactured-goods"
description: "Audits trace manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_trace_manufactured_goods", "rar_sha256": "83ed49103e80a73a2dafac32342dcee1a2d0bb4fde832cbb97e51052c7f6504f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 83ed49103e80a73a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_trace_manufactured_goods_agent.py` first:

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
    "version": '2.0.1',
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
