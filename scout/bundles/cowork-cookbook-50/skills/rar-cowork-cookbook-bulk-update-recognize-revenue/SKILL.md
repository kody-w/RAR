---
name: "rar-cowork-cookbook-bulk-update-recognize-revenue"
description: "Applies a bulk field update to Dynamics 365 F&SCM recognize revenue records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_recognize_revenue", "rar_sha256": "1a1b56b988f68dbf8763b70efa2d40e791effa8131945cbec3454dc032119b94", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
