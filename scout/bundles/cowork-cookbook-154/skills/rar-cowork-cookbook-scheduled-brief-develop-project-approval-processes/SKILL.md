---
name: "rar-cowork-cookbook-scheduled-brief-develop-project-approval-processes"
description: "Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_project_approval_processes", "rar_sha256": "faeae0d2474c96026692ab9b2db2898166c9157a49f287f0843e28b96bd24138", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_project_approval_processes`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_project_approval_processes_agent.py` and in the RCI capsule.

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

Develop project approval processes Scheduled Email Brief — Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 faeae0d2474c9602…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_project_approval_processes_agent.py` first:

```bash
python3 scheduled_brief_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_project_approval_processes_agent.py   # or on stdin
python3 scheduled_brief_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Scheduled Email Brief — Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_project_approval_processes',
    "version": '3.0.3',
    "display_name": 'Develop project approval processes Scheduled Email Brief',
    "description": 'Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own',
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
        "upstream_slug": 'scheduled-brief-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dca7b17013cf4b64',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop project approval processes stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop project approval processes for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop project approval processes, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own', 'example_request': 'Build my 7am weekday approval-process brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly D365 approval-process brief with an unsent email draft and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopProjectApprovalProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProjectApprovalProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
