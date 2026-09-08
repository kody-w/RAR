---
name: "rar-cowork-cookbook-report-ensure-client-approval-and-sign-off"
description: "Builds a read-only client approval and sign-off summary report from Dynamics 365 F&SCM (ERP plugin) for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_ensure_client_approval_and_sign_off", "rar_sha256": "0cc7206e2b1450bba9b58d91a91bc8d17904bc7d22be9f813a63246452bbd4e9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
