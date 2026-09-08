---
name: "rar-cowork-cookbook-audit-nurture-opportunities-and-finalize-the-sale"
description: "Read-only audit of nurture-opportunity and finalize-the-sale records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "e470b181878312143afc8c1a4e3e52b0a15e9af4ba77f045008ae479196f8af1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
