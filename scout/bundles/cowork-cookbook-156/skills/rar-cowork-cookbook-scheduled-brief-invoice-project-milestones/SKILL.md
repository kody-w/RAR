---
name: "rar-cowork-cookbook-scheduled-brief-invoice-project-milestones"
description: "Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_invoice_project_milestones", "rar_sha256": "ae6fac914ab8b1027bbb7b42074322bac838e0c7b81a8699dabb3788fc900cd8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_invoice_project_milestones`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_invoice_project_milestones_agent.py` and in the RCI capsule.

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

Invoice project milestones Scheduled Email Brief — Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones
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
      "description": "The responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 ae6fac914ab8b102…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_invoice_project_milestones_agent.py` first:

```bash
python3 scheduled_brief_invoice_project_milestones_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_invoice_project_milestones_agent.py   # or on stdin
python3 scheduled_brief_invoice_project_milestones_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project milestones Scheduled Email Brief — Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_invoice_project_milestones',
    "version": '3.0.3',
    "display_name": 'Invoice project milestones Scheduled Email Brief',
    "description": 'Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-invoice-project-milestones',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-invoice-project-milestones',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e376afa7ed8c594',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-milestones'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-invoice-project-milestones', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'The responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where invoice project milestones stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on invoice project milestones for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads invoice project milestones, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp', 'example_request': 'Give me the morning brief on invoice project milestones from USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly invoice project milestone brief for the responsible owner, as an email draft and Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefInvoiceProjectMilestones(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefInvoiceProjectMilestones'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefInvoiceProjectMilestones().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
