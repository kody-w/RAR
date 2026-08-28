---
name: "rar-cowork-cookbook-audit-quarantine-manufactured-goods"
description: "Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_quarantine_manufactured_goods", "rar_sha256": "607b9c22621b8d617979ce3de3c73c4dc62e0a55a22f27e1591b1e28b16d4c7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_quarantine_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_quarantine_manufactured_goods_agent.py` and in the RCI capsule.

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

Quarantine manufactured goods Completeness Audit — Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 607b9c22621b8d61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_quarantine_manufactured_goods_agent.py` first:

```bash
python3 audit_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_quarantine_manufactured_goods_agent.py   # or on stdin
python3 audit_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Completeness Audit — Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_quarantine_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Quarantine manufactured goods Completeness Audit',
    "description": 'Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33dc2e802681d6e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditQuarantineManufacturedGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditQuarantineManufacturedGoods'
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
    print(AuditQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
