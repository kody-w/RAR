---
name: "rar-cowork-cookbook-scheduled-brief-analyze-and-reconcile-compensation-and-benefits"
description: "Builds a compensation and benefits morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "1f1dd2a478899118c42d114ed4376966cbe3f322e5f09cd3de2dfbadc71e5f46", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
