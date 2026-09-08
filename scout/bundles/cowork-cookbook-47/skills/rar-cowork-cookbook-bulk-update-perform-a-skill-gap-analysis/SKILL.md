---
name: "rar-cowork-cookbook-bulk-update-perform-a-skill-gap-analysis"
description: "Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis", "rar_sha256": "bde61f59fa86148f0ab51586ffbf38b4b2937254a4be2ba5330849ff7b0f93a1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_a_skill_gap_analysis_agent.py` and in the RCI capsule.

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

Perform a skill gap analysis Bulk Field Update — Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, required before changes are committed.",
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
      "description": "The field(s) and new value(s) to apply to each record.",
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
      "description": "List of skill gap analysis record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 bde61f59fa86148f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_a_skill_gap_analysis_agent.py` first:

```bash
python3 bulk_update_perform_a_skill_gap_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_a_skill_gap_analysis_agent.py   # or on stdin
python3 bulk_update_perform_a_skill_gap_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform a skill gap analysis Bulk Field Update — Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis',
    "version": '3.0.3',
    "display_name": 'Perform a skill gap analysis Bulk Field Update',
    "description": 'Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-perform-a-skill-gap-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6426d198ea16f850',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/perform-a-skill-gap-analysis'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-perform-a-skill-gap-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of skill gap analysis record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when perform a skill gap analysis records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to perform a skill gap analysis records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef', 'example_request': 'Bulk update these skill gap analysis record IDs in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'List of skill gap analysis record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many skill gap analysis records in D365 ERP and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePerformASkillGapAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformASkillGapAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, required before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of skill gap analysis record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePerformASkillGapAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
