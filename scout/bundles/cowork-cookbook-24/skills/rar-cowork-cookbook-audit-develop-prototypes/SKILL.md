---
name: "rar-cowork-cookbook-audit-develop-prototypes"
description: "Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_prototypes", "rar_sha256": "01534c8c8b92d9548f0e4788103a54dacfeca2387c171fa0cdbb2d19d4e9b1e6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_prototypes`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_prototypes_agent.py` and in the RCI capsule.

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

Develop prototypes Completeness Audit — Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-prototypes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 01534c8c8b92d954…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_prototypes_agent.py` first:

```bash
python3 audit_develop_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_prototypes_agent.py   # or on stdin
python3 audit_develop_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop prototypes Completeness Audit — Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_prototypes',
    "version": '3.0.2',
    "display_name": 'Develop prototypes Completeness Audit',
    "description": 'Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel',
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
        "upstream_slug": 'audit-develop-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94625662df013b30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/develop-prototypes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-prototypes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop prototypes records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop prototypes. Output an Excel workbook 'audit-develop-prototypes-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop prototypes data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop prototypes records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel', 'example_request': 'Audit develop prototypes records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-prototypes-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of develop prototypes records in Dynamics 365 ERP via Cowork.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopPrototypes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopPrototypes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-prototypes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
