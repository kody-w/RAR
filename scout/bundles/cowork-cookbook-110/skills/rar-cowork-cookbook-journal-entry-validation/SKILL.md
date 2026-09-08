---
name: "rar-cowork-cookbook-journal-entry-validation"
description: "Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/journal_entry_validation", "rar_sha256": "1fad25199ab0cac70a4bc4bbfc749d3f76c0e02487ae336e730cb21b99d6d71e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

Journal Entry Pre-Posting Validation — Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_file_name": {
      "description": "Name of the Excel workbook, defaulting to Journal-exceptions-<YYYY-MM-DD>.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "The accounting period to scan; defaults to the current period.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `journal_entry_validation_agent.py` and embedded as the fenced Python below (sha256 1fad25199ab0cac7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `journal_entry_validation_agent.py` first:

```bash
python3 journal_entry_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 journal_entry_validation_agent.py   # or on stdin
python3 journal_entry_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Journal Entry Pre-Posting Validation — Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Journal Entry Pre-Posting Validation',
    "description": 'Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6980b3ac5d4a9f06',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the General ledger user role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One workbook with one row per failing journal line and the rule that failed.'], 'confidence': 1.0, 'deliverable': 'One workbook with one row per failing journal line and the rule that failed.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'output_file_name': 'Name of the Excel workbook, defaulting to Journal-exceptions-<YYYY-MM-DD>.xlsx.', 'period': 'The accounting period to scan; defaults to the current period.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Catches posting errors before they hit the ledger, eliminating the reverse-and-repost cycles that delay close.', 'expected_output': 'One workbook with one row per failing journal line and the rule that failed.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the General ledger user role', 'Cowork D365 ERP plugin enabled'], 'prompt': "List all open (unposted) general journal entries in the current period. For each line, validate: account is active, dimensions are valid for the account, debits = credits at the header level, and the description is non-empty. Produce an Excel workbook 'Journal-exceptions-<YYYY-MM-DD>.xlsx' with one row per failing line, indicating which rule was violated. Do not post anything.", 'steps': ['Open Cowork and paste the prompt.', 'Approve the read-only data access.', 'Review the exceptions sheet; resolve in D365 before posting.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF (scope: December 2017). Cowork found 3 open general-journal headers (00619, 00471, 00459) and ran all four validation rules (account active, dimensions valid, debits=credits, description non-empty). Produced 'Journal-exceptions-2026-05-23.xlsx' with 1 failing line: batch 00459 line 1 (account 600150-001-008-022, debit 1200) - failed the 'dimensions valid' rule because the offset 200190-001--022 has an empty middle dimension segment. Other three rules PASS-ed. Nothing was posted.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Reads open journals and runs validation rules. Output is a workbook of exceptions for the GL team to triage.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is', 'example_request': 'Validate all open journal entries for this period and give me an exceptions workbook before I post.', 'inputs': [{'description': 'The accounting period to scan; defaults to the current period.', 'name': 'period'}, {'description': 'Name of the Excel workbook, defaulting to Journal-exceptions-<YYYY-MM-DD>.xlsx.', 'name': 'output_file_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call before posting a general journal in D365 F&SCM when you want a read-only list of journal lines that would fail validation.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and paste the prompt.', 'Approve the read-only data access.', 'Review the exceptions sheet; resolve in D365 before posting.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class JournalEntryValidation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'JournalEntryValidation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Excel workbook, defaulting to Journal-exceptions-<YYYY-MM-DD>.xlsx.', 'type': 'string'}, 'period': {'description': 'The accounting period to scan; defaults to the current period.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
