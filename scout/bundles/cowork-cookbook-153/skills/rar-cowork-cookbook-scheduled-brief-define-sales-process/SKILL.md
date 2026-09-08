---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-process"
description: "Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_process", "rar_sha256": "5d18b17f96246aede4470cbc67a1673d0291afe9ab3b45673b947e6b1df36b79", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_process`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_process_agent.py` and in the RCI capsule.

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

Define sales process Scheduled Email Brief — Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for running the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_process_agent.py` and embedded as the fenced Python below (sha256 5d18b17f96246aed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_process_agent.py` first:

```bash
python3 scheduled_brief_define_sales_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_process_agent.py   # or on stdin
python3 scheduled_brief_define_sales_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales process Scheduled Email Brief — Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_process',
    "version": '3.0.3',
    "display_name": 'Define sales process Scheduled Email Brief',
    "description": 'Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to',
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
        "upstream_slug": 'scheduled-brief-define-sales-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39616f89f68c9567',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-process'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-process', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'Optional cadence for running the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define sales process stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define sales process for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define sales process, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to', 'example_request': 'Give me the 7am define sales process morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'Optional cadence for running the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly define-sales-process brief for the responsible owner, drafted as an email (not sent) plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineSalesProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for running the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineSalesProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
