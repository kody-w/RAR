---
name: "rar-cowork-cookbook-scheduled-brief-process-supplier-rebates-and-incentives"
description: "Builds a supplier rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, plus an email draft and a Tea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives", "rar_sha256": "3b60ee6de95071c36455aba462ad768eec833bf508526686647480cc20d8b29f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
