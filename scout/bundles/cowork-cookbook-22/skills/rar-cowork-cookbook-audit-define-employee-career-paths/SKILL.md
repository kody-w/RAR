---
name: "rar-cowork-cookbook-audit-define-employee-career-paths"
description: "Audits define employee career paths records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_employee_career_paths", "rar_sha256": "b539a37888dc94a6cdf2730d074584ff8f3e1c238b494e67c7e2f103a91f908c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_employee_career_paths`. The original RAPP
agent is preserved byte-for-byte in `audit_define_employee_career_paths_agent.py` and in the RCI capsule.

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

Define employee career paths Completeness Audit — Audits define employee career paths records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 b539a37888dc94a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_employee_career_paths_agent.py` first:

```bash
python3 audit_define_employee_career_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_employee_career_paths_agent.py   # or on stdin
python3 audit_define_employee_career_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define employee career paths Completeness Audit — Audits define employee career paths records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_employee_career_paths',
    "version": '2.0.0',
    "display_name": 'Define employee career paths Completeness Audit',
    "description": 'Audits define employee career paths records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-employee-career-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-employee-career-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47f10fa6afbac9ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-employee-career-paths'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-employee-career-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineEmployeeCareerPaths(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineEmployeeCareerPaths'
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
    print(AuditDefineEmployeeCareerPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
