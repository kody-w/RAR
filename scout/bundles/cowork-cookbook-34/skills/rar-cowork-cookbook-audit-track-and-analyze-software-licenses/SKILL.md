---
name: "rar-cowork-cookbook-audit-track-and-analyze-software-licenses"
description: "Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_and_analyze_software_licenses", "rar_sha256": "cd23d35dca26e292d66c86fe1d45a7ebb6f5254ad5ffb1bfe2d08f31a155695b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_track_and_analyze_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `audit_track_and_analyze_software_licenses_agent.py` and in the RCI capsule.

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

Track and analyze software licenses Completeness Audit — Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses
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
      "description": "Name of the Excel workbook to produce, e.g. audit-track-and-analyze-software-licenses-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 cd23d35dca26e292…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_and_analyze_software_licenses_agent.py` first:

```bash
python3 audit_track_and_analyze_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_track_and_analyze_software_licenses_agent.py   # or on stdin
python3 audit_track_and_analyze_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track and analyze software licenses Completeness Audit — Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_track_and_analyze_software_licenses',
    "version": '3.0.3',
    "display_name": 'Track and analyze software licenses Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-track-and-analyze-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b25e3de9fdf87f6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/track-and-analyze-software-licenses'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-track-and-analyze-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-track-and-analyze-software-licenses-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit track and analyze software licenses records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to track and analyze software licenses. Output an Excel workbook 'audit-track-and-analyze-software-licenses-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no track and analyze software licenses data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads track and analyze software licenses records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit software license tracking records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-track-and-analyze-software-licenses-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change audit of D365 software license tracking records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTrackAndAnalyzeSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTrackAndAnalyzeSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-track-and-analyze-software-licenses-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditTrackAndAnalyzeSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
