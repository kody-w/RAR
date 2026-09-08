---
name: "rar-cowork-cookbook-bulk-update-discover-suppliers"
description: "Applies a bulk field update to discover-suppliers records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook first and a confirmation workbook after approva"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_discover_suppliers", "rar_sha256": "b9ed58b0bfebae79ff5f343c6746adce9316e16d3cd6fe86b944afbfb22d0875", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
