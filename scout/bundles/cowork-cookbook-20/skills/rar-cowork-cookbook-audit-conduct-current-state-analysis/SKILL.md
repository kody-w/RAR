---
name: "rar-cowork-cookbook-audit-conduct-current-state-analysis"
description: "Audits conduct current state analysis records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations in a read-only Excel repo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_current_state_analysis", "rar_sha256": "62f6118befda0257935a67df6894cc8f0df8d92b41ef4ba16c03ab90a40ec874", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
