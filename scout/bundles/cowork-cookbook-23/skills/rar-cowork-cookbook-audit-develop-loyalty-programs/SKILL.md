---
name: "rar-cowork-cookbook-audit-develop-loyalty-programs"
description: "Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_loyalty_programs", "rar_sha256": "df555fd1c779f809db6e7607153c932bb5eae64b8a81535009f1f290d37e9561", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_loyalty_programs_agent.py` and in the RCI capsule.

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

Develop loyalty programs Completeness Audit — Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; recipe default is USMF.",
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
      "description": "Excel workbook name, e.g. audit-develop-loyalty-programs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 df555fd1c779f809…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_loyalty_programs_agent.py` first:

```bash
python3 audit_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_loyalty_programs_agent.py   # or on stdin
python3 audit_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Completeness Audit — Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_loyalty_programs',
    "version": '3.0.2',
    "display_name": 'Develop loyalty programs Completeness Audit',
    "description": 'Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit',
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
        "upstream_slug": 'audit-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a03177fa3d36895d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; recipe default is USMF.', 'output_filename': 'Excel workbook name, e.g. audit-develop-loyalty-programs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop loyalty programs records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop loyalty programs. Output an Excel workbook 'audit-develop-loyalty-programs-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop loyalty programs data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop loyalty programs records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit', 'example_request': 'Audit develop loyalty programs records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-develop-loyalty-programs-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of develop loyalty programs data in D365 ERP via Cowork.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopLoyaltyPrograms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLoyaltyPrograms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-develop-loyalty-programs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
