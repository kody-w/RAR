---
name: "rar-cowork-cookbook-bulk-update-conduct-a-compliance-risk-assessment"
description: "Applies a bulk field update to compliance risk assessment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment", "rar_sha256": "34807fe6666e46a9bb6a4a947ed0f91d39ae870c3ede16d3eb65a8298dbf598f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
