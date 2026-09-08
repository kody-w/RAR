---
name: "rar-cowork-cookbook-report-manage-data-security"
description: "Builds a read-only manage-data-security summary report from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook with Summary, Detail, and Top10 sheets for a legal entity's most recent posted pe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_data_security", "rar_sha256": "beff03741fb72480da5080f9d4247969f33f5cac07366b84002526c2f19bf56e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
