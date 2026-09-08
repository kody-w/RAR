---
name: "rar-cowork-cookbook-scheduled-brief-record-intercompany-transactions"
description: "Builds a morning brief on record intercompany transactions from Dynamics 365 ERP for a given legal entity and owner, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_intercompany_transactions", "rar_sha256": "a0c494a00bafb48e39ae70fb5814fee1f4da03d4dfe1abad3385240483cdd0f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
