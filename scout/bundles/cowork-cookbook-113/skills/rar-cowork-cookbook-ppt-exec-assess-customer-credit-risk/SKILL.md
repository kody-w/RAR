---
name: "rar-cowork-cookbook-ppt-exec-assess-customer-credit-risk"
description: "Builds a read-only executive PowerPoint deck on customer credit risk from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assess_customer_credit_risk", "rar_sha256": "c94adb1cc2077810ef5b3a41e91ba046b641ba68e0416ea739b7c8184ea4e0cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
