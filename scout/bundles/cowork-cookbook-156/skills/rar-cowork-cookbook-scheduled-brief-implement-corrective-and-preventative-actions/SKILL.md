---
name: "rar-cowork-cookbook-scheduled-brief-implement-corrective-and-preventative-actions"
description: "Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions", "rar_sha256": "2f817850480e8e57153c47f0eac38d75479e0bc680d84c69099ff7b7f51e16c1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Implement corrective and preventative actions Scheduled Email Brief — Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions
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
      "description": "Dynamics 365 legal entity to query; the recipe uses USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 2f817850480e8e57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` first:

```bash
python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py   # or on stdin
python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement corrective and preventative actions Scheduled Email Brief — Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions',
    "version": '3.0.3',
    "display_name": 'Implement corrective and preventative actions Scheduled Email Brief',
    "description": 'Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-implement-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '610e58195b619f61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/implement-corrective-and-preventative-actions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-implement-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where implement corrective and preventative actions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on implement corrective and preventative actions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement corrective and preventative actions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts', 'example_request': 'Give me the 7am CAPA morning brief from USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly CAPA morning brief from D365 ERP, drafted as an unsent email and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefImplementCorrectiveAndPreventativeActions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefImplementCorrectiveAndPreventativeActions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefImplementCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
