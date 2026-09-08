---
name: "rar-cowork-cookbook-bulk-update-recognize-revenue"
description: "Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_recognize_revenue", "rar_sha256": "1a1b56b988f68dbf8763b70efa2d40e791effa8131945cbec3454dc032119b94", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_recognize_revenue`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_recognize_revenue_agent.py` and in the RCI capsule.

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

Recognize revenue Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of recognize revenue record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 1a1b56b988f68dbf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_recognize_revenue_agent.py` first:

```bash
python3 bulk_update_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_recognize_revenue_agent.py   # or on stdin
python3 bulk_update_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_recognize_revenue',
    "version": '3.0.3',
    "display_name": 'Recognize revenue Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f643c00e11feed5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of recognize revenue record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when recognize revenue records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to recognize revenue records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these recognize revenue records in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of recognize revenue record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many recognize revenue records at once and want a before/after preview to approve first. Sandbox only; data-modifying.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRecognizeRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecognizeRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of recognize revenue record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
