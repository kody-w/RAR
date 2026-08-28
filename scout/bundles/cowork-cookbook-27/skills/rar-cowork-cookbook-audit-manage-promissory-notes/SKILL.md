---
name: "rar-cowork-cookbook-audit-manage-promissory-notes"
description: "Audits manage promissory notes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_promissory_notes", "rar_sha256": "6243ac30942a77bb6541aa3a99b11e6a906a991cb06dbd57b67c511728519b77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_promissory_notes`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_promissory_notes_agent.py` and in the RCI capsule.

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
