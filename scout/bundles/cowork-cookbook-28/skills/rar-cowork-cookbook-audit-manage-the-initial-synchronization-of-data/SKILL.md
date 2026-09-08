---
name: "rar-cowork-cookbook-audit-manage-the-initial-synchronization-of-data"
description: "Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_the_initial_synchronization_of_data", "rar_sha256": "5407b51627704c275e8cba816db14b584abec4ad8d3d012c0a090f0afcd89fd0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the initial synchronization of data Completeness Audit — Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
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
    "date_window": {
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 5407b51627704c27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 audit_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 audit_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Completeness Audit — Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_the_initial_synchronization_of_data',
    "version": '3.0.3',
    "display_name": 'Manage the initial synchronization of data Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e1c5f0e1a6b4a84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage the initial synchronization of data records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage the initial synchronization of data. Output an Excel workbook 'audit-manage-the-initial-synchronization-of-data-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage the initial synchronization of data data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads manage the initial synchronization of data records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary.', 'example_request': 'Audit the initial data sync records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check initial data synchronization records in D365 for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageTheInitialSynchronizationOfData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageTheInitialSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
