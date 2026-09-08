---
name: "rar-cowork-cookbook-audit-forecast-cash-flow"
description: "Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_cash_flow", "rar_sha256": "aa18e8e21a629a32986f4ff8d88ea8ae1a3f32bb7054baa548e79dd8d2ed2c28", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Completeness Audit — Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 aa18e8e21a629a32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_cash_flow_agent.py` first:

```bash
python3 audit_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_cash_flow_agent.py   # or on stdin
python3 audit_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Completeness Audit — Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_cash_flow',
    "version": '3.0.2',
    "display_name": 'Forecast cash flow Completeness Audit',
    "description": 'Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2256c3d37957e241',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit forecast cash flow records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to forecast cash flow. Output an Excel workbook 'audit-forecast-cash-flow-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no forecast cash flow data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads forecast cash flow records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of Dynamics 365 forecast cash flow records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations; returns an Excel workbook with a sh', 'example_request': 'Audit forecast cash flow records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness/policy compliance audit of forecast cash flow records in Dynamics 365 F&SCM, delivered as an Excel workbook, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditForecastCashFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastCashFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-forecast-cash-flow-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZV/YBISa5oiIaCSEJBAgQCJTOcDLP80x2/vfeSOfYzqrMqlsR/dRy2BKw95rXt9by5rcXs22CvHr59KK4ZrY4mEkSBm61MDNnscv7vIrBVx5b4O/CzrOmCq22yav65cOL49Z2FRZNmGdgu+yazsc8S8aF2Tphs8i9BT1mZhra9WKNYwsvr1zbrJsF+CdYeEneL8CNvHLqRZgtzIUfdm62SFzfTBZu1oTN+AGsMn0/zPxFGtb1/O2FbuLUHxZ1YybuwjEbF1xYiZnFi++kAffCzLQbQBHw8NzKzWy3fqhU5Eloj4suzBPzsfRvYEXTVtn8eLEfbDdZzEo/9O3DJgCS1QFQ1h3MtEjc+uXTz798eAnB75dPv73YiVmDWy/UrDLzpuEOKMgA/cAuIJkPHhcjsHEGrgu3AnZIwS3H9RZvVz/WbuJ9WPz3f8e9Wfn1T58+Z4u3z+eX+Y/cZosmcBdNDqi7DrBgYVphAkz0uqCS3hzrb0oA01TAUq/Pnd8o5cXi7/OzH59MXn23+fHzSw5EeNjh88tPi7wC/Kp2/v06Uyl+/OkVqOFWP/70jU7dWpFrNzMxIPXrl7frN7Jg4belobf4olz2uzdewDhh4QLi3+k3f56iv5F7M8mX5+If8+LD4s8pz/r8Hcj7dLsF6P45WWADsPPlNcrD7Mc3HlUOQs0EMfHjT39F1g5cO07Cuvkf0f35STgAKQCs9WaSnz483PfLYvmm21eaf822AAHzn2gClr+z+2qov6L98Ow/kE7CDCTGuy//lNyfbVj+ffHzX+r2rzaAlP78QrsJyMzKtBL30+K3R4j8/IPz7eYPv/wOSP9bMkreVvaDwpfUzELPrZsvX37+oX7c/uGXn39oCxDFrpl+aavkz2j+mV0ffP5gwbdVP/5xL+CvZnGW99niaw4tfsuL/1X9/rrQzCR0vt2vPy2+z8T5s1zMSrwzfZrgu2ysgazf2fGnl98B5GRAm9Z+PAb48V//teBDu8rr3GsWip23zQI4uAlTdxb+GoQAVusHalQusGsdAsO+rQPxP3t4lhiA9K//237A/Ef7DeahB35/ecfrLzNef5nx+tfXxRXQy6sQYDJAaZm6XD5npg/QeuZVVG7tVh3AJ2ts3I9g/8f5x4zuv/4VyS+P3a/F+OsDncMnzsm704xxdZu4r7M2twBUhqfsNkBpd3DtFhBOchtI4YXJXAQA8zwBeN/MmtdxmCQLJwTsQK0aH7SBdT7NxH799VcLsP+cPUF5vXiWjRoCC76Ks/j4EajjJaEfNJ8z1w7yxQ+//f7D4v8s/tWuB/GZxwVUhTfbAwlZRRQWIJfaFCybqx0AcdN52P6339+MCshkoOoCT4Wgxj03g1iMXefdwsqR+ohg+MJyZzMuQAXKq2auiWHzujh5i6/yAqbzo7kWBDmot45buJkDSuAIqJpAna+WzPJmUYOAqz1Qa9vafXD91arMh4gpSGqz+XXB7y6g8uQJ+GcW87EIbM6zEJj/q/+f9wGR6od6sX0n8boQ5uhbFGZlFkFlvvHwzKdfQMV53w6Im4vM7T9nc211Z1M9UuFpHrAIWMZ+c+nH2eegG0lB3j/bh+Z9jTnXx+ujTlafs/otzM3KfTQbQJRx4behM4P/395Cqg7yNnEe9gOSzpTevOC8eeURg8w/ty+7fJa0AWyBtx8dwOJzi8ArdPH/cy80G4M6HOT9gbru6cVeuMrG00lzezg789lRAqFnPZ8J+a1jeUeld3D+nCUhiLhq/Ntz5cO1b2uegNdWwBMyJT/og7gCTprpPsJ+tmBVzQljfs7eq8AHIOcD8oDnAUaAHJpD953h/PRd0gCYf77+1hG8+WG2DwjtRdFawEYLz3Udy7RjIFU1p+6bm0EOuLNv+yC0gz9oNXsNhBqgvwBChCAZQaV4/YrMz6fvov9h47Pxmbc8msIWZG71IADkmF338NzsDCBe8+zGgZ6fHkSAGmnRzLpbwKFA0+dN4POyDevwESBPu7oFwOaP8/dT0/muOxQgXYCxQFIULbDuI40eEQfaGiADCCuQVWmYgTIPjPJmhAdBM50xAWDuWwA9KT5uvynkPnJvrk/vG2dF5j1zyV94QHRwZ/weOq5/FiaAXjqvePD9x0j7ym2mPcNnDSAQcHx/+uwNXp/l/dk/LN7pfvqncefH/2wiehRs9Y8B8GkRNE1Rf4KgZ5F9r7GvALygp6z1s95+fMeEjzMmfJwx4Q/0nqp+WvxnMv2BxFtOfFqsXuFXeH50fouptw8wwe7j1viIzk8/Z7L7DVIB+zwFQTU7bAQF/mv9e18CiqBfAcACi5/1sJ7LaA8q96MAAOt/zr4P8jnJQH3J/Dko6/y75H80AiDgn876WqfAo6wBvJ25TfTd13m6msWv3ZdPWZskH14AwLr/Yhaba1A6R3A9T24gV0C31YTu4+oBCEMz//zjVCs+fpjJ64J2Afgk9fdR9lY55sr5XTI8lQNK2YDDhycwz5UOKDcznxPJrEFkAofPSjRjMUv9HNvmRm/e8KUPMwdI/U/y0ODhoprN9gjqB/Y/6s+jAQcIrio8AxI1zWfG5oykKWgCgN0YA0hI/CnHR6H58iw0f8Jyrljf16IZTR8x+2HhvvqvD5Z/SvdrP/vPRG+gtZjpOPmnucp+eMMu8A0K2IfF13Hiw+J9wJs5uFkLZuef51Fmduhjy/wD7AFfXzd9/b8Jy3355c/kegDclznanjHzj9IJM3ABYJ/d+Q91EMgM+Dqt7b5p/1fZ+xGBEfwjjH1E0NchqYc/sRAQ5QHNoMDNWn0z1zeh88cwNgsNlGye/3fw2wsIY3N271sgv3XzYDlAso/13NVAIMcBQ3D9zEbw7H/c57/tqwMT9Jtgo2muSJd0kZWJIxtzjWxI3EM9j3RI0jVJ012Za2+NWBYBY6hlmhhKusTGcUgHcR3ERkhA75nLX+aWLZxlmQUBJvgI4MD99hjcct6UeAo9W+jrWDEr+6bLby8WjoKVR7Q+Uc/PDtqsLMggrKHSIR0mh6S/tQVjhsedI6qXDD91VitGW4klzRYez8YukpkolFPufg6Cjbcz8v1SZpf9dXP2xKtA09ESbtdm627qvRwqMo94YsZD4NmlEnkiv9+rc7/bcL4HNcPuLlakxrb1JrzZxZ7JNVTPNZnziKEhlmd7mR7JSWFp8pzdl8kh26KKN5BM4EUjPjohjLv7LRK7TMhywW6JwHp7D5mghbToVJwmru/HCBJhRKnu4XFQGe+GhgfDY65bJTnCtbws9X201mt2ZYfJ/ibJq/heSKkrG7GXcLuTcDXGBI793XKf5XakiFQuohmiDhF68Yxcvt/VbMOUticF8ZkjrtChdIrEC8WwWKPcZESqdemgroXEkcAQ6HKt9fsGfHvrM4NgsCrdC4oONUQXCeW4m67n+IaFfVXz3UVX1elCct0e3YGOP5nw5WpvVzoPXaZBoyZbdkruaOwpzd/W97C7ZBg8udHA3flNmju8Wu2TpSsTigU72CXP4XoMEtTbQRPV1LItF7ahm/dV3ck38pLRJZetV6krNf6y4NiVdD7dUT1dBVm0l+uiJyRHR6lYlZJ7F4em4hzLTYiyjjkt48obqIZSjXBfkPrOa82LcnNKzz3cMQsmtmOyT82TeBGujMxyR9Glg/vJMPtOrY+nM1mTt8SNq1G/UheIqDhZqHCGsZj9JuBYqDRPoVE2Ellc794RMeDR6WKZ4Ggs5hXfLyq7rP2E9opoe26iE8QeMV8pdX6z2iuofqRaxAmhADU3y4tx48fcK8v1qT5KkkEF4108eUPVVfgxoLXoEKMCGqtiYhzC7soFFWPuVkV/IO+C2+LF7eRs+wREp1FokdDt1grnk/F9B+23OqkFba5YcYNExkY9eF4s1eew6wUIlvAdi1bO6SYh54sPn3HTX94EC4XbgSPb+rZDb5RK8hu6XysX+zzcwgE9UL1AohC7dL0YuliYICHJ8hyJ51NhXgQvDCFbXqJRd0mvTXjcHIk7xGfQAEN91W1HZxyRnbbEr/SNLhyKtE4R7AyX3Ne2VMEAVwR9qJ7GIODPWIiiN+voUox7WjGKm0cIfmYTlHMyZGK3p061s6NJJ+kaDvb8Cc4UNZDR5C4bYqz0Y+VJmSHmInQi0c3oshjOpgPT9GG6OxoTfZPybEMI9dT2dX0QsqJBIyQuyaO+rDb0fr1LGI489cqF4XYynBs4mpgefV0rfdTXeuzKsXpb9t5lf8QkofQzoQcR1eE3Er3c64iNkXZ9TC3urkOVRVV8NwCfa9Gu9FduzNvuhlRHfjXoyI5miN0R8ht8m3HBWRFWEKvno7Y69+NG5+7FNYbCgeNMmuNP2+PkYh0RZFzOuMx2fyf4GmI4fpB9iLYEmpASEyYEcrfUrmMmcuOFRVAjkJ3t1hSwSeKxBLWz+HJb1ZrTHNjg2MX99u7fUWKNscx5c1/uJZ2b5H6zOXrh9Y7U+oUR79Opi8RtgF3r/Mjht/uUGjhu66G4L9oxt6/DxfIHI9uO3YTFMNlT1SRafd1SbHFBc23SVW1Q9gkAVIJbrZtInI4Gg2LFhoWOStdDh5U7atl0zdfrU5aviCjKWxoSW2Y6WtT9oGUJTy2Xp8Ez4tOw7EKubqZrfcspO1tb0M3TGSjmes2bQgpBeYOWZY4JzQNNTOtIzFassYGvZR5rxlowedkVVcO/aB62oqj4xl/YUI+GmKRCIzkDc/aMFUGwf3XVbnL8O1co3rYcD9ZquXHuWr1HoqMb05ySYBHVCrfb3Un3Z0k+3Vw6xAtYXXW3+8pgGcqV9w0bbYcDxmoHWt4WleBsdk0j9Il/FHqZCp11p8YFXejLPLO11Z5SeJOjo9rUo7NmdqtysqiYaUrkYqKlkixJFb829lkK8fOFgHHR65ZoPDJ5ODGXgKEuOVzCSrShkVQhslrdpv2FdDAvvRzbqb/tEHyVbJdrQ5KAMpfDtUL5rh+X0NIVr9byGlUEQNJSzUSA7lgRe0pl+MEOH03bd9bnCUZhVqFOMJKOYY52p17vzMhSB3a1CbMtjuW46l46DIXciIWgk3wguFaxC+0oEvTp3tFyeHKtHb06Bix2DRhzyDYcleCOhLOREuQFRk6cg292UJ3fZTuI7a2lJvzuiMD2jRpwTFXzPeYqhhexXhPsL90YC4dzeksKoYR4ArJhs3PH2o22B0Pf74OBsdWh1uGJLndnh4bS8+58QC6i6ZA8drutVUXsxns83XUpNWUxD66G4ko+wk1Ey7hTfXWw3SnkNh7agaFrv2VYUqFq3DhmY10h8XhlkY2QlIJJMWEV7CZk0LYbzSupAN55aHpTYzzwNb6sPDyRHG0n8Koo37uz3can086PMUlGGJ0r+WANgRJL7sMQaCIEh7u49zWmp0s6Ig9NoHZbbtBHfXttRFoxnZOUxCpFyG7CbC0uMA7wOO1lY+cHyi4sY8GZNKKDixAUx17eIQF35PqTNHkaoVU4ytu62Zfr6njY3PGiorqtN51WeciMPTymaBI4UdHYMq3Ca9YW2B5vwliiBeLmw1SzT6aVnqT8eWLaXILvRK1Woy+TUDGq0a4LaELHnYCxuw6G2CTMAzxp7fzGhooaS5OhxceM2baB6AYRpZwy3A8T4oxfxVGO+TAt6pWxzJeHlpZ2IUsulyEkyFTf68S+uF/79HBVhABLcjwYVKHZuIULWq1q5VN6U7ocjhBGlUm5B+1FmRf1piM0PCv3MSSoBqjtsW6RmHgO4NWaiTegzAsont9Mbrkl6Czd+AcBKW/BOR2COI6YVJK3eLylshErZTCCEVrcneKernkjoTjTYP2b1dFNeC5D/tDVWM/CrEbnqx6u7yQY5Jb8nZvIBgm889iNG1H3ayg/APdEZx3fxiRNgaYkMDCaJfLGSPLzFCeH1MssVOIOjY+Lt9UJXW+kg7xkONovkk5PHXYZnVtyu9+FZn9mQy5wCqhUDCnr+nRv6cGhPrcHaAd1UCtQSHmRU/xaoudAIW/EMmpoNCYn9XjGJJ9LNsN+yzfsJd6GiZCahX23V9BUiaaQZ3BydXXqUGIsQhrCKRYULtoelZargjAlG00/9/Z6CZq/jMMq0G4Rvrs5CHq2KyWTdu4UK5XokYhzKz8W25NBMT4VpWbZbxWJuhqH+1jmrivpWq+zgZemlIOueN9RDoVB3BUxIPztOSob9VyMGnVFtcsKJz0/vhPJZWv5BLE2baaRHBfqrigsex6/h1tfV0cDZ2NtfXeuAgxdy346OUgzworGMCl5TNMt6jcCVBA7+j5yQuMWVrxnKB+vpEOOD9h51fHGqBOxh7YcrUDZ1d3arM7qjJLdmr7wVyrmrggIVNTSElkTzE17Y8tqKNqUxMWGUvdMGaKHIQa0j7atSKfXu9ZB4haVYGrNHO78ruGMAmuxqvPBMLE/SW14Qmx52nYaozjp6bYupWG0cIlbSqJaEmvYHAU3clT4vPQgSYuHGxtcm+mUtZJmjL0XoQPawFd0ZQoNfs6XBaNJuGyWq2yCdvBacZr0qhskD9+Hjun2OX8sFX8/oEZcDE2wKW9LuDqs9sKY7YK1e6k4Q664c8vKCVyK4zmtkI2TcJF3Bf13eLdzTdh2mxj2yoiI7re0ZDYewUm1rBrHHV+yAXXseewEGyZ+Nqtltq325ggaBxBvtxCMa9ROS5BDMKHiSgJhyHCD2ippxZFsvAt8uAj21mWgcN6mgmvMLBMbxw7jJE+DqzSnmGeWHrdc7ry05GVIDmCf7ihyVWwBDt14hqsYBhhdxLUx8ZtKaGOPL1KQ+D3npBIm8SlBs5RvnStnKM7EJZWVbsdy+7RQa3a5OUm0Zmf0LhEhlV7bXpeIPiK7bEfd8TOOoasqIY8bprseGvJy1TiaXC9Ffn/al4iaS4PmJoYiD0fkmO/u62NNmnDOXqGavzibSEBQqVjpOdHWJ5hD0Z0bEBJ3D8acuBBOFtKVa5YevovQjTH5h/vuVpmdtnRsK7zWpnMQ4MEwbi7iIpcjG2XUiT9OacQbp6OkjVlqarZOjlawvLpMW+2rFumyQwclIl+qSra8lqo2Kkp5vBB9gyPbiLhGHsorLWxYjN40RQz3+6UuqFYQwrcyn1rlQgQqf/HD4W6gFocr0BmiAu6+uo2oYF0NDN4TjC84wVE7W3lNca2wFXHPFWi9pK7HApJi55xxEBJ6anitDlfC75vohsMni5nG07LH1w56QGnc9JDU3vurvWTXJ/t+QO5mqshUVO8xH3Su4dmkpky77G5BhyjbkXD3drPG6dwK81VE0sQ6HbqNiWuqxmD49rZd+qtghNWzo9AqBdObNJiyzNg5FrJvwrtwgI/rbTAd++uklfdIA5PO8rq1BFcVs9vyOnIu6+9JthQbXwigvS8tL3LtEfTVrAnDQF3QhE2bthMlk910x+zuVVk5paNzyoz01i5xkojcfH0h80zbq8QyY/2dU3BmLSPe7QiDmr40E7E8jCV5d28X0PGZcnHjfHELNW5L0OSFYVaGkIiEF1f7WgLTUXU64meSQTnhtAWmgU9hvTTI7TXB2LbaeeOdR0yIq8srsGR1Nk4Ro/v6piLrQdfv7RaZbgnNkkVSnetlba/qyRrqfUWzG36tmb16JmynIwrl6IwQdFx3y4OH8DF6whvtApERlKSBKjnj+r4EaluTdTswyoVzuXXqb+hk2DCByvQ4zV7KEOnOJO1oK/Qo4y3ozqVzuIdDk2tPXbDHdqCC2sTUSIl3M6/mrTEbZj8lE6xx/ViscxSnV/Xg9a5Kn26ld8vEs2ugtsxEuI8cj0sHUvnIKVmsYUmxseqEouggXp43orNBBGO8D1XSOX24QpFyLcQU7g+jImgT6INpYWjlUulaNC4n061XBTKoOp1F8LUxCDwuL6scV5RsZUNm0LbZZs8EfRxTq1NMD9gSh0eiTi7R+crI+qGoLHVr8LrOK4xVp9atbe533TMPpa0aTNoQJyRHTcTBL7dWvdx4I6CmjVxjnqh0w1Y/oPbphvenlamwW7XYl50cu0mHb8G4ejwBdBKilMFgHM0tP29Nq5TEkY3xU5REAACRrWpqu8M63CEdjVCJV644RTybjtdSNkVRFtbDW0Fdl4i2rGSUdC+gFmprJDDO2AFKbhnNZvfD0iZQqZfKoYaGYeIJb9fjRc6RCEkkfGLrAFGGFYlPvVh2RHJQT5kHN0hyO6WWxNdYzQx8pMs3blPn+FSjF2m8b6ddJ4TEVUMEMIvxTnPTRhjL102+9+X7xC5JlPJUck/ghmOAWXB53PkIm6K2ipsp0ZB4pdSCY9pH0N8Xk9DAweiutmJNYhIyoqs8jS6g4ZcwmokzMGSK56Q96BVp80f+6nMBnh9bTEG6Y03Rowx5mbDPU+F+LJyjcskhmdkoOYtJjgOCSbNS6sKL65QOeGRddLcudvGK8+4rdGqzg91Gp1L0zCiDzMSZAgQvAn4gYb1ro/t6zWUulhnEepOoBcZcDo642miEZ8jn9XoDaRrOM46b5VlkrwKnby8mLpkK5hCDvjxk2JGX9JvPOUWukMoNtS/+ytKiwV/pZ150Rh43hx5dYau7gNeEgx8uaBhMknuNYmLYnnZ39qBKSMxJh36dr8H0vOV31WqycZyGVRVa46hENQZzpY8Y21wZ0Ey2nkvbR6LgdrmKoqQfGCjuDZpfsvvo6Bzk1mESE8v09hYsaRRF4w6Fw42Z+DDEXXWXJY6ljqbw9XzktcTTsCLPWEhgXFkDvmyRIO1pbWOLSbuzZbXlqbqqt5fN9XY8hQOkK7HcJtbxLi/1C7ym7IbIEbgiydaGc/HWVCYhXJoTQjZbpdpop7THoX3JCYSLWKZ6N9ZJU9xgiyd0UR/EJmGtrdl50sQyG/E2pJV6QEZ1zKS+pv2poYsaBtWT6yyWw9aliAjb/Xp506bTqduN7JlVvaAyHBDlPHLxBWxb3yIlG03qkORujJ4nKTlbflIOqxO2tdpmp/SX4GAN03g+iGm7PuUr79Y1KiYvoRvcCzJWyKJYJlVXK52bZadOrwFedFBGn6bO5KNTctmfd7QzDlO/U1QaX0U+1K267AxJoXTcDLLnkES9Tezu1qtsh0B3JbMAK8yzRH555vpVQl7CUi8xwsj0LG4LEpcOnKfqGawzfKftEH4c6oOcjnImYasSR7DtBmERLOlOkUDDo+kYG1PvajAT83tv3LLEYW9y+/FmHRUHGftLc44DF2Wto7HZ0rBvYKy12e2VnQMa6Z5G1S6pKVuMbihz86oDvLY2yjDtrpE/5MtIzHpBg8upKlphiKQI3YstqUmb0V+ey8itSa4r8ahjK2y4FrUlqaDiOBDVwg5USfVuA2VjBumML1cbrhdafToZ+mWbr4/DqReUK7tZm+cq4Uo6LNONFbL1esmhXgu101F1fDLAlqvawJzpVm4FVHQ0Sxib9aEhCixNGZeDsPDQ2PfokEcbqLM3B+5+oXkwSZMMPLqTeRmugiYpQRRc0F7YSTlFq5U+1nAva5TGoGVe+wKMd7h39Xv15hzdjVmzuy26liSyjXnEN2MmkJzLtS+O/UF2MsNljzbPQHpOX50UGQ4t7pDCeTIpKYeG6bqOrpWDxqI1FMfTsTD51brdunLmJmBQ2bfCzWHEPCwKeKtdY4A4epXmXrJeLy9LWgqdJVVfM2i9W69ltrzsSeKqLCnSYUlhvcXNNpTg1fLmcQruRl5/EpClC43wHpSFv//95cPLt0Oxl3/70tZ8cvP/7JDoedbz/h7G45TPNZ1PD16f/r0ov3x4qewQCPI8+KqT1n87SvqHY6+Pf3VgN+8an+89vZ8GP8+VG9OfX/t9CTOnrZtq/FLnyeOtC7DDauv5jcF6fqnUBt/fH0s+GM2HaY8D4S9N/uX5ZtbL/DLf/CaF64Rm475d+m9nfx9enLdXhb6sceyLWxWzbm9n90Cl9Sv8irz8/n8BqOLUtrktAAA= -->
