---
name: "rar-cowork-cookbook-report-ensure-client-approval-and-sign-off"
description: "Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_ensure_client_approval_and_sign_off", "rar_sha256": "0cc7206e2b1450bba9b58d91a91bc8d17904bc7d22be9f813a63246452bbd4e9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_ensure_client_approval_and_sign_off`. The original RAPP
agent is preserved byte-for-byte in `report_ensure_client_approval_and_sign_off_agent.py` and in the RCI capsule.

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

Ensure client approval and sign-off Summary Report — Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off
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
    "breakdown_dimensions": {
      "description": "Dimensions to break out by where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-ensure-client-approval-and-sign-off-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 0cc7206e2b1450bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_ensure_client_approval_and_sign_off_agent.py` first:

```bash
python3 report_ensure_client_approval_and_sign_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_ensure_client_approval_and_sign_off_agent.py   # or on stdin
python3 report_ensure_client_approval_and_sign_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ensure client approval and sign-off Summary Report — Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_ensure_client_approval_and_sign_off',
    "version": '3.0.3',
    "display_name": 'Ensure client approval and sign-off Summary Report',
    "description": 'Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-ensure-client-approval-and-sign-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-ensure-client-approval-and-sign-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88247cc9cbf88212',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/ensure-client-approval-and-sign-off'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/report-ensure-client-approval-and-sign-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-ensure-client-approval-and-sign-off-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where ensure client approval and sign-off stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of ensure client approval and sign-off for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-ensure-client-approval-and-sign-off-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads ensure client approval and sign-off records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a client approval and sign-off summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-ensure-client-approval-and-sign-off-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-data-change summary report of client approval and sign-off activity from Dynamics 365 ERP, with totals, breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportEnsureClientApprovalAndSignOff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEnsureClientApprovalAndSignOff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-ensure-client-approval-and-sign-off-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportEnsureClientApprovalAndSignOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
