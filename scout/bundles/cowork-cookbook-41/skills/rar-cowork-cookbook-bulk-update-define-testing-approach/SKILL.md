---
name: "rar-cowork-cookbook-bulk-update-define-testing-approach"
description: "Applies a bulk field update to define testing approach records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_testing_approach", "rar_sha256": "756801bfed5bdd7b2e0f3ec6fd808833e5dfc24436903b5f89c06a528138b3bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
