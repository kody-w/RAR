---
name: "rar-cowork-cookbook-audit-use-the-knowledge-base-to-find-a-solution"
description: "Runs a read-only completeness and policy audit of knowledge base solution records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "dcc9a5094f854bec8728dca408fa0c8ea98d87b432580d14c643cc84eb1818e5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
