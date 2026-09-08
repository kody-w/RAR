---
name: "rar-cowork-cookbook-scheduled-brief-manage-opportunity-process"
description: "Builds a morning brief on the manage opportunity process from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft em"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_opportunity_process", "rar_sha256": "0fb39a06bd431dfdcadff3a24e74db069b2b5c7786d0adc99ab686ad0c7b8e7f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
