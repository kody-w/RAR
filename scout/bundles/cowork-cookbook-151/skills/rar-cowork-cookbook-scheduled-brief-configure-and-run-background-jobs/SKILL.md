---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-run-background-jobs"
description: "Builds a morning brief on background job configuration and runs from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions, then saves an email draft to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs", "rar_sha256": "6ef2d6ca5f0114bf536204fdec3ff563b9a562f0581ce969ca6827bae3b71dbc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
