---
name: "rar-cowork-cookbook-audit-conduct-current-state-analysis"
description: "Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_current_state_analysis", "rar_sha256": "62f6118befda0257935a67df6894cc8f0df8d92b41ef4ba16c03ab90a40ec874", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_conduct_current_state_analysis`. The original RAPP
agent is preserved byte-for-byte in `audit_conduct_current_state_analysis_agent.py` and in the RCI capsule.

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

Conduct current state analysis Completeness Audit — Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
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
      "description": "Date range used to judge stale dates; adjust for demo data eras such as FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "The D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-conduct-current-state-analysis-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 62f6118befda0257…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_current_state_analysis_agent.py` first:

```bash
python3 audit_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_conduct_current_state_analysis_agent.py   # or on stdin
python3 audit_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Completeness Audit — Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_conduct_current_state_analysis',
    "version": '3.0.2',
    "display_name": 'Conduct current state analysis Completeness Audit',
    "description": 'Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3e7f5ba4291b311',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'legal_entity': 'The D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-conduct-current-state-analysis-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit conduct current state analysis records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to conduct current state analysis. Output an Excel workbook 'audit-conduct-current-state-analysis-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no conduct current state analysis data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct current state analysis records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo', 'example_request': 'Audit conduct current state analysis records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'The D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-conduct-current-state-analysis-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of conduct current state analysis records in Dynamics 365 ERP via Cowork.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConductCurrentStateAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConductCurrentStateAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'The D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-conduct-current-state-analysis-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
