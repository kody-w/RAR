---
name: "rar-cowork-cookbook-audit-quarantine-manufactured-goods"
description: "Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_quarantine_manufactured_goods", "rar_sha256": "9f369382cefd2471914cc92addd8e4daa20f71ea923d1a1c3c5347408e320b9f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 9f369382cefd2471…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_quarantine_manufactured_goods_agent.py` first:

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
    "version": '2.0.1',
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
