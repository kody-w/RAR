---
name: "rar-cowork-cookbook-bulk-update-retire-knowledge-base-articles"
description: "Runs a bulk field update on knowledge base article records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_knowledge_base_articles", "rar_sha256": "de861f0b14352dc63ebe21ec25ffbb8fb1265a6e9f8a0b0fd7ea5818a2225bf0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
