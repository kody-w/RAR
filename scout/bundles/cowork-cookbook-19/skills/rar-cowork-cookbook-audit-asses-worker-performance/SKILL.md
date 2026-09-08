---
name: "rar-cowork-cookbook-audit-asses-worker-performance"
description: "Runs a read-only completeness and policy audit of worker performance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_asses_worker_performance", "rar_sha256": "f4383a7549df8524d4b1dc680a9213375a660dbfd40c04b6820661c037ea1f0a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
