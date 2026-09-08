---
name: "rar-cowork-cookbook-audit-create-knowledge-base-articles"
description: "Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_knowledge_base_articles", "rar_sha256": "1b55d56b61f26ffaa6aaa444635ba4e026b8ddbcac989c18f5d18d48d06909b8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `audit_create_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Create knowledge base articles Completeness Audit — Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-create-knowledge-base-articles-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 1b55d56b61f26ffa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_knowledge_base_articles_agent.py` first:

```bash
python3 audit_create_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_knowledge_base_articles_agent.py   # or on stdin
python3 audit_create_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create knowledge base articles Completeness Audit — Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_knowledge_base_articles',
    "version": '3.0.2',
    "display_name": 'Create knowledge base articles Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-create-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f44324b6ee6bf4d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/create-knowledge-base-articles'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-create-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-create-knowledge-base-articles-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit create knowledge base articles records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to create knowledge base articles. Output an Excel workbook 'audit-create-knowledge-base-articles-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no create knowledge base articles data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create knowledge base articles records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit knowledge base article records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-create-knowledge-base-articles-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants knowledge base article records in D365 audited for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCreateKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-create-knowledge-base-articles-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCreateKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
