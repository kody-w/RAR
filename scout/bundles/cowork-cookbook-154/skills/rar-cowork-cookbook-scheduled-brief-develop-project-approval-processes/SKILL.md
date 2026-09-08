---
name: "rar-cowork-cookbook-scheduled-brief-develop-project-approval-processes"
description: "Builds a morning brief on develop project approval processes from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_project_approval_processes", "rar_sha256": "faeae0d2474c96026692ab9b2db2898166c9157a49f287f0843e28b96bd24138", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
