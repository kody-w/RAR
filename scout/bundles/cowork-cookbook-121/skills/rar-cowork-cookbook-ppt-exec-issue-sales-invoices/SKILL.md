---
name: "rar-cowork-cookbook-ppt-exec-issue-sales-invoices"
description: "Builds a read-only executive PowerPoint deck on issue sales invoices from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_sales_invoices", "rar_sha256": "5db545de56abc6af4945a66bd1957af02c7f832ff4578e88eab5bfa0b8f0e2d1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
