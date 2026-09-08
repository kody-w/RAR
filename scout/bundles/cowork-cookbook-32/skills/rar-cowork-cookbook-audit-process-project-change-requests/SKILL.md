---
name: "rar-cowork-cookbook-audit-process-project-change-requests"
description: "Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_project_change_requests", "rar_sha256": "f41ea840ed18647a826316e1937ea2505c49150da16f5aec230a3f076ebcceda", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_project_change_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_process_project_change_requests_agent.py` and in the RCI capsule.

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

Process project change requests Completeness Audit — Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
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
      "description": "Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 f41ea840ed18647a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_project_change_requests_agent.py` first:

```bash
python3 audit_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_project_change_requests_agent.py   # or on stdin
python3 audit_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Completeness Audit — Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_project_change_requests',
    "version": '3.0.3',
    "display_name": 'Process project change requests Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5a37476854b9583',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process project change requests records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process project change requests. Output an Excel workbook 'audit-process-project-change-requests-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process project change requests data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process project change requests records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou', 'example_request': 'Audit project change requests in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants project change request records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessProjectChangeRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessProjectChangeRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G8N2Kq6mK/LAIE7uiIASEQSEIIhBAqd7jYQez7Urf++ySSbFd1V9/pnphPI4cNJJlnP8856eTXN6ttwrx6+/SmeVa2EKwkiUKvWliZu1jnfV7F4JLHNvi7cPKsqSK7bfKqfvvw5nq1U0VFE+UZWK62Wb2wFpVnuR/zLBnB7LRIvMbLvLp+kCvyJHLGhdW6UbPI/UVR5XfPaRZOaGWBB1aWrVc34OrklVsvomzBjZmVRk69WJLEgv+f2vqw8HMg2yKIOi9bJF5gJQsva6Jm/ADWNW2VRVkAmC02g+Mli1n8h+R91ISLPPMWdeh5zaIACvpR5s6THavxgrwaF0XSzgpobZpa4PE5E4jp5C1Q1husWZ367dPPf/vwFoH7t0+/vjmJVYOhN2bWSalyB+iqPNVaP7RSn0rN5krAM5hajMDeGXgGQgBlUjDkev7i9fRj7SX+h8V//mfcW1VQ//Tpc7Z4/T6/zX+AmRdN6C2a3KobzwXiF5YdJcAC7wsm6a2xfhli1qUG7sqC9+fK75TyYvHX+d2PTybvgdf8+PktByJYszM/v/20AFb+/Fa18/37TKX48af3JO+96sefvtOpW/vhQEAMSP3+5fX8Igsmfp8a+YsvmrJZv3gBH0eFB4j/Tr/59xT9Re5lki/PyT/mxYfFn1Oe9fkrkPcZkDag++dkgQ3Ayrf3ex5lP754VDmIJCtzvB9/+mdkndBz4iSqm3+J7s9PwiHIA2Ctl0l++vBw398W0Eu3bzT/OdsCBMy/owmY/pXdN0P9M9oPz/4d6SQCmfrNl39K7s8WQH9d/PxPdfvvFnxY+J/fOC8BqVxZduJ9Wvz6CJGff3C/D/7wt98A6f8jGS1vK+dB4UtqZZEPUu7Ll59/qB/DP/zt5x/aAkSxZ6Vf2ir5M5p/ZtcHnz9Y8DXrxz+uBfz1LM7yPlt8y6HFr3nxP6rf3hcXK4nc7+P1p8XvM3H+QYtZia9Mnyb4XTbWQNbf2fGnt98A/GRAm9Z5vAb48R//sThETpXXud8sNIBXAERbgIqpNwt/DiMApvUDNSoP2LWOgGFf814YPEsMoO6X/+U8IP+j84J8+AHWc5bMyPblNfvLE7G/vBC7/uV9cQbE8yoKogwgssooyufMCgAyz4yLyqu9qgNgZY+N9xHk9Mf5Zgb4X/4l+l8epN6L8ZdHHYmeCKiuxRn96jbx3mc9jRCUhKdWDqgA3uA5LeCS5A4QyY8Ads81os6TDqDnbJM6jpJk4UYAX5q5AMy0gd0+zcR++eUX26rDz9kTrpeLZ6mrYTDhmziLjx+Bbn4SBWHzOfOcMF/88OtvPyz+a/HfrXoQn3kooHa8vAIklLSjvABZ1qZg2lz9ALxb7sMrv/72sjAgk4HSBXwY+ZH3XAyiNPbcr+bWtsxHjCAXtgfMDEycFnnVzGUuat4X4lxzX/ICpvOruUqEOai6rld4metloEA3oQXU+WbJLG8WNQjF2gdFtq29B9df7Mp6iJjOzmp+WRzWCqhJeQL+mcV8TAKL8ywC5v8WDM9xQKT6oV6wX0m8L+Q5LheFVVlFWFkvHr719Mtc8V/LAXFrkXn952yuwN5sqkeSPM0DJgHLOC+Xfpx9PnchABGe7UTzdY41V87zo4JWn7P6lQBW5T2aDyDKuAjayJ3Lwl9eIVWHeZu4D/sBSWdKLy+4L688YvDVAvyT1qYGrdTveqJH07D43GIIii/+f26fZsswgqBuBOa84RYb+ayaT4/NHeXs2WcTCuR4CPjIzu+NzVfw+orhn7MkAuFXjX95znz4+TXniYttBdyiMuqDPgiyWV5A95EDc0xX1Zw91ufsa7H4ACR/ICMIAwAYIKHmOP7KcH77VdIQoML8/L1xeFl89hGI80XR2sBPC9/zXNtyYiDV7NOvbs5mKwKr9GHkhH/QanYEsBugDywNRAWXPnv/BuDPt19F/8PCZ380L3n0ji1I4+pBAMjhzQLO0TO7EIjXPBt4oOenBxGgRlo0s+42SCSg6XPQm6MpqqNmBs2nXb0CoPbH+frUdB71hgJEIDAWyJCiBdZ95NQcFinofoAMAFZAiqVRBroBYJSXER4ErXQGCADAr3b1SfEx/FLIeyTiXMa+LpwVmdfMncHCB6KDkfH3OHL+szAB9NJ5xoPv30faN24z7RlLa4CHgOPXt88W4v3ZBTzbjMVXup/+YYf047+3iXrUdf2PAfBpETZNUX+C4Wct/lqK3wEgwE9Z62dZ/vgqmx9fSPDxiQQfv6LNH4g/9f60+PcE/AOJV4J8WqDvyDsyv9q/Auz1A/ZYf2TNj/j89nOmet/BFrDPUxBhs/dG0Ad8q4xfp4DyGFQAkMDkZ6Ws5wLbg5r+KA3AFZ+z30f8nHFPfUGE1vnvkODRIoDof3ruWwUDr7IG8Hbn1jLw3ucd2Sx+7b19ytok+fAGwNL7F/dyc6VK59Cu510gsD+AxCbyHk8PpBia+faPO+Tj48ZK3hecB1ApqX8ffq/6MtfX32XJU1GgoAM4fFi4wDz1XA+BojPzOcOsGoQsiNZZoWYsZg2e2765UZwXfOkBVOf9P8rDgZeL6lE85mivGyt5VptHA1//ZaFrBx5kcJrPjK0ZYlPQKgAb8iaQcPWnHB9F5cuzqPwJy7kS/b7uzDD7COYPC+89eH+w/FO63/rhfyRqgAZkpuPmn+Za/OEFauAK9jAfFt+2I8B+rw3izMHLWrD3/nneCs0OfSyZb8AacPm26Nv/c9je29/+TK4H8n2ZI+8ZP38vnTwjGkD82Z1/V1aBzICv2zreS/t/Ka0/YghGfkSIjxj+PiT18CfmAnI9AByUwVnF77b7rkH+2NnNGgCNm+d/RPz6BmLamn39iurX1gBMB3j3sZ4bIRgkP2AInp9pCt79320aXkTq0AL9KqDi46hnUTjiuShF4iuLwsglSnoovVx5YApCODiNEohroaRPWJ6DLRFr6SMr0rMdx3MtQO+Z8V/mli+aBZulAvb4CEDD+/4aDLkvjZ4azOb6tkeZNX8p9uubTeJg5havReb5W8M0asPGyh7ZLXxFoOFm8jsr0slk1TmNXpwz4bAKe1aeKnban8g257lYa/JJ9fe4qTs9p5xCKFfpuCNSt3AtsCQhthXdrteMtJWWbmZC/nRc0fexcwkyy7V+F3vXgpvEWrWDXVzqeuuPQxxfbpEkI5ljjAkTy8cSjy5mAcMd4uOltFuHfGCwaxkZz14kMy4/auooS2ao1iolqUhtOKwv3opteFlLnoTEvVrxqh1RI+RHFw9uzwMhDrfinhgGGZupWNh7kTXH3cUgBIP3DM+QtOJmnqWBXgt6bTcK5RVkikKSkWitKiWivhuTfewkzp4/aYjH9LujPk5nJ4rGzuoFA70GQFTdW0/nNQCz5d1ekcRR6VJIXt7Kc7iCoFXkoRBlICmlVWt4k9TlBYuP+yKinVLfxQds3ZpVIVzJi8APiXrKimrbDmnrmrgdey2/HprNoc+ZclgPqRRBh70ErB9KAW9criR+N2Le04i4XSNNj2uNyW3UliPV1uK1SNDk/SSsuF2TkMdlUtMXfTfl8nhSoNNF2okYop0pWtnBqS7xpsZmcgAzliJtSMNGJO0Eay2PFY58NbkxZqhAajQ2dPD2gFHXlnZXpxXsrMalFAnJRU8tc3fgR1mVbtuDdy7M+HCysFNfVKGn36xVejFj+VwEAsTTmWSg5LY47Qz6pEi39LRLTkVECGpBTQJFYaaSpXuaZ6FRYNENL1nJJeZzm9gHpBjraLDd+Ju7mIRNl1hS3x5PLgVvgruObGttqG0tukwUahB8YK0VJj6q0sBBMgfZJ4oRa5xKhO4whvp9jaCRrTdBdTKaA3OtpOYCX3YqVxjjVQ8vUWLUGLRvDgW3duO94yR+aOlk4LaaDDF3VMOHVjr3MQYzGVqw1EYbFPN8CAPDJ2r9JO9pUJn66JIaN/52vOcEk4Wp5XEUBSN5b6jQ1ODItE32/ADZPAbZgrzTiKbzPAni7tiVqQR+tKMDDElwr3Zw2h/GbuT2m5WwX1G+jwvX7tQSqnjeMZMo7iWsNS/ruBExU+ytTetUO7wOjunpur+ZZBBQW3wdxbpfWawGMSgf6Reanyap9rUjrtN8md1Xq5N7yIA1+FCKSy3ZKUy5s3kkVNbGnuRFDhZwmWhuZwKWB6YZUFKWvY2BB+UF30Db5HSz5PSG3FdyYJO+J2as1EEoXRHm2LiVKtxi834gj2rq3abb/arJqHbYi9mJILiUgG9EIeY1dzenlqq2Eo5ZcaNqctlRcXMUl7aIOW7VDENKZBdKGPvdVMGF2eI7wgYmFjIZX4n0xkfxy+4ulNJteToMSE9e2uDmQIqh8IkWHK5Qye92yl7ShM2S7hwtSWlRRazToQ9HqTvWyqQ7mLs8Z0VPyI4DXwIh6ZO0kI6UrSXodX1bmYw6Eg6aHW5biTOIzkALXpJEM1aVMiDo1fV2RLcUyZ7y642d+oluzlFXE3m3LFpdxmu929HUeVlYQXtwlsdlKqr3nbO83Y87PWwCs5ki6RjV5LI+idWd3fK3bSAjubCTHZQovJ1Yp2u9RK6FgLjJtvcnLBNQ1lUH9gD7xE13bBcuqPPhYukbNNt78JEiSPPQ9Mf4Znh6z237u7WKTlWGxuoFaS2aDMVlnIXUQfQTDSHRJbPmTZd2B4aLYmk/6jZ079zNaUT1BCGZ9eYuFQcN2pqYuPdrsRscUrq0B/ZcE0d103WDa6oMgNobVzksvWE0Zq8OzHbqe1SLg7tcMcuKhgmhi2/9+sQFAL6yLRGaByi/X0/i0rufMFHEZJ2zDNeKxT4N1seBK03a0Tztwqj4yTImwz+R1bmUTDLUT+V4wToENAq3K1tk5n2JyFS927F91x77wjW7WznlQb3pdobkIk7G6Qc8rf0CFu/MRAv+lYCczkaonFifx3HilZC3lRwpES3iOCzVqszJXTaMeOnMxuqyg1EmWDXIym3Wh107BhO+Vzq4isqRhmFo3EMq5MEunmqcIpXjAZng4VQHelhuBIxQlgGR6CeekKISzesLf+cjMT0vdcY5IRjqOysG1TVK1fbrdHkB0NkPIoW7ThxyGnLlyJKh1YbxdJoz+hs0+QSxjq/oTnLt65ipNVJvdUF3bsWyNnnJZry9BWldXK4ZweKybEj2l710tybSOsCOutO9i9seMnGS8OtFKSiecErKum/REXjGCC6bCzpWx51NL/0LZ60bl55iLjqT8QFym0O/Om0qfuzsqjKJukTPO4ESnA1rmJaaRu0WtTlYD6jTRlSvEyyEWAgqg9GttH2ccC13IW6X3lImk+ctgIzoZegYG3CdVlVettyOkYJzDF7pWcxazjZtZJm7KqlQFoE6xmtbPDoXMVE3FFNFe0/dFEhFdSgyu+liaYqkFxsu4NlhjU93yqiZa8dbw0a4hOuG4wbLF8GeaheYWheNYc+fHOMcItKaZDOk2gg8CqdZRbjFVdjupqBA74x+lEy1ZiljgpXbhdF2RXOWhRuaTsiZCyZWwadNJNpiqLXnFmuIgzuQOQb2RlFw0/jCk816E3rEqlNJ8ZxF7b4LkdjjGN7aGsatvOKRTh9LM1NO2f2UFniM3C57GUoJq9YZ36knUBEPmtFER2yjqZgiVvGpHuLd5XISGBQVNkNvRufryKuZ7nCtATebU4ZYwX23VpY3FxMD26zoSJdD0t6trOZ+25p8TOXJioTOpSJDiiWy5+ncL4+0faGcNdBALNYT6yvsKl67/Wku5ock57SVwlGr1t8jjgCT202J3Y8dmduxEKetLwwnxCouQpFpgqZJ59sgbkoH9Gx+np/WxtQIFh2tA7lXC9a/FRE2sjWVkUprcVbFwvFJ1LFbkR041U3KXciR+/Tcaa7b6PHJiTJegMz2xJgKs9zx6UY/BqNLnrW9AOBLGpqMb11GZdA6K3A0h/eOtdkBp2o+X8ikQ1pnnTudA7bPk3o3mlaytpQxEhAWp25lUzH1iV9ybggvaTjN7UsaTC4h43fuDB2XjWLbg0yk+dGYoM15XyWn8OhKSsCWiRJhGmwQklIpDmKFSnHEbtEmYU4xSo63TVCqxk0cT0Onn1CSmMqzzMWMW8XIBalLv/EP7cVWuRWeqHdt78nMMFxyg2U2Zbk673OLOeP73uVFVTrbql6gt2DIdmVA8+r5yjopD1kmW6NtfPc1I7k3iQjx63StbW8sV41JbONbZVh6hn0huPAYXmui4nz3UpwmaHuhEcj3FfOCQNoaE06jFBcYcbEllIdjnqs1JIHJM6+CflhfiSN68ndbyR4zp98luUOio5CcAnwX7AprO5X7E+13VUze/LtEwcJ5BfcKdeZZghrLq47GFd5WK90Teh0rybi9Y9C6FcTjftQGXYqOQZTlZ4sKk8mNlY6DMOqUanh1YG1vW2a9Gso9cdlc2VzfSkdBEre1aiRwKBXrteXYuZlCOK9qxk7Fg/vBbVZTcGH0i1TiAR6Fe/m0hYILEt+LpnNFhLWLaXXewHh7NNFDXPtsEKTq0gnyKwoiMqwojjEg0r0guiVDg5WHujldsmvFxVk6nYc6zVXKzOtAafZuU5v3eyjvRqbwuc0l29YYaDmNDVEGE0/fyTA5ehMmTsJWKUkeGTdVyUFowDLnQxKZ0SYXTy4hmrpwl++3UmabfYvyRcUoNhpqCD5hiIhC5n2/tdljA8eFj23pAyUsL8tpGaQUS7O7q2Btgiipdr0h0HjOniW/k82wKE/HjUQjphyynbvV40vE7nCSvQhTWjgmdz1ihuVZ+/7cyHFfQaO1YXa1ldNbmuG1DUbxN6OQuTA99Tafc/QQNrAG9kM8tKrZhk4PFX+7cs4mXlusqlKjUe8Z8ireNAjHwf5viKIwL9ntusuS43rXqzwT6V3jwPD2ilxLpT2Bsst3a7g93m48LAmIQYONhrVFpYK7Kf5W0MtTtjMOt915agcTXle5LQr4bu1jADQE7+i3Nx9sY3tmMmU9J4SUC8V17pFYfV9aiEix2/1BZTDRlYUKDbLdkdxXu+zGJYqhS63bu+V0VqFevTI4gZ+2A4/yTjGklzMPoSXt6whXk/0Oous7tF8R2dmJ01xZmn2/tahqI0cEUjIdXEst2o/7XcCZESrXNYkZJNpf0Czly9CCRqNkKUXVJsgSmVtVZbakUG58SFui3g1VfYUY7C7ilikP0EpS1Q1xc4eCcE9sAR8YnOdJH5GyzO0vXB9FeRtIayZ3ax4z0kbjL2en9qI1IbvKbYgTTOz37HFM5CMGhUnMmWwVTFwx1IHdDbZIHDtqzRioOim1JQWrTC1LnDYiX5CCSTnb91InmzU9XM2YWg5LOzFWp6Sia8nEBM72zlwD+s3ptDksZeSGGtTaccSuwXSr6r3zZBm3bEntC30V0FFHsEQHjOhh+xa5Tf1AbtFG3U6u11DItBwVo4SueytrYrzDBtmVSZRYCoTGOnJUA6hTMM8LQqQt2tGvluoqiNbDWexoJzWN5Rls1jG/7SMUPq1cURB8W7YSBQFPlwi72BUUKpN6sqd2c1VVOGpZNVzvkSAOY3qLNcxtsKNz2dW8iO1Idt9qmtVhxdZ0Wj5zdpRCa+u0mtyGDvu9jeOm4hpV2JyXfLpMIbCF2Pe9y3Yqu22wAyoejuOt6hgYhvklzDqVYLhx31UZTF1gCbMsS6DJzvWWJxuvMzmUquzUyLgGswV+i5A9ZyIsf11q+2wFhUcGoi8ZZBrjTsxA63VileXh2jNxLI8+RdlQeVZsjq3P/GGvXI9jjonyWbna17YJxSGtAwkL9T3S9auM2wrO0oxHGL/cY1jd8Mti2cIrW8MVzePW2l6/KiBp266FuVrakCKy7PD1Blq5QzwiV80vlE2pjjdItMj06orLq5G5m05L45WFW3K058m9gVir2Npil4uyz1AT9sKQjt1DEzGHlOEPICFpetWv7Jrehtszq8VpUlUb/nbgzp7GX5u0Mto74aWtruh42UtcBbm1itP1KvY66l7XOCGwGXS/ATQq/chr+QI/uXSg7pBUi+6aZBmw4jKmq4OWaXMMzB4+650Gt2v+YLVx6Q9nGQ1Ba+wE8n0d9PTGrTY3ihRq9QjRpJ7UBuhncGFieqTutvLawW09WtGXM4FTvletum7us7HjbTcoe263khEC6ts6uFTejr6n5hKSQuxuXoiGBs14J2A5p9z38HiPD+XUJUYZm+y9JduBPzuhbh9zT4688rTM7EIwLtQGC4Srd7pPVi4izkRnbdq2nXU7rMJqgiK8LMRgaoVYPvCuRgkrc5Pc7MCkt3cLk9YQHXsUZJ5XTNo4YADlgwl0ywLWK2abS1OTHGLIaKy9nQ0IUjhhOJ7jmtjyCMrtUQgztqkcsMRyk4Yl0dlb57AeWZjeorsLJ+RRj227YKfUUVugmzpWioRTd/TEblPOwvBGx5T7sTlaDYrE9GQvPfrIUB4pXxqwb1NoyMVa28mHho2KuHMj8upQR+8YTU7lufvCL2IK7Cm6ne2RUKPhHduYy6NqoBx3T8nEWWVuUbuJfMCSkQqi9KB0u53NCB2D7J0RvUF+nTfH0o1kgXM9J8AkniBM90ad7sRA4CRkY9dwSFYESvnSbrk+nNKd2YnHQtJvaNjd0H613lhJt0pu9EoQ8YxS+CFgSaxIs+UwRdFepmDQLEiD793y3eAHtLYTkqmgNoJQxdrapW4CgQjolLoabm0pRvXonW+6AtErrNR6AGuABXQAI2zdOCp2mbZCcT9kFALulvHVx5ANyUClfVfZQQxllQ+OU9szEHrimmgl4CRSKqAX5nfKakWscVvqjbs9Kv1YwGpQCMt6XyMQ0t3GmJO65hQtV1eqGexmhYIcv+8FqnZ36d1NLAKDJF2vOFNEV8LRFrt7j9WUGaCYJvQkyQeOQO8bOc22ldQginRloHyvLzfXK4kqDs2b3lm8rWHKtdluA99TD2G7Ag0OpE6dTwzS0EjGemPG5qQK7f1LGsudhcjS2mPsbrvdOTGWL6kiutwNCL23W5u+qtuES5N8CMsyhvsSxT0nhXzyoAg+Qt4w3da2BV+YAXla1rFDMXHDQL6OKxzE04RP6msWvpPyKpi8wCkuOOhMbnTX6iXGlaJ3NZb37WAb7CELqasGX5WaIJ1NQvOdLg42mTpQjhe1mWNDbLh5fzB02aVNrDr70RYjLNuI6Ijqj2e3weik8aihE/HeoMVN2ppsUJ7XauOS0/4gYlg7Eqvg0jV3ZH3Q2CpL7OAU9ddqpR4ZbztRNcOFiAmzSEIOlQxUXAnWiTLiY0ZHCMQWR1lwmwaqD6TSMCHdROW21reDq3Pk1CNjVYZ43HWy0oSW1KBe5hH3NuiomxvoRwhm3SkkWQGmSyaFHfkY+o4wOf5m4mRiI6yauG03Y3kkSwttN+10ha6n5QVaG5urTcDrSWpuQ4nGd+qIBvaqcFsXw9HONQ9UXw0+Lfd0FRxOysbvADaoYXoP9/up7Xh34zdyE+h0QLeqxiHOaedLfK7xImclJj2lJVOJTKG46jYeoLjJVJxqy3DCUYTj71K/3d7WSiGzKc7pgbWjh9FPFI3TJod0CcUO8xAll+bydsvPNt1CJA81TO53OFEQQN7O0a4yrGcpiDzcqpaHrjNdjUgP0VJR2XWmqwg1Mm0ItlpLv0prP1nCkAzJp7sLMfUZ1FZuu1SlRB/TIU2oC21zAeEfWBBQ8UrXVsvT9t7V8Km5RoNhxfF8jPLXv759ePt+XPb2730BNh/j/D87MXoe/Hz9juNxGOhZ7qcHr0//plx/+/BWORGQ6nk+Vidt8Dpk+rvTsY//0iHfTGJ8fl719Tj5eUjdWMH8DfJblLlt3VTjlzpPHt9zgBV2W8+fLNZfpf79ueaD63PgoUiTz7P8x1iUzR9peG5kNd7rMXgdGH54c18fEX1ZksQXrypmTV9fAgAFl+/I+/Ltt/8NTQKWgEcuAAA= -->
