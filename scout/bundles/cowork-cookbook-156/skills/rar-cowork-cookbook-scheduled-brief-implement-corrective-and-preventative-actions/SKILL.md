---
name: "rar-cowork-cookbook-scheduled-brief-implement-corrective-and-preventative-actions"
description: "Builds a morning brief on implement corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions", "rar_sha256": "2f817850480e8e57153c47f0eac38d75479e0bc680d84c69099ff7b7f51e16c1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
