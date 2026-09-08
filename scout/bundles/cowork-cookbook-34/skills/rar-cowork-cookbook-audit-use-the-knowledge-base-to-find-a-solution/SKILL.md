---
name: "rar-cowork-cookbook-audit-use-the-knowledge-base-to-find-a-solution"
description: "Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "dcc9a5094f854bec8728dca408fa0c8ea98d87b432580d14c643cc84eb1818e5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use the knowledge base to find a solution Completeness Audit — Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
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
      "description": "Date range used to judge stale dates (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-use-the-knowledge-base-to-find-a-solution-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 dcc9a5094f854bec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_use_the_knowledge_base_to_find_a_solution_agent.py` first:

```bash
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py   # or on stdin
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use the knowledge base to find a solution Completeness Audit — Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution',
    "version": '3.0.3',
    "display_name": 'Use the knowledge base to find a solution Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef59277245f63399',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-the-knowledge-base-to-find-a-solution'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-use-the-knowledge-base-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-use-the-knowledge-base-to-find-a-solution-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit use the knowledge base to find a solution records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to use the knowledge base to find a solution. Output an Excel workbook 'audit-use-the-knowledge-base-to-find-a-solution-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no use the knowledge base to find a solution data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads use the knowledge base to find a solution records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit the knowledge base solution records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-use-the-knowledge-base-to-find-a-solution-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit D365 knowledge base solution records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditUseTheKnowledgeBaseToFindASolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUseTheKnowledgeBaseToFindASolution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-use-the-knowledge-base-to-find-a-solution-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditUseTheKnowledgeBaseToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
