---
name: "rar-cowork-cookbook-ppt-exec-issue-sales-invoices"
description: "Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_sales_invoices", "rar_sha256": "5db545de56abc6af4945a66bd1957af02c7f832ff4578e88eab5bfa0b8f0e2d1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_sales_invoices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_sales_invoices_agent.py` and in the RCI capsule.

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

Issue sales invoices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-issue-sales-invoices-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior-period comparison basis for the trend chart, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 5db545de56abc6af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_sales_invoices_agent.py` first:

```bash
python3 ppt_exec_issue_sales_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_sales_invoices_agent.py   # or on stdin
python3 ppt_exec_issue_sales_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue sales invoices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_sales_invoices',
    "version": '3.0.3',
    "display_name": 'Issue sales invoices Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-issue-sales-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-sales-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a047a01c23e2443',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-sales-invoices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-issue-sales-invoices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-sales-invoices-2026-05-24.pptx.', 'review_period': 'Reporting period and prior-period comparison basis for the trend chart, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for issue sales invoices reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on issue sales invoices for a 15-minute monthly review. Produce 'ppt-exec-issue-sales-invoices-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads issue sales invoices data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint deck on issue sales invoices for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-sales-invoices-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior-period comparison basis for the trend chart, e.g. monthly.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on issue sales invoices status from Dynamics 365 F&SCM, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIssueSalesInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueSalesInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-sales-invoices-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior-period comparison basis for the trend chart, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecIssueSalesInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
