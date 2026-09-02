---
name: "rar-cowork-cookbook-audit-manage-promissory-notes"
description: "Audits manage promissory notes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_promissory_notes", "rar_sha256": "6243ac30942a77bb6541aa3a99b11e6a906a991cb06dbd57b67c511728519b77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_promissory_notes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-promissory-notes:dad02b0edc7494693e9a8d6971faebedf1fe7cd0351724c85c2ef8ef15f7adf1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_promissory_notes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_promissory_notes_agent.py` is
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

Manage promissory notes Completeness Audit — Audits manage promissory notes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-promissory-notes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 6243ac30942a77bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_promissory_notes_agent.py` first:

```bash
python3 audit_manage_promissory_notes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_promissory_notes_agent.py   # or on stdin
python3 audit_manage_promissory_notes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage promissory notes Completeness Audit — Audits manage promissory notes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-promissory-notes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_promissory_notes',
    "version": '2.0.0',
    "display_name": 'Manage promissory notes Completeness Audit',
    "description": 'Audits manage promissory notes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-promissory-notes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-promissory-notes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c022a590a14a9a7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/manage-promissory-notes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-manage-promissory-notes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManagePromissoryNotes(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManagePromissoryNotes'
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
    print(AuditManagePromissoryNotes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
