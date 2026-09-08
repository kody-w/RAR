---
name: "rar-cowork-cookbook-audit-nurture-opportunities-and-finalize-the-sale"
description: "Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "e470b181878312143afc8c1a4e3e52b0a15e9af4ba77f045008ae479196f8af1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale`. The original RAPP
agent is preserved byte-for-byte in `audit_nurture_opportunities_and_finalize_the_sale_agent.py` and in the RCI capsule.

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

Nurture opportunities and finalize the sale Completeness Audit — Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale
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
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 e470b18187831214…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_nurture_opportunities_and_finalize_the_sale_agent.py` first:

```bash
python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py   # or on stdin
python3 audit_nurture_opportunities_and_finalize_the_sale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture opportunities and finalize the sale Completeness Audit — Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale',
    "version": '3.0.3',
    "display_name": 'Nurture opportunities and finalize the sale Completeness Audit',
    "description": 'Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-nurture-opportunities-and-finalize-the-sale',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-nurture-opportunities-and-finalize-the-sale',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5673095529b245d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-nurture-opportunities-and-finalize-the-sale', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit nurture opportunities and finalize the sale records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to nurture opportunities and finalize the sale. Output an Excel workbook 'audit-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no nurture opportunities and finalize the sale data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads nurture opportunities and finalize the sale records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit the nurture opportunities and finalize-the-sale records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants these D365 ERP records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditNurtureOpportunitiesAndFinalizeTheSale(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditNurtureOpportunitiesAndFinalizeTheSale'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditNurtureOpportunitiesAndFinalizeTheSale().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
