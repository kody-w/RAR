---
name: "rar-cowork-cookbook-scheduled-brief-analyze-cash-flow"
description: "Builds a cash flow morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (saved, not sent) and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_cash_flow", "rar_sha256": "d3cd19dd1dd9b17a46256508a142481d88b1771ad3a48e3d4097e6ca5227ccc2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
