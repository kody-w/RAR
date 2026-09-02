---
name: "rar-cowork-cookbook-journal-entry-validation"
description: "Validates open journal entries against a configurable rule set before posting and produces an exception report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/journal_entry_validation", "rar_sha256": "6b9711a1812f44c713d1df7c028eee0c12b79b9d333a924ea7ced6d57c600794", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "journal_entry_validation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/journal-entry-validation:65242a79d8a2815bf3040741c281745531a7cab29183f8e4d2de5d9b3c7ac097", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/journal_entry_validation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `journal_entry_validation_agent.py` is
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

Journal Entry Pre-Posting Validation — Validates open journal entries against a configurable rule set before posting and produces an exception report.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/journal-entry-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `journal_entry_validation_agent.py` and embedded as the fenced Python below (sha256 6b9711a1812f44c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `journal_entry_validation_agent.py` first:

```bash
python3 journal_entry_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 journal_entry_validation_agent.py   # or on stdin
python3 journal_entry_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Journal Entry Pre-Posting Validation — Validates open journal entries against a configurable rule set before posting and produces an exception report.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/journal-entry-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/journal_entry_validation',
    "version": '2.0.0',
    "display_name": 'Journal Entry Pre-Posting Validation',
    "description": 'Validates open journal entries against a configurable rule set before posting and produces an exception report.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'journal-entry-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/journal-entry-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a2cf8d48f92e7c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/journal-entry-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class JournalEntryValidation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'JournalEntryValidation'
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
    print(JournalEntryValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
