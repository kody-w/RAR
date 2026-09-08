---
name: "rar-cowork-cookbook-scheduled-brief-record-intercompany-transactions"
description: "Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_intercompany_transactions", "rar_sha256": "a0c494a00bafb48e39ae70fb5814fee1f4da03d4dfe1abad3385240483cdd0f4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_intercompany_transactions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_intercompany_transactions_agent.py` and in the RCI capsule.

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

Record intercompany transactions Scheduled Email Brief — Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions
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
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_intercompany_transactions_agent.py` and embedded as the fenced Python below (sha256 a0c494a00bafb48e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_intercompany_transactions_agent.py` first:

```bash
python3 scheduled_brief_record_intercompany_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_intercompany_transactions_agent.py   # or on stdin
python3 scheduled_brief_record_intercompany_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record intercompany transactions Scheduled Email Brief — Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_intercompany_transactions',
    "version": '3.0.3',
    "display_name": 'Record intercompany transactions Scheduled Email Brief',
    "description": 'Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-record-intercompany-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-intercompany-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '388859699d49eae7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-intercompany-transactions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-record-intercompany-transactions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where record intercompany transactions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on record intercompany transactions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads record intercompany transactions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a', 'example_request': 'Draft my 7am intercompany transactions brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly intercompany transactions brief emailed as a draft to the responsible owner, with a Teams-postable summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRecordIntercompanyTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordIntercompanyTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRecordIntercompanyTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
