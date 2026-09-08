---
name: "rar-cowork-cookbook-report-manage-service-accounts-and-certificates"
description: "Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_service_accounts_and_certificates", "rar_sha256": "a59f909a07ffbfbcc2255cff10660456e2caadf9e2748bcedf742dd2a601e78e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_service_accounts_and_certificates`. The original RAPP
agent is preserved byte-for-byte in `report_manage_service_accounts_and_certificates_agent.py` and in the RCI capsule.

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

Manage service accounts and certificates Summary Report — Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
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
      "description": "Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 a59f909a07ffbfbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_service_accounts_and_certificates_agent.py` first:

```bash
python3 report_manage_service_accounts_and_certificates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_service_accounts_and_certificates_agent.py   # or on stdin
python3 report_manage_service_accounts_and_certificates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service accounts and certificates Summary Report — Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_service_accounts_and_certificates',
    "version": '3.0.3',
    "display_name": 'Manage service accounts and certificates Summary Report',
    "description": 'Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet',
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
        "upstream_slug": 'report-manage-service-accounts-and-certificates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82d09cd56c56ece1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-service-accounts-and-certificates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-service-accounts-and-certificates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage service accounts and certificates stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage service accounts and certificates for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-service-accounts-and-certificates-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage service accounts and certificates records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet', 'example_request': 'Build a service accounts and certificates summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of service account and certificate activity with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageServiceAccountsAndCertificates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageServiceAccountsAndCertificates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportManageServiceAccountsAndCertificates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebeiWLbnV7HvW6sz8xkRjDJErVqrGQRBQUUUIaNWJDPIKDPkq+/eBzWGrIp6/fJ1/9VG3KvCOXvev733Pfz+ZrdNVFRvH99Ovp0vRDtN48ivFnbuLbiiL6oEvBWJA34WbpE3Vey0TVHVb+/ePL92q7hs4iIH29k2Tr16YS8q3/beF3k6Luo2y+xqBFfKomoWRbDI7NwO/UXtV13s+gvbdYs2b+oHN9evmjiIXbvxwQW3ibu4GRdBVWQLfsztLHbrBUasFsL/PHHKIiiAjIsw7vx8kfqhnS78vJk3zKTKom588OZXceG9A/ybtsrjPAQ3F+vB9dPFrNhDpz5uosXpKei7Be83dpy+exDRixKBF3Xk+w1Q1h/srEz9+u3jr3979xaDz28ff39zU7sGl960h4bKQ7vTUznmpRuTe9x3mgFSqZ2HYE85AsPn4DsQE2iTgUueHyxe336u/TR4t/j3f096uwrrXz5+yhev16e3+Z/W5osm8hdNYT+Ude3SduIUmODDgkl7e6xfes8+qYHf8vDDc+c3SkW5+Ot87+cnkw+h3/z86a0AItizVz+9/bIAZv70VrXz5w8zlfLnXz6kRe9XP//yjU7dOjffbWZiQOoPn1/fX2TBwm9L42Dx+XRYcy9ele/GpQ+If6ff/HqK/iL3Msnn5+Kfi/Ld4seUZ33+CuR9RqYD6P6YLLAB2Pn24VbE+c8vHlUBQsnOXf/nX/4VWTfy3SSN6+a/RPfXJ+EIpAOw1sskv7x7uO9vi+VLt680/zXbEgTMn9EELP/C7quh/hXth2f/gXQa5yADv/jyh+R+tGH518Wv/1K3/2zDu0Xw6Y33U5DLle2k/sfF748Q+fUn79vFn/72d0D6/0jmVLSV+6DwGWBNHPh18/nzrz/Vj8s//e3Xn9oSRLFvZ5/bKv0RzR/Z9cHnDxZ8rfr5j3sB/3Oe5EWfL77m0OL3ovwf1d8/LC52GnvfrtcfF99n4vxaLmYlvjB9muC7bKyBrN/Z8Ze3vwMcyoE2rfu4DfDj3/5tocRuVdRF0CxOAH+aBXBwE2f+LLwexfUC/J9Ro/KBXesYGPa1DsT/7OFZYoDTv/0v94H9790X9kNPDP/8BPDPLwD//AXAPwPA/Pw9gP/2YaEDNkUVh3EOwFljDodP89a8mUUoK38mAWDLGRv/Pcju9/OHRZwvfvuTnD4/iH4ox98eqB0/UVHjpBkR6zb1P8y6GxGoE09NXVAE/MF3W8AvLVwgXBADYJ/LRF2kHUDU2U51EqfpwosB5oBy9ywrwJYfZ2K//fabY9fRp/wJ4djiWQdrCCz4Ks7i/XugZZDGYdR8yn03KhY//f73nxb/sfjPdj2IzzwOoLC8PAUklE97dQEyr838uVzObgew8vDU739/2RqQyUHhBn4FpvGfm0HkJr73xfCnDfMeXRELxwcGB8bOZkPPZTFuPiykYPFV3lfFnitHBErpwvNLP/f83B0BVRuo89WSedEsahCedQCqZ1v7D66/OZX9EDEDEGA3vy0U7gDqVJGCX7OYj0Vgc5EDF6Zfw+J5HRCpfqoX7BcSHxbqHKuL0q7sMqrsF4/AfvplbgNe2wFxe5H7/ad8Ls/+bKpH4jzNAxYBy7gvl76ffQ4aGlD3c6/+wvuxxp6rqf6oqtWnvH4lhV3NrnBBkQBMwzb25lLxl1dI1VHRpt7DfkDSmdLLC97LK48YVP6rzc+rHVk8u4rFpxaFEXzx/3ODNZuHEUVtLTL6ml+sVV0zn26be87Zvc829SFwUT1T9FvH8wXVvoD7pzyNQQxW41+eKx/Ofq15AmZbAfE1RnvQB5EG3DbTfSTCHNhVNaeQ/Sn/UkWAyIsHZIJYAKgBsmoO5i8M57tfJI0ANMzfv3UUj8CpvFlpEOyLsnVSEIiB73uO7SZAqtmjX9wMssKfPdlHsRv9QavZAcDZgP4CCBEDr4JK8+Ersj/vfhH9DxufjdO85dFUtiCXqwcBIIc/Czi7Y3YUEK95tvhAz48PIkCNrGxm3R2QTUDT50W/8u9tXMfNjJxPu/olAPH38/tT0/mqP5QggYCxQJqULbDuI7HmSMlAWwRkANgC8iyLc9AmAKO8jPAgaGczSgAUfvWxT4qPyy+F/Ec2zvXty8ZHnIM9c8vwDG07H78HE/1HYQLoZfOKB99/jLSv3GbaM6DWABQBxy93n73Fh2d78Ow/Fl/ofvynGernPzdmPQr++Y8B8HERNU1Zf4SgZ5H+UqM/ADiDnrLWr3r9/okH71948P4LHrwHfN9/jwd/YPO0wMfFnxP1DyReqfJxgXyAP8Dzrd0r1F4vYBnuPWu+x+e7n3LN/4a9gH2RgVib/TiCBuFrofyyBFTLsAKQBBY/C2c919selPhHpQBO+ZR/H/tz7oFClIdzrNbFd5jw6BhAHjx9+LWggVt5A3h7c/cZ+h/moW0Wv/bfPuZtmr57A3Dp/9m5b65g2Rzt9Tw6grwq5/v+45sDZE08kM+fPRDNef1s6H7/hxmb/3rva/SBjPu6Y/GVCtDT/xB+mAu3XTVzJXy3mMUIixmEQaNTAhqP7g8sBuUJSNeM5azRc1Kce8sHng3NP0uxf3yw0w8vNK+/T5JXKZxbge9y+ekEYHwXKP1u4T1KENAAOGG2x4wDdp08tPqhLI8C9PlZgH5glrlq/aFGzX3Gsyba4SP1X/Y4nxThhwy+dtn/TN0ALcxM0Cs+ztX83QsRwTuYjIBZvww5QK3X2Dlz8PMWTPS/zgPW7PrHlvkD2APevm76+mcUx3/724/kesDm5zlYnyH3j9KpMxyCcjFb+R8qL5AZ8PVa139p/ycx4T0Ko8R7ePUexT8MaT380HDPFuCf5Tp83yF8548i/wuwU2C3KUi7pnjInc09JgiRuXr+obNY2B2IrweWvzq0Zq6ozQ8kAaI8KhKo67PZv/nzm1WLxwz7EDq1m+efXH5/Axlpg3i0Xzn5GoLAcgDg7+u5vYMAhgGG4PsTbcC9/9vx6EWujmzQjwN69ooOaJi2YTIInMBxXRRdrdwgQGCCgPEV4aOubXsB7aMkTjmu7wUkjnoeahMw4pOUD+g9Iezz3NLGs4grmgxgmkYDHEFhD5gcxT2PIijCXZEobNOOvXJWtO1825rEuffS+6nnbNSvk9psn5f6AK4IHKzc4LXEPF8cRCMOZJLOKG+gKwxpQ8/kW2uNm+iS8kY/4NHugEo2i4oN3jGJscbFbJSd8344OSNOWRyusFTErvrbIAfp1dOt9VnVIB+lkYQ/KrfEwy5IcF3dl3djhWV8g67t6n4srA1RSnHObVX5YkRmrIuKNjrD+TQYQnma1oZztaJDagQyZ01JN9xIiL46Y3Fh5dtdiVJxTSNZNgjmOUitUvPjGqGFPr6dU/Tuxq3ReoQEA3s5qXaOt8tlEMs+5AfWeGkHhM8N457uMrNcV7W8HnenhDsf7zB8LqlzkJ1qV68E2vDt6iRciG26om6ZGVb5haqbHX68EKXbLhFl2Cb1cXVRMiXa5DpMCPXFHnOp9w8kQZv+tVrRULBJ7teKJJd7gbxig3saNmWjnEbpPm0bl7CuDnup0nNU3JidMN4jC4oMM+cuwumS1EOS2KVwA4Ge4YKUwiHGhlzBVUue7iHloPOr890drYoraco217g+XOXtmo22mVHHNxZ0lGffXsPaVrxxVN96Dux21wtV1Wqse8vpulZb81hcVvzu5J97Z9Oyq+YcnWXZOg1F3bcheyjXg+EQpX7S7pRxbwrMKw6cttqyGcyy0Qm+2/QpmHj8tKsncpgOlZGahmGc5DpK9ppwEevWLXFFONmjtk5COiSZ2iWN4pQN/XDTGWg0K9vb72pBN4s8KVwovZXHQmBWpem7ZQ1amj1xortEI7fTKlNGfoAvhnmJDqUWwRcZqdayuZQ3w257Xp7tlCuoG3aDdW4Kjr4cJkhJbI8BdnYSgytsmDmupLy+CLdgFzNRk+177FhdW+241W62yB7uRngpHCNkdnSG3LEilUq0oLfS0caxC6Y23AVLEulaR1MX31xBy/HkpE/+/qAWJrQvD33UBKFOwJG/3Zmbs5z1+O7q62tx8iFbLJeyd0mzwZ+K7X4rJxaWa1g5WWzY3Iqp03HsphPgZwV+yE3d7HN8ulwVMgti0+zR7SXuMindQJUA3XgPqu9WCsHru0wrVwyGIBDiPI9JKW7UUXa0DSRqTeGedtvBlKyL2NaVhLvJnnN31+36avYiyNwbtTs0ObPvFDsupYGFaV4ebBnJtqSkhJ1HbSabjzL6rGG1fEaQ7fFOnZK63pwOzOrUFshaxTfhiaWgJFwr0Jo2GRTXrpp4c26TebpGSIJaV3tfi2pnNvjNS+7U5rq6IbyG+NWW4MyhZe6t0++TjBEb9jx5/ImityAllqyTLlcWubnX8cllW5x28D6j9aRkReLq37FcgNy0wAQYxQOrU9sgylqu7pcbooCrjKVRgj9ybqDi56MiIAZrCdKZceU82kHwtNZOy1JzcLOJRLkzZWgfItJmj+75MjoX5a4uTdUhOkrdnW4EfGbgcEg2CZoLLXraH6vcoEsTh1eqV0OXeJ2Od/ac3PzDcieW59swMFPcrkhJsjalvFx1V7mU5VKC4WO+jVY0jq0YYROT7DG5CrupJ+n8GgWraQiCnSQrZng57HYUK/hre2lZVR2ZbZpsp649X7V2bxdpc5SaSef27Irs8FAzsjMWpR6zOZ13cdSemF0Z9dYKLa1lA958iO02Qmb2FuIom+mGJalMNpiVj6EZ74s0UQ405a6uy8HUKUjaJnSBc3DU6bk8ntwiyUqBGnBzhTUl5mKcgNoXrDnbpjnpR0w5Hlc8d1JWaSyTmMaoFb1PSiuh8jvZ+20jSuRmKykHjJU34mbMGFIeg3gIXC7GIw0A6JQMDrdndAk/8qfjmr2tqQH4x8HoGtlgKCtwpJBwmygb+GO9Ezjb2601/LTWBb4J75J19qnObrgzuzsr+6AdfOlO1RdJkNYkMBgSEWIcnCqJCXfVhmxsM7ngjoNWF4qfNnx8tO+byTp31O6OmPLlGjOnKuvDA1+WmatrUiPuJFzeaRhNuNBuxLx0J1Bxr1MnZ0eoW1Wp+homEauguRuci6aW+G2wWfL9JcbPGM83dy0Kp3s3QJsBovThvFzeyhW1Ox1Wo3q/5L5+KawmD2LSCiO+kIR2y+357GKF56TdNka9Xd57bXArM8jZfXF3nAMjTOoAdPd3k3XhzivtzLkqFaWUqAn9smQOyTnMESlU8YxzE/toj9F44tMsHe2stAhC5YXutr3A3uZWJMHB39lC5KakYnpuYwlHjbihRINBB8Onk0ASdmqtWgoRWOnyjEo9XZc7mNiIWtTa1hVy+uV+zzFuuLaEwb2fzqGEUIpkN4Yj2W6nmEdTGHtnCBvRWePsivb4Pg7sLaPaXMkFeM0w691+g0IXUFBFLBH4NYJD8lXXs4KXYDbShi4kwy67XKh9SF1lZz/l0CY6juG1z48NlxNxrYysFApaZHcXgTjD/U207R1/Gy5bOb4f5XvYX6+Wdzy0ksLd06VwlTI3m5abJcInbVh7WyGXz7HeixEeFsXoH65HlQfNxI3bFpiRRiv3OB4Q61SwDY9XdyQqXf/IIKBPCgd5x3KqjjblCRLvzRpf3V0xrE0uHWBun3RjpwqTlIRcYgg7y8KuziHimBsl0EpuxNJ1d0JjZ2kI/R5t8LtIZFd5reqDnYbJZnOeRGZgPMWa9BNS3gtcRCLh3k83nNURQk8ocV3bwuYgGwNyjrFlPgpujwRlnm+3rZmkm7VTb2s+HYerVIQh54cIG1tcifbDWqsT9SYVik3WwekQdSHM5GcZ8lKIOFlxCGyla/nNPacpMhlWLMBI1FUgNWrPIbyrNk5hz0yHybFo6jKZKrvl820nkGhPIdu0bWQ6vhzLbe/lZDoGeR7l7WTR3GiuhjO2hBGYMTb5DnC1G88YK7cMk3NeZEeLt2Way294aShJ7SBFK3lH3bhviHBrkyB2nI5fhbttZ4smKObEaWvqgdCfXduSa2LpEPrKuNAXE9/WJ590TeUWmiZHr3cHyQzYdQVja79OSvh6W+EO3K+PqiMTvmoHI8besvDKmPlgT34uYidkB8sMA29lh6sjqbSzG3UfGsY/iGBcgHc66/WYFUCQt73f7GQvOuUBTtx1qa2ggnT88qAg7LgMes7y3G1ciCd+xXjyMfLgWm3tG7HSs9tZoVYRU/vnSArPZDceY02y4XPGiamrbzZISzKy6k78zU1ibnXrtWNfMcSOoYpzup/GpqOvpJGNOa1F2tQfqAQitwNqsY199HRJ32UXfStEabEVS8t0eMU/ukbcMASGyewmtpeVYeystN5utzQXmwflggWqfoDXNBuxPKtoLnRW2VhQ/Q3Lko7dtyKX+aesbQz0jmOohjvnrQtadwPiNluUSNEjQnuQg6bWGtuOUhhc1okUV92W51nIjG96sd67KStc19cTnKfhvaSWh5yk6EDHx0AfNhB2OAWiZeicx1yqVeCoF3jPeiVMlUNhM05/ptVWDLfrNBSUxtkdTe2a7M7Aq2tXX29LZIuC8NFbhGWQbG1zirM3Ynit3vcEc2UsObruVvqlFniz6YeYMLa1Ihm4lSQ6KweSXWFxuZKvJcRJLbaDeKbijkOjX/ubebNO/WQx2+IqcsfTktEFBWGuXt8xBC1od9hziihsWrnvGxnWzmWoHuqqreQdWutcdcqcjTNoLimI3Y0JsUHkVmQThk01tvhu5GThXnm2aZFoRl705MAenOIYQafsoNr+jm3iQRwY5dzQImced+NmENg8xxDIP9w0iBJ2zkouQDJwJ+K8FYosGreuyKwHci85kozv3EOMC0uxNs+H8chu1gh9g1ewNEDbcKL82KSkYBD3Y3B0zp2j7hwSctUA3eGiSnRmHxaBXchKtBfPSt1sRvSI7uL7qrv7uk86+tZso1W7ZCwpSfZRwyaSZGxpI/a1TDil8J2oXX+kpantN2SfQo02HqV9klPUNRhkSlmFKyFuIk2q+aliliezT1UUymKv3CZR7R7usqDcE9boxaM10lHioUpy3+Pt2gokyLQQz5Uaf2eV9KrfhkdeUj2n9i+h6frXpZoNo9D2O1pH8AJls40p3SUevyiVarQ2Pi6FJqI5BYvr1MomzsBFCSZiMCy1XMI2oarA1mBoV12mDoSq5RUs66TnN+RSbrrgooIewrOkUNmmtFxQprHTNkGeOWYSb5K9zOFHWdfuu968LKGJKO9nNdL8jG1Bf3Vsj7GkBLsLzw/XbEPXS2Ud3WtD1E8DpR+4eOMtKwxvzKVzHe7j/miTxEEUi3DJVeuBOFjBngV+Y+X4ipXQcalzgWAe18CU7rGy7GhflZcjntTr7rYcSVcJ7LbyKQqhGCHrdVIwjqPB+SxnF62+Zu4IUxRYaiY8x+aTo4S3FJgPtDGtfSqEGxUmx6AX7OZypmlYb9ImStOeTTaadoNNeGIGdnXNgsNB2e7Rleo4uX2dTsruqlWVF4uj7a9w0bQ9WiFqe9NpeOglLpRrtj31AdNZqKXFfoaaZwvossN99lgubQJxvUGjckQpDyhB4bJ72OPLaqLdhvBQvarJ81B3+26PU3ezyupzddrDyxuKnJZRct0dxM7Nl5yyc2SmLKes2COqDzk7FtY1UhcMGcKsa+gTE4VxYASefG/bYZCEBGglSJje3Y0l0yBIwiDITSEi0IVPVXlE4M26KjOO90ojvicpjFZTaaDmIXIwP0QhP95VuCO3GtRv++1hNyXogaerCbJuB0psG2+F0kqgZgLJ3Hl2qUIXa62CmWHjglJPdzxEBQGEOwAqUf22nbzggGJLdSlBky2gLkkNYPit8FLc3Lmjx4lYKRGaBRJYORxNrJE27sjzOXbKpDukT7pX4Frqndjewm+EeIPZUZc3HEWZS0JXnNul0xF1p+R7tETVo7xq0ZAiuQuqOm5M7si67LFsvz/r5mipw4h2B1ptnBDFgnLvlFCQSKDRkYMBwnLPs3w/ozQryHEeWrKlCqOis2doWcyoMVx3eZFPvgXBpJZxts8SFJJer7xeo7qqEWgUuNVpeYq7FbWsNo6iHBSyPCq4nBylKuldtQPzy9XLLOoI9+eD19jEACK4RTZJdCGtO1Ldl9dVl/LqfutyJxQ6ohJuoR4BetjzwVDMGzNRQ40G/vUwsDlH0RKgICHmaRgb3rzhuHKA6Y3hbC6nFVuIrgIjCtZVYVaIU7nND0J4T27YxBCbS6qb/KjCnOmruq3kAYccxr18pDuLX/V0CLqA7uRLdpLQS7RBgsOE1z5ErsKDAGo2d2idqXSnRtd5hs7vEqJhl2NPZh4Wmx6MCkuDIlKl7a4Bex9WNHncJuMWSon6lrt2e2uvyiR4hp5u+Is7SRO86vbZ2bOwrrMZNyLZTi1wGCGFrAWtEME0ybIzOnGto8JuLV4QFBQSR8tDjAzj6k7xJEND+2F7weqq6afWV2ukvLWYyit7DykLBB1QB4kUSzbKLs2NCC0hpNleJdMuh8adQsIZUgIk1WYSYKaItnJVHg7irRVZi4GWN7pIzdVdag8Dzqw2qBZcsulk5CimWRcbj24Y02w8bFXxQ2fkDUEtJz8FudLcG4oeBasRBx5SqQC9X12cav04zbrmRqbHNRhGGOd2psblmhj2prcci7iugoAQyhFf0qA0eeuO2+n6NOyLVSeS9C7E+j2MphdCchkRKlYhZ1OsfvVuJInDJFEhRqNRg13djL1qXT2lcl1CguwAFL/NXoBGbu+WvrgpyWRzlAcwFkd1iSeI1hntkF95U9ayM6RWmybQAPREfVuHa9TyzvFyfzY0OkN30Ilzcwx0UPUVZ+A4KigiYNnovlrfGmWSsOVNZKZ946o7mNeGQQpWjjDkhr6jSrXB89q+Y4MXubU77C+kL/YxlVMliW6763LZ4F7L3I5XQwziW6JJ/DGQyKiizpKPyZTTlqMCukUyLwL9hq6W47QnlOaOKTtM3fKIYyPtCqYT3hnhzba7gVlCxnSRS31s0poT6isrG700GaYgegnpNnIyQqvCXGXUICetrQxhbxfVuk2tMYQmtq8nx7VLC5vKlJoQvrqWF2HKV2Q7OZEm8lbiRjtKJdVa7LqEhdW6EpKOGEF3e6Qa/tyx/unAFPdjquqnQ9LEBOyxnN/r7SZXzDK4HUZUNhoHM9rtRq8ICy9cuIDu270eRtkScRuebDCHB3GVI2pW1SpyFE+iwagSiZ73S+mkHX2lWO1BWJAoBHOJDF04zckjP6TKFTGxqUN3aqkXeVS5XQOdfDDbGmPLD5qDuDQ9DUh8VUefoYVDK5Jtn3PB5Yi6RO8qBynhr+elxxFoMUKq0Izu0hOczSqE7wgJH3Z2ilWtDIXNyZB4GEy4Sra/EUivtvdApb1Ex/Zlz+/KTR9zGCbRjCzcuoSJ7QFCMa5n9phWUNgYOI3cYauEvaeHtSZoNO8FIainIBidoOL9eHNc+9Nw4bEtixuXPW3itndBdq5+xe55SzVGS9wnPwhGvkMRMnfcldtATe4u7U7r+F1EHwgN6011oCachWHc94yWpLltit+j1iiaKg+QDd9g9P48nLtNvT+gzS03TMTujaW4nFRvbDCRDjIkF0XfvuINmprGNGShd+sCktr0y3Gw1ZQUraklEVRAqR1NlUUbdezAlMvtPpLO4e5+0ZcK3F80RpDJu1RHB5o1vE0zknexE9vBrK09g5PFhVKLPcoYCR+HZJuvjodQiTKvxVOvD6+kt6kcakQlemwD2ocMhtoe3CNG4z2J+bKfFb4+xuiZbyy8u9YWJpsjORyiVeWdAICZXmjCK4/tuxS6YhwEQVm3LntxxaDesExhgl4bzkVMjsb2OvBos+HJEFECy+u3tysYZ1xvmnCZ1EiszEqNYZi3d2/fDgff/rvPzs2HQP/PzqKex0ZfHn55HIL6tvfxwevjf1vCv717q9wYyPc8javTNnwdVv3DWdz7P3nMORMbnw+rfTnxfp7xN3Y4P+79FudeW4Px6nNdpI8HY8AOp63nh0Lr+blhF7x/f8b75A8+2N7zuRa/+twUn59HkvNRXZzPj7z4Xvzta/g6rXz35r0exfqMEavPflXOir+epgD6Yh/gD9jb3/83G7dIE7cvAAA= -->
