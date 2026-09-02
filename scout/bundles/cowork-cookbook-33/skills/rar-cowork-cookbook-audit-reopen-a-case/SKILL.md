---
name: "rar-cowork-cookbook-audit-reopen-a-case"
description: "Audits reopen a case records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_reopen_a_case", "rar_sha256": "2d16379b90c30d95b59ef31b0dc5e41db0dd328946f686be7e8e6a7d25623e94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_reopen_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-reopen-a-case:a816bd93468e8a27ac66691fc05a99ff6356d7b90e96f62c8ae2e1de58720a3b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_reopen_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_reopen_a_case_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 2d16379b90c30d95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_reopen_a_case_agent.py` first:

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
    "version": '2.0.0',
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
