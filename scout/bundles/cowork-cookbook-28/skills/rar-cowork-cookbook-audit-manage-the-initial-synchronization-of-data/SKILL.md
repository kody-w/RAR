---
name: "rar-cowork-cookbook-audit-manage-the-initial-synchronization-of-data"
description: "Runs a read-only completeness and policy audit of initial data synchronization records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_the_initial_synchronization_of_data", "rar_sha256": "5407b51627704c275e8cba816db14b584abec4ad8d3d012c0a090f0afcd89fd0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
