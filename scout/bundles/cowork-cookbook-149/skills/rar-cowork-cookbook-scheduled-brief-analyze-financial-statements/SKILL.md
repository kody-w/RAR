---
name: "rar-cowork-cookbook-scheduled-brief-analyze-financial-statements"
description: "Builds a financial-statement morning brief from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_financial_statements", "rar_sha256": "3029952188c961221b891c4a8094ed0fb5a9acf6e395c0e8fd541d884eb48b6a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
