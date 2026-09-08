---
name: "rar-cowork-cookbook-audit-merge-cases"
description: "Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_merge_cases", "rar_sha256": "cdf9bf8aff11e5b24ffca50f75a7785a77373e461b532f90a69d30fbbd57b458", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `audit_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Completeness Audit — Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
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
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_merge_cases_agent.py` and embedded as the fenced Python below (sha256 cdf9bf8aff11e5b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_merge_cases_agent.py` first:

```bash
python3 audit_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_merge_cases_agent.py   # or on stdin
python3 audit_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Completeness Audit — Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_merge_cases',
    "version": '3.0.3',
    "display_name": 'Merge cases Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4540898d97c53d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit merge cases records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to merge cases. Output an Excel workbook 'audit-merge-cases-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no merge cases data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads merge cases records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit merge cases in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants merge cases records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMergeCases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMergeCases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzFV9WRfEJuEX3TEsCNWCRASKne42EHsmwDV9Hefg+61y9Xt7jcdMX+NHLYEnNwzf5nHh99f3KFPqvbl04sZuuVKcPM8TcJ25ZbBiqnGqs3AV5V54O/Kr8q+Tb2hr9ru5cNLEHZ+m9Z9WpWA3BjKbuWu2tANPlZlPoPVRZ2HfViGXfdkV1d56s8rdwjSflVFqyJs43Dlu13YATK/aoNulZYrdi7dIvW7FUrgK/5/moy6iiqg0CpO72G5ysPYzVdh2af9/AHQ9UNbpmUMJKy4yQ/z1aLzU90x7ZNVVYarLgnDflUDq6K0DJbFvtuHcdXOqzofFq3NoShccPlc+QpsCyd30b57+fTrXz+8pOD3y6ffX/zc7cCtF2oxQV3UZxbtwfrcLWPwoJ6BM0twDYQBpQtwKwij1fvVz12YRx9W//mf2ei2cffLp8/l6v3z+WX5A3y46pNw1Vdu14cBULN2vTQHlr6uqHx05+7d4EXnDsSijF/fKP/gVNWrvyzPfn4T8hqH/c+fXyqggrtE6vPLLyvgzc8v7bD8fl241D//8ppXY9j+/MsffLrBu4V+vzADWr9+eb9+ZwsW/rE0jVZfzAPHvMsCsUzrEDD/zr7l86b6O7t3l3x5W/xzVX9Y/ZjzYs9fgL5v2eYBvj9mC3wAKF9eb1Va/vwuo61AxrilH/78yz9j6yehn+Vp1/9f8f31jXECkhx4690lv3x4hu+vq/W7bd94/nOxNUiYf8cSsPyruG+O+me8n5H9O9Z5CsrwWyx/yO5HBOu/rH79p7b9K4IPq+jzCxvmoGRb18vDT6vfnyny60/BHzd/+uvfAOv/lo1ZDa3/5PClcMs0Crv+y5dff+qet3/6668/DTXI4tAtvgxt/iOeP/LrU86fPPi+6uc/0wL5pzIrq7Fcfauh1e9V/T/av72ubDdPgz/ud59W31fi8lmvFiO+Cn1zwXfV2AFdv/PjLy9/A2BTAmsG//kY4Md//MdKTf226qqoX5l+NfQrEOA+LcJFeStJAWh2T9RoQ+DXLgWOfV8H8n+J8KIxgNvf/pf/xPOP/jueQ08k/vKE4S9PGP7tdWUBRlWbxmkJUNagDofPpRsDtF2E1G3Yhe0dAJM39+FHUL8flx8LaP/2D7y+PMle6/m3J/inb8hmMPsF1bohD18X/c8JgPQ3bX2A4OEU+gPgmFc+EB+lAIEXjO+q/A5QcbG1y9I8XwUpwI1+AfCFN/DHp4XZb7/95rld8rl8g2F09dafOggs+KbO6uNHYEeUp3HSfy5DP6lWP/3+t59W/3v1r6iezBcZB9AB3r0NNJRMXVuB6hkKsGzpXgC23eDp7d//9u5NwKYErQfEJo3S8I0YZF8WBl9da4rURwQnVl4IXArcWdRV2y9tKu1fV/to9U1fIHR5tKB/UnX9KgjrsAzCEnTVPnGBOd88WVb9qgMp1kWgSQ5d+JT6m9e6TxULUMZu/9tKZQ6g11Q5+GdR87kIEFdlCtz/LfBv9wGT9qduRX9l8brSlnxb1W7r1knrvsuI3Le4LB37nRwwd1dlOH4ulz4aLq56Jv+be8Ai4Bn/PaQfl5gvowOo9LdxoP+6xl06ovXsjO3nsntPbLcNn8MDUGVexUMaLHD/X+8p1SXVkAdP/wFNF07vUQjeo/LMQfW7OYT5fmh5tvnV5wGBN9jq/6P5ZjGaEgSDEyiLY1ecZhnOWzCWCW8J2ttQCDR4qvYsvD9mka948xV2P5d5CjKrnf/rbeUzhO9r3qBsaIHHDcp48gf5s2gK+D7Te0nXtl0Kw/1cfsX3D0DnJ5iBCAMsALWypOhXgcvTr5omoOCX6z96/buvl5CAFF7VgwfCsorCMPBcPwNaLSH8GtVy8R+I1ZikfvInq5YQAI8B/sDHQFXwNZav3zD37elX1f9E+DbSLCTPcW8AFdo+GQA9wkXBJVmW4AH1+reBGtj56ckEmFHU/WK7B2oEWPp2M2zDZki7tF/w8M2vYQ3A9+Py/WbpcjecalAWwFkg+esBePdZLktCFGBgAToAxADVU6QlaODAKe9OeDJ0iyVXAba+T5hvHJ+33w0KnzW2dJ6vhIshC83SzFcRUB3cmb+HCOtHaQL4FcuKp9y/z7Rv0hbeC0x2AOqAxK9P37r+61vjfpsMVl/5fvqHHcvP/96m5tmKT39OgE+rpO/r7hMEvbXPr93zFdQ/9KZr99ZJPz4L/uOz4P/E6M3GT6t/T5k/sXgvhk+rzSv8Ci+PlPdkev8A25mPtPMRW55+Lo3wD8wE4qsCZNMSqRm07m8N7usS0OXiFsAOWPzW8LqlT46gNT8RHrj9c/l9di/VBRpIGS/Z2FXfVf2z04NMf4vSt0YEHpU9kB0sk18cLhusZy104cuncsjzDy8AEsMfbqyW9lIsSdstGzBQHgDm+jR8Xj0xYOqXn3/ei+rPH27+umJDgDd5931ivTeFpSl+l/9vZgFzfCDhwyoAzuiWJgbMWoQvteN2IBlBHi7q93O96Pu2B1umtoXgywjgtxr/UR8WPFy1i8MWsU8suw1BvJSxC7z2FPZfq5Op8qBAi2q54S4IWoAmD9zGO0DN7Q/FPrvFl7du8QO5S4v5vqEskp+5+mEVvsavT5E/5PttQv1HpmcwOix8gurT0kU/vGMW+Aa7ig+rbxsE4MT3LdtzQ10OYDf867I5WaL6JFl+ABrw9Y3o238reOHLX3+k1xPYvizJ9pYyf6+dtgAWAPQlpn/XL4HOQG4w+OG79f9QtR8RGCE+wvhHBHud8m76gWuADk8sBh1tMecPP/2hbfXcVy3aAuv6t/8G+P0FJLG7xPU9jd8Hc7AcQNfHbhlXIFDbQCC4fqtC8Oy/H9nfCbrEBRMkoPCDiPSinRtFm02IewgWRb6Lw9EWd7fb3fIPukVDjNh4OIpEJOwSZIDCkecF+NbD8B3g91a8X5YhLF2UwMltBJMkEmEbBA6CMEKwINgRO8LHtwjskp6Lezjpen+QZqAO3i17s2Rx27fdw+KBdwN/f/EIDKwUsW5PvX0YiNx4BLL1ZvqybonQ6TIq7w05eJxx4nStU9Hqr7SQzvF103cXir9mpi6pzmkOL/ytoByCO8BM1GWQT1yFc70/ea61jdz5eKQlXJ2v6joiSku7PSBVaDfn6ZTKp9psedPzJG5zrm3pnOsycRtoBYIOHTTxRZBnsnzs8qpoLpJdWYMu5cK+W4Ppf5RnW5/rIMYMqrOvmX1Kb7Fdk/3JG+SR56E1WeXY2r0/MjJIC+MU353mbjOV2V9l6SRktk12Ep7bm8z3aiYd9vxEsrlza1sl8a9akQ97ou39xJT8ZnOqL3vbFM6+0RoYT5/d+mSfca7ULjx5KXYIdyPxmt05ogg9HkGheNg2uluxrZDETofuIb+Gzg5rK90VlnXidj474qbw+Ea8+nGh9nypUQ9IrsZB3SpMpzisJGEnh0VOj80omJHMdgKlxxYkJ1I5IYF66Zy6OxazH54VezrtefikUn5JG403AV1t+jCFjSur6hjfmHk3DbvGxcO0xy9qPz8u5KPq1KzW6mY/+6YBswd5d4H3iSMnp/4qxlKZJdtWRU445QQXF7r5GuqyWBZmsdTP9NXHBpVI/FsIh1tY3/UPd6rPt1LjuY05l/uYuNkWDe8EZt97e4NLcmqT24Y3VzIyjdPNoqDZvbuaqpz9i1OVRMXcbVa8BlPtN1LmRnKN3fucxfEUMo6RP9lnjt+fbTTXHItQai03Tu6YGeK0n/eO6wkSPKWHI4mRHK56aodlqnU9s3VTXtNOZgWYF/j9Duw/yt1lT7MmRKs13k2RysixzQrIhrm4HdUeYQ1jztugP3eGbFq6AneT1bLu/doXgc03DL3d+1u82dKnK0Sbu1jbXbXqagy+LN732np/v3DsZGwpLOkQkb7CJ5zu0DuSNFF6sW08vHQEc8tSV7jiu4Nxe5g33OC2JH4kw10TbgPFWOODZCEHvj6zXZS66x0N4TeILR67K/ZgoW6NWAR0uNc2GuM6r7a0RDLZXZ4CxaV3V4bpiz1tjWtFlyF5/+iyTO7tOGCYMUpl4N/1vbrg2ON0li7c4cKrhTS2FzVHjO31fMXIARYtqW2NyTGkusjN2yQ3yBjsjzE9iBg1kklgUNymGdgjO1raeHATPhTcTcprkxbuI203D6Pv+FFoKKQY8QamQ5MrI1KjuUIublmYwr01rI6j32jSBZbmC9mWJ/tRpMEo5IMS+B5xrT0LZtVzdApNVCfNs1nftxo/bABzXL6JW6dKbHdz07Q0fSTMwfUZWUi3jWpaDk2BqrXQpnCmicw27cnJbjPjVp0sHbf6CavPTVZNmddtp1OHKLN+o0Z2ZumjYRG+gHvdVOTWo54F3CAbM8zaRlB4AfNNDT3LEupQxuY+cs0NTu8O4hFjYo+3wnXSo7Vbk+0ub26TO9+4Q2/W2HWd3ae+y7l7mdzh/HicIiYlbkjtUmedQRm0fPTxHoauYsj7SR8LPXubdaTYIIdsZ9eJjp3KRDrdFF3jYB4F0COZeJVK4b632wTRIjo6uJR3krQDRz3Ind1f2w4dyuloTPXRO/u+EkOPsr5MqEQY/ZU/xoc7o1iDxAxRxT0a3ke9dEuQ1ZqMcIGCt8SlpGlfn9dYbA1EjraI9mDRe3pyd7dDn93CSZ3TQ87qm8rgjxtDjHfwujSwBK2gtcEdDmTo0Nwk9+EM67xjJMoYOzoTz6igF1rJGXed2ET3aI8yrJgYXEeLDCI5QhzPhLvXj0lFTKIdG7F2JmtnQ5z2dE8J4kmoUn7iee9EUYbUOMEVYs69Wp0uFbg986i7e5gpYaOsN2CX+xjOnSuLUSUDx27Cjpe3Nifxw/UoXmE4VwjYVCQ+8zljv11DeptN1/uDnwyZqe0SYYJ0GgJDMhobktIcObuHYwUZhiebBhAEETx3UPrNVqYCxU/jDR8c7mULrx/Q7nBv2e1uX15gB2muuXRJNCIMPTFN4f14bGbJ3QnaTOantJGLiJ8FJ9jEeYwi43pkAuuECD7VFl7KXvYKWjwapjjIMZugMyM8WmHvbmLrJjvKlO/lib0fTztMTeNZFnPmsO+Iq62VlxTSxquplNnIppWyv+CWwIWnEWfObkuS6m2DWGWbxWPTcXmsi4f5JuYX76LNcupbmkGEM1JrLVphBJUZxf52qJRZzbAjdp8K4cSZiHBRTI7TukjlPKyZexKp+aDkHjkjKLF6FIejexooPSDZsxLAdyxIlWFPc9blsctIUnDiXX1sHo9MoUsKcxsC1wT+wntntYSkisaOTSwdkatBJvY+3xtNbEbcrHR1I3Sy37MQdJK1XSVISVy0Ct4a/C2kLM5IGSGrNjCZaRABXbp4zzTFfDyrdobM9OkS65fwMLpnXt9xVdHBKN0TquCos+kfOIw6drtWZjrLmDxG3JcPTudk7ARoXKe723jJ+H4yMNRZlY6YRXMFWp9rZj61Y04pTGt2XquVxwJO1sy6tG8Gp+SzF2j3fTqLJoGnwrUbZOcK5ban7QndRlQ6pYj9oyTaWsZQVXScBMuQgJeuW6tCNELNqVHJLHKzyU/SutbsFlU5ro946iRzspvxnuCpQs9YrnnexwmAYvl0Q82NmeQ7qk9c05Kr3RkDm2M1OVQwFTfhAboGyD72nJZMT1pCeHTpBMm+dDYmUtkKsX7ISk8emj1tPCrMuYR9utaTY7nj/Nt1uFvhvp0kqzmQNZ2WFW36d3Qz+YNYY8F2J1+NTgj8430LC7vBPa5HCnbrDV9nMm+aewkfK665nqgoakAlmY9eEMiUiZXRqGgfr9Nh3HS7O0ENLjO74D7FgpGbm0ypMlSCw8RpG+hOvd3Yxn6uhbSBH9wFeWQ7VqAsJ3F4VtpWvZM5yiPLhRTS0bgKVI/e+H2zn8p16z9g2URp81G3WuFc+RPhs0JOVfH5lNuHrQHxHJ7cvVi1+oDDnB7zsHoNQVt4njsNsSqpgUP3bEyktA2jemjgUYYjioh8Nc8tmvFxSlWNW973pHmcQbc+CP6JKLV8HieTy2h9IK+0xMWeYTp7134wvljgJ7Z6zJw0WLRnhNcZ2c3wpXwo0+QWQoIQKE0zNd1dRa5oXN1rKOpwlMeA50APQIzT1XaOUik3mSKpdyUbLCbSdAqj63q/HQDz7dWUb65EtL4H9Udjvjc6l81OqqC2OKHQvcpppZToQ0fcxNTKbetxhx7rnaveoy7kBgdgrzPWGSrgiYkaeD0SnF9H6xMY2XEpFyWqkdXbEWf9k7+mr72q6fRxbDJROiW79oj4dwvehQfxTiLr4SaRB/4CdWEG6YlFtObaCJWz5tHni9zJ1xaGtXC2LaEt8Oxh+M253mUI6YUtdARzyd1ng3aje6KZnXJylhtnyFklu/G4n0+Y5EiGyLp47uAhV2bO3qnBtt29VTK/dyqK4UdJeMS0c8C7RvInCcYZYX+NCOMy04ONPJxbZbcnsbjVUOKTU3jlnEHUb+ptjU3HpJWgw02MUEO54Y88MDwRFZuUN9vg7IcXhb/7BHK4qrSFTQZ5sEmB6TDWVCnJmqeNEWy3lmw0m/wmys6Bu5y7RNqM+8Q9Qq496vkx750GjLWJPMX5I+V1JtkE8pkzK9YZ3N53m3bYd7DNtzV6VQPlhoJ6JNdbpMQ8JNTKaR8hrYkQQOIousxhvYex+bgnLmaolDlrs/HOP7WisW+I1hrlIyP0Z+MwzteUPWLYIRcSe3MknIuen89nXIG9OymOTV9EKG35k3G9kJRFR57OBy01J9jsX/etub+bthfBcy4nkeYpXoSnzca1nQu2S27UvkcFo6A3wgywyEABbBIhZ3cpXh23XH9nTHlTSskRQ+/kSJLc9nHq8lSyNzu2xM3LQc+1ixqhQi+BoWjjaVkAR/VE02p+ak41r498e5Ll9UDtARcn0ChfJK8HR1nj8xjG9CicLwCvE2eMSSISdIAre1PECpcaMNMSHhu7PKfYYcsmdaurXKiFZI61J9SFKcyjHr5i3Wbqjp6zOs/DnFTLce1saHdIFDBNsVO7BtHf8Qc/7wzyqPC8q+6CLXds/a630T1ubi++mSF3o3QpLa3QBkwh0LZnmexUh5gYcmsRwNVDWzOc/ZiDrFwjE6NcApk3RLiF6judKtrMQ6WfdcBxcpFtcKY2T1Pvr2cPraEjZ2DoLT1LVHYWJMYyrzihHuvzcLk3yUxvpKlx7cYWE2XIVUYoh3pyZkeYNHE+GKdk3iH2RQkpe3Qf1GO/Va7sTfUOaxfbPVS1Pp/JNUWrfGrMjmF2zgUCW/Ujh+xPkpUdGm5IzTJBruxW0k1luF2c/E6U3mH3oNlg4gor2vRW8eDbAYqI0MIiQbmA3jsKsTSoCOs45xOma0d7EMoNq4/0BdZauATA7tkPduLuSAqV6LXos+1dN/QgCCb84lwM9dI6unltUVtqrfB8EYa7WqxndR/JTQoXAeelCMqD1kv0rd4nPIxiItna6AA5Ft0LUW9lF2yPSywLCQU0EDeIj5hwps5XC7ioPoCtTcQgMNj4RTmwtfbxHQGj5TRoASRiOR6sJ3Kv2PDaK7tu0zvXSPaujKK0QrdVEXyz3UzxWrgP/V7myCFECQwT6/a+fYgoJEZb/myeMKRBofUFmtBjs5dQ91qGZdanm0udcI6MSUFjbpMGl4qpofydkXmw4UXy2ugbtGdbki9wGKNjxj1rmshFI+zHwCEQuZ0nC2pVY30492JaX3dbxJYfSX3BtgQ7gb1ttXGY3am5B7kuhg62AbOSnqGiOO8OhFIMPU9uOFwvyLUZh0fJrFQoDMDEgRPBpOV9FPcQJhSokqlFRBOmxmO2Kd8Pk3reWVBTDETvuSS+2ySnC3u5IxZ7JJDa91tjXfZRXZOujmL+4CtJqu7p4rgvy3HH93dUOgfisN6nQOQZ6cgxa6obfJ6djuwCAYEP2u7SJHhpn9mKvT56QhJ7KEzsqNLyA6uM3GOzxTuU93YWCPshpW99Kpm5mZnOJE6zA9WeTjc6cWLYo4p59eSF64ERKFe/Ces2dRtT59S58gRbi8Gsd5RafNSqOdhpp1xxchYhs0PJoqDZFaR0TgqTRbdnCK3gpZ0NUKtMFs/v0vVw1yMERL9KtJDdCoWMHvZjNOospA+NxUJtdrgCOON9xNslF98/5SgYCG6bztFvw9hN/CNMssuhGqQ4JHy0bEH6BQiLdIJqjO3DbdTJt67lvVgPsXLVvU07J8yo1lg1D3p8UEGX3QloyG3sSzwifHpdK6ZO5kG6PlsVX9y6AJHY+vbQe00YRl27VtJj6vkiNEMXtfLujFV+Uk+WMeIiP29Yb7NFCiXTjjSGHsMbgp23YkexswGRLN+Et6RLsINyE0/RlSfNRttwgZWsY9srqIOqo4FoSl0kkO4aV4pWKgv07uI+TpA5kxFkI0RbGOr9YWvU18IpTAjdZtJDxEdCIkcORwdjXYEe5eh43xOeAIN9TDdMeE9MlYK5F1cu0r69w4PuFrpnonaW8BC1TdNipG8PzSw1ZfPITEI5N5BzM0b2Uo7sudht12FHupKPILhPith+T8z547QGEO7RgmzlnJ0dTkWjEROqElhAywcTJeduvaG5nbcWGWymgtCeTQXjjauI6FGy5hhsOHAI79xHutZoA8d2DEtt5nqvPtRbSMDyLEtJoG13nEGTcuQEAs4c6OsQZkNmI3d1+whov2cMBDSBIrmp5Rq2HzzqRxECcwi1vimxpc0WI+c9pZVBTJONA3kcctjANRdei8k9ReX0wC444m3Brv6C2yexGuHbFcnX58gVO96UCvRcmdtHi4BdANK7m/76yG/hWSi9qZj73TYCfdTOO9UhWVHLLhPhnc9g5/ZQbn4AMaNOhyWSPawbWjK4kbX3sFJOd966CJM+X3kntPY4w+4Cj74LUHymYfrebmKV8HfWkVJ7Fi7pkNhSFcAZGbKTTBsIWJOYkPLuoij7FEKhuzq1b2dyY7XhlrwYh5wtcmqym7yDxmaThf6wC3P1IERwc0Vcz6CufO3ExBHtOn9HZT219mHQy0lli0BwxtGQldmoh2yp61nZlCWDtl5QW41olv69h0x9hjv2GrFYlxdD+DA2OK4QJz0Du5kNb+wC6Vhvjv1N7bZ0fO2y6061zEEb1MiL+8Frkf3jSKpIeTqc8+026G4srexy8zzFQpqoIChwaXUFuzXxQzkw5wnRj0dyL+jmeT0Je1rvAq7it3M5oJTOgolBfESePKDew6Yfwq3ck8X6kOYjGWD1rWyHfHM/sjtO78fzkdRvoLTjsNvJB4JI7/Udg2/3AA0OV/uKDq2XbEnNJ8AEccghMr3dK4+Ud9ogwn0lRnSMio/9UbQsGt+42zusNpe0EXI3xbsOgk80Gm14qRTgcMQgF1GDHq82VL/TyMHd5t6guSgcaWq4M++PSJNHTbxp1FYLASJqCd6YI9EihbkJoXY4I724A23ZOk5jvjsJiXSi2Ma+bXXXkYeYiQHEno8lYl0CsR0xWdFvF78/qzfKD0ZlfRoF76iZNFbpYk2cWIzea487mt0GLoW8irSCApn4YbOF2gsxiomxTQHICOUZn5QdyprhSTfjoL1rBMnquFwc15J/ULeyZfAW27FEKVW6tr67E3GOoB2K9TqF7oWHftj0SmTwBfaw9iwtY48dLIr2ncEmUphO7tit4Qg0dWiU0uhydJmMoyjqL395+fDyx1HYyz9/B2s5mvl/dkL0dpjz9XWL56Fe6AafnrI+/Qsd/vrhpfVToMHbOVeXD/H7IdHfnXJ9/IeDuWX5/Pbi0tcz37dz496Nl3d0X9IyGLq+nb90Vf58nQJQeEO3vOTXLe+B+uD7+3PHp4Tl4BFw/9JXX57vmH0lTMvlJYkwSN0+fL+M30/5PrwE76/vfEEJ/EvY1otZ76fzwBr0FX5FX/72fwD+T5n5Vy0AAA== -->
