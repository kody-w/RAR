---
name: "rar-cowork-cookbook-ppt-exec-assess-customer-credit-risk"
description: "Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assess_customer_credit_risk", "rar_sha256": "c94adb1cc2077810ef5b3a41e91ba046b641ba68e0416ea739b7c8184ea4e0cd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assess_customer_credit_risk`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assess_customer_credit_risk_agent.py` and in the RCI capsule.

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

Assess customer credit risk Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length/scope of the review the deck must fit, e.g. 15-minute monthly review.",
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
    "output_filename": {
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-assess-customer-credit-risk-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare the trend chart against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 c94adb1cc2077810…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assess_customer_credit_risk_agent.py` first:

```bash
python3 ppt_exec_assess_customer_credit_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assess_customer_credit_risk_agent.py   # or on stdin
python3 ppt_exec_assess_customer_credit_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess customer credit risk Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assess_customer_credit_risk',
    "version": '3.0.3',
    "display_name": 'Assess customer credit risk Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-assess-customer-credit-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assess-customer-credit-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2fb9780cd1318ad8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/assess-customer-credit-risk'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-assess-customer-credit-risk', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'meeting_length': 'Length/scope of the review the deck must fit, e.g. 15-minute monthly review.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-assess-customer-credit-risk-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare the trend chart against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for assess customer credit risk reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on assess customer credit risk for a 15-minute monthly review. Produce 'ppt-exec-assess-customer-credit-risk-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads assess customer credit risk data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build an exec PowerPoint on customer credit risk for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare the trend chart against.', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-assess-customer-credit-risk-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/scope of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a credit-risk review deck for a short monthly executive meeting, sourced from D365 ERP data without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAssessCustomerCreditRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssessCustomerCreditRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length/scope of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-assess-customer-credit-risk-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare the trend chart against.', 'type': 'string'}},
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
    print(PptExecAssessCustomerCreditRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
