---
name: "rar-cowork-cookbook-bulk-update-map-value-streams"
description: "Applies a bulk field update to map value streams records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_map_value_streams", "rar_sha256": "196286e54e0e1e6b4145a241b0de966ba37168b1b2ff18eb2c888da25e7b7cef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
