---
name: "rar-cowork-cookbook-audit-analyze-sales-data"
description: "Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sales_data", "rar_sha256": "e196e36e84f532a660059d44f560769e87864970e8009b1784f2cfb8934b5aeb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_sales_data`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_sales_data_agent.py` and in the RCI capsule.

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

Analyze sales data Completeness Audit — Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 e196e36e84f532a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sales_data_agent.py` first:

```bash
python3 audit_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_sales_data_agent.py   # or on stdin
python3 audit_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Completeness Audit — Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_sales_data',
    "version": '3.0.2',
    "display_name": 'Analyze sales data Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d89116c061e5308',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze sales data records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze sales data. Output an Excel workbook 'audit-analyze-sales-data-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze sales data data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze sales data records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit sales data completeness in USMF for FY2017 and give me the audit Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants sales data records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeSalesData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeSalesData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOb2JLmX9G8HTFV1bINYscdN2KEWMSijVVQvuFiFSA2sUP1/e9zkF67qm5X9RIxn0YOWwLOyT2fzPTh1ze3a+Oyfvv8poVusRLcLEvisF65RbDalUNZ38FXeffA35VfFm2deF1b1s3bh7cgbPw6qdqkLMB2tSualbuqQzf4WBbZBFbnVRa2YRE2zZNcVWaJP63cLkjaVRmtGjcLm1Xgtssuv6yDZpUUK3Yq3DzxmxVK4Cv+f2u7wyoqgTyrW9KHxSoLb262Cos2aacPYF/b1UVS3ACDFTf6YbZaRH5KOyRtDLY1cRi2qwqoFCVFsCz13Ta8lfW0qrJuEVnr8twFl6+VQDC/7Iq2+QRUDEd3UaJ5+/zz3z+8JeD32+df3/zMbcCtt+2iybZws2kOtUUZFugCdmVucQOPqwlYtgDXgDlQIQe3gjBavV/92IRZ9GH1r/96H9z61vz0+Uuxev98eVv+AIOu2jhctaXbtGEAxK5cL8mA3p9W22xwp+Zd/UWHBjimuH167fyNUlmt/rY8+/HF5NMtbH/88lYCEdzFbV/efloB2355q7vl96eFSvXjT5+ycgjrH3/6jU7TeWnotwsxIPWnr+/X72TBwt+WJtHqq3bmdu+8gGeTKgTEf6ff8nmJ/k7u3SRfX4t/LKsPqz+nvOjzNyDvK/Q8QPfPyQIbgJ1vn9IyKX5851GXIH7cwg9//OmvyPpx6N+zpGn/W3R/fhGOQcQDa72b5KcPT/f9fbV+1+07zb9mW4GA+Z9oApZ/Y/fdUH9F++nZfyKdJSAnv/vyT8n92Yb131Y//6Vu/9mGD6voyxsbZiCBa9fLws+rX58h8vMPwW83f/j7PwDp/5KMVna1/6TwNXeLJAqb9uvXn39onrd/+PvPP3QViOLQzb92dfZnNP/Mrk8+f7Dg+6of/7gX8DeKe1EOxep7Dq1+Lav/Vf/j08p0syT47X7zefX7TFw+69WixDemLxP8LhsbIOvv7PjT2z8A5BRAm85/Pgb48S//sjokfl02ZdSuNIBT7Qo4uE3ycBFejxMAoc0TNeoQ2LVJgGHf14H4Xzy8SAwg7pf/4z/B/aP/Du7QE5a/ui80+/rE5q8LNv/yaaUDemWd3BLwcKVuz+cvhXsDELzwquqwCese4JM3teFHkMYflx8Lkv/yVyS/Pnd/qqZfnnUheeGcuhMXjGu6LPy0aGPFAO5fsvsA3cMx9DtAOCt9IEWUAGIL/jdl1gOMXDRv7kmWrYIEoEi7wPtCG1jn80Lsl19+8dwm/lK8QBldvUpXA4EF38VZffwI1Imy5Ba3X4rQj8vVD7/+44fVv6/+s11P4guPM6gK77YHEkra6bgCudTlYNlS2QCIu8HT9r/+492ogEwBChPwVBIl4WsziMV7GHyzsLbffkRwYuWFwLLAqnlV1u1SxJL200qMVt/lBUyXR0stiMumXQVhFRZBWICC28YuUOe7JYuyBaW3TZoIFNCuCZ9cf/Fq9yliDpLabX9ZHXZnUHnKDPyziPlcBDaXRQLM/93/r/uASP1Ds2K+kfi0Oi7Rt6rc2q3i2n3nEbkvvyzV/H07IO6uinD4Uiy1NVxM9UyFl3nAImAZ/92lHxefL10FyPtXq9B+W+Mu9VF/1sn6S9G8h7lbh8/GAogyrW5dEizg/2/vIdXEZZcFT/sBSRdK714I3r3yjMH34v77VmX3+7bm2QGsvnQIvMFW//91QE8TCILKCVudY1fcUVftl2uWVnBx4at7BJI8RXym4W99yjcs+gbJX4osAXFWT//2Wvl06PuaF8x1NbC/ulWf9EE0LTIDus9gX4K3rpc0cb8U37D/A5D+CXTA3wAZQOYsAfuN4fL0m6QxSP/l+rc+4N3mi2dAQK+qzgPeWUVhGHiufwdSLZ785lwQ+eFimSFO/PgPWi2uALYD9FdAiASkIKgPn77j8evpN9H/sPHV7ixbnq1gB/K1fhIAcoSLgEvMLE4E4rWvzhvo+flJBKiRV+2iuwcyBmj6uhnW4aNLmqRd0PFl17ACiPxx+X5putwNxwokCTAWSIWqA9Z9Js8SGjloZoAMAD9ALuVJAYo7MMq7EZ4E3XxBAoC0793ni+Lz9rtC4TPjlqr0beOiyLJnKfSrCIgO7ky/Bwz9z8IE0MuXFU++/xxp37kttBfQbADwAY7fnr46gk+vov7qGlbf6H7+D6PNj/+z6edZpo0/BsDnVdy2VfMZgl6l9Vtl/QRgAHrJ2ryq7Mf3kvjxmf8fl/z/A72Xqp9X/zOZ/kDiPSc+rzaf4E/w8kh5j6n3DzDB7iNjf8SWp18KNfwNSAH7MgdBtThsAmX9e9X7tgSUvlsNUAgsflXBZimeA6jXT9gH1v9S/D7IlyQDVaW4LUHZlL9L/mf5BwH/ctb36gQeFS3gHSzN4S1cJrFnSjTh2+eiy7IPbwAhw/9kAlsqT75EcLPMayBXAPq1Sfi8egLC2C4//zjBnp4/3OzTig0B+GTN76PsvV4s9fJ3yfBSDijlAw4fFiQHOV4uQJstzJdEchsQmSAoFyXaqVqkfg1rS3u3bPg6AFQuh/8oD9AFcFjMtrB9AlvaBbclp4GqL2b/tjK0Aw+yNS9fdQRYNgf1HxiPt4GY5J+yfZaQr68S8id8f19/fl9tFgmeAfxhFX66fXqy/lP631va/0jcAt3FQicoPy+F9sM7kIFvMIZ8WH2fKIAx32e85xxedGB8/nmZZhbvPrcsP8Ae8PV90/f/lPDCt7//mVxPtPu6hN4rgP5ZuuOCYgDlF9/+UzEFMgO+QeeH79r/VSp/RGCE+AjjHxHs05g1459YCIjyxGlQ7RatfjPXb0KXz3lsERoo2b7+++DXNxDT7sLjParfG3qwHMDax2ZpbCCQ8IAhuH6lJnj232713/c1sQtaTrAx3NBEiBIhhUU4irgEAcM4HWDgioBJgg4pkiIwmoRDCoZpb0OCdYgfeRSNYh7uhh6g90rsr0vXliyyLIIAE3wE2BD+9hjcCt6VeAm9WOj7ZLEo+67Lr28egYGVe6wRt6/PDqI3HmSR3qRcoStMjY7N1Q/HKCW6P5Km5doxTFoXFcxMQuB5/MBYJpcmusAfimHA8Idwill6W5DSOUDnZrxcsMdUeHo1Do6gSNzsUIQ/0xR+gGyqRkN/2qckPxmy4La7WJENLNEDR+EepivLl3i82qYm9xC08dZyo93KWHXx+4kj9HDX7AJ8PFwqIfNVFfRal4oI5Cx3m9vsH3eqeMdQzZm4weLXJ09q10oG4VPUM55y3EaZedUyLhbqzJ54rXmUqIgNNTFPEldZFrej1oxWWvxUrEMj0TWID0ytO7gbW95Ysn4yE0EzYvayuT9Mp+pj07kyewWnzVyEeDMd1PRilpkT7tGwiaIIhRCs79Ngok+j3aAkha+pxiJbX6kZpXk0DmAUerfbeG82G46BK6ASy9ED6Ws3omvknaDr2vrEp5kVuuVeeRxtRONsY3u146HmkYhz7nigXm4T6/E6gWWGNIC552I+phbnpZZX+dNFKcyp7IEFd5p9VOYdqYdpRrhQ5k+IdETJAxVf1IxLbqlHSzJLrWtGvaTZ/cHvxsy/JYEmJs1GU488V2ehSglEo9La1roIyE08qDtzfdX8C6L3bnHFi9DCDwNVqVWe7JLKTw3NiqfiTlg8ywnZXX64WDHN8pnPLIk1CIfp08jZmW2Y7JUd3xvsxurOmaNyjvUQmAx/5BOFiGR1RNbq/lGd80sl73Z5Oz2mnXFcZ02SSnvWnqQ9zoH9x+OG07DrftshQeLfTsdpviFt5sHEI8jloTx4F8M20klay9Ho37ijQnFTkc88NQ4Pxjh4niG1j2HXshf0JgUtYro0V50OZafN3KkxH3SOqGaR38R9E899nja8Vvi8NzHQKLfm4TDHBoVf+4En4DiUFXt/l/IBk85ACTFPKeSoYyZBKoeky+5cz3LDYZ6xkNJn6zbaKhVpI0i+bi5tVIIzfA7xTKX2d79jrPPagPbiGZLP1Mk+j6V3OCMz5JxnqoL4nlIktMpsUfXud4FiNeJiI+oetIY30z9TSVrvhjxoYh8EPi7eYAEjTokrMS12MbHUMCUiRa9lk19vtXkwc22nhg/sJCD7mu/rneiqknCvdvUoa8kQiA8vk9fp6ULM7RxGVhcGM2XMPi3c9GssNLY6h+Y+wWdFHJv5zKQ1okYlPTyiHQLhqDXSt4e6a2OvugzOdD1ol4w+0IKYrp31duDWoEliH4c46ZyNN9wgeRuZ98oyq90ZoppSCR6sEyHduRC8XXClKvMW3K+RO0aDoyHUJB9PQb1RCRl6iA9RZdU9vO2HHCerNRdGlWRj56kEnR6qBGdi1O4tzxInblvdZZEsyL6UTIGWYy40QDcy1edTf2a5wNrWl8KBySPlB7KRgw4c3yeRcTLzqWa4udtuUe4kb84Sb21as225KmaL+8A6NwknUZzL9NGdkq3SXivMWd/7sb3jWl/E/aG9UemJcUDMaJtL6eNrpjsT6BZ4ZEooJWYV7ujuec1npa4vG9YSOCoGEZdN27bcpPqVV9U9L2k76FhaUS3sggwavBHRcpgJ7HlLoQFeGS4ZoDV13j42JfM4IQEVORukdfRbIBINVZU8OgoMeq+u515Mat6HSV66kRKNQJsCHfvq1HCoj/lKxwpbw7BiGwmKkJLGWj10D+18FLGHIxkbL0w5SDwwx+1cGH57EMVNIU0iPlOSshOF0azzU84qxlYqCC4ZtxPPFkGt3w9oSbst2pdOzXRGubM1AGsgO3jbaUNOuqhiQGcVVnH2JqQ6N5blLXljbHmfqwOWUIf8xogleuzudNzBmYg5R+vCjBZyhokqUvUpR1tFIfaywPDbEUX3KtI3+8fGPsLWTmhqjjZyaUADfXTGrrpd7KqgsOAqJXNUKFMy4LtKaQyau+/WqZaq8lrLjnADh/GF9ESoc5Hzfh0PikoG7nhDvEYUjwTXkwg0YnQYi/75mt/7Hs0JJRLqZrjXGMmez0d9Ul0O3l6de7lmc9yflFjlYSHBU1F8qJ3mkWXkCcLjQV4Pp/rhJay1hdF8enD58cC1hHqhJEfVtYZtNml8ssfYsgMsuTPz+WAk3agPNcNEmym3RxR2KAybkj4YJvsI4SMcnrpDayT5UYmkkqU3cLnBTQSb/cQvxMBaF342eSax4WfKFtMdfeM1eZqSUxJZXnRj+Epq1tXIqiNlX/vd8YRfH7OZX65HwMoX7JSy935xVvDr7sDMYRpwNRYkeiuqB/06Qre1kB4vhNWZDD7MOLrDmqTCgh1xrbzr4TorBEOWj5uJAbANeNMot5due6B0RU5Q0R+kCT6j68YQgoup8zvLsmdUlnbU9i6Jzp7bmHpx6ke/RgzJ4nVXVAR5UhzmodwE7bzHjsGuDHdmYmlXBml37MENxPPmbmwJN8xoxpET25phgPcGc0miXUzAvN5viB7G05Tjh8tujOW9bIvHEHogtqVJhlAzF9M168g5wAK+PQ9Xe2pcMQ4bPZJb3Dcx4mpyF/qYTWZ6oR6VI+3GGVn3m8tel33UYKpYoG5zwLWHQusZ/UwE3HgO75XAhAnUNXAtKBsp2UTbjuAVSPSlS6XDZW3rTmqVmmNosxCV6JbzGKhsKm9aG3FzF2uxFF2yibRz3N/gbZxEUYdALXMYhz3JVbU+Iqw2uLN1GGViumjojFqG6zXRlRu94bqFzrTn0L42HrAtzcyxO4A2sQ6ugOgu4uWtkK2jwuMn/1rEZDc7+G5ynJGNOs+dmJ6us/giny3XimXLud3vxS6/SAzBtrsiXVeXg9F4m7IR4WHXcCZRyJ7dDprX0/hNkauZOIBRt0H2siRYmCwc6L2KRqcyw5HMDCeR3T0Mcn+VzIJima2OxQ7OMljZ+ne7nu+ZkFCnfVMHB327abLqMtbQjSI3Mosymi60R8QnBNRkUiqWyotm8eaJ0c6H/aiy7o2KmoBDxLZkSambIRKG9PL4uJROB5/avWj3coj2xOVxPPjtfjgVKCsBD2yL04VlORv3vMAokM6N5k3Bn8rZsZuTEUtbvT4PF00V3ftV2IH2Fd4DUNeZyjg5k03K4tyd4EJdY6JkjQqMbc573ZNLRuTVLXTP2IAO9hkjM9etiAumuEnO091MZsF/uAxy14Zuh4sKGCJYvA1EYX3fKNdIVu8KvZUVOfXuZ9NLkk11uYuTM+mUdcYJOrpUO8/kQ/Jwko5Wxlyxk3lOMSqENErHG8Wq2FNOMo+HBV01oRoTFVZwGV9LLi5M9Sm8c7cSUU+X46jimHBCYFMlgGMugVlyU7AlMjLapyUVnMd7FKUxBI09ZfA4TU0P3doYKdGlpBXmozHJU97VBH0v9rwuwZVVG0N6YfTMaayLS3TTfr5BQSjpjm3kl75DTR03bp4/2Z18ux/Z6iRfYM891Bo5ZkbMCN0RPunOkcEqmRepi4rICI1PY2TymtvJp32njSlLqjKhqXCOoHdraBOJrsWI8vZ+mGuCEs83XSI73ZDkKVKGEaIHjUJ8fGNce3qSy9goUbPYZ9Ooo1qV5freXh8MP6XVSm05Xdj5fKXcOBqz82aiOzNT+EhH7s6hnqRGuHQkfr81pSgpWKRNu658KJqAxsJgmDGXMcyjz5QtZgTNlb4+jr654V13TBGDJHFZJXNox0+XnkTden2hkb6eTZ6MarZ2N2qArBUHr7ssjY87c6N1JWJZNHFyesFkYz+jLQ/Ttnu2AzMBhKGcUI6DLJ/cww5kdxcmLTfM12EOXV0yMhjqE+yYpCC0tlO5a+xr0dgux9agJ+O3bRvHPaTxZmuOUQMX0F0uOCdXg3Y6Z1szCh17xzn02ZQzz4cSAaSpqRb8Drr1aKO4QhWXB33YT30PJR6lbASYF+9EXF36Or1bVvSQH0qfK95MB5fH2dNJDBlSTVHlWKuNzqyU/flq88F27q4hVKcWdvLhtY1Tei1RbIzZVTjbVpbzY0yvDwFDMeggdOONFZnd4O3NR2DUcdq4vHAEMSgiBuIJXXnsaxZrWOOWHczt/mA+CsE1/SuGoCSdd5JzxSOrvUabiHADuykv98IeK3SXthIJ392CjYRTimz35BbiG1KCEL2ZlFRXigus3SYX6QUSHh6cdB01tIpSvGuEXXwzdpiVEzr0CJm9190TwiXMfiDWBzMuRcTxmrvKqZKJCoW92Ws5m06IvqbPhKJdBFrQJFGcVFXCCJ25xjUvZzMUYCfrFB31w4VvijMGi48OL0RdKkluiswjr+2PheNjbclc7g58gG2vLlnUd9uTWtPs9tgYGryGGV5WmEDoyapzJWSd1zvyoAgPHYEFVD3e4tndOwAHnH3C7U8DwbgeRc/DmUIvs51pVyp0Oes0nLhNeRSdNRgGepLl8GgI4YpmG4fo/VOrxp1wg8UQx21jHDZXMjgxNDxPWJ9Pm4x0uiPofK9qGIThOBnB3seuaXS6rlMUDJ8XKq/FsA/2650od3ICbSjn6Akngs8edCAfH2Es4ElzojYuFfYCj5GbnDAzaM21R2HUeNQICHSQYFkQGTc3KDEpaVTaGUqoHTUeuqf2IYOKjau7kZArpdjzvQb6GjyAkW72gzgZatPDaEWzHLrVCylHT6CwH/bDQDOdeplb5DCKh5Bw5jUUQpBqQPYDTVJutCMI6df7fVKJxaOKaTIE9dcM92CArdsMqRRf6G+5x5UiOwnGWWXaNRhyh7ochH7jK1l7C25SdYFhX4VYZtri0jlCe5k/r5tBGCgXduWs0HsQ4pJQRm1bn63hfmON7SHWHjRiYAHoZxTOPRC67yfkHJWmS8I6CvqYh4c6MuOw/CMJaJK8WteiQrnEopEdGd1cz+8uk+vuKxG+dlexO0Dc6I7K+uHM9bFF0Hx2+dgH7ZFz2ABEysap3U+Wua5rAg76wTGcq3BxLyyXqOd9itV60EwwcQ4olfPdvGoveDwGF0Pc5KNDu8Qxe4TkpTVT8vA4nFViLjx4OjlreveAxlQMhSiRihTdOJ1yxXKl2l0Fdu8JGsgC8Y6nG/Y+QtoQnm3HqLnTzR4gLbE2kM/tbTjYHWn+QBqcf3eaLXKQdZZTwRyb4sPRngLKNyoFaxmEvh0LZqzsMKekVs20GcL9vQrTUTeTfY9vh+sEGsfxzOsyGBJxdOiam9kHCJvmNrqW4k1qm3hLb2Spw5GEPacKNKS302M43/NqJjVADBUtL5FSZmLj4QoUpBF/2Ez9A5lV4jZvT7Y5nu650QwNuplJ3cz89mRv0EAVDcsfTLO+KXf1VkRsVrPurhgwNx+P131ZdGSHR4cSrnULOU3wzt/gNZIzqMVLZ/+An/Nk7lXlALB1I9/908UnFAkLk8QO0800YHM77EUMtSX0ivqkerMuZzCZwEnq8FtduOAkPady/4hDyd0TjljqvS8eya2Q917XxiLa61Yf8hJqwTQYkq7RqdkEO9VvAHqd6YeFns7e48LN+3kMCN4TiIdBhPxpXVHy5hSdUzzTj5ERohtPC0boQgd+FHtGIp88lFebNbIhrjtSvyr1Vl5fdtHdH5nA3VZIFte3ksSHLjBrIzpYDwyP51wtNATZC6cTqnR6HXSnEeKMyCamk1+Edrv1QLFPZFBjrpZAXz2htY838/zQc9SIkiRdU+iO4bxtZ29J6Uj4JZyOKTpAu7VtFQ9zdzhjW8PqaioeGDZV54oXyUPq4vqDnE9qeCT9g8bQQmAHO8yJeL7r7u19A0YZD42YQxuoiDo6SJUeevxR51wHhWhbSjBAw+v2Qd5zbsNZW1Igtyxk4CdEaaK01kpqaNl7CfV1sTmTMIqk9tRTZXVW40ogW6Wh1nCvTveZb9ohQ85XuB/x1t3UupoqwrpphSxtWw/3EdmAU8bGRkI4eWKfUkhz8G+bPBQGF+FvvgwpLZMXRX/OdFa5hrRmSZ2Y93QSdK44+Lk6cWeMQBRfis4HtlQCXRE9OBvyW1wBuDhtaXPNqIa5tpB0L3rWpnQ1jrqh/unk41UTt/h8qIV2U+3xcEN0yVkujlIs1Ve1gmJLGdZ4C0OBHYKAQFwkQNWtIz3sLaGjh1tAXZp+e9JCLIJohYRpOOYYCIav6DrHt7grjXC9Q71rWG3qQkf9pu3DcwLft85ZIZoM6aJri+AVi9NhySRXWlD9cdRtXG/ZbUOqpQtmFBRO3fa4tnsvcVpHQZR5ix8R1D5ZG3J8UCnLePBdE/CbsKsOlbBB66EpWc8llaJjrBg5X7ajKHQhsMJOYcIy4DAGU9AJ3p72akoJU1QLDepBhjNrbGqMzTq3ivHojI+5rbrNWFxYjDu1lHmhp9taIdKwoUTIzPaRfp2rIsRAwIDOuo8EVEcJlx6Y7rC+QkjaMa1eXsd2oEacwTFxj60ddvtwnbOQXoMmyy6NqaLexToiBZKME7EmTocSZdH9nrRGtuqOVsP1cd/MV7tux/66fuBVXOTZWqYri2kop2TtGiU2DHU+UNbeCS+WTVZ8MCGbGIITk0zQwb/I0T4rNV5k3cym5/yxrcVtdQ7U/X0E80qhYlQnxzO2gVk+lYb93tmdqyOTY6AXc2U6nqJsO7Ha7BMBviXjMt0QqI06Tql7dLgm+HW7Le0Iwyt8fGx6X4uOg1HnLNxwbo0e+t5rNfx+SNDTeNoVhgpT07aL58cMeXVeRhkKrQ/r4yUN1ttGLyBnh6Kq9Djez2kgYzNd7fdqJDEpcUw9A5foShlRBIopFJcfaQlz2+32b397+/D228HY23/57tZyevP/7KDodd7z7cWM50lf6Aafn7w+/9ei/P3DW+0nQJDX4VeTdbf346R/Ovr6+FeHdsuu6fX607fj4ddBc+velrd/35Ii6Jq2nr42ZfZ8DQPs8LpmeXGwWd4t9cH3748mn4xeN5rlXYuvbfn10ZXtcuqVFMu7FWGQuN8vb+8HgB/egvfT168ogX8N62pR7v00H+iEfoI/IW//+L9VdBUKty0AAA== -->
