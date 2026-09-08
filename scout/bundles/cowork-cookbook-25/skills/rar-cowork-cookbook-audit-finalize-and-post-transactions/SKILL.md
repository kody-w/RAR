---
name: "rar-cowork-cookbook-audit-finalize-and-post-transactions"
description: "Runs a read-only completeness and policy audit of finalize-and-post-transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with findings by category plus a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_finalize_and_post_transactions", "rar_sha256": "22195cd6ca7cbc482706f24e32db29bbfb526d5e70a796a85841afaa79c2cab6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
