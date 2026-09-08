---
name: "rar-cowork-cookbook-scheduled-brief-process-supplier-rebates-and-incentives"
description: "Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives", "rar_sha256": "3b60ee6de95071c36455aba462ad768eec833bf508526686647480cc20d8b29f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Process supplier rebates and incentives Scheduled Email Brief — Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 3b60ee6de95071c3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` first:

```bash
python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py   # or on stdin
python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier rebates and incentives Scheduled Email Brief — Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives',
    "version": '3.0.3',
    "display_name": 'Process supplier rebates and incentives Scheduled Email Brief',
    "description": 'Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-process-supplier-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2837bcb73441fa45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-rebates-and-incentives'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-process-supplier-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where process supplier rebates and incentives stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on process supplier rebates and incentives for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process supplier rebates and incentives, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea', 'example_request': 'Give me the supplier rebates morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly supplier rebate/incentive brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefProcessSupplierRebatesAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProcessSupplierRebatesAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefProcessSupplierRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
