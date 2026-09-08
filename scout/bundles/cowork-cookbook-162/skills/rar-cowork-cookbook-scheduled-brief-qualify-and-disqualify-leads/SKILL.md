---
name: "rar-cowork-cookbook-scheduled-brief-qualify-and-disqualify-leads"
description: "Builds a morning brief on qualify/disqualify leads from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_qualify_and_disqualify_leads", "rar_sha256": "1e02ce1dcbc45173f28bd6905250fbecb86cf13e09ebe00c576eae8706ee0daf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
