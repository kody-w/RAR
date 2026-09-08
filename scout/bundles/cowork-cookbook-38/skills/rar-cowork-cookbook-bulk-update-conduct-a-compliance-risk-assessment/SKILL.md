---
name: "rar-cowork-cookbook-bulk-update-conduct-a-compliance-risk-assessment"
description: "Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment", "rar_sha256": "34807fe6666e46a9bb6a4a947ed0f91d39ae870c3ede16d3eb65a8298dbf598f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
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
    "approval": {
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; sandbox USMF by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
    "record_ids": {
      "description": "List of compliance risk assessment record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 34807fe6666e46a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_a_compliance_risk_assessment_agent.py` first:

```bash
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py   # or on stdin
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment',
    "version": '3.0.3',
    "display_name": 'Conduct a compliance risk assessment Bulk Field Update',
    "description": 'Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a288f489c37ddc76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/conduct-a-compliance-risk-assessment'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-conduct-a-compliance-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; sandbox USMF by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of compliance risk assessment record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when conduct a compliance risk assessment records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to conduct a compliance risk assessment records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit', 'example_request': 'Bulk update these compliance risk assessment records in USMF sandbox - show me a dry-run first.', 'inputs': [{'description': 'List of compliance risk assessment record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many compliance risk assessment records at once in a D365 sandbox and want a reviewable dry-run before applying.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConductAComplianceRiskAssessment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductAComplianceRiskAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of compliance risk assessment record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConductAComplianceRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
