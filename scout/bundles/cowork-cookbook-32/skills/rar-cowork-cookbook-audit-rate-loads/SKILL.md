---
name: "rar-cowork-cookbook-audit-rate-loads"
description: "Audits rate loads records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rate_loads", "rar_sha256": "fc0748a2c972aeec8ced694c77ee96a40855c3b8a483d90b401566ae76d0d733", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_rate_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-rate-loads:25f384a7a459a643f5597f9194847c4f0e7775acbc514ec54d932302936f9c4a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_rate_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_rate_loads_agent.py` is
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
