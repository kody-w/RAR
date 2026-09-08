---
name: "rar-cowork-cookbook-bulk-update-perform-a-skill-gap-analysis"
description: "Applies a bulk field update to skill gap analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval gate bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis", "rar_sha256": "bde61f59fa86148f0ab51586ffbf38b4b2937254a4be2ba5330849ff7b0f93a1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
