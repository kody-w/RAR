---
name: "rar-cowork-cookbook-report-manage-data-security"
description: "Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_data_security", "rar_sha256": "beff03741fb72480da5080f9d4247969f33f5cac07366b84002526c2f19bf56e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_data_security`. The original RAPP
agent is preserved byte-for-byte in `report_manage_data_security_agent.py` and in the RCI capsule.

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

Manage data security Summary Report — Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
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
      "description": "Dimensions to break out where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-data-security-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 beff03741fb72480…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_data_security_agent.py` first:

```bash
python3 report_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_data_security_agent.py   # or on stdin
python3 report_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Summary Report — Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_data_security',
    "version": '3.0.3',
    "display_name": 'Manage data security Summary Report',
    "description": "Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe",
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
        "upstream_slug": 'report-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d435238521264c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break out where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-data-security-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage data security stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage data security for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-data-security-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage data security records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe", 'example_request': 'Build a manage data security summary report for USMF from D365 with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-data-security-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break out where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a manage data security summary report from Dynamics 365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageDataSecurity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageDataSecurity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break out where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-data-security-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
