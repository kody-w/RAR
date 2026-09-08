---
name: "rar-cowork-cookbook-audit-develop-prototypes"
description: "Audits develop prototypes records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, and returns a read-only Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_prototypes", "rar_sha256": "01534c8c8b92d9548f0e4788103a54dacfeca2387c171fa0cdbb2d19d4e9b1e6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
