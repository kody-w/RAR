---
name: "rar-cowork-cookbook-audit-configure-and-administer-workflows"
description: "Audits configure and administer workflows records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_administer_workflows", "rar_sha256": "5674c25965063847b4bb3e38a982980b6447007c54b1237a8d32b3a3f5c44f26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_configure_and_administer_workflows_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-configure-and-administer-workflows:d506965fcc88d3cebd7322bfedfb740ec0cd2bc12281aef1d974cbef89b6a8c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_configure_and_administer_workflows`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_configure_and_administer_workflows_agent.py` is
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

Configure and administer workflows Completeness Audit — Audits configure and administer workflows records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 5674c25965063847…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_administer_workflows_agent.py` first:

```bash
python3 audit_configure_and_administer_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_administer_workflows_agent.py   # or on stdin
python3 audit_configure_and_administer_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and administer workflows Completeness Audit — Audits configure and administer workflows records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_administer_workflows',
    "version": '2.0.0',
    "display_name": 'Configure and administer workflows Completeness Audit',
    "description": 'Audits configure and administer workflows records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-configure-and-administer-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f146a057f2cc4ce3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-administer-workflows'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-administer-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndAdministerWorkflows(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndAdministerWorkflows'
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
    print(AuditConfigureAndAdministerWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
