---
name: "rar-cowork-cookbook-blueprint-period-close-readiness"
description: "Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_period_close_readiness", "rar_sha256": "fee1dd980d0022c9988e34a5dfc3a9a7e619b7cdbfc184b9ba99f19648a182d4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "record_to_report", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_period_close_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_period_close_readiness_agent.py` and in the RCI capsule.

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

Period Close Readiness Blueprint — Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
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
    "legalentity": {
      "description": "Legal entity code in D365, e.g. USMF",
      "type": "string"
    },
    "materialitythreshold": {
      "description": "Currency amount above which differences are flagged, e.g. 10000",
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
    "periodname": {
      "description": "Accounting period to assess, e.g. 2017-12",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_period_close_readiness_agent.py` and embedded as the fenced Python below (sha256 fee1dd980d0022c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_period_close_readiness_agent.py` first:

```bash
python3 blueprint_period_close_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_period_close_readiness_agent.py   # or on stdin
python3 blueprint_period_close_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Readiness Blueprint — Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_period_close_readiness',
    "version": '3.0.3',
    "display_name": 'Period Close Readiness Blueprint',
    "description": 'Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'record_to_report', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-period-close-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-period-close-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8cd624e64d6223fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods', 'record-to-report/record-financial-transactions'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'record-to-report/blueprint-period-close-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the General ledger role', 'Prerequisite: Cowork D365 ERP plugin toggled on in the session', 'Output matches: One workbook in `Documents/Cowork/output/` plus an email draft. Where a check is blocked, Cowork returns a constraint table naming the entity it needed — that table is itself the deliverable for the admin who has to expose it.'], 'confidence': 1.0, 'deliverable': 'One workbook in `Documents/Cowork/output/` plus an email draft. Where a check is blocked, Cowork returns a constraint table naming the entity it needed — that table is itself the deliverable for the admin who has to expose it.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legalentity': 'Legal entity code in D365, e.g. USMF', 'materialitythreshold': 'Currency amount above which differences are flagged, e.g. 10000', 'periodname': 'Accounting period to assess, e.g. 2017-12'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Answers 'can we close?' on demand instead of on business day 5, so the controller chases the two subledgers that are actually blocking rather than polling every owner.", 'expected_output': 'One workbook in `Documents/Cowork/output/` plus an email draft. Where a check is blocked, Cowork returns a constraint table naming the entity it needed — that table is itself the deliverable for the admin who has to expose it.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the General ledger role', 'Cowork D365 ERP plugin toggled on in the session'], 'prompt': 'The attached image is a workflow blueprint. Build and run it as an automated task using the Dynamics 365 ERP plugin. Follow the diagram exactly: execute each phase in the order shown, honour every decision diamond, and stop at a red halt node if its condition is met.\n\nDo not ask me clarifying questions — every input is bound below.\n\n## Input variables\n\n- periodName: 2017-12\n- legalEntity: USMF\n- materialityThreshold: 10000\n\n## Trigger\n\nTrigger: monthly, business day 3\n\n## Outputs\n\n- close-readiness.xlsx — Summary, Unposted, Reconciliation, and FX sheets\n\n## Notification\n\nEmail the readiness summary to me\n\n## Guardrails\n\n- Read only. Do not post journals, do not lock or close any period, do not run consolidation.\n- Produce the workbook in this run — do not return a plan or a methodology document instead.\n- Report readiness and differences; leave every close decision to me.\n\nIf an entity is not exposed to the plugin or the period has no posted activity, report exactly which check you could not run and why, list what you did complete, and stop. Do not fabricate balances.', 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary.', 'example_request': 'Check if period 2017-12 for USMF is ready to close, materiality 10000, and email me the readiness summary.', 'inputs': [{'description': 'Accounting period to assess, e.g. 2017-12', 'name': 'periodName'}, {'description': 'Legal entity code in D365, e.g. USMF', 'name': 'legalEntity'}, {'description': 'Currency amount above which differences are flagged, e.g. 10000', 'name': 'materialityThreshold'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to know if an accounting period is ready to close — unposted work, subledger-to-GL differences, and FX exposure — without posting or closing anything.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BlueprintPeriodCloseReadiness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPeriodCloseReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legalentity': {'description': 'Legal entity code in D365, e.g. USMF', 'type': 'string'}, 'materialitythreshold': {'description': 'Currency amount above which differences are flagged, e.g. 10000', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'periodname': {'description': 'Accounting period to assess, e.g. 2017-12', 'type': 'string'}},
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
    print(BlueprintPeriodCloseReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
