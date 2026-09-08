---
name: "rar-cowork-cookbook-bulk-update-hire-for-open-positions"
description: "Applies a bulk field update to hire-for-open-positions records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_hire_for_open_positions", "rar_sha256": "681373cda581c45f61cb38d069deff4c7abe11b26ec872f81551a7f3ed76e94c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
