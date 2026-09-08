---
name: "rar-cowork-cookbook-scheduled-brief-raise-purchase-requisitions"
description: "Builds a morning brief on raise purchase requisitions from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the owner and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_raise_purchase_requisitions", "rar_sha256": "7d4aaacd064c86dfc63108c606633420d848d2f2aa81e1786cff1d3c68d31869", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
