---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-process"
description: "Builds a morning brief on the define sales process from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_process", "rar_sha256": "5d18b17f96246aede4470cbc67a1673d0291afe9ab3b45673b947e6b1df36b79", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
