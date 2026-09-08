---
name: "rar-cowork-cookbook-scheduled-brief-analyze-cash-flow"
description: "Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_cash_flow", "rar_sha256": "d3cd19dd1dd9b17a46256508a142481d88b1771ad3a48e3d4097e6ca5227ccc2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_cash_flow_agent.py` and in the RCI capsule.

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

Analyze cash flow Scheduled Email Brief — Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
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
      "description": "Dynamics 365 F&SCM legal entity to analyze, e.g. USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_cash_flow_agent.py` and embedded as the fenced Python below (sha256 d3cd19dd1dd9b17a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_cash_flow_agent.py` first:

```bash
python3 scheduled_brief_analyze_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_cash_flow_agent.py   # or on stdin
python3 scheduled_brief_analyze_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze cash flow Scheduled Email Brief — Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_cash_flow',
    "version": '3.0.3',
    "display_name": 'Analyze cash flow Scheduled Email Brief',
    "description": 'Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c2657760d64f882',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-cash-flow'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-analyze-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to analyze, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze cash flow stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze cash flow for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze cash flow, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and', 'example_request': 'Draft my daily 7am cash flow brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a recurring daily or weekly cash flow brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeCashFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeCashFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am, daily, or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
