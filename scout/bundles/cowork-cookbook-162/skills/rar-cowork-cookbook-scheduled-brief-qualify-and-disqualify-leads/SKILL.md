---
name: "rar-cowork-cookbook-scheduled-brief-qualify-and-disqualify-leads"
description: "Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads", "rar_sha256": "1e02ce1dcbc45173f28bd6905250fbecb86cf13e09ebe00c576eae8706ee0daf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_qualify_and_disqualify_leads_agent.py` and in the RCI capsule.

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

Qualify and disqualify leads Scheduled Email Brief — Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 1e02ce1dcbc45173…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 scheduled_brief_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 scheduled_brief_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Scheduled Email Brief — Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads',
    "version": '3.0.3',
    "display_name": 'Qualify and disqualify leads Scheduled Email Brief',
    "description": 'Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu',
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
        "upstream_slug": 'scheduled-brief-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf537300df9aa2d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where qualify and disqualify leads stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on qualify and disqualify leads for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads qualify and disqualify leads, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu', 'example_request': 'Send me the qualify/disqualify leads morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly lead qualification brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefQualifyAndDisqualifyLeads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefQualifyAndDisqualifyLeads'
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
    print(ScheduledBriefQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
