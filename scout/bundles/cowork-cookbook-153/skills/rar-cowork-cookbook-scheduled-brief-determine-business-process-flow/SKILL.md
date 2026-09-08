---
name: "rar-cowork-cookbook-scheduled-brief-determine-business-process-flow"
description: "Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_determine_business_process_flow", "rar_sha256": "77c35d8f1d97a60631bf5562be19f3b5e4030ade1c69f9c09d705a3bf16b9647", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_determine_business_process_flow_agent.py` and in the RCI capsule.

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

Determine business process flow Scheduled Email Brief — Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 77c35d8f1d97a606…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_determine_business_process_flow_agent.py` first:

```bash
python3 scheduled_brief_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_determine_business_process_flow_agent.py   # or on stdin
python3 scheduled_brief_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Scheduled Email Brief — Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_determine_business_process_flow',
    "version": '3.0.3',
    "display_name": 'Determine business process flow Scheduled Email Brief',
    "description": 'Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t',
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
        "upstream_slug": 'scheduled-brief-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '108ce5b86e7aa429',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where determine business process flow stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on determine business process flow for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads determine business process flow, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t', 'example_request': 'Draft my 7am weekday business process flow brief for USMF and send it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a recurring (daily/weekday 7am or weekly) business process flow brief emailed as a draft to the responsible owner and posted to Teams.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDetermineBusinessProcessFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDetermineBusinessProcessFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
