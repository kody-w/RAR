---
name: "rar-cowork-cookbook-bulk-update-conduct-competitive-analysis"
description: "Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_competitive_analysis", "rar_sha256": "0a596ddd0703bf624894cc5798c9aa067ab02cdd9da1eddde466ad26070b7cd0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_competitive_analysis`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_competitive_analysis_agent.py` and in the RCI capsule.

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

Conduct competitive analysis Bulk Field Update — Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of conduct competitive analysis record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 0a596ddd0703bf62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_competitive_analysis_agent.py` first:

```bash
python3 bulk_update_conduct_competitive_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_competitive_analysis_agent.py   # or on stdin
python3 bulk_update_conduct_competitive_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct competitive analysis Bulk Field Update — Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_competitive_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct competitive analysis Bulk Field Update',
    "description": 'Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-competitive-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '126af7804d6023f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-competitive-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of conduct competitive analysis record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when conduct competitive analysis records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to conduct competitive analysis records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p', 'example_request': 'Bulk update these conduct competitive analysis records in USMF sandbox - here are the IDs and new values; show me a dry run first.', 'inputs': [{'description': 'List of conduct competitive analysis record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many conduct competitive analysis records in D365 ERP and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConductCompetitiveAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductCompetitiveAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of conduct competitive analysis record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConductCompetitiveAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
