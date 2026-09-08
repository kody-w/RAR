---
name: "rar-cowork-cookbook-report-renew-software-licenses"
description: "Builds a read-only software license renewal summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_renew_software_licenses", "rar_sha256": "028519e7aabfc4dc328013b65ac5ac35732a9a569da67bddb5b66d40d2a6232b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
