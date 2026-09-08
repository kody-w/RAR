---
name: "rar-cowork-cookbook-audit-plan-software-releases"
description: "Runs a read-only completeness and policy audit of plan software releases records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings by category plus a summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_software_releases", "rar_sha256": "3b25449009816fc0bb38300380f63976c720d18726462f99f3a6b13e680a6879", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
