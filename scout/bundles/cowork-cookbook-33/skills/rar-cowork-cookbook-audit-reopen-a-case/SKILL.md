---
name: "rar-cowork-cookbook-audit-reopen-a-case"
description: "Audits reopen a case records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_reopen_a_case", "rar_sha256": "756bc63a1725668ba4cc013ff397203e6d007ec0282f126eda3c6bc8958894af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_reopen_a_case`. The original RAPP
agent is preserved byte-for-byte in `audit_reopen_a_case_agent.py` and in the RCI capsule.

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

Reopen a case Completeness Audit — Audits reopen a case records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 756bc63a1725668b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_reopen_a_case_agent.py` first:

```bash
python3 audit_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_reopen_a_case_agent.py   # or on stdin
python3 audit_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Completeness Audit — Audits reopen a case records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_reopen_a_case',
    "version": '2.0.1',
    "display_name": 'Reopen a case Completeness Audit',
    "description": 'Audits reopen a case records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '079bf1a90c82bd86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditReopenACase(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReopenACase'
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
    print(AuditReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
