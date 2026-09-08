---
name: "rar-cowork-cookbook-scheduled-brief-clean-up-and-archive-background-jobs"
description: "Builds a morning brief on clean up and archive background jobs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus a saved email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs", "rar_sha256": "504db7dd1b3ebed984c714c3769c85ac6ee9c81dd96feaa025c215ebe6d1b372", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
