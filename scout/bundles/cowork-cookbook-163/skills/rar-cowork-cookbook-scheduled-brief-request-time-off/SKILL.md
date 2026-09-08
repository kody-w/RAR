---
name: "rar-cowork-cookbook-scheduled-brief-request-time-off"
description: "Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_request_time_off", "rar_sha256": "41f5fc9acfdf4d8b89b89b41820b0fa161b0380211798385acebb02000e78008", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_request_time_off`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_request_time_off_agent.py` and in the RCI capsule.

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

Request time off Scheduled Email Brief — Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-request-time-off
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_request_time_off_agent.py` and embedded as the fenced Python below (sha256 41f5fc9acfdf4d8b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_request_time_off_agent.py` first:

```bash
python3 scheduled_brief_request_time_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_request_time_off_agent.py   # or on stdin
python3 scheduled_brief_request_time_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request time off Scheduled Email Brief — Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-request-time-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_request_time_off',
    "version": '3.0.3',
    "display_name": 'Request time off Scheduled Email Brief',
    "description": 'Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read',
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
        "upstream_slug": 'scheduled-brief-request-time-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-request-time-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7df1ea2edaa9d7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-time-off'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-request-time-off', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where request time off stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on request time off for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads request time off, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read', 'example_request': 'Draft my morning brief on request time off from D365 USMF and save it to drafts.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a time-off owner wants a daily or weekly morning brief on request time off drafted as an email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRequestTimeOff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRequestTimeOff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRequestTimeOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
