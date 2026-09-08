---
name: "rar-cowork-cookbook-scheduled-brief-analyze-financial-statements"
description: "Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_financial_statements", "rar_sha256": "3029952188c961221b891c4a8094ed0fb5a9acf6e395c0e8fd541d884eb48b6a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_financial_statements_agent.py` and in the RCI capsule.

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

Analyze financial statements Scheduled Email Brief — Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements
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
      "description": "D365 F&SCM legal entity to analyze, e.g. USMF.",
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
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Optional Teams channel the summary post is formatted for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 3029952188c96122…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_financial_statements_agent.py` first:

```bash
python3 scheduled_brief_analyze_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_financial_statements_agent.py   # or on stdin
python3 scheduled_brief_analyze_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze financial statements Scheduled Email Brief — Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_financial_statements',
    "version": '3.0.3',
    "display_name": 'Analyze financial statements Scheduled Email Brief',
    "description": 'Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams',
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
        "upstream_slug": 'scheduled-brief-analyze-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51f2a5394cb373b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-financial-statements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-analyze-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to analyze, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.', 'teams_channel': 'Optional Teams channel the summary post is formatted for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze financial statements stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze financial statements for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze financial statements, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams', 'example_request': 'Give me the USMF financial statements morning brief for the controller, weekday mornings at 7am.', 'inputs': [{'description': 'D365 F&SCM legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}, {'description': 'Optional Teams channel the summary post is formatted for.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a recurring (daily/weekly) financial statement brief for an owner, drafted as an unsent email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeFinancialStatements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeFinancialStatements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}, 'teams_channel': {'description': 'Optional Teams channel the summary post is formatted for.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
