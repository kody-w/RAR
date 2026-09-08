---
name: "rar-cowork-cookbook-scheduled-brief-manage-opportunity-process"
description: "Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_opportunity_process", "rar_sha256": "0fb39a06bd431dfdcadff3a24e74db069b2b5c7786d0adc99ab686ad0c7b8e7f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_opportunity_process`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_opportunity_process_agent.py` and in the RCI capsule.

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

Manage opportunity process Scheduled Email Brief — Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
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
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 0fb39a06bd431dfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_opportunity_process_agent.py` first:

```bash
python3 scheduled_brief_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_opportunity_process_agent.py   # or on stdin
python3 scheduled_brief_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Scheduled Email Brief — Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_opportunity_process',
    "version": '3.0.3',
    "display_name": 'Manage opportunity process Scheduled Email Brief',
    "description": 'Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f4b57ba36ac0e410',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage opportunity process stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage opportunity process for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage opportunity process, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em', 'example_request': 'Give me the 7am manage opportunity process brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly manage-opportunity-process brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageOpportunityProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOpportunityProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
