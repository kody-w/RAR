---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-run-background-jobs"
description: "Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs", "rar_sha256": "6ef2d6ca5f0114bf536204fdec3ff563b9a562f0581ce969ca6827bae3b71dbc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_run_background_jobs_agent.py` and in the RCI capsule.

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

Configure and run background jobs Scheduled Email Brief — Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs
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
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 6ef2d6ca5f0114bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_run_background_jobs_agent.py` first:

```bash
python3 scheduled_brief_configure_and_run_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_run_background_jobs_agent.py   # or on stdin
python3 scheduled_brief_configure_and_run_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and run background jobs Scheduled Email Brief — Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs',
    "version": '3.0.3',
    "display_name": 'Configure and run background jobs Scheduled Email Brief',
    "description": 'Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-configure-and-run-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7a7e37915d9f7bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/configure-and-run-background-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-run-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where configure and run background jobs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on configure and run background jobs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and run background jobs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own', 'example_request': 'Give me the 7am background jobs brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly background-jobs brief for the responsible owner, drafted as an email (not sent) plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConfigureAndRunBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndRunBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConfigureAndRunBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
