---
name: "rar-cowork-cookbook-bulk-update-hire-for-open-positions"
description: "Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_hire_for_open_positions", "rar_sha256": "681373cda581c45f61cb38d069deff4c7abe11b26ec872f81551a7f3ed76e94c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_hire_for_open_positions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_hire_for_open_positions_agent.py` and in the RCI capsule.

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

Hire for open positions Bulk Field Update — Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
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
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of hire-for-open-positions record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 681373cda581c45f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_hire_for_open_positions_agent.py` first:

```bash
python3 bulk_update_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_hire_for_open_positions_agent.py   # or on stdin
python3 bulk_update_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Bulk Field Update — Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_hire_for_open_positions',
    "version": '3.0.3',
    "display_name": 'Hire for open positions Bulk Field Update',
    "description": 'Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a',
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
        "upstream_slug": 'bulk-update-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '527d5f256aeff29a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of hire-for-open-positions record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when hire for open positions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to hire for open positions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a', 'example_request': 'Bulk update these hire-for-open-positions record IDs in USMF sandbox with the new value - show me the dry-run first.', 'inputs': [{'description': 'List of hire-for-open-positions record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of hire-for-open-positions record IDs and want a reviewed dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateHireForOpenPositions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateHireForOpenPositions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of hire-for-open-positions record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
