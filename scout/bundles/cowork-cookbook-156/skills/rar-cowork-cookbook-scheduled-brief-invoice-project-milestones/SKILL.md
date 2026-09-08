---
name: "rar-cowork-cookbook-scheduled-brief-invoice-project-milestones"
description: "Builds a morning brief on invoice project milestones from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the resp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_invoice_project_milestones", "rar_sha256": "ae6fac914ab8b1027bbb7b42074322bac838e0c7b81a8699dabb3788fc900cd8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
