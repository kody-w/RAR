---
name: "rar-cowork-cookbook-scheduled-brief-analyze-and-reconcile-compensation-and-benefits"
description: "Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "1f1dd2a478899118c42d114ed4376966cbe3f322e5f09cd3de2dfbadc71e5f46", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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

Analyze and reconcile compensation and benefits Scheduled Email Brief — Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner the brief is addressed to and the email is drafted for.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 1f1dd2a478899118…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Scheduled Email Brief — Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits',
    "version": '3.0.3',
    "display_name": 'Analyze and reconcile compensation and benefits Scheduled Email Brief',
    "description": 'Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd95266fcbe748fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner the brief is addressed to and the email is drafted for.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze and reconcile compensation and benefits stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze and reconcile compensation and benefits for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze and reconcile compensation and benefits, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te', 'example_request': 'Give me the comp and benefits morning brief for USMF and draft it as an email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner the brief is addressed to and the email is drafted for.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly compensation and benefits reconciliation brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner the brief is addressed to and the email is drafted for.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
