---
name: "rar-cowork-cookbook-audit-track-and-analyze-software-licenses"
description: "Runs a read-only completeness and policy audit of software license tracking records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_and_analyze_software_licenses", "rar_sha256": "cd23d35dca26e292d66c86fe1d45a7ebb6f5254ad5ffb1bfe2d08f31a155695b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
