---
name: "rar-cowork-cookbook-journal-entry-validation"
description: "Checks open, unposted general journal entries in the current period against four rules (active account, valid dimensions, balanced debits/credits, non-empty description) and returns an Excel exception report; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/journal_entry_validation", "rar_sha256": "1fad25199ab0cac70a4bc4bbfc749d3f76c0e02487ae336e730cb21b99d6d71e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
