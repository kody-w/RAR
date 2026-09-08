---
name: "rar-cowork-cookbook-audit-develop-loyalty-programs"
description: "Audits develop loyalty programs records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning an Excel workbook wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_loyalty_programs", "rar_sha256": "df555fd1c779f809db6e7607153c932bb5eae64b8a81535009f1f290d37e9561", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
