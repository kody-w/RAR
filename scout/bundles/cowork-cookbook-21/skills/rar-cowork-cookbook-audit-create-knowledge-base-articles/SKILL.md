---
name: "rar-cowork-cookbook-audit-create-knowledge-base-articles"
description: "Runs a read-only completeness and policy audit of knowledge base article records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_knowledge_base_articles", "rar_sha256": "1b55d56b61f26ffaa6aaa444635ba4e026b8ddbcac989c18f5d18d48d06909b8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzFV9WRfsUrgjo4YxKIFEDtClCtc7PsOEqheffc5SPfaVdXuN90T89fIYUvAObnnLzN9+O3FGfq4al8+vWiBUy52Tp4ncdAunNJf0NWtajPwVWUu+LvwqrJvE3foq7Z7+fDiB53XJnWfVCXYrg5lt3AWbeD4H6syn8Dqos6DPiiDrnuQq6s88aaFM/hJv6jCRVZWtzzwo2DhOl2wcNo+8fIAUPCq1u8WSblgptIpEq9boGt8wf1PjRYXP+ZB5OSLoOyTfloYmsj99CDeBv3QzhKUC3b0gnwxi/6Q+pb08aIqg0UXB0G/qIFyYVL6SRktPKcPoqqdFnU+zMJrQ1E44PKx8hWoGIzOrET38unnXz68JOD3y6ffXrzc6cCtF2rWhAYa9wH/rssWqEI9NZltlDtlBFbWEzByCa4B97BqC3DLD8LF29WPXZCHHxb/+Z/ZzWmj7qdPn8vF2+fzy/wH2HbRx8Gir5yuD3wgd+24SQ4s8Lqg8pszdd/0X3TAR2X0+tz5jVJVL/4+P/vxyeQ1CvofP79UQARn9uDnl58WVQv4tcP8+3WmUv/402te3YL2x5++0ekGNw28fiYGpH798nb9RhYs/LY0CRdfNJml33gBxyZ1AIj/Qb/58xT9jdybSb48F/9Y1R8W36c86/N3IO8zCl1A9/tkgQ3AzpfXtErKH994tNU1KJ3SC3786Z+R9eLAy/Kk6/8luj8/Cccg+IG13kzy04eH+35ZLN90+0rzn7OtQcD8O5qA5e/svhrqn9F+ePYvpPMEpOdXX36X3Pc2LP+++Pmf6vbfbfiwCD+/MEGeXEHcuXnwafHbI0R+/sH/dvOHX34HpP+PZLRqaL0HhS+FUyZh0PVfvvz8Q/e4/cMvP/8w1CCKA6f4MrT592h+z64PPn+y4NuqH/+8F/A3yhnBysXXHFr8VtX/o/39dWE6eeJ/u999WvwxE+fPcjEr8c70aYI/ZGMHZP2DHX96+R2gTwm0GbzHY4Af//EfCzHx2qqrwn6hedXQL4CD+6QIZuH1OAEI2j1Qow2AXbsEGPZtHYj/2cOzxACGf/1f3gPnP3pvOL96IPQX7wFsX76i9JcZpb+8oXT36+tCB7SrNomSEgCySsny59KJADDPfOs26IL2CrDKnfrgI0jpj/OPGdR//VfIf3lQeq2nXx/onjzxT6UPM/Z1Qx68zlqe46B808kDwB+MgTcAJnnlAYnCBND5ALTvqvwKsHO2SJcleb7wE4Au/Yz7j8oxlJ9mYr/++isQIf5cPsEaXTyrW7cCC76Ks/j4EagW5kkU95/LwIurxQ+//f7D4r8W/92uB/GZhwwKx5tPgIRHTTqBshcNBVg2FzwA7o7/8Mlvv78ZGJApQcUCHkzCJHhuBjGaBf67tbU99RHB1ws3AFYGFi7qChgRVLekf10cwsVXeQHT+dFcI+Kq6xd+UAelH5SgJvexA9T5asmy6hcdCMQunD4shi54cP3VbZ2HiAVIdqf/dSHSMqhIVQ7+mcV8LAKbqzIB5v8aC8/7gEj7Q7fYvpN4XZzmqFzUTuvUceu88Qidp19AJXrfDog7izK4fS7n8hvMpnqkyNM8YBGwjPfm0o+zz+fGA+DBs4Po39c4c93UH/Wz/Vx2b+HvtM9+A4gyLaIh8eei8Le3kOriasj9h/2ApDOlNy/4b155xOCz/v+TZqYDzdMfuqBHw7D4PCAQjC3+/2uYZnNQu53K7iidZRbsSVcvTzfNnePszmezOQsCYvWZkt96mXe8eoftz2WegJhrp789Vz6c+7bmCYVDC3yhUuqDPoisWVJA9xH4cyC37ZwyzufyvT58ADI/wBD4HqAEyKI5eN8Zzk/fJY0BFMzX33qFNzvPxgPBvagHF3hnEQaB7zpeBqSaPfnu3HK2H3DZLU68+E9azZ4AFgP0gY2BqODrVr5+xezn03fR/7Tx2RLNWx7t4gByt30QAHIEs4CzW2fnAfH6Z6MO9Pz0IALUKOp+1t0F2QM0fd4M2qAZki7pZ6R82jWoAVJ/nL+fms53g7EGCQOMBdKiHoB1H4k0B0QBGh4gA8ASkFdFUoIGABjlzQgPgk4xowJA3beAe1J83H5TKHhk31y53jfOisx75mZgEQLRwZ3pj+Chfy9MAL1iXvHg+9dI+8ptpj0DaAdAEHB8f/rsGl6fhf/ZWSze6X76h0nox39vWHqUcuPPAfBpEfd93X1arZ7l9736vgIYWD1l7Z6V+OOzVH78mv4f5/T/+A4xf6L9VPvT4t+T708k3vLj0wJ+hV6h+ZHwFl9vH2AO+uP28hGbn34u1eAbwAL2VQECbHbeBEr/12r4vgSUxKgFgAQWP6tjNxfVG6jjj3IAPPG5/GPAzwkHqk0ZzQHaVX8AgkdbAIL/6bivVQs8KnvA25+bySiYh7hHenTBy6dyyPMPLwAhg39teJuLUzEHdjdPfSCFABT2SfC4euDE2M8//zwHS48fTv66YAKASXn3x+B7KylzSf1Djjz1BPp5gMOHhQ9E6uYSCPScmc/55XQgYEGszvr0Uz0r8Jzz5s5w3vDlBiC6uv2jPMxcndrZgjPbB96lw1xDut75Vjz+9qgMII2LaubvzDhbgCYBWJK7AEE332X8KC1fnqXlO5znIvSn6jPX8tnsHxbBa/T6YPldul/74H8kegatx0zHrz7NVfjDG7KBbzC7fFh8HUOAGd8Gw8ccXw5g5v55HoFmvz62zD/AHvD1ddPX/9Rwg5dfvifXA/6+zPH3jKK/SneaYQ3A/uzVv1RVIDPg6w9e8Kb9v5LbHxEIWX+E8I8I9jrm3fgdawGxHiAOSuGs4TfTfVOgegx0swJA4f75/w+/vYDIdmZXv8X220QAlgPM+9jNHdAKIABgCK6fuQqe/V/NCm80utgBfSogArs47uNrdw2HyDoMHWftOA6GYWsUdx0sACq7hO+7nuORBOnBRIj7MOFjhA+tSYh0CUDvmfVf5lYvmeXCyU0IkSQSYjAC+X4QIpjvE2ti7eEbBHJI18FdnHTcb1szkC9vyj6Vmy35dWyZjfKm828v7hoDK/dYd6CeH3pFwu7qvHEnwVpZEDHmN6Np7HPlMs5ma2tuAsGdPe6gSbGRvrNoTk34PVuIvC0IzH2gLw4lQ1rYZSsVvXeTomDNVErjSb5fDodD4UmWXITyRircfSodJN2Sm5zj/GMQy4JHoxyULDNCFie6ONrJ8QQVxHnKD1lHX3cE3Zy0lXS6hmNYmubhYCHbQWIRPaA9OsCnMKaPAjalF9peljXfMTS2pTPJjg/OkS0lTAvHjovDdI0gK3YiyaAUbucKToaVmR7qw50vw3TErpYgqrJsm2U+smxyT7GdGF9Qx1rD+klsPVUydzhbGLHi8sagTubUVYkmZq1x6EQSLgaS5fKQXbFnGA1bbNJk/xYwOEkuwxJFV6sTajd6vCGWG+IIBwQCxZ0g7gatmDKUV/DO5XgP5oYqOrAiSthjqIhXqBLblk9idkKie+zgDUOaFOypflLvq8PWVJjB1lKpxIl7oJN8wiJKatTWla63kkik9IkIXRnKzh3oYw5M6OCZZdjNQaKQQRR6cb20wHzF3bHRc5c1mq9dU1zRyk1M3C0T0sQ5O4yXxMwHWWP41ZbVCi0/JgraSHXB3s4uXOIHCqcMh5UQbHsIT7ecJSscqUnMLvOr3u15Q7OrCCNN1mSzysMxiUu0Ue2qLFdQouum1DbNJEKlggrX6NkoXOta5zGNNPGdt2TYV1n7PBW7GJ+KaY2yaJ1t/AOztPY6dcnjo3q2TXvbSKR2ndIjLdhLTZ4OrOA47lrMboNE+cSKXdEQtOmCsXO325WpXtULH5fKlskST13d9cCCBIbf0OLxfh0Plc/f/O25MBmLz7atdjthkwPSVevUtR7zbdSMmrtzAnPITBU/TNz6QK+whjkZeHm0CGq7rL3KVeOLtg+p1bKKIFYftY1CxN1Z3tZWNW4JIkBGgDIGbtuivTpRNXZZ77NhtUeKHQ0XG0nWI0o+9rJ758MShylFKza6Q+QjsSs9ZBtAvLfamUsiJmPGX0FXJ1tBrHEkRUuGAGJIVmTxmJqXfLihOKGGrxd2mXdH3L6tElruWv5SaLvgCm9KmqkuKU8oysAVEhqxVnFSoY6h+mIzNQiTHpFuGiceRo8IouDOQFJGqtk8xFFmcNTOZyaRlDMkyUwh3G6yJFboEAS0PWw3yrG+RYi4VUuhvnv3zaHu7jKT1sgxqMgbH3LI8ohqd1+p1KlkjVs7OpWJ1VtG5ndalZxjla2R68G77/Eyu3Bm2W3u032iwzKxG8VkhHOyuq/FKrQb5tgig1TuXMe2Vm1LteI1hhM4Ah3NleZPknaQjgiPtYfmoEpKLFIuVu+8Ru0PqAXlHkPJmmfn68FVSvWWc9KY75BDil8vDr4mgzivif3SyqY7dhHutmBLO5Qvcum+2su5sWrvU5ZOY7MXXNuKErWkILUhAobH6xbqnUY+HI/HLZtsc2gvl9JdGHeq4m299rpnUOi0PPall3uEuS4lbSlieyEPYEHdxfcS22ErkqCWZStcb7EIdxpceYFzg0oh2FJJJx5RenM5tJnspOcT55k56xnDRSCQiGt4mshGyL3T/dXUbGV7I+aqY3k9TxhLieQ5jQYNZuftSW9j+f20zOxzYIyMeyuN06Cn+4k4NJvzSSJiyB2sm8zB8mRuSRqPt1ogkfIlimOay2r2SKboNTEcKLlWEBWNFJ9cTKaDq+0uw1VRIU2ovFR0fZm84hjIO/1GHxNzdycs1sTklbI10hg6U/EuBljB+AVhteQan5qunnYaSe2u+W7axcplnU1r5KBPKVaw+/tJU5wdaZcXACz0XmEKY+MlmmqOdaPw2mhdvdplqiNvMTodpQrbXsP6qF21krQkfN8eQNxDBhMq0DV01mMgmKW8DQT/XAUbxCgFpnAFiUMlWtqIq6ve4NL9NKoZV3JjwYfOcZKPuHnId2uLFDNU26jr/Z7JpBW584urPMTKSdt0yynam/Khkte34Cpka8KX857klwE8kZpu+I1RStaZwuss1DbAnox+yMtbiAp3CIOOmn2Az82UVJdMZ5cWdkmbXYGkGOkxhuXi9JbY2W6uxnogariqbHB7RNWOqTN93E31qE2m3kR3icl5VcFrdqSR89apc7HdTVMX2erIVJOrqAeqN3djEVZ+jkO+FygcjyfdnZHxyz1BjVpdmktsIlKlTXxzKFdlHucbuJPPN4M6OltHtYAfR50ZiL1iK2eh8r2o0pRbXE1qXzL8Nrtk6ibQrxA1XkyQHxN5i3YBVR95fnOFCd1XTyNzSPhlWK1lyEyoKadttaNwGBOXU9NGkFus+AriVpgtMCwNs7FF90PUIlAVatsTZbaTSEQCHZFZfV0tcSXlmNrr2N5eHTOx4xWtys6UdeL2/OAl1hJF7oQR0XVxpqe0i/YKn2CUV49LxozaMsovLclHFVJs1yc5c9cTT7nLq5bEV1gXGZp2kktHXRQ4VuOzP2TJEnE0kdhPGB+7Ss4kHquO12S45JsDpSD2gRab3t3gJV8rDMHBYrpLDpa716d2sLhI6mGVlXXTyyjoSjdnWul8xrsw7Ba6lyczd3yeug3XZJe4tZXVVk+n+ErNDjvOm6j1FdrQPG4PUHjMErze5NK5CkEGGJAxXeCJrXP6GgdOLBnKUjQlWAx2VNJnsW1zTGond7Ka2CE1mFHZrjYCAbMMsw07Lc9l2vZPMiICHOaPsXpEYSTHzvhaBIgeIDXWtm6fDD59xCIFZyczFJTcoIMRsjZTuj0qRLIJyhr2pKLBOjTij+p1Z/qoYkUy7nuxT6sNrBknXyDELHNud/oiGMiBWlq25md56XQ5aLYoO0rP1FLXdyRzt3Gf2HoGayDkXqaUWLr78qG4svDFUCy1hy90uQrN4x40JGaQu9qGFNEI4M7VNPVMLIcETs7RVdIMx1761/hSXRCmwl0jTUOYvlCM0Ut0WZCBDS3X+rCLtrRBJ1vbM40ASGnoux05UGPqYEdW9W8oppOrFVzvctUVS80PC4+PvHsAkV3IloUT4a6AqeIwXKoDdDwR0cmoyLspMG5WLXv/rjbsMlvb1UEztoxgtEdIo2vukgG0XYHWozWaVsSkcGkWnpoHZC3dyZsaXPdtGpviSRhQZcubTnTJDnoD14dGvTEqBUoPq+1yH+e0VC2ZQmkbLSw50+Cmi4vX0T5g+uM+gPZ86dK64dB0g8roxuC4UyroCiee5MHnOV4I6stuud+dV3oUV5KAkuuVlLTyfVsLFQwrhezY3LoP4tKQfE6K97olxCfzVih1sFZEOhWhpQJz+zACEwWnGxeRx7fjOfJVaF/zRI0RoRziyHJI3HUglqA3w5ZSrMmpIan3WrFdV7Obq2IXlmmHPLyHQxETsoyJWl8nqfwaYBAu804Kig1GX0belhOP2PWVVodLhUUZRwIJTamTHmfubnMMRT47HPN6qNsGjSzuWNV8AvadUVTKja1qVEKCJ1zWYdUSSrosI4Vhc9x5TKCjucis0gBP2eQ8erulY/PBxMfp+Y54u5t2il2SxUS6ATJmsMo3cJFasoWKG3OY4Jh2Hf4gbAJ4KCBCu9yG+kyZTJw4ZYEIvdW5oBKsnGQYyXhEmQs5+QltmR7tdGRcBLjF7na0n7UCrfI0awcaslOqzQF2Uq5VNoME5THXExdNlPdLxgWgiaHksU9vHjxCyyMTAFxCA8cuqOigFTFf8gGnaN1ddbrQrWmmSHKvuR51YxscdCa6bepUcySVdUXRitOpla6cdojYayB2sCdaTalxginfibNEGAYeYnt4yyVbiMwFpTIrsagqC+9OoHRf1o09WHXJraI4w8ojtq7aiFWOp30T3tQDr/dhe94LeuJNkgmpR4WEFLIb0FjkHOrCRWvrCt9IZLcZrYHMjMSFKYrjPGINj4G6UlwIby/Ztk5pEV1KrHdkW8molNGM81BToRwFttClbXrmlBad+nJ/34vNNp0i+M7k2oHmQj1Vbquxq9LqLKd4Ylt5XENFZ8QyqrauccE8n1/fT2lBi8hZkc704WLt+YZaaoOS5qdu3VzCVOosWAQjTpVcr+4Oc5bQ2UDt0QGzOmiQ6hNvS31G3tNpozGeJDZkm+Qn1wlY6mifAJiMaNwYZtOlQyK38UFUonR0RMzhN9pKWLG6ZKtn+AK3YZFjPsOlJ1/a2/uwais+OAXntS9JR+ikbFNoVemS5GabTX0iDPmKxQcjuIi7jC/soEmbdj+u/GzpNuPJzYZbscVcpKvLCUtONoXELSWOvHe6bQPpnu4bjowRMH/hih8p2grJ4aZvIrfeb8MWdL+Gce4PgnI1LYSxzMZHw7vWhMr+JPfe+VRUDis0LcZEksZHwQhwlBlS3fV3nmfpa53GQjt0EGE9IrGPNLvtJnX1CINFDXNdA7tzXKVbdy3sIfwuaPJ5WrnCGPqFg+oTgbNrGEb3cXDyxSByjpACB8s6g6hymPIWxssunbYXQT5pe5ux68AP7nKp1U5aB02E0FafDfeWrOodaq9MiQo7wcsymXDrGGJDXMCUUNFGEcdU7dihNeMInnpST/EhuwmKZnr2qVluyj6+Y2eSaG8hRATr9ojAiLyrIzcxSNzpc3jVnd3gpOPhJYyrjWDTiSVc/fR2YVBtv9yCkjFelwmGiOL9mJGhtMJawpT2FgujaNiM3coa/TPFn7FwMtH8EO/TeC1kHcAZ1gxNYQiva45l8FFq8cg9YElknOoDa3ljSGkAYCo6TU+IZq9s5zQ5XIMad7kIktjkzTOxLy9BnwrUNj3YNOwCDB3teyntDmJ43h1w4X5dp5CbG9fhKPIc6mcHrhDXg7wqpfWaJ3wRazRsOEgCISibYmJ940Yedw052dKpxEoBNAmoX5lur5y9cYM1QpzCm2NR+RtjkOBqqWklbq+cuB/2+M6c8F1GjQfQrGLLI3TfdLWUuiGrMrsGpGBw8SzDBwHancPz0NuONdwE8wLd+Z6Btr2NgDYKCXuluRLexMQlltgV6Y9uQi6PE67EYzIiY5ZotXbkLgyFiyF0LavdztRA17vzZKhKewvd8gO8V1Jf12V4uzd33nTq6ey2YtWKhUl7R9jSUnKsrNPiTXDb32McJLwQsI2g18cN2VsttJa5FEYtk7u1nbZWM99q1MKFx018kpjNbn1B9cPNv0kMNgyNzqz6TLKFk82FVkvUoUhUTOO363NTjSfBx/3kcMYYIQgpL2VhKM86l5c692b1B+9GRPsCruxm2Qry5UT62/PkoK2VM7ux18Zt7vs3twKdP3ZaYodmfaViRN7fOxC75NE7Sa7e7ou+C2yD7m54eS5SPKeLsqB9aKPabqbrJX1Gay+OJ9AX4dYWQnQBWhZnubBBM77f6rGGX0/psNva1GqIVxq/LU1VdNObyu0RNTSbSTP26BmucgeLdZTqj71r+imGtjrS+z4ue8hys9ev8l4qTUvvlDsalmSbozwrKDF7t5Z3XxgCRA5Nd9iFMgy1Jh/4+lj6/dUP0JrQxzXhro9tEMEx7GvLQBugQdaQwtE2gRq7SxaFOTHSrcgx2yogVmfacK5mAO/TbTOcL+GOteGYrG8AjSYBOyItcvPHXCgYYsiPaEIpGehfDkN/NFo4vtr9eNeoSx7WhU0i+0PVrmRuirbOxBeGPN21gu/F1URip1s4ZBUf6ykz0Vya1iv2TFeZJvkEvsMhC74VfoA7+wqMBuMhxGtufRcYe3kulpCKdFA59lFxHi4tv8wZY9zpS4dfJu4UXjfOzqVOFjduMiyLkjq/MTZ6OYROJSPjKSV9Xt2t/S7J97i30jyRWMtqX1u4bWxqxehdAFBO6Ag9rtE5OlXqKfG2WtWg/sbuazVPgzOSu2p37z08ZNeIkXdcQ5KMmFkQ7u6cXnHdYyr6JA1CWEKR4q6ncJQshazNAsMcnOR0JboUxMGZy6ZAiVbC+eaOVwyPfMpdk5eTVMosRJ0EhTzerCy+OVJWJghs14w79Iym7CNQ58eplU+NtBKq3DWvvrJJh5UJ6TiYW23RXjd3mXD6YF8K13K4MmO7zO7sLVxfmAPHsIImkTlzTdis4mB/vyVW07UUUK1R9stIvXp7F9rnXWlhneD3wRqgGegipzXi4cTZjNMjFnLGFb6j6VD6R1+7w5R4XlaR3Eq8i/CnzuZaR2S4LB3isTHx653ZdG1/3wajdNkfO2S9nZBraJf55SKEmaYhIgUZx1JEhm5tFlToWEeCvDmQNK6p/ZEap2kFHdTDEWaqkpLB/Gjdtrf1yY1GHbcRZBM0V8k1vEsplWMDLblW5gLP95HhtKZCKoaRZL0fDGt0DAaZbsmybSSivJZHqUB6TvfNGl3eNiBUz+2FS6/XsQztAdhhxUenDmXQypK3EbofDzcyUNV+YwvN1pOSu3ly0J1rX5e6gvorchAr97hh7mR9Gdd40Xu0e/PWydkt3YGz0XMqizxhrnTv5GB39jTuN+hwhy51R+gTuW7HUtU3nhtyHpxv1zuJXUUYZNMRddL6kL/rW87YGlbSJBOF6sWqIiVmq9qQv4GbW3bYp8M2nNbK3dk2ypnbQoRMZyF15BB/wHL/Flkbf9+6xIQc4Lt+XYKGkgq4/cC7AeH4bsle797piKs4v0UGAm0hcZMNNoPltwTtapg1RekmNV4BKjFPtvvaXq3ucgJhjBe5IrY6ZxPJnt10K8gQ1KbyBgJBBGfi3j4VfGwFzcXz0zt2HEEzeND2SkRRLx9evh2ivfxbL4TNJzj/zw6Snmc+7294PE4IA8f/9OD16d8T65cPL62XzEI9Ds26fIjejpf+cmT28V85+JspTM93rd4Pmp+n170TzW8jvySlP3R9O33pqvzxngfY4Q7d/PZiN7/g6oHvPx51PpjOZ52z9H315fFa3PvGpJzf3gj8BEj0dhm9nSJ+ePHf3in6gq7xL0Fbz5q+vSMAFERfoVfk5ff/DUdqWfdILgAA -->
