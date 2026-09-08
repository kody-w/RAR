---
name: "rar-cowork-cookbook-audit-perform-market-research"
description: "Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_market_research", "rar_sha256": "d966a001bbe0948f84299401916982bcbd33b9af45d26090fff10a2f1143ad44", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_market_research`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_market_research_agent.py` and in the RCI capsule.

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

Perform market research Completeness Audit — Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
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
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 d966a001bbe0948f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_market_research_agent.py` first:

```bash
python3 audit_perform_market_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_market_research_agent.py   # or on stdin
python3 audit_perform_market_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform market research Completeness Audit — Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_market_research',
    "version": '3.0.3',
    "display_name": 'Perform market research Completeness Audit',
    "description": 'Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-market-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-market-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '944fea706c72b213',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-perform-market-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit perform market research records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to perform market research. Output an Excel workbook 'audit-perform-market-research-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no perform market research data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform market research records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits perform market research records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of co', 'example_request': 'Audit perform market research records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of perform market research records in D365 ERP via the Cowork plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPerformMarketResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformMarketResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-market-research-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPerformMarketResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
