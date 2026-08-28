---
name: "rar-cowork-cookbook-audit-rate-loads"
description: "Audits rate loads records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rate_loads", "rar_sha256": "71bdaceb60dfd029cd44e595a7ecfde17c576d043afd4c409643fcb1fb3400c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_rate_loads`. The original RAPP
agent is preserved byte-for-byte in `audit_rate_loads_agent.py` and in the RCI capsule.

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

Rate loads Completeness Audit — Audits rate loads records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rate-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rate_loads_agent.py` and embedded as the fenced Python below (sha256 71bdaceb60dfd029…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rate_loads_agent.py` first:

```bash
python3 audit_rate_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_rate_loads_agent.py   # or on stdin
python3 audit_rate_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rate loads Completeness Audit — Audits rate loads records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rate-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_rate_loads',
    "version": '2.0.1',
    "display_name": 'Rate loads Completeness Audit',
    "description": 'Audits rate loads records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-rate-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-rate-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76e51f398a9bc0af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/rate-loads'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-rate-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditRateLoads(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRateLoads'
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
    print(AuditRateLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
