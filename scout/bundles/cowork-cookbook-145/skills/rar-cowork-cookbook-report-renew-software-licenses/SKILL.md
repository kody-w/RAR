---
name: "rar-cowork-cookbook-report-renew-software-licenses"
description: "Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_renew_software_licenses", "rar_sha256": "028519e7aabfc4dc328013b65ac5ac35732a9a569da67bddb5b66d40d2a6232b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_renew_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `report_renew_software_licenses_agent.py` and in the RCI capsule.

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

Renew software licenses Summary Report — Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report against (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-renew-software-licenses-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 028519e7aabfc4dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_renew_software_licenses_agent.py` first:

```bash
python3 report_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_renew_software_licenses_agent.py   # or on stdin
python3 report_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Summary Report — Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_renew_software_licenses',
    "version": '3.0.3',
    "display_name": 'Renew software licenses Summary Report',
    "description": 'Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '186e52e006037bbe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-renew-software-licenses-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where renew software licenses stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of renew software licenses for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-renew-software-licenses-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads renew software licenses records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a renew software licenses summary report for USMF in D365 with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'Dynamics 365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-renew-software-licenses-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of renew software licenses activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRenewSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRenewSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-renew-software-licenses-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
