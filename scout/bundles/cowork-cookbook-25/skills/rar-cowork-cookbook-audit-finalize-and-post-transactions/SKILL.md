---
name: "rar-cowork-cookbook-audit-finalize-and-post-transactions"
description: "Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_finalize_and_post_transactions", "rar_sha256": "22195cd6ca7cbc482706f24e32db29bbfb526d5e70a796a85841afaa79c2cab6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_finalize_and_post_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_finalize_and_post_transactions_agent.py` and in the RCI capsule.

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

Finalize and post transactions Completeness Audit — Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
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
      "description": "Date range to scope the audit; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-finalize-and-post-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 22195cd6ca7cbc48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_finalize_and_post_transactions_agent.py` first:

```bash
python3 audit_finalize_and_post_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_finalize_and_post_transactions_agent.py   # or on stdin
python3 audit_finalize_and_post_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize and post transactions Completeness Audit — Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_finalize_and_post_transactions',
    "version": '3.0.2',
    "display_name": 'Finalize and post transactions Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet.',
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
        "upstream_slug": 'audit-finalize-and-post-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ff8a248c59705c2d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/finalize-and-post-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-finalize-and-post-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to scope the audit; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-finalize-and-post-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit finalize and post transactions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to finalize and post transactions. Output an Excel workbook 'audit-finalize-and-post-transactions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no finalize and post transactions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads finalize and post transactions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet.', 'example_request': 'Audit finalize and post transactions in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to scope the audit; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-finalize-and-post-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants finalize-and-post-transactions records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditFinalizeAndPostTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditFinalizeAndPostTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to scope the audit; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-finalize-and-post-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditFinalizeAndPostTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
