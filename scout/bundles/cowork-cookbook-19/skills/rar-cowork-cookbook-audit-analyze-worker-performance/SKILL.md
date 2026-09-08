---
name: "rar-cowork-cookbook-audit-analyze-worker-performance"
description: "Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_worker_performance", "rar_sha256": "5a2e1cc430eaa4f4fe96cd26a0f775882a592db0b3a15e39ba3f61a89677293b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
