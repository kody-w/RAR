---
name: "rar-cowork-cookbook-journal-entry-validation"
description: "Validates open journal entries against a configurable rule set before posting and produces an exception report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/journal_entry_validation", "rar_sha256": "5710ab62cbd91f45b7ffd21f9543a74514036ce3558bdf2f0fac550c132c0966", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/journal_entry_validation`. The original RAPP
agent is preserved byte-for-byte in `journal_entry_validation_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `journal_entry_validation_agent.py` and embedded as the fenced Python below (sha256 5710ab62cbd91f45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `journal_entry_validation_agent.py` first:

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
    "version": '2.0.1',
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
