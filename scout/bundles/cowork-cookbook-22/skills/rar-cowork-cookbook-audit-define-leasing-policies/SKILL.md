---
name: "rar-cowork-cookbook-audit-define-leasing-policies"
description: "Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_leasing_policies", "rar_sha256": "6266a116bcddc87a90003f128db19f7c1249998137f95d762900c769158d028e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_leasing_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_leasing_policies_agent.py` and in the RCI capsule.

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

Define leasing policies Completeness Audit — Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 6266a116bcddc87a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_leasing_policies_agent.py` first:

```bash
python3 audit_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_leasing_policies_agent.py   # or on stdin
python3 audit_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Completeness Audit — Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_leasing_policies',
    "version": '3.0.2',
    "display_name": 'Define leasing policies Completeness Audit',
    "description": 'Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bddf356904ffb19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define leasing policies records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define leasing policies. Output an Excel workbook 'audit-define-leasing-policies-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define leasing policies data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define leasing policies records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet', 'example_request': 'Audit define leasing policies in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of define leasing policies records in a D365 legal entity, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineLeasingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineLeasingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObSLrmX9GcGzHlutgHhAAhd3TEAEIIJBBiEYhyh4t9X8Qilrr13yeRznG5ut19b0fMp5HDFoLMd8/nedPJby9210Zl/fL5RfXtYsHZWRZHfr2wC2/BlH1Zp+CrTB3wd+GWRVvHTteWdfPy8cXzG7eOqzYuCzCd6ry4bRaZbzdxES6qMovdcVH7bll7zSIuFtuxsPPYbRYrAl/s/rfKiIsPtW97n8oiG39eBGW9yOPmMbn2b11c+94iiP3Maz4umtbO/IVntz744WR2kS6+0w7uxYXttvHdX/hFG7ez3sCv/cKdx8+uvJlzj8vMfptS+21XF7M64Dc7uH62mN19eNrHbbQoC3/RRL7fAl/9wc6rzG9ePv/yt48vMbh++fzbi5vZTfPu+9YP4sI/Pv2XZ32xP4cJWBuCMdUI4lyA35VfA19zcMvzg8Xbrw+NnwUfF//5n2lv12Hz8+cvxeLt8+Vl/qN0xaKN/EVb2k0LIuPale3EGfD1dUFlvT02bw41CxuEqwY2vD5n/iGprBZ/nZ99eCp5Df32w5eXEpjwiMmXl58XIAlfXupuvn6dpVQffn7Nyt6vP/z8h5ymcxLfbWdhwOrXr2+/38SCgX8MjYPFV1VmmTddoBziygfCv/Nv/jxNfxP3FpKvz8Efyurj4seSZ3/+Cux9loID5P5YLIgBmPnympRx8eFNR13e/cIGBfLh538m1o18N83ipv0fyf3lKTgCFQ2i9RaSnz8+0ve3BfTm2zeZ/1xtBQrm3/EEDH9X9y1Q/0z2I7N/JzoDVdt8y+UPxf1oAvTXxS//1Ld/NeHjIvjysvUzsFpr28n8z4vfHiXyy0/eHzd/+tvvQPR/K0Ytu9p9SPia20Uc+E379esvPzWP2z/97ZefugpUsW/nX7s6+5HMH8X1oedPEXwb9eHPc4F+vUiLsi8W39bQ4rey+l/176+Li53F3h/3m8+L71fi/IEWsxPvSp8h+G41NsDW7+L488vvAHcK4E3nPh4D/PiP/1iIsVuXTRm0C9Utu3YBEtzGuT8br0UxwN3mgRq1D+LaxCCwb+NA/c8Zni0ug8Wv/8d9QP0n9w3qYXtGtK/eA9K+vmH61+oN1H59XWhAaFnHIcDdbKFQsvylsEOAvbPCqvYbv74DkHLG1v8E1vKn+WLmgF//pdyvDxGv1fjrA7PjJ+IpDD+jXdNl/uvslxH5xZsXLkBuf/DdDkjPSheYEsSZ/8D2pswAG7RzDJo0zrKFBwjFBcw1PmSDOH2ehf3666+O3URfiic8rxZPUmlgMOCbOYtPn4BPQRaHUful8N2oXPz02+8/Lf5r8a9mPYTPOmRAEm9ZABYK6klagFXV5WDYTIwAzm3vkYXffn+LLBBTAA4GOYsBAz4ng6pMfe89zOqe+oTixMLxQXhBaPOqrNuZy+L2dcEHi2/2AqXzo5kVorJpAW1WfuEBZhyBVBu48y2SRdkuGlB6TTB+XHSN/9D6q1PbDxNzsLzt9teFyMiAg8oM/DOb+RgEJpdFDML/rQie94GQ+qdmQb+LeF1Icx0uKru2q6i233QE9jMvgHvepwPh9qLw+y/FTLX+HKrHoniGBwwCkXHfUvppzjnoTXKAAM9Oo30fY89MqT0Ys/5SNG8Fb9f+oy8BpoyLsIu9mQb+8lZSTVR2mfeIH7B0lvSWBe8tK48afHL9n5udOVFMOZvbAt0g5Y+uYPGlQ5Eltvj/uD2aA0JxnMJylMZuF6ykKddnouaGcU7os8ecFc9uPBblH/3LO0a9Q/WXIotB1dXjX54jH+l9G/OEv272XaGUh3xQWyBRs9xH6c+lXNdzLuwvxTsnACcXDwAE2Qc4AdbRXL7vCuen75ZGAAzm33/0B285msMEyntRdQ4I1SLwfc+x3RRYNSfpPcvFHBSwlPsodqM/eTVHHpQbkA8Ct5hLAfDG6zecfj59N/1PE59t0Dzl0SJ2YPXWDwHAjjmFjwTOGQHmtc/+HPj5+SEEuJFX7ey7A/IKPH3e9B8V1MSPennG1a8ASH+av5+eznf9oQJLBgQLLIyqA9F9LKW5JHLQ5AAbQJWBlZXHBSB9EJS3IDwE2vmMCwB337rSp8TH7TeH/Mf6m9nqfeLsyDxnbgAWATAd3Bm/hw/tR2UC5OXziIfev6+0b9pm2TOENgAGgcb3p89O4fVJ9s9uYvEu9/M/bIA+/Ht7pAd9638ugM+LqG2r5jMMPyn3nXFfAYDBT1ubJ/t+erLkpzfI+PQOMn8S+vT38+LfM+xPIt4WxufF8hV5ReZHx7fCevuAODCf6OsnbH76pVD8P7AVqC9zUFlz1kZA99+I8H0IYMOw9sN58JMYm5lPe0DhDyYAKfhSfF/p80oDRFOEc2U25XcI8OgIQNU/M/aNsMCjogW6vblzDP3XecM1m9/4L5+LLss+vgBY9f+7PdrMSPlcy828rQOrBnRh7fxo3uTN0DC08+Wfd7ynx4WdvS62PoChrPm+3t54ZObR75bF00PgmQs0fHwi9sx7wMNZ+byk7AbUKCjP2ZN2rGbTn9u5uQGcJ3zt48Ir+3+0ZwseLuo5drPaB8QlnRf639PDXxa2l3SgD5gXgOfn5XwbgCOgXJCexQddFXcz2OagVwBR3V2B6euff2hLBtKafX0Syg+MmWnsMeSdc2ZOn3PwceG/hq+LWdMP5X7rgP9RqAFakFmOV36e2fjjG76Bb8B5HxffNiAfF+9bwlmDX3Rgt/3LvPmZU/2YMl+AOeDr26Rv/6Ph+C9/+5FdDxD8Ohfjs6T+3jppBjcA/nOi/44wgc1Ar9e5/pv3/3KFf0IRlPiE4J9Q7HXImuEHYQL2vHcBs2t/xOwPy8vHHm62HHjaPv/L4bcXUOX2nPK3On/bBIDhAPI+NXMLBAMcAArB7+eKBc/+ve3B2+QmskGHCmYTKEHYyyXhuJ7nkmt7gyDIKliipOcsN8HaXaLYZrMhl6t1sMG9NYGCAe6a2Cxx0kNQ0gfynov+69zkxbNBszVzxABufPcY3PLePHlaPofp225k9vjNod9eHAIDI/dYw1PPDwNvls7awJxhY0IT0V2dklMdMc8wUsF1p+yuaYteGfq0FduKtRMWoM1akDx7na/R88RHzCnabahqLfibaWqmRhpNK/RENAwZpZukYqomGcd763TFplNmOOLuGusJL2PEkk/HBDnjxjFF1UC5VefGrSbSOYt9eiQhHIaRCh43d2Y7CmpgsWzXg0Dv8wO+hZduIBdLHt7HW9QtavKc6tPhKqx2SM5XUlpmm1yWU01eulGVHgbG0nVrKyu7Na/yGbULq2BZceIRUUM3IY/IKIjXpD9eodTEbF09xGsmbB3vxk47uURN19ha3XnUVKGscrU+HA9OZjGjH8D0RTgQ6po7eAIdxId4QPlm35H4Uh2MBNlI7X01TfCmKxycCGIo8O4reErj2l0LQZ9GUXjgQSFmqIocOTRGeQMnOf22RHfsBDNtf6LG6dw23gQd+kLPG1JKZJPSrrmUM5Sty1XCDC1JBq6cChf1LHp574rmkSrVKTmeQ2XVWNHQXXabOOx2ipVkqHCQ2bt4bPlbZ4Id1GUSYNELdGjCd8cd2/IDFLNKEjCkyUqH603SG8GBaDOMYYdGr4PANdHO7DbboA2sLduQJ4VuGBY9M+PFbJLUuttmQBS+gUtnpI6IPGbU2p7Ys0WPdUIYDL0TvRs/oaK126WYU6atilr0PQmq/tL64TK7lneiNA7TqIsoGy/lzF2b0VRscHWlnmE9upgYzauXLLWuZ6JtWTw0rP6CcQNFNrfl1pLLYSvLFr5BBnF92w2cbnKuLCgbT2mUKxeFPb2NY1eBJ8Wvb/toe0m4FJOwLOWyKxffNTuqdzazrHqOtCS/u1UG79Eat1sXV+GSSPcG1cS7eLEYmOVMUs+6UjXTO5dokNDet0J+PVpBf4f6CGG1QV2fyagxZFrI0g1Nkj46VF58GZTqnvVNIKzLfJV3BdSbebsjeTW9TZR4EkxR46Armm2ViqiRDoDqsLSVMOCo6l5QQUfBPZ60iXq67sUktmS4reDo4ictUR7PwlVo0nOzV8do5JQmxONAoYjmdD6eSFVDUTRvk/N1v96vVywiu5RBDjc+hbK9Vot5BAuo2KLq3veOvbspT7kTGbtDnySVxOD78LJbhsSZ2h7bjAlDmFqTyVRjFga6kqRmjRUzBoh3FBWLiX3N1qrCi5xro8naetglO4843Te7Q37pWptdYkZ08pGrUkgaizYYIsYuY6YnYQtNPU9OqkqTG/W+2nQ3JtExq+Rh3p4iDx3aPLHXYmC1wjIYOfSE+kEiUvjBkAJ6xE98CdGY0Dg1W3T7bIuwZ5jxkEn0dlCuLQ/HPY1vMmwwBGWqRDe9yD0exgVVMbEYQSvUUZGQENfbFb/KJOuUYVZWjOJqdKxQcy757jTAe7E6+BdcsSMMm5iCZUthve+SmzdopHppnYtuKUR5htHTyJt1F7Ayd78k29N+at0rZkHFfehSwF1FVIjRHaVzt141LIPtL1ZecnhQ32hbW+Y1pstcLqyRk5AibsIaCmI3okBuy2A6IrQdVVzeqevt4UCnO5ReRcadTDPEnrgGXirWOTojZIB3FzuzYQQ6bdIdIZ3WGLEuoSlp3aHgOcVSHKXfgVZ2dVKzK2QqkGHgLdBDecWqXoV360jzpyUnnw7lKprYE7M39ZqjA5/ZWBja172Y+hl/OxjLRhnF8DZxMTF0nq0ukTAD4MxHhdynDR87uJZfibxpKarMeopLqOyQneC0oOi7ecMvrUlNt22In9moFRjOd7nJHQmKtyiVxJFTGWd9gm4sHUV1l4bDraqjbrRUdldbpjhFyR1vWG/jEx/rZsgNurFfdZgy6iMrZ16HbZsDvTsjumxgpV/eL+Ok1yfWp1C8xtoERNKl471q1rTB2YPp3jUchwPYdgFJ5SxfMcrxvq2WbMaVJpmKmnBPvainGIXpNCYpggDvo0nqkbXNuopWrGteikjIT2p5gjG7lqwA3hXXpZenmbSzhDVeGtTxHDFbRyyc3gXw7xuHc55j6FWBOMXYkw4feOOpvDmCvF0O0SSK++0a8uVViARwzANyPYbt4apMbZmyq6hWWbld74gkCzfVMm7JnsloZnMsJWqoFEajO2sn1l51lfSreijy8Rjv3Itv4URJpTcb67ZIkyTFEFeX465zLGu786X7QfEvrqvfD6PS2DdzS1yGK1FsdjnOrwhKpXAFV7xoJ+3QunGhVtCaAR+qgU5UQxa7k7msqUuIFxkkM4pQ7iyml9Ve9ekysPfWfQffJU0aGD5WoaBcd2XNMjtLRAKXaPb1OBy4dPJUYtNY+ZkI/bAJhastkPLSUHe0ULIGrd/7uL/jyVrUgvsakMZtZ1dHK04ah8HdrI9OlMHebeZiqjhyIc1umfbG2ci57bi9pmjvRzBV9UO3N8PjMa6uUcoFzfrcw1wR00plsGyyb43z3heMXZI2A13IDW/1ZdcdWGQXHC9HvsQ1d8c2VyYaOEbmzUvA2qNJJ4NSM43auI5UUOUVgkS4uCQKO7WQJe1WQozvLzec4YSqY3Sw8784El+evFyibzQhHAsiEk49THJitI/kFB3PyZgoCFyNekLfK+pixheas4t7Cgm7MEvWstieVxOV1deI6Gv+oDh0i5lpKV/3OKCZvmp6mF116aE+VLaGGkEe8+oonXmJCeC0WbNnuVFQEHJsI7ErY7rGzq0J4x2ydU3VZK7muLz2AgY2FVnbQYdK5NOI2mYO1W6s9TIQ7I0g5zkrqu3aIiC3wDHMX996/0zmhus6UKEZ5wvoVNwbrXTjuR80WmTTlLioNG+e7yWCXKqbFWey3+5oPpWXIXB30ByUYzQPCUT6cvGueEpTUoVZFo/eBUUpz4RdD53gT5nesXFQ3obTcjmZFUz14U7lDePc+4ejKeQHEheUUt7Dk9HFYWijGtJfEbBdl+gLsworiTSM1WnD2rcsZEIK0TVjZ7FL1ZQKSNFsivR1qLMbBrqJNi5f4X0nyfujrOSE6jTHROuNNZS02zVLTPr2iJ/DQ7YZWVpaCnJDl5ks3yrXcuFgIoodh2i40WppJFDsvmXDXOEPmM6pXOr65tbyj7bF+tboLAVhW8vIyoIwRlCVG4YtA2ZArZCOmErhRkq+mEhimiGV34vQPti1HrLWlZP6quptLTnAI5t209aVyANxPll8bXSEnlxVm9HVi7G630eUqfNU7wJGwZKltm/ClS5H+4a0fL6X6YsYFMNa0o9xvV0LBxftsS7YJ2sMu0P5fXdjofg82lfC5LF7Eq2v6FAeXA/1mA5gOcsgrTnYpALfopE9aXfCo+i9nzimd7B2DE3wsnrBnFPtZKRZcmG96WU9WNMV2AkUVxgpjbauvczwXPRwQ+tEHfLLJKWOot8LPzNubCg21UqMzlKTcYoW95dLg4zBjqgG52wYaKrhKxpBV6W3TEUaOa5AFtWTI1g5QdCDWhxYPmpSraGUzKRWGT1eb+uI3h6E+0DVOH2NQSOX9EpzBaUrBEjgMQZYofnOWIr5aRkncb7fBJxA3RmRrfOqUGoT5YmOU48XwyZHzYCIdZujTrLP8oThMaQ9jLKacrtyhe4y6lK0kZpkS5Ili5aMfKTyS3QnZFyHpBe0xXTJ2q1hu7Dp7XYYWdy9mgJ3x9glHEf3/d61zfiQ8X3d6uQhhqNUKKKtbThFoPetvYUM67zH2LJRqvOd0ciCw07BljtwBI7d9BN/NpagZdKp5nQiSj+fxPNptaf7kizHw3RmMOmAqjvB1CT8ZmSad1wWbaIlVnIdYqeTK8pb80wkErwgR+dWusrTDdOJm9TpVSHCZHRx9hK6rgkF5VmonqQDVSyFtm2rY+wptMMdiMOhtLE9tMHrPuvbanTB1guH3SCgTxg6VdfksjvTcNBw0+qWHNMjnhjdCo4vF/gqB/uTnp8DQT9cDtTURdf1WHvHKzeMUMA1dYKRGAISxsNetyf0jOeAJQLTrcYMbZikLWSmP9Ok6iTq3sZQZECOsQYpeSjdWERppcqS5O7oj8LaHo90mTiFtSMGCyUGOu5NP7+LTrl3rds+V7N7QSJORGjmDkDuHRvj/f4O66hkA441jst4a2RZUCPLnOH3jjx5vBg1azG73APbODV6Dru4a5oy54JVtDmsedhchwNzlHdlH6X3YdsAY1nEdvbnAVGoohiKs3GxbVE+cCu6Ui6psT2mVOtqZUht7whcaqfTMZOOZbbN2OuIZ7d103UQUevZdM/wkQqOp1vGYEWQXdxaKm/BkLv6uBR1V2L241qbXKpMnVCES3eXboOTjO0lCQpRljhugnt4hjbqgZDMwpCQJK2lZreePNaUFGYp7TU41JbeHlI2FW5OaBfleu3m2hGmXWUQly0qG56+EvnALpN1QezV0Nyu+T03NBJdWpPqcNA2MrENNwyNtbxByyhBqLqpZZQgccu6n64bZ9q4reGhGgAkdmjup/sJQw7qMTLTOjhFRLJc7qCIlVBOOtUyxPDH/SG+I+QlnvYnsOzIjVe01SnmCK+hffSwsYITREmidK7sYkMHURqad/0SxQlcGFRxDugU7ELySwR3/HElK9KlzqnCsT0mM7Opk9eXo+gqcT1pcBZIUUb4DmWdUJdPZH/sIq9ACzE45Zs7qfajp7XD5dweutWVlBBrW/MwvDZlmK29uDqMNjAehoQV4mASvQ82vH6vcxWdlDbKdlNxjpCy1DFXHK5Z3EhUPK1LrN9C0fHoedNtY3GEwQsVYyuStBLNntGj00GlsKk9Z4Fta7bR2p3ETtmEXOxxvK0wjNguW/x69kLqat4CpThx5DBEscxt6O6kNXig04JPLPFBGIzOaSIqZCWd3IEWAFpzjSViBxvvMLoh17YjpHx+H0ZVugz5SCrScI9u6r3LQgK2o2ZZoYNubgsAqNl1TaQ3edmvI71YurAfdZ12KsbhrKqUmqt0D8GubXmoXwxbbae4XFU7On1lHTNWd06TW0aXWJYJGsibe7nuIrDnbRRk09RIcHdvQcMPW7ogYmuEvCyItZNEYudsSBSiTxW1VoWdnfAbKUDWWalz1wNNOZx4XPVDZJoR00irCxWgmrSM9iLnDlLChKBv8mp2hyHSdfRICGmPWBuhULmbKHrTFJLPEtRYCTBZ7qcBgyR6aQYozd9Lm7jkgXNTUAefkGgrUTVX5ntT7FtS3t7y5jbtYa00JoLIeViE167vVxrsElk44bbtJ515mNjWgNP11nM1foNcbl2uX5xVuCoxEZYiM19drdu6reU6P+X1ET+WS2czsbGiDELle5Tv5EyLSyfyeDvct9DpyE+uf3KXR1+EHKU2jLyRa51xEbxAb2eoPaS5JOIDGk9meSvkvG1VfLvVT7sic/eaL961G35lLLSn2d3Z8fgLhnphf+T3G2Q1epF8yHnt4CenYcyOxM10bQrKhWpXryjJx+hqCft1I+/9Vra9Jaova7NYE54FduNETUjxPmiJAO1Mt7y2W147BRuCMNyxC9Ri32GwfNEL5ABVMW1e7veljdzcwPOuq5NkLJk6gYhUX8nC2jsmelXnSHZJeS/oT1hZNdSV1ExhIpxsuCW78hKgvO5yy+G2G1Ww0aSgQGjIa0uKxGZti9jY4jIUhKkzcLx24Y30jKQ3l+tXDYp5ESOqxeZmtas1X9awnA0hfRjrnJPHSY0PrQgTEMJip5WL7K71oOA0o+AozGxpfRT2J7hJXIIlsBF0hNKR3CrDIASYsxtyY6+RldRiRWNXQegoSCMO6GXSuSpxC7Jao4fOdlwUEVeUXx5TvR2U8ZDeQyH1+iV0kxuc5eQ1occy2OcJBxnF8DtpZoXHoUsnB+sSNDlSe115AlRxaIZxum+3O0MgzzaT+SsANAcktcahqR2vu9amCbEKaPYp0DLzXpSA/eZVk+qtcbOn/Zlot1TfbaUULQdtgkP1YBX13qiO14LzCs8t7moscgmPMwXpoEdXCo5iUu6985F3kKrPw7By9tWJInWIVnQXMvwEPLksS1tlyXDlnk5XZFpzTiqqjbOCShfZBzVxZcHFrThuFNuEBKfVpnSVrOoIW8JaVVh0yyupkcVbdeuNw9QzKrod2oJeBffgtIeKa28S60klzFUoHTq/RbDAb6v26J0J0IZuOmyapGM/6r1/Otp10aWe36pQOd2KptzEhueAvX2r19ZU031PxmfJPU6NyS0Fc1O1HSjD8n6FRSY1A7/EHf3eSYNMUr460EQeukI66o7Zqdak4Y3TxD7o59mrx0Ps2VhbgOtS4+RfGaEsxrV7pKi1x9XTLUVX9mS0myCRBEhX9xqKEAGLmnl96tAe4TbcKSw3WXzbl/p+8PT1MomypQmqQw5Oh2B5sU8AXyYfPrbbgFg6dBHgZAuL66t4gI1m67QbndtNvS2NpEZSSDoGHhoTUHxIsVtVG1hSCQHu0d4K0nQl0SdoBwhw0mrOlvrTnZ5uld95HbYsPF8n+3qQN2K/qUPxLLPwPdnvw36qsHqH7S5pVy9R4QzhsOk5/FWHtI7eKnrHUBmzIvPcFbrwEIuCdjmruG4Ku6oPVsfuZpM2tmOGFNNCNyrIPHT0rR0eDgk0Bhk/MmNuIftRWW0VbUn02MrySrWGVsE27tEQ4STSJSEMGRG/2qfkzRsYwoglaR2biIFU5IQpTqHXkX3jbcOjzDMhXWCUwIs1vlmTiVyu+L0WH5E1WZyXEDJqW1Q+iAgcB+Kooub2YHdbZXvhUgi5Ifge7snzsGyFkJ2PWP7615ePL38cnb38z94Dm492/p+dIj0Pg95f63gcCPq29/mh6/P/0J6/fXyp3RhY8zwja7IufDtw+rsTsk//8oBvnjo+X6p6P1x+nlW3dji/YvwSF17XtPX4tSmzx+scYIbTNfOLic387qoLvr8/y3xom7/dx5ng17b86sVNVTbz6VhczC9p+F5st+8/w7fTwo8v3ttrR19XBP7Vr6vZxbc3AoBnq1fkFX35/f8CDqntLCYuAAA= -->
