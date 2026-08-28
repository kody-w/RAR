---
name: "rar-cowork-cookbook-audit-configure-and-administer-workflows"
description: "Audits configure and administer workflows records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_administer_workflows", "rar_sha256": "5674c25965063847b4bb3e38a982980b6447007c54b1237a8d32b3a3f5c44f26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_administer_workflows`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_administer_workflows_agent.py` and in the RCI capsule.

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
