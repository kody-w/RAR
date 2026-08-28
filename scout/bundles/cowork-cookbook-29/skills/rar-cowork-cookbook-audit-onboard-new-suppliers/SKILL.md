---
name: "rar-cowork-cookbook-audit-onboard-new-suppliers"
description: "Audits onboard new suppliers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_suppliers", "rar_sha256": "f85abb310b17b4ea78c78f9eba75585eb14da73cacbb927f86fbb5952b8398de", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_suppliers`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_suppliers_agent.py` and in the RCI capsule.

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

Onboard new suppliers Completeness Audit — Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 f85abb310b17b4ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_suppliers_agent.py` first:

```bash
python3 audit_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_suppliers_agent.py   # or on stdin
python3 audit_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Completeness Audit — Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_suppliers',
    "version": '2.0.1',
    "display_name": 'Onboard new suppliers Completeness Audit',
    "description": 'Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5847536a7e1154d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditOnboardNewSuppliers(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewSuppliers'
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
    print(AuditOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
