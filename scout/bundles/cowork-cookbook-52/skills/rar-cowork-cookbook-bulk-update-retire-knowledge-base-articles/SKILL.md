---
name: "rar-cowork-cookbook-bulk-update-retire-knowledge-base-articles"
description: "Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_knowledge_base_articles", "rar_sha256": "de861f0b14352dc63ebe21ec25ffbb8fb1265a6e9f8a0b0fd7ea5818a2225bf0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Retire knowledge base articles Bulk Field Update — Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
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
      "description": "Explicit user approval after reviewing the dry-run preview, required before any write.",
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
      "description": "The new field value(s) to apply to each listed record.",
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
      "description": "List of knowledge base article record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 de861f0b14352dc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_knowledge_base_articles_agent.py` first:

```bash
python3 bulk_update_retire_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_knowledge_base_articles_agent.py   # or on stdin
python3 bulk_update_retire_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire knowledge base articles Bulk Field Update — Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_knowledge_base_articles',
    "version": '3.0.3',
    "display_name": 'Retire knowledge base articles Bulk Field Update',
    "description": 'Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-retire-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '870aeddc45fad84b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/retire-knowledge-base-articles'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-retire-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the dry-run preview, required before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to each listed record.', 'record_ids': 'List of knowledge base article record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when retire knowledge base articles records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to retire knowledge base articles records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval', 'example_request': 'Retire these KB article IDs in USMF sandbox — show me a dry-run preview before applying.', 'inputs': [{'description': 'List of knowledge base article record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to each listed record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the dry-run preview, required before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to retire/bulk-update a supplied list of knowledge base article records in D365 sandbox with a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRetireKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the dry-run preview, required before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to each listed record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of knowledge base article record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRetireKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
