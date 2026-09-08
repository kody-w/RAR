---
name: "rar-cowork-cookbook-audit-analyze-worker-performance"
description: "Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_worker_performance", "rar_sha256": "5a2e1cc430eaa4f4fe96cd26a0f775882a592db0b3a15e39ba3f61a89677293b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_worker_performance_agent.py` and in the RCI capsule.

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

Analyze worker performance Completeness Audit — Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-worker-performance
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-worker-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 5a2e1cc430eaa4f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_worker_performance_agent.py` first:

```bash
python3 audit_analyze_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_worker_performance_agent.py   # or on stdin
python3 audit_analyze_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze worker performance Completeness Audit — Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_worker_performance',
    "version": '3.0.2',
    "display_name": 'Analyze worker performance Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5d67b66df9d69fe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-worker-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-analyze-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-worker-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze worker performance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze worker performance. Output an Excel workbook 'audit-analyze-worker-performance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze worker performance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze worker performance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit worker performance records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-worker-performance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants worker performance records in D365 F&SCM checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeWorkerPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeWorkerPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-worker-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
