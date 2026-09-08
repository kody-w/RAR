---
name: "rar-cowork-cookbook-scheduled-brief-determine-business-process-flow"
description: "Builds a morning brief on determine business process flow from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_determine_business_process_flow", "rar_sha256": "77c35d8f1d97a60631bf5562be19f3b5e4030ade1c69f9c09d705a3bf16b9647", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
