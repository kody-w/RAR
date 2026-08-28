---
name: "rar-cowork-cookbook-audit-manage-promissory-notes"
description: "Audits manage promissory notes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_promissory_notes", "rar_sha256": "a2045e41dcdb5fa139bb8aa09b98375209e54d537ace503c73d7f3fb46fccd50", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 a2045e41dcdb5fa1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_promissory_notes_agent.py` first:

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
    "version": '2.0.1',
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
