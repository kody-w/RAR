---
name: "rar-cowork-cookbook-audit-merge-cases"
description: "Audits merge cases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_merge_cases", "rar_sha256": "6a7276c2b800be4db8a078e331107f8b238bb7c61fd0e20027ffacdb4aa9ce43", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `audit_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_merge_cases_agent.py` and embedded as the fenced Python below (sha256 6a7276c2b800be4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_merge_cases_agent.py` first:

```bash
python3 audit_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_merge_cases_agent.py   # or on stdin
python3 audit_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_merge_cases',
    "version": '2.0.0',
    "display_name": 'Merge cases Completeness Audit',
    "description": 'Audits merge cases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d16db423886e8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMergeCases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMergeCases'
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
    print(AuditMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
