---
name: "rar-cowork-cookbook-audit-develop-continuous-improvement-initiatives"
description: "Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_continuous_improvement_initiatives", "rar_sha256": "a11ad47949311a6b9ab0e19cb8f46acae1b0f27cb41ed3f5a99f9735fe53d3e7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Completeness Audit — Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 a11ad47949311a6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 audit_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 audit_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Completeness Audit — Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_continuous_improvement_initiatives',
    "version": '3.0.2',
    "display_name": 'Develop continuous improvement initiatives Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9e415524c5fbd71',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop continuous improvement initiatives records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop continuous improvement initiatives. Output an Excel workbook 'audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop continuous improvement initiatives data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop continuous improvement initiatives records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s', 'example_request': 'Audit continuous improvement initiative records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants continuous improvement initiative records in D365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopContinuousImprovementInitiatives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContinuousImprovementInitiatives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVpbnV9G8jhinW5kPEBJLVlTEIAQCsQgkFgmnI82+7yAEbn/3uUgvF1dldY975q+Rwylxl7Of3zn3XX5/sfsuKpuXjy9n3y4WezvL4shvFnbhLehyKJsUfJWpA/5fuGXRNbHTd2XTvrx/8fzWbeKqi8sCbD/1RbuwF41vex/KIhvB6rzK/M4v/LZ9kKvKLHbHhd17cbcogwe5uOjLvl3EedWUNz/3i24RF3EX21188wExt2w8MF0sdmNh57HbLlBss2D/55mWFkEJxFyEYGGxyPzQzhZge9yN78G+rm+KuAgB3wVzd/1sMWvyUGKIu2hRFv6ijXy/W1RA1yAuvHmxa3d+WDbjosr6WZdzn+c2eJyV9e/2rE778vGXX9+/AHmzl4+/v7iZ3YKhF2rWaeff/Kys6K9q8d+04r8qNRPL7CIEu6oRmL4Az0AIoEwOhjw/WLw9vWv9LHi/+Pd/Twe7CdufP34qFm+fTy/zf8Diiy7yF11pt53vAfEr24kzYIHXBZUN9ti+GWLWpQWeK8LX585vlMpq8fd57t2TyWvod+8+vZRABHv266eXnxfAyp9emn7+/TpTqd79/JqVg9+8+/kbnbZ3Et/tZmJA6tfPb89vZMHCb0vjYPH5rDD0Gy/g47jyAfHv9Js/T9HfyL2Z5PNz8buyer/4MeVZn78DeZ+x6QC6PyYLbAB2vrwmZVy8e+Mx+6qwC9d/9/O/IutGvptmcdv9H9H95Uk4AikBrPVmkp/fP9z362L5pttXmv+abQUC5q9oApZ/YffVUP+K9sOz/0A6i0HSfvXlD8n9aMPy74tf/qVu/9mG94vg08vOz0B6NLaT+R8Xvz9C5JefvG+DP/36ByD9X5I5l33jPih8zu0iDvy2+/z5l5/ax/BPv/7yU1+BKPbt/HPfZD+i+SO7Pvj8yYJvq979eS/grxdpUQ7F4msOLX4vq//R/PG6MOws9r6Ntx8X32fi/FkuZiW+MH2a4LtsbIGs39nx55c/ABIVQJvefUwD/Pi3f1tIsduUbRl0i7Nb9t0COLiLc38WXotiAKbtAzUagFZNGwPDvq0D8T97eJYYgPNv/8t9oP8H9w39oQduf/aeIPf5G3h//g68P38D7/a314UG+JRNHMYFAOcTpSifCjt8YHwL2Pmt39wAbjlj538A6f1h/jFj/W9/ldXnB9XXavztUWjiJy6eaH7GxLbP/NdZezMCheKpqwvqgn/33R4wzEoXSBfEANznytGWGag83WypNo2zbOHFAHW6uSzMtIE1P87EfvvtN8duo0/FE8TRxbMWthBY8FWcxYcPQM0gi8Oo+1T4blQufvr9j58W/7H4z3Y9iM88FFBc3nwFJDycj/IC5F4/az/XRAD6tvfw1e9/vBkbkClAQQOejYPYf24GsZv63hfLnznqw2qDLRwfWNyfC2/ZdHPxi7vXBR8svsoLmM5Tc+2IyrZbeH7lF55fgAreRTZQ56sli7JbtMARbQBKb9/6D66/OY39EDEHIGB3vy0kWgGVqszAP7OYj0Vgc1nEwPxf4+I5Dog0P7WL7RcSrwt5jtZFZTd2FTX2G4/Afvpl7gPetgPi9qLwh0/FXKIfgfJInad5wCJgGffNpR9mn89tCsCJZ5PRfVljz/VUe9TV5lPRvqWF3TxbEiDKuAj72JuLxd/eQqqNyj7zHvYDks6U3rzgvXnlEYNvPcJ/3fu0oO36rn96NBiLT/0KRtaL/59brdlI1H5/YvaUxuwWjKydrk/nzTrMQj8bVsD8IdUjUb91Pl/Q7QvIfyqyGERiM/7tufLh8rc1T+DsG+ChE3V60AfxNgsJ6D7SYQ7vppkTyf5UfKkm74G4D+gEEQGwA+TWHNJfGM6zXySNAEDMz986izczzz4CIb+oegf4aRH4vufYbgqkmn36xc3FbDrgvCGK3ehPWs3WB8YC9IF5gajgayhevyL8c/aL6H/a+Gyg5i2P5rIHGd08CAA5/FnAOXpmvwHxumezD/T8+CAC1MirbtbdATEDNH0O+o1f93EbdzN+Pu3qVwDLP8zfT03nUf9egTQCxgLJUvXAuo/0mmMhB+0RkAEgDMi2HMQkGHa/GOFB0M5nrABY/NbPPik+ht8U8h85Ode5LxtnReY9c+uwCIDoYGT8HlK0H4UJoJfPKx58/zHSvnKbac+w2gJoBBy/zD57jNdnm/DsQxZf6H78p9PUu7924HoUfv3PAfBxEXVd1X6EoGex/lKrXwEgQE9Z22fd/vBWTD98Q4IP3yHBh++A5098nib4uPhrsv6JxFuufFwgr/ArPE+Jb7H29gGmoT9srx/W8+yn4uR/g2DAvsyBWLMjR9AofK2XX5aAohk2AJDA4mf9bOeyO4BK/ygYwCufiu+Df04+UI+KcA7WtvwOFB6NA0iEpxO/1jUwVXSAtze3oaH/Op/eZvFb/+Vj0WfZ+xcAlv5fPwLOpSyfA76dz5FgEUDHLvYfTw/8uHfzzz+fsY+PH3b2utj5AKuy9vugfCtAcwH+LneeOgNdXcDh/cIDlmrnggl0npnPeWe3IJBBDM+6dWM1K/M8Lc795bzh8wBQuxz+WZ4dmFw0szVntg8cTHovnCHABiZ9MPvbQj9LLEjuvJwH7Bl9c9BQAJuyVyAm/kO2jyLz+VlkfsB3rkzf16GZ8yPO3y/81/D1wfKHdL/20v9M1ARtykzHKz/OFfv9G96Bb3D+eb/4epQBRnw7XM4c/KIH5/Zf5mPU7NXHlvkH2AO+vm76+ucSx3/59UdyPUDx8xyJz3j6R+nkGexAMZh9+g9lFsgM+Hq9679p/1cz/sMKXmEf4M2H1fr1nrX3H1gOiPiAeVAsZ22/mfGbMuXjgDgrA5Tvnn/P+P0FxLg9u/0tyt9OGGA5QMUP7dw5QQAXAEPw/MxgMPd/ffZ4o9dGNuh1AUEbQWxvjZNrEgW/MIe0HdhHSNchgjVmu7aPOHCwwl1njfgeGmxskgxIHN0E/gb1UB8H9J648HluF+NZxllAYJoPAFr8b9NgyHtT7qnMbLmvR53ZCG86/v7iYGuwklu3PPX80BCJgEHcGUVu2WBBOQxbTo8Pd2fve7wi3gevnMj2QOE7I79Rqcms2T49rw4cEIVIDknhMpR/DYmrhacBe/E0Ta/seLOSKxfZMWHcY32DQZXhXaHCv0qaZ+dncetFWWbdzdxDBP8gX/Lzxa6V87k9VRfJHOOYNIQrNmkWVp5rsxYlUzyWZUMEPgSlKxfJ06qiYz0RLCvP79sxSgsYTlLzJHDmyG7OjU34I6zSuBQPfacX+7vWX4udfptWHgyxGEQsj+i6ybJ8uzXca85XTGOqsbRbgdKjSPWyjBNPMpDIvCmlWzOGZ7kOx7dhd2cNr0ltQ8j2fSZU+0aNp0QWxG1pT7oQ9ys+JetV21k3L+MheuDCexAElwDDmvbCIZgXs8FNqaYlxreKTeg4f7Cyi72aqLSdNFLHxJRpsnW7Ls1gbZjsUFiuUYmSdVD2MSVnhd9To1apXhiyCC1bxoHZBMXusNnbAcO7yT47Q75Bb112x+k85Tq5a4mGcdVarq7iRDzyvNvepF0r5L1Z4r454XqLQGcnslBBFtX4cIMlQrz7KmPEtXGG0yPD+vQBaYtKY6Jc9xrzOKBGo4wnhKZymDesIb4uG2RLSEq368ndTXRXrW2Um+l0kvW2GvljieiDp2zDWDTHvcWbAxBcN4ma7lpXusKDQuTNKtHoeyh0dRjUqUgakpddhGy89ueK6LP4iBkKGvOkcSAn1riqemZdfHUVBW2Umha3lCc+DlKVqUd41TISsSsKVGPufcntrYNkE2PKTch+YJVSk8OYY9N1BO1j4gIr1Fk8KgejGdqS5YdOZnJE1AVYblSKxUYbCeRzqmKxdxT1epiavRNkWeZFVD2yS0G6DZXoqTZ6OAXUCST5lTvn6+0UhA653rmMdvfXqhS1ZsDa+pXcEaWN3nMjuhgGfkzKDV1Ese1rawKCw8mMsHsHEwlnYPlx4wfHeA15riD268mH0oFI2OMlLPZifklaBeKDtQsHibmygvtOJAItS0j5RnCHoc6uvFHq6YrYnVfq1U0DbHUtmSuzte6XyuC8NAwNrKVV1d8RJ9MRFISglxBlj3dhFcXrLF0v2XqT9bGoiTuFI80UtxTD9ib6KktwrfsHw8y5imb4yujoKhpDkqbEhmSYsChvDWWitEBISCLZDm0vVV/bZF6JDdfVMkZHeRSawQvqGyKLpgC35SHhBLq48PRpyrflZox4M2HOyQmiCWbZusuklwatV9E2zJaGcarjc3vzRSUSQeatRrIZbMdVJBTGbxuhYRpFiZB4iCK2D6eDeOTWx8NKWNdSf422BsXGzBKz8mOtnGS7y0UenCvUVNuXUknbB7O4xxl7ioyt0zbLS8t4uyMQjF5SBHUwNtJxc3WTPheddNqnV6jOzYyud0JmE44fwTosQebUUzzaR2NKZxl+nnxTcntdjM/MMWXRpg/0tnfFs2qd7vUN0iSYXR5IGDUJwuDSu7ATeJCvEXmQx24AnHFIG9g1muxvIaLIrroqJcO6p0V0P2PUlb9U7H5tXUoaTray7CIcd9ZPlhQ3seXrDr66cFtIsXNc38oSw04ToXdW06J9cVdP90p1dAI0mNB0q+I7KFqnzmLVUL7RftMf6D4omalmXQS3Be12uFzRHbK0Ta6+uANvWUOEMtJR1dvb8QAOJCSsJpfWIvNQOPKyqdmlt5J5Ad/Hh3OxrBinYqzmGKxNEQhhUifp3FzajrZU/XpWeS+Jr0f6HlWOtd07qNeiHAgUdkAlPeJVze0qc1sP8rGIeeLAHLPNimKZXQ3ZpmxlImWsYzGjzQPlaicTDen0bOecGQyeowksi23V0xB5q5tEVFPmDaupN/B4W5myvCNhmSPp+nahSWsTn+O1lHIDJkYZA/vigW1dxlSxZX8ERTq4TdnmxNOVXuT7IN5FwakySkM5TFluO4paknJUHM4RbhEBVjAdN9yb/c6rhyhEmqV6QaflsdAO5JLRNr6IKb6SGCvrbKy1rijyzbrsaGF/pBIx3eUbf8ROOstxyUbjj9hwPrnNNSgiSUDJ65JCKYRZLtX0ts11xL3qg8P0unSkzdSAcSrPGOI01q4+Fua55IYTu031o60R10JhOqnOC1rJp2QnqAB0k1yt0yUK1XYhn1g5PQ2Tre+HpV9uxQkpDGu/3E7abpdbCj2JXZ1vFOWo5z2t0ptGdmC7gtjt2r3oNBzBAR9rkWiTkD5EW2GarJ2WnSLaplpzO0iseE4b/KY0pTps4o1YltaRahkhdK9ODqFOhzITI55P8brviw29tl2EsuxCOhw1gnNluxaLDOYt3wBn/MD1U/pomGnnCDdOGFKd7qj2EnrsfdvQrKK3Pl3sU/2c6aqGHNRVPm7qrYDxxNZnTKy2pvq2DnDTZPXtxVIVSYhtiBK4kS4Sfk361HQU5PP+7EV5t9utMRCil8xV+TYwrG22Sddtt6vOh5GlQZlVnPoquxcU0SpQYJ1t4Oyp0lWjpN6RTRQFApueHBbAzN5C8gnWdGraBlOOlDE7rr0yXaaWv5NQ/56osInYkkyvbnl6oTXN3w3qlrGm+8VYL7GJo4edz1mNAPARbeCwWkugZIl7X+7Yzjz4lWc0k8KsDY8NtVoQzIzFaUfKE8qobZ3fH2Fu0JPLhle9Qy7sZOa6lz1Mri4EfBfck8Bo5RVaZsU13JJxu6quKFdVW69YqbHX6xe63txE/FAecRi7hgznF3HULVciS/BpoiapoxikhfXR2RwT6KraFUbphYhA3mXqMZ/zIRCuzra4dLqF73zN5S8ubsugtsKDt6tkhmoJg2bF3VZpYN3laysvdn7EntiSR+rQKEF7VbVSgVNLm66bPhIpKnICdaRPcD820TkiHVTLhIA86TepPl0bVtp099Pob6NQbNWWjkICNltNMjajmpz8wllfjvkhxJZnmLmi0KWXGEQKwuowAD/JXW5fHcqItqV6NjODMs6QzG1OiR0SQesxaNlfNbzqJ4iDl2MrOKFZ1XognE6jx3L+rSPrdC3ACr8JJD7Lpv022PAKsb1lA4mc1RELoFvu6naiZGdkODMpdT7C9rixtEYKGf66Eg/YZmLhqthmBZ+4abwPFdVr8ELIwvyWJCdYFjtaZX3EDvuUP9tZpfcXdeeoBQUzp30WHNgTbzVUrje15xZjGZ83kkzAvBjRqzbubTHV5OhQm6Aw4nG1rGvJID093Wv7kz9ayyN3w/el6Fr8geR00EPpVX1xpiXh5skdJ4shG1Y5qu0zKV+jbG3bnCIUapI16JDX6eUghRuePZ1SW+HxOCkGUa6iahnuWT3c1KmcYbsBTvRloHDN2C/zpCKlAoVAGwcJk7YpjD7aVOomyM162a2ryUAqzcwmocq9TDt5QJqoi44hnWvInhLPJcr7uH5IlwJC62hxrGJBl/szYWWjzcRGWjAjC+eaS8ZDrYaVma+KQ3PcwnoVp0teGAonIFhEzbJT3Yurw/EMJztIE7CzMfawl7b3Tj1ty3VAiJyb59pejJBSO+D9RZexMRCHkfMGjVq6mKG7ATkIZaTXqFFw2XhX0aBrci3Ql5Kuayi+Ea1TpCc7O7htrZg94E5/3ZDBoeARcBTgSGYZJ9H+TsMQQ9X1hmGwpLE1H4nEUZOy1fWM3M/9btTDXDzgF0/XFWcvI1lB69imX7VUpNxAsQpycRxRuHWCGnZ2S0hLqltL+vJakAjmSmvtQV+Par3S772SZY2nqC5xcVB1XdcxdD+67V65qveTYMRGvFNVzDNEwszc6/nCbC+mj4mw6slFUfItfoubKhT2F4TenoUVsZ/MTqajwhqoQyl0B6SDtK2+Jgfxajm4YpjlKTyu77yk03dyk6/5c9CSeq17k813SsoajKSbSxYKQrJ0PJOiWWqJcBCxC06nNXqt9MRg9ZojykNR2I2Yc5tkFWOmJVs837TQlGP0SdjoFS3IIBtyfWv5VI1oy2246lQExeW0wC9SDaCzjvaue3ToITpIJEoTRR+5MWHtw74ydVm+dbaFxv2xH0t7DTksnHjF1QWVYoURW3rwR1ofbcq/ryrbcnZYRRxzMmDGjEa39+bGBXi8Wp71ctS6A7ajqkbNSaOAQ9zZKp0qV/Hgrcrgah+6rr1ZR4Wc8ChamX2R3GgFWhKSFeeRRa1zYXkG/X7UXto0xq8YcrsXQz9xko2lx+Ue2qYnYzTJIN2SvlYnIZuUkLb3YE64XSoh1VnkMGSh0q7wM7eWp+raY0EYrc6Q1RK93if6mvd9Ijsv0dpyBrrZBQZVKvLK3tgSt6cGsrxJrHAhfV5b72115C+nlt6sj3ngH4r1TeMoRy9IRp6UK04gwEX7ZJO4uOhA1t7blAg4vODqpBDw9igjbq4ZN5qTfRHVWakiuIxAs9YhIQazjmvFEiMVCt1duEH0euMEJwsH1mnlfQ7h1cT3fcBtlqsLscQlpGEbCxOnJukVAfExld2vkuZsk6R2LAWlTsRLrwUWx9CHy8k2FFKeMG8kGcibkHa/IjF2LfurGj8pa2tANWVVwfUyvp21ELpXOYg1qFC2jHqYTHcKk1hDbeZ87YCe3EqKna23YxG+ul3y89SGwXnqSVVcknrejEtLTmDOWZetUm/bjTehXH7JJwJa2wPsJbe7EXbCEeUJeX3dNmYAQc4FYoOGNc8pXDQFRJygDTLYhUDbuhxcpCw2tCrKwGks8qpzHW02VjzVe56I9hf0VA0QIbq3BD72cNOkeIiEQnWFYfcE7U4jtamKXeibx4A85Mq9RirCEJXiuKpMWnahi6P6XiIwq1voniMdJ7oBT3bc0aKu8IpYgwSHQkQczcbPj0Q2Bqm0T2O3tAP8gmEYTh6HVKtu0x4PRQ3v7ntNPJEWnRJ2Rd2KdT/1HgknruySq4482lPTROVKUYqy4063/iytsDwwJhLb47iEOQ5PH/itYPHcDofu9wy1sGB/zOnI75yLyWMj4xdEKkCOdOq8/QjJZOlXwJrmHm13VgJ6b7Qk/Y3mXe+xtFNIe7LIjQsxtitOcNQ0TGJUfMya6Zkg9lvMh6p2Z9f0oNOKebxeiimJVx1dlFbf7AlF4gzG5y2cX0nCjqVOq/aUWIRypQ2yhjf8ujug5CDnu13lgPQ5EFGnTTfyrHAJslnf+iWUHrZByaUNRWouOHZNpUJjI2d2Qnk8Wgk4DHG+fLrkKKqXObnHTJmWFMgDLY82EEvECSwxwY4bd5IMxD6q7jHG8hPaTL3Z69PVzBXvbkU7+ibn4USup3y5vGK2dEv7xLhhwoGJkzgZiTXlrtM9Tly960U3fI7QV1a+JvkNSmLFxt2jpr2/o2fKyW8SBsM+JtWHIuS2PWJ62MEqfBi1rnE0cgV/CHbwpRDhQ39RTKunNjsOPeVYhjeOdB4p0B5BmXSpapoZuRDq3cOJ1B3kwEMXC9ltsci8XSn4jnsjI+3JpYM0uHdc9Xl/8SenQopm2QtJgZYbqNP6DVjHu5XVO+JNv8EBZ1HKqVwej5TTQo1KnrLk5jh+PnT+ut84iO/Qfb1d8vJqucEE4rxeio5ViRmGsRdpdxMEh9rfKFggUMTp3Wvl+TUZy3uK9F1pOV6T7IQnNVFMBYpOIYqEUyJcys3GPwgoLam5cL3xfnUA6iQ3KxtwmrGzG55ZJI6BQCAU9h5uMULMwfFRjGNwUBouuOqEa3JSjfjGcClz4AqDYPfbJj3zvmztNzBiwIZ2xmy0ZJJdrUIDdpi6pSC6ndzxzaP04PTGZpO2yS3Z2VvKpmxWQm/4UFdaLUV6qJQ7YcIYhwvlCPg2gXRluTq0wa0688SYIW4JBUkuTkbuwY5j9M6FXJpSx6OeFaQ7xyYoIZDNGN2ilUBnPocmq8w2pc0VNbp6JRm3BqJ15JynVsMxynCfrIzwciRq0ry9r1HRHSQxuVhkLekA3JS4t7A7Uo/I4X6xpltSWaf9Lh2PagRxwMXbBmcpb+cId2u3bFsGZnaiiojDJa5BZkfexWw0XvSQ0jZZgpr8o6+uo6XVb3ZMsyehGqWSEukkUvdtZirO5U6Dds3K2owigvcqtQJwLUyKre/KSGLQI0WyeB4yZLnXkmLHBbdgWZD5dR1iR2DqXZPIdux28LomG6cTO32DihXZ2xe0bIZBp2xF3DRZn3ppN2KVhit96YWoR89/sVZLS7vthhI78eaN2cBKAtr45frilJvOFlfKRFUsipZHE3FA6mvQ1klbdV+VHG1J1h7B84sLLx0Ml4pevkR77qxEDNv3p+X2LO58/rRfV+QRpQfqiJ5KAh2DZtUieODy03grpIggkWMxytamnpruhmxvp10pyZ2kqWRcuiyideZSrIVl4cTnJZl6uFcZqImxA3qDWagR2oN3uw2FC5uRGkB2KN8u+0t5UbYhit+lYfJPpw63RBHh66Sq885JjsSNqEuxhcbz+ei1UGStVu0asadTT+ODtyE6VEBde3VbHe2rsS6gnLeRwZT2sYJiCNoO02EYjQZGi2WOoYeLm92uSrzW9WUSb3f3FJxjKgp1G+6ooyp7otkKu/JEpbRxulbwDNX7YN9v1dY68huct6BDuUcoLN2dhmClESGjYqZTXAqBc2XGvwX43tndaDyoUOh6Q0p5uws4RellqcNrY3MUClftszDxfDwj2E4IpCVjbpbC2szjfVaoLHzc+QHuuShJABg/oYOd7rqBrX2oL+2lfZDv+/C0t4P7pcQk7qJL1+VkpbLQLhFijXO3Abpgh3O+2e4oivr7y/uXb5dsL//tF83mG5//Z5dLzzuiL++IPG4Tfdv7+OD18b8v4q/vXxo3BgI+L9jarA/frqb+4Xrtw1+9MJypjc93u75cVT/vwjs7nN+QfokLr2+7ZvzcltnjDRKww+nb+S3Kdn7R1gXf31+XPgSYXVM2vmu33eeu/Px2hRoX81shvgdY+2+P4dvd4/sX7+1Vpc8otvnsN9Ws89v7BkBV9BV+Xb388b8BTDp/+uQuAAA= -->
