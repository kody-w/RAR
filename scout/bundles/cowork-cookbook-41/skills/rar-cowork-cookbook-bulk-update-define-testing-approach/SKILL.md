---
name: "rar-cowork-cookbook-bulk-update-define-testing-approach"
description: "Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_testing_approach", "rar_sha256": "756801bfed5bdd7b2e0f3ec6fd808833e5dfc24436903b5f89c06a528138b3bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_testing_approach`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_testing_approach_agent.py` and in the RCI capsule.

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

Define testing approach Bulk Field Update — Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
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
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox first).",
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
      "description": "List of define testing approach record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 756801bfed5bdd7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_testing_approach_agent.py` first:

```bash
python3 bulk_update_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_testing_approach_agent.py   # or on stdin
python3 bulk_update_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Bulk Field Update — Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_testing_approach',
    "version": '3.0.3',
    "display_name": 'Define testing approach Bulk Field Update',
    "description": 'Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '853b7606c1ada259',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'new_values': 'The new value(s) to apply to the targeted field(s).', 'record_ids': 'List of define testing approach record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define testing approach records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define testing approach records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm', 'example_request': 'Bulk update these define testing approach records in USMF sandbox to the new value — give me a dry-run preview first.', 'inputs': [{'description': 'List of define testing approach record IDs to update.', 'name': 'record_ids'}, {'description': 'The new value(s) to apply to the targeted field(s).', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many define testing approach records at once and want a before/after preview and approval gate before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineTestingApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineTestingApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The new value(s) to apply to the targeted field(s).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define testing approach record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
