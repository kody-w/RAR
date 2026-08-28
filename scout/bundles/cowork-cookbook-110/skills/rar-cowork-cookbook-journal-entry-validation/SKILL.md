---
name: "rar-cowork-cookbook-journal-entry-validation"
description: "Validates open journal entries against a configurable rule set before posting and produces an exception report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/journal_entry_validation", "rar_sha256": "6b9711a1812f44c713d1df7c028eee0c12b79b9d333a924ea7ced6d57c600794", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
