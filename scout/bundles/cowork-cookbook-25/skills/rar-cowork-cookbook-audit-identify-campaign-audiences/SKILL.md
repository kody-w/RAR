---
name: "rar-cowork-cookbook-audit-identify-campaign-audiences"
description: "Runs a read-only completeness and policy audit of identify campaign audiences records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_campaign_audiences", "rar_sha256": "a6ee5bfd72a382b234700ff22124ff616489f8b676c8d0f3741627eb88fe9c88", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
