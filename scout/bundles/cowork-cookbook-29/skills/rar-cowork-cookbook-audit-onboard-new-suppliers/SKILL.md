---
name: "rar-cowork-cookbook-audit-onboard-new-suppliers"
description: "Audits onboard new suppliers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_suppliers", "rar_sha256": "09c344921f1ede7563dcde2ca0e598f2ca81f3a071ff654b2d889f9dacce02f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 09c344921f1ede75…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_suppliers_agent.py` first:

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
    "version": '2.0.0',
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
