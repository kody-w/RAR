---
name: "rar-cowork-cookbook-audit-rate-loads"
description: "Audits rate loads records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rate_loads", "rar_sha256": "fc0748a2c972aeec8ced694c77ee96a40855c3b8a483d90b401566ae76d0d733", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rate_loads_agent.py` and embedded as the fenced Python below (sha256 fc0748a2c972aeec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rate_loads_agent.py` first:

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
    "version": '2.0.0',
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
