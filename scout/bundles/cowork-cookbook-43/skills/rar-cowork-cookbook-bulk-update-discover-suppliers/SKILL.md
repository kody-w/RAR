---
name: "rar-cowork-cookbook-bulk-update-discover-suppliers"
description: "Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_discover_suppliers", "rar_sha256": "b9ed58b0bfebae79ff5f343c6746adce9316e16d3cd6fe86b944afbfb22d0875", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_discover_suppliers`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_discover_suppliers_agent.py` and in the RCI capsule.

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

Discover suppliers Bulk Field Update — Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; default USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field value(s) to apply to each record.",
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
      "description": "List of discover suppliers record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 b9ed58b0bfebae79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_discover_suppliers_agent.py` first:

```bash
python3 bulk_update_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_discover_suppliers_agent.py   # or on stdin
python3 bulk_update_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Bulk Field Update — Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_discover_suppliers',
    "version": '3.0.3',
    "display_name": 'Discover suppliers Bulk Field Update',
    "description": 'Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '477382d35763a442',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; default USMF sandbox.', 'new_values': 'The field value(s) to apply to each record.', 'record_ids': 'List of discover suppliers record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when discover suppliers records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to discover suppliers records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva', 'example_request': 'Bulk update these supplier IDs in USMF sandbox with the new values — show me the dry-run preview first.', 'inputs': [{'description': 'List of discover suppliers record IDs to update.', 'name': 'record_ids'}, {'description': 'The field value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; default USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of supplier record IDs and new values and want a previewed, approval-gated bulk update in a D365 sandbox.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDiscoverSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDiscoverSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; default USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of discover suppliers record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
