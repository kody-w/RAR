---
name: "rar-cowork-cookbook-audit-plan-software-releases"
description: "Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_software_releases", "rar_sha256": "3b25449009816fc0bb38300380f63976c720d18726462f99f3a6b13e680a6879", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Completeness Audit — Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-software-releases
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
      "description": "Date range used for stale-date checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-software-releases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 3b25449009816fc0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_software_releases_agent.py` first:

```bash
python3 audit_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_software_releases_agent.py   # or on stdin
python3 audit_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Completeness Audit — Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_software_releases',
    "version": '3.0.3',
    "display_name": 'Plan software releases Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar',
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
        "upstream_slug": 'audit-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b1c1be68b260d5f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-software-releases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan software releases records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan software releases. Output an Excel workbook 'audit-plan-software-releases-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan software releases data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads plan software releases records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar', 'example_request': 'Audit plan software releases in USMF for completeness and export the findings to an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-software-releases-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants plan software releases records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-software-releases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
