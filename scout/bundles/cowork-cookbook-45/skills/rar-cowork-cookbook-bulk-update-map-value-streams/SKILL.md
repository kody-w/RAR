---
name: "rar-cowork-cookbook-bulk-update-map-value-streams"
description: "Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_map_value_streams", "rar_sha256": "196286e54e0e1e6b4145a241b0de966ba37168b1b2ff18eb2c888da25e7b7cef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_map_value_streams`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_map_value_streams_agent.py` and in the RCI capsule.

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

Map value streams Bulk Field Update — Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-map-value-streams
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
      "description": "D365 legal entity to run against; sandbox USMF by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new value(s) to apply to the targeted field(s).",
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
      "description": "List of map value streams record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 196286e54e0e1e6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_map_value_streams_agent.py` first:

```bash
python3 bulk_update_map_value_streams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_map_value_streams_agent.py   # or on stdin
python3 bulk_update_map_value_streams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map value streams Bulk Field Update — Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-map-value-streams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_map_value_streams',
    "version": '3.0.3',
    "display_name": 'Map value streams Bulk Field Update',
    "description": 'Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-map-value-streams',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-map-value-streams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03f7a1a3d6944fad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/map-value-streams'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-map-value-streams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; sandbox USMF by default.', 'new_values': 'The new value(s) to apply to the targeted field(s).', 'record_ids': 'List of map value streams record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when map value streams records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to map value streams records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit.', 'example_request': 'Bulk update these map value streams records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of map value streams record IDs to update.', 'name': 'record_ids'}, {'description': 'The new value(s) to apply to the targeted field(s).', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many map value streams records at once in a D365 sandbox and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMapValueStreams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMapValueStreams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The new value(s) to apply to the targeted field(s).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of map value streams record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMapValueStreams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
