---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-quotations"
description: "Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_quotations", "rar_sha256": "73ab3f3507ca5bef599625eb4d464f42120f8b6f4f78ed2f7c5a51ff554e82dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Scheduled Email Brief — Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 73ab3f3507ca5bef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_quotations_agent.py` first:

```bash
python3 scheduled_brief_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_quotations_agent.py   # or on stdin
python3 scheduled_brief_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Scheduled Email Brief — Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_quotations',
    "version": '3.0.3',
    "display_name": 'Define sales quotations Scheduled Email Brief',
    "description": 'Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow',
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
        "upstream_slug": 'scheduled-brief-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '573ce4566cc5975c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define sales quotations stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define sales quotations for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define sales quotations, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow', 'example_request': 'Send me the define sales quotations morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales quotation owner wants a daily or weekly (weekday 7am) brief on define sales quotations with a drafted email and Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineSalesQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
