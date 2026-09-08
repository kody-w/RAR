---
name: "rar-cowork-cookbook-scheduled-brief-request-time-off"
description: "Builds a morning brief on request time off from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_request_time_off", "rar_sha256": "41f5fc9acfdf4d8b89b89b41820b0fa161b0380211798385acebb02000e78008", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
