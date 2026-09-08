---
name: "rar-cowork-cookbook-scheduled-brief-clean-up-and-archive-background-jobs"
description: "Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs", "rar_sha256": "504db7dd1b3ebed984c714c3769c85ac6ee9c81dd96feaa025c215ebe6d1b372", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and in the RCI capsule.

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

Clean up and archive background jobs Scheduled Email Brief — Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
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
      "description": "Dynamics 365 legal entity to run against (recipe default: USMF).",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 504db7dd1b3ebed9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` first:

```bash
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py   # or on stdin
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and archive background jobs Scheduled Email Brief — Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs',
    "version": '3.0.3',
    "display_name": 'Clean up and archive background jobs Scheduled Email Brief',
    "description": 'Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email',
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
        "upstream_slug": 'scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd6a631b5973c30db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/clean-up-and-archive-background-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-clean-up-and-archive-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where clean up and archive background jobs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on clean up and archive background jobs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads clean up and archive background jobs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email', 'example_request': 'Give me the 7am morning brief on background job cleanup in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly scheduled brief on D365 background job cleanup/archiving for the responsible owner, with a draft email and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCleanUpAndArchiveBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCleanUpAndArchiveBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefCleanUpAndArchiveBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
