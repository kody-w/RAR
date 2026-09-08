---
name: "rar-cowork-cookbook-audit-identify-campaign-audiences"
description: "Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_campaign_audiences", "rar_sha256": "a6ee5bfd72a382b234700ff22124ff616489f8b676c8d0f3741627eb88fe9c88", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

Identify campaign audiences Completeness Audit — Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-campaign-audiences
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
      "description": "Name of the Excel workbook to produce, e.g. audit-identify-campaign-audiences-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 a6ee5bfd72a382b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_campaign_audiences_agent.py` first:

```bash
python3 audit_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_campaign_audiences_agent.py   # or on stdin
python3 audit_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Completeness Audit — Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_campaign_audiences',
    "version": '3.0.2',
    "display_name": 'Identify campaign audiences Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ee67787ac18b713',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-identify-campaign-audiences-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit identify campaign audiences records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to identify campaign audiences. Output an Excel workbook 'audit-identify-campaign-audiences-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no identify campaign audiences data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify campaign audiences records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit identify campaign audiences in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-campaign-audiences-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants identify campaign audiences records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditIdentifyCampaignAudiences(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyCampaignAudiences'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-campaign-audiences-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
