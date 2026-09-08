---
name: "rar-cowork-cookbook-blueprint-period-close-readiness"
description: "Runs a read-only period-close readiness assessment against Dynamics 365 F&SCM for a given period and legal entity, returning a close-readiness.xlsx (Summary, Unposted, Reconciliation, FX) plus an email summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_period_close_readiness", "rar_sha256": "fee1dd980d0022c9988e34a5dfc3a9a7e619b7cdbfc184b9ba99f19648a182d4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "record_to_report", "advanced", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVrLmX9G8N2JsX1UViwCJmuiIYRMCiUUgBMLVUWbfd5AAT//3OUhvle1u973dEfNpVGULwTm555OZdfj1zRn6uGrfPr/pgVOueCfPkzhoV07pr5jqUbUZ+KoyF/y38qqybxN36Ku2e/vw5ged1yZ1n1Ql2K4NZbdyVm3g+B+rMp9WddAmlf/Ry6sueN5OyqADS7oOfBVB2a+cyEnKrl+xU+kUidetNgS+2v9PnZFWYQVEWEXJPSjfCT0lyoPIyVdgb9JPHwDRfmjLpIzA0iebj9/ZfBrzblz9qA9F4bRgqVHWVdcH/oeVFgA1vCRPnEXwD6u99dOqzgcgWLkKCifJV91r0yegYjA6RZ0H3dvnn//64S0B12+ff33zcqAEUJnOh6Buk7JXnxIyiwjaNwnA7twpI7CsnoCFS/AbKAL0KsAtPwhX779+7II8/LD6z//MHk4bdT99/lKu3j9f3pY/wLCrPg5WfeUsGqw8p3ZcIH8/fVpR+cOZundDLObvgIPK6NNr52+Uqnr1l+XZjy8mn6Kg//HLWwVEeFrhy9tPK2DwL2/tsFx/WqjUP/70Ka8eQfvjT7/R6QY3Dbx+IQak/vT1/fc7WbDwt6VJuPqqqxzzzqsNvKQOAPHf6bd8XqK/k3s3ydfX4h+r+sPqzykv+vwFyPsKQRfQ/XOywAZg59untErKH995tBUIKqf0gh9/+mdkvTjwsjzp+n+J7s8vwjHwPLDWu0l++vB0319X63fdvtP852xrEDD/jiZg+Td23w31z2g/Pft3pPMlUL/78k/J/dmG9V9WP/9T3f6rDR9W4Zc3NshBVreOmwefV78+Q+TnH/zfbv7w178B0v8tGb0aWu9J4WvhlEkYdP3Xrz//0D1v//DXn38YahDFgVN8Hdr8z2j+mV2ffP5gwfdVP/5xL+BvlFlZPcrV9xxa/VrV/6P926fV1ckT/7f73efV7zNx+axXixLfmL5M8Lts7ICsv7PjT29/A9ADcLIdvOdjgB//8R8rKfHaqqvCfqV71dCvgIP7pAgW4S9x0q3A3wU12gDYtUuAYd/XgfhfPLxIXIWrX/639wT5j947yEPuN1D7+sLdr09k/fodWX/5tLoAulWbREkJwFijVPVL6UQLoAOedRt0QXsHOOVOffARpPPH5WKVlKtf/jvSX59UPtXTL0+wT164pzHCgnndkAefFu3MGNSEly7egtlj4A2AQV55QJowAWi9VIauyu8AMxdLdFmS5ys/AagCKtf0pA2s9Xkh9ssvv7hOF38pXyC9Wb1KWgeBBd/FWX38CNQK8ySK+y9l4MXV6odf//bD6v+s/qtdT+ILDxVUi3dfAAlFXZFXILeGpQQCNwHHAv2fvvj1b+/GBWRKUIOB55IwCV6bQWxmgf/N0vqB+ojixMoNgIWBdYu6avulEib9p5UQrr7LC5guj5baEIMKuPKDOij9oPQmQNUB6ny3ZFn1qw4EYBeCejl0wZPrL277rNFBAZLc6X9ZSYwKKlGVg/8tYj4Xgc1VmQDzf4+D131ApP2hW9HfSHxayUs0rmqndeq4dd55hM7LL0vJf98OiDurMnh8KZeaGyymeqbGyzxgEbCM9+7Sj4vPQW8Cinbpd994P9c4S728POtm+6Xs3sPeaRdXeKAMAKbRkPhLMfhf7yHVxdWQ+0/7AUkXSu9e8N+98ozBV8FfPSv+6nvJX31vCFZfBhRGsNX/f03Roj3F8xrHUxeOXXHyRbu9vLJ0h08Fng0lkOUp7zMDf2tZvsHSN3T+UuYJCLF2+l+vlU9fvq95Id7QAtNrlPakD0wDvLLQfcb5Erdtu2SI86X8VgY+AMWfmAdcDUABJM0Sq98YLk+/SRqDzF9+/9YSPOOifZoVxPKqHtwcxFkYBL7reBmQarHlN+eCoA+WvH3EiRf/QavFGSC2AP0VECIB2QdKxafv0Px6+k30P2x8dT7LlmdXOIBUbZ8EgBzBIuDi8EfSA8Ry+lczDvT8/CQC1CjqftHdBW4Emr5uBm3QDEmX9Aswvuwa1ACUPy7fL02Xu8FYg/wAxgJZUA/Aus+8WeKoAH0NkAFAB0ijIilBnQdGeTfCk6BTLCAAQPa9EX1RfN5+Vyh4JttSoL5tXBRZ9iw1fxUC0cGd6fdYcfmzMAH0imXFk+/fR9p3bs+sAHjZAcwDHL89fTUHn171/dVArL7R/fwP086P/95A9KzYxh8D4PMq7vu6+wxBryr7rch+AmgFvWTtfiu4H38PDr9l7R/ovlT+vPr3ZPsDiffc+LxCPsGf4OXR6T223j/AFMxH+vYRW55+KbXgNywF7KsCBNfiuAlU+O+F79sSUP2iFuARWPwqhN1SPx+gZD+RH3jhS/n7YF+SDRSWMlqCs6t+BwLPDgAE/stp3wsUeFT2gLe/9ItRsAxpz9TogrfP5ZDnH94AbAb/wnC2FKFiiehuGelA7gDr90nw/PUEiLFfLv845CrPCyf/tGIDAEZ59/uoey8dS+n8XXK8lATKeYDDh5UPTNMtpQ4ouTBfEsvpQKSCIF2U6ad6kf41xy2d3xPdX+D+j/Kcfgf9wOP+s89iQcX4sAo+RZ9Whi7t/4wo8CGwirMg8oJpQPLc/0fqzNC2z07BKaphQXYX4OQ73PlJCArkEjbds6CGOfD8UkqefBEYfP6M8fcm9x+5maC/WJDarz4vpfbDO56BbzCYfFh9nzGADd+nvueEXg5goP55mW8Wpz63LBdgD/j6vun7P1e4wdtf/0SuV+q9QufvBaM8b1F/gcL3qru0J8+K/a4ucPb2I4L+o8KA8hN9QQ1bhPxN+99kqJ4D11OG3Olf/z7w6xuITAeEivMem+8dO1gOwOpjt3QqEEhfwBD8fiUaePZv9/Lv+7vYAb0kIAAKHeL75A72YRhFPZLc7YIN5uB+6G0c0tkGBEK6W893Qw/ZYS7pOiQZIiSB7Rxkh/oYoPdK169LO5YsMuHkNoRJEg0xBIV9PwhRzPd3xI7w8C0KO4AE7uKk4/62NUtK/13Rl2KLFb+PFYtB3vX99c0lMLDygHUC9fow0PrqBijkaq0LWTiZnKLeM6+DODdqf7/Sw7bYJAroXeoI9fzTsD8SUeol+lhnicnOA3MzKWg8bBlIv2yVdSgZjLZHDZxgNtqGegTmJGazvdum/ojNZDred7KbGVrTZHPUp2w1K9VDN8ZLE1wn+ySsdeO+IdsNebGRq348ItNdJDLdHa+8t3Zo9tG2aAh6MOaeehx890XNqC/NeHG1YooqRFHu9/x8hyDVn7QBuRykswmbltjyXM7hzN4ermlsFdpwRdmjmOe6r3WdeLYKWz+tZSgROpUYYr/3y+rAKdBle4SPHIzRd5IuIk07KNmk18oY3AsrA/EOKkg+FSO8P/aMeC/Yhytb7Q5XrBnZhlDNlNZ2Cw3jwdoiIY9ZuOjKIZi2YHoKJdctFCa2qgtDUvwOerTeJTom/dE7GfYocwlNGqVUUvbo3eTHjWoeHC41EhGUlz0+SVZ2YW9NGJoErXC79DHdDvwIcwkiGzdiJIzhsicTLunViGrVU78nlE1arZFtfYMhr7tMe6U861masLLpnFn1uDM9Ta/qyyE+R56FCSU3cbUMd3rlH4sByfmHO6CHXKTviXtjKIQXLcQTNdUJAKzdD9K6d64RPkWjLKn7qT1WmczmKv0YeJOREAu28qBhT1K1M/dmXk/phYKmW+v40omgcDcXvELekqah8dc6jt3ArruujxWC9e+ZRjgsnok3impar+minA3rbVVN1g1VEm195eNjhq4TUTql0SFUR/XM870/uke052VN3V5vEi9XjcRrGHffqxhkMHxOMPZltpvBw4ttaydUjrTnIyynOpWvZ+fqwnoAM4ZFa01pCgi5tYVmfjyyE6JvoST1cr0kEp3U79IJ4qr7/h6p6cw8dkgYnZCa3XH6qGAXKY7MEO8MQT6Rd2czNUhh2ntfTTGMKunSCQ6E7t5QHlb2GOaIEWyYbFlm6NT1aL1OU6WI9Y6H5+sZWtPQg77fWx61VZJmmeCCz6Ry79jTw85t/pJYYn6n4CHj++xCoE27v8ZX+lBccy+Y+Fm9NvlZniU6CoUby8xb90G3M18lF/LsK9PkBExv4KYt1Hu0pBE0wu0hiI50LWSOkx3vXH080TBDqMLVVyLajcJ5sNRpfX2QV99j0UqzaL67JRf/ajXE7Eqn7sCrh02eBhQsyZuIgPYtIpW8iE51cpIGp0sPRZ8eufwmXQWZxtlMgPzdTDVdHt9xlKCHnUir3lpQmI0cbmEKu9yafTZuITZy/bt8uuvVY7153EST2ztkqySzVmD0oCDAaXtvHg9qZHWn1jCO9OPeJ+JBURxrd77hqHGUTb+eOxIOuDI6kGLJskprnTrknNwj5XzeyZsMLfelSdXp+tihm/5U8qXYItbUy7CJB1p121M0e7tSRTBQnDS3WY0nDl6zG8UZVIE9UWGUOjt/Tbbd0KaxTiTn/Sx3sAQZKNQ+FLMtUcQoME+7H+cdH2B7f9fjGDTEdCpijwE74luVkxt2HzmCFoeSLxbMfjrrwT6fKFk89zLtX/eCZxCSsDNrZ+0bKWpfqDubNIWhSPuyhdTjrAZ3Wx13U2ScXRPgdwTNbe6OmEhouY1fKPn+CKxCZMDsru2tI15v9ki6ubT4dg7vfJRvJ1YfE4PfKVg2xZycYZZC4pdZT2xfL5mbRhgJWrtDzFMYJHMKTYjtwRSN9SOtpQsZjofYsAzDPZjDjcHZ9DpxRm1cGVnjjRK7wBLazMF9Aw063OfSxMeZoR+tm3mYC4vbxA4P1yZFlPaUz+WM5q1FjwnFIpRxkEshyq8eWmG0cNveB46MJ66z+WtEU/x6XJdXsTreTdSPtyE1VRhssNYDc4YrkpBmyyjMmvWn7uTvjPJEN+zGP+wl09uMMkGql5Yk/anBaDGRqcPWvRDyUeZaUjA2+qwR+0PcSb5TqBsrhfKHWPmk8ohmx8y4A+mP9JoMotOONKy1alU7S4y3Xq3siobC6yzU21t0pvNMnzHVzbfNwDJcI+8n/ny9sozu9Q3Qu6obFJ/YiiiJfZGhm2JquFw/KtbBFwQr6rC6MqnNhduxcMzTzjna70FZC85VzibJkQlwaSqvaVfOJm84c32wjM6NMox2Ai1t0M2+7Ss4jtvD+sHn2xzUIURwxVTc71N3I5kqZp2hs3wAYg8aQhYUWeatTsF8oW8tmU/UFDicvurnizedkilRHB+yHg/qeGF9ls2uDXPkepOeysNDuMBQfGHuXCIl4Wa3HmJXQBBKsaQu3D9OecG7yh6VfVRCdDgTitMDgaKBT+Uzf2t9mp44HGJvXVJj/pGw6ovaz9uUO0u1KWSlsz8guUkUmqsf7au+Tu9MFMs5LAjq6FR2EsOFKaHdej9zxp7kTusiprO9eWsemgRd0d4XBqM5gJoilILCMc2QqSAF6aZuy6a/5XD+8Fs92on6eJKACBx7n4ZW4tpr5w1G2ptb6hAdIJFP4NEVr+sOthOGZVGJ1rF8TPPTZPn8Tjo1mXqQaV1CiH4zFCnLUdDO4pKbK9Bm585mj3u6i4rNMSbcU5bL6nhMRt0rzzNPjZQv1XPtNZddw2iPY1ydEacpeyW1IS278XTO0P0dbpnj7Pr1+iLseREqlKAK60Q/ohx6Q/LoWjSmMyO8XyU3LOsbm6v0EU0YMzN42S/U+vDYjM75fGTUBoFIUR4pdsPZnY5t9qMthyp/7H30pjFEMJxkeVTaCrcfB8kuuwENw6uEepEW1VObDWTH+Bdta0ZQk93Eo7QJ7xeYVEI/G1h/SyXGdmzMyDmu6Qd7z9pIl81GWmeHyharrCrj7FxLN55UipRkLxJcuUjVCTDF94bcUwYC9VEGeYeZul5tQ/EFmATPnFTJJyODQxo9BfLEbvsGFeHzkep29uMWSMaUDvuLYItO7qlFYupuWprGHr4UpDL1XM9Qc+606IEx9X5dSWfWkbsDdEkFYX/qoxZPmu14YoN14NCSDIU1x+/9qxefUWzExfmgQl5jwTcHNH0UfJwrpznKWbceaipA5Hi0t10OVw4jsxbCGP2Q1JQh7O/DlDKccfdySb/BlYluHTYwbInwhRjzizptbKXoUMU5sBkvwcLeNTzqKnKIcYGdfJ4YBbE9DdGKTHR0fS/WG5uLZ2h0kmrPWPw12HnhdM9ADB/d/UHcWuSY0dMpmvA4392YW0QgY+dqugXdwnyMHTK1tui5P7V2l4kgWkCpiZlBQUGg2PxED3TVcuIx0HQ04gWJ547b66nBjnzszmxgkYzgmwPhatX1Lq1RLjT5Lj1BExKG9007Zc6FRkauGS5NETOGnUzdmhcRM3iMj3N9uVEWMSFnbl8BnNflTL4fLyhv1N5IpKUu7uX1mmIhc3/0XJppuG5fng2G0wXA6HzQ9FFlL+UMY8oeumjYugK9JXa+iIZc8VWFmBjG7C07JPOxttncKOY56fY9dR5zzCbMdLfB2ZORR5lvJ9XoxCyV3nY+fY6wZkN0DaYNlKKN6eEh3pjYZM9Di4jXK9XRZSZIKTr41XHKFNg2L/bAcWAqJB/GIPVMbJMCS/uOUzLd4botpdGy1qU/S7jGwzgyzMzBWWsDAPQ7W0vBMa12YodDSJQ7wvqcbCfBa2G5SjORauVjfucJ22w8FAnVwB8YOvPO3GWX+1o+EDnMUdzhWmikcFfNunR2Qjhw6xsF63OrN/g8wY/1YzhE2/HsXa5HUyvSLD1vDJc61NFmw1bHUV87uIZeTUyWBG3e3Tih4Tc6fXJpzSRsu2ol0+e0CWkPMLtJx1p0u5YxJUYQqgecXkMa0kv8aDW6AY3C+Ri00DjWNYm7aPTQ8RtN5w98n1eYlhzxLKstVTifuLq+n2x7XSH37Z0L2WMS1bhy4vAd82BspWSiERvhGgXNy+42Bn1KdaGnjITDaJYjkpuMy6W2LiAY03Tnkivdzbx2J5reurwtyCZvEzyhwIN1h7Ws2J2gHWNpUYpzlOeYiF/1VHpqYo/fndCAhw+gKypv62l3xS0FCzpBkE4Wr0v2Lq24fc/xnrNfR26lgfGnry6PnD+ymGAhmVI8tJ1/YycuErlewJg6a8tdAs32oaPt00a2eJGbUeeciI89HTsEFcnSVRxxJJ+mVFOuyP24H0vxoG6JR4qVEIau5eJyZVharXicJG6EGqulE+bZ4HLHe45N3L41jnbmUfFakg4YL9ZIj3UpL3RMLuZ6ohjsRPQMMtrdQBQ3ZBs1pdsLR++4f2ybcG9v6GY+0ujZqXZ8rB2Qgb3Zx3Q9e9u9czEGcuJKiE6vtwuPqlHFa2uk0fe5gsDsrGPY8VyNrFVbVn+sYbTRbZw08cHjb4MwSdSt7LNtl0R+cDv0RBmRwfHGHh45aaun4EzJjuRAtyvi7RBO5TYHMEFmONPsHrZ9DtAM9GUxnoIJ90oxfANzs94yVWE9ti2Cnq/ndaYhphc/NpDWjcxxXTfSLcPG+ZZil0RzTiMS7gf0ZhsCRrjbNjvyFKpVG84gH5dilJB+uIVJOuJXnb1xMCHHqLiZyRM1ohY6IA8TROjBbjcXw/CHs7MmydM2hGN5cxVJw5SxM+6ofB9yd90+4ZMG3yotK90ClILdWpn4EMSqqB0cTeDpA8vVxIXQtlNxPrfOA5e8SfGRrJBDMQh91TM15MwrfGMp9gWP1DtAxXTUZ7ObslJXtuPDDKzTUbhqZ9faZHqg+uhVJu0QDe+Qsae4IJwYH5JvJ2JM6pPblCruRvv6tqZjnd41aIKMhRgFc8jg7mHXBVu7FvtMzQIfs2+XjuT7wD+U/eUcwErHVuQZX6t12bvGbWMaW7WXT9O1Cw6RwYbN0JutN4SOHFzH9cYq/VON++U2CNOynYvJv2zA/N7jCA66hovo75PetS0IDcxMhC/ierLazQhF6Y1PpyI/qqqd8iT9KCB/c+jRPNS3qHB3+tAtHyOh2mc1V3SIfmzRdr/dqFBjQgLXPmi93ojnqYQOg0dh9rxPr6rGC8jB5kRFyJHAvgxTRp5ON4fZ7vr4YNYbSL9VF9RloXJ312wVITFXQklUzft4LR8Ed81TAw/4wmCGJVpoTULrJF4jcrnn4yQOoSlf801cdn6FYsx64BjlSN8r7QZq6DFKr5kZHoJCIuRuxjRJuVTSMYSTB5iXt5cy78gzR1VbIxHWY7ymRSH1ipPKQ0U2r8cKERvekx5zvemavjJO9xGBDy2YrCnkFmdibuHuTJeSV2DRGHiKgN1hlaj61vHqTdSnXRw9sgTfnyACsiwrrAcj8+bitpEOZuD3cjbxp0QwSpDFYJYkMqKEruJmxK66pOoFjG6xRowv+Loxs3CbNSpSEefpTpBrmx7W8xBNM81lFCJk7IivMQwlulod2QunzScdQRKlKyhhmG4V2ZEOgoRiZxFgT1NScNzBfQJKIzRo18v2IMWYvRZKqSyrmXQzwtrUR8uUDy1zVngDDFhp9IB01L9ivkAZfGQ/5kuC4jvfQPHyaLhTYIh1hEd4rzQC2h1LVaDR/sKOlTNyW4IXcQHrReBZZRIJ435vA7uJuYyEnJzYKawmkNAGP0sxqYsM3ZV+7M19et57wWUDWn79hHAGTvD0GrRdNoLoN4iw2cFgjYtfduuDpO68ayb6OzVPlS4etgpijD6NuMrZU/f28bwpZlPuWuLe216ARwepwZEGNXuj2yDzwdVyr0cdGZ0LvzpjGh74VHhTOJ+Qle7UHO/seriSJdYLW9TfYHih7h0HHTchFxWqRMAYjuLICYklW7va97w0YzSG6v54EST5Rjz421YxMTu4rx+j9/CpA+gnCcbt3S54UKp4gHAP1iu8ERpVwyj8gGrhlZjO8AGdakHvvceIR2h737p9im3aCwoFcq06CL4PNmYQEEwXtLd4nsOSbPPNUQLTNzdb69Hfrf10v66J3Z7jZVzP5TDhdhCPbgZAK2iHgIRQPd1s9kp5p0ATtz2EdXgOkN11AvPsdrZ56rh3iOjqRydCQE5Yi5j9bXfz3dZUTqhKyBOGr+n15pRom23OhjOjem3AqulWGB4zR+uFlYUG11zx2xa2PfkR86K9dowwWPOeEZ6m9YOqbQIX6Z0HHzWyMY+hxirzjMbnOIaEvVo1qgTgZETwLLUuarIzetm2NfQklmHGnUOmRM3Rc+5Zhp4uYL5MhR1fsi4r0bbVgxLG2ur2anVWcCAh9zx71NRbRuNWKbcX7tTpuKVTyLCDmUZV5CEe1a7X4KO63YJSeapLM3WT+6OoITqqzU1/6uA1fLen7CTetZu+tdta2IVN4Vz7emyLXe8f0dTNHZwIuWNzzTv5Rp4OcmaNhGua/RlGNb7aEvvsJm9Dx5WDoNreO/yEl80B7UXOCsJygOR0z93kQhulcBwAutzH+bzL7i6SdM4ZupxpxClzgenxmRoxWcZPOZjuXbOtjLKWN3E985MVXYJgPiKtR5CPiSCtszq1U3RHk7S934zNus2FMBzys3VbK7taIr2jklCT4NtCrXoJvRkZW6YrlARIC5CA2lgwoe/2hH4qZSfx+rGFArIfTr2BY6ecHBxr056SR3N+gCHjcvJva9HNET0tL0Plp5ZPd1B6L4VyeEjMHEjsnkuVmHSu+H3KUXvjBs4ukWD1cqoRFqmD9aZVoPNFRWAMlSjYEHMJHTosLzd3xxJ35MOBlRtJkVTk4PgFYzKTIc+TWB2qe3CKKMzn7w9XJDsAn8GUHyTDcw7S5pHA630r05YyFFuLWSeHrMKLhDgMhvXwGpkYH8W6bfhdeb9rwZbByq3TKvhg8Qp0sZRIgSY8hFwJ4on1GLKnmEx7YotxB+9OkRHa5YeNXw2VJQvmcWzN5t7K6qAeTu22w4jUUz0v7F3Ft9trS1uY21IblNh47nU+4YHQ4S65gVC/NuV+NzN2EkLtxYrrgn2op016D+9lZVrrvIfd2BF3nhjSbqXTFOXrQzgWBXMFw8VlY2i4FNZ7Gw42p6Fy1qJ/nDbZeDgYBXSyGblWdHqoCYVdn8Oc4vpCmttNxg7XfQBdCH4r97F8R7ZQZRG7nGGhg6wGstJvEwsf+MiLhjyar8EWwfges6T1xIJW9Hb0tcMlrWidjZAS9B0yFJzuh4cS0sNZOUhWvd3p8Ymss1yay2uR78gSh9eQSWXB7lHl26Kx0tZRKXUjp+49HFmKov7y9uFtOS1/P/P+l1+wW07b/p8d+r3O5769QvM8jAUMPz95ff7XRfrrh7fWS4BAr4PNLh+i92PAvzvW/PjfvTGx7J5e76x9O8h/vRrQO9HyKvdbUvpD17fT167Kny/QgB3u0L0EAqp4768IPE+Tv35nt6z63fXrZP9rX319vWMHbjn+fbGB/7a8sdkH0ftp74c3//1trq8bAv8atPWi7fuLGEDJzSf40+btb/8XNiwDvo0vAAA= -->
