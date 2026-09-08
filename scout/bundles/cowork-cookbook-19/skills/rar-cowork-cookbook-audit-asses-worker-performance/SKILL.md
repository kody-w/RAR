---
name: "rar-cowork-cookbook-audit-asses-worker-performance"
description: "Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_asses_worker_performance", "rar_sha256": "f4383a7549df8524d4b1dc680a9213375a660dbfd40c04b6820661c037ea1f0a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_asses_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_asses_worker_performance_agent.py` and in the RCI capsule.

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

Asses worker performance Completeness Audit — Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-asses-worker-performance
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
      "description": "Date range considered current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-asses-worker-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 f4383a7549df8524…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_asses_worker_performance_agent.py` first:

```bash
python3 audit_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_asses_worker_performance_agent.py   # or on stdin
python3 audit_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Completeness Audit — Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_asses_worker_performance',
    "version": '3.0.2',
    "display_name": 'Asses worker performance Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6449880d3f05e5f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range considered current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-asses-worker-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit asses worker performance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to asses worker performance. Output an Excel workbook 'audit-asses-worker-performance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no asses worker performance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads asses worker performance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit worker performance records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range considered current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-asses-worker-performance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants worker performance records in D365 F&SCM checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAssesWorkerPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAssesWorkerPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range considered current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-asses-worker-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
