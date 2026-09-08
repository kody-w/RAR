---
name: "rar-cowork-cookbook-scheduled-brief-raise-purchase-requisitions"
description: "Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_raise_purchase_requisitions", "rar_sha256": "7d4aaacd064c86dfc63108c606633420d848d2f2aa81e1786cff1d3c68d31869", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_raise_purchase_requisitions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_raise_purchase_requisitions_agent.py` and in the RCI capsule.

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

Raise purchase requisitions Scheduled Email Brief — Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 7d4aaacd064c86df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_raise_purchase_requisitions_agent.py` first:

```bash
python3 scheduled_brief_raise_purchase_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_raise_purchase_requisitions_agent.py   # or on stdin
python3 scheduled_brief_raise_purchase_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Raise purchase requisitions Scheduled Email Brief — Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_raise_purchase_requisitions',
    "version": '3.0.3',
    "display_name": 'Raise purchase requisitions Scheduled Email Brief',
    "description": 'Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and',
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
        "upstream_slug": 'scheduled-brief-raise-purchase-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6cab4e580a345c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/raise-purchase-requisitions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-raise-purchase-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where raise purchase requisitions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on raise purchase requisitions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads raise purchase requisitions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and', 'example_request': 'Give me the raise purchase requisitions morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly (e.g. weekday 7am) purchase requisition brief for the responsible owner, drafted as an unsent email plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRaisePurchaseRequisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRaisePurchaseRequisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRaisePurchaseRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
