---
name: "rar-cowork-cookbook-scheduled-brief-capture-details-about-a-case"
description: "Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_capture_details_about_a_case", "rar_sha256": "9ffdfa158c3cbd602c6f2af28bdaa6b44b1c591240a4c96ba6d58e08ce985592", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

Capture details about a case Scheduled Email Brief — Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Optional Teams channel the Communications-ready summary is written for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 9ffdfa158c3cbd60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_capture_details_about_a_case_agent.py` first:

```bash
python3 scheduled_brief_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_capture_details_about_a_case_agent.py   # or on stdin
python3 scheduled_brief_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Scheduled Email Brief — Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_capture_details_about_a_case',
    "version": '3.0.3',
    "display_name": 'Capture details about a case Scheduled Email Brief',
    "description": 'Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba7dffc7a700a91c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When to run, e.g. weekday mornings at 7am.', 'teams_channel': 'Optional Teams channel the Communications-ready summary is written for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where capture details about a case stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on capture details about a case for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads capture details about a case, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team', 'example_request': 'Give me the 7am morning brief on case capture details in USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}, {'description': 'Optional Teams channel the Communications-ready summary is written for.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly case-capture brief for the responsible owner from D365 F&SCM, with a drafted (unsent) email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCaptureDetailsAboutACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCaptureDetailsAboutACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}, 'teams_channel': {'description': 'Optional Teams channel the Communications-ready summary is written for.', 'type': 'string'}},
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
    print(ScheduledBriefCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
