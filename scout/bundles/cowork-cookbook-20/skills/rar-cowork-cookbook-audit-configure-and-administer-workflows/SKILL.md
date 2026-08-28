---
name: "rar-cowork-cookbook-audit-configure-and-administer-workflows"
description: "Audits configure and administer workflows records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_administer_workflows", "rar_sha256": "3cc46c6234cc93be9163868bf096e276815939ea768619fcf2a0d82976351191", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 3cc46c6234cc93be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_administer_workflows_agent.py` first:

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
    "version": '2.0.1',
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
