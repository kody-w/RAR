---
name: "rar-cowork-cookbook-bulk-update-define-project-scope"
description: "Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_project_scope", "rar_sha256": "746e08e9fae7a8e51750850c4434a6f913e2ad500d4063bc17dfb07c58d06fca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_project_scope`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_project_scope_agent.py` and in the RCI capsule.

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

Define project scope Bulk Field Update — Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
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
      "description": "D365 legal entity to run against (default USMF, sandbox only).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of define project scope record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 746e08e9fae7a8e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_project_scope_agent.py` first:

```bash
python3 bulk_update_define_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_project_scope_agent.py   # or on stdin
python3 bulk_update_define_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project scope Bulk Field Update — Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_project_scope',
    "version": '3.0.3',
    "display_name": 'Define project scope Bulk Field Update',
    "description": 'Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f26c76b2079df32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/define-project-scope'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-define-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF, sandbox only).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of define project scope record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define project scope records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define project scope records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define project scope records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appr', 'example_request': 'Bulk update these project scope record IDs in USMF sandbox with the new owner value — show me a dry-run first.', 'inputs': [{'description': 'List of define project scope record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF, sandbox only).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many define project scope records at once in a D365 sandbox and want a before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineProjectScope(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProjectScope'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF, sandbox only).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define project scope record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPayJLuX+G+EzHtHmxrX/DEibhCCC2ABBKgpd3h1r4vaENST//3KQF2d5/js0XcTxeHAyRVZWVmZT5P5lv69c3u2qis3z69ab5dLHg7y+LIrxd24S3Y8l7WKfgqUwf8X7hl0dax07Vl3by9f/P8xq3jqo3LAkxnqiqL/WZhL5wuSxdB7Gfeoqs8u/UXbbnw/CAu/EVVl4nvtovGLSt/UftuWXvNIi4Wm7Gw89htFhhJLLb/qbGHxbvMD+1s4Rdt3I6Li3bYvl80QC+nHH5c9LG9aCP/q46beRqnHhdV1oVx8R6Ibru6iIsQKOTV44e6K8Difh/798U8Yzbo/SyhAAOAYUFc5/ZsyrenCztoZ0dUVQ2M9Qc7rzK/efv008/v32Lw++3Tr29uZjfg1tsamHx52Lp52Hl8mqnNVoLJmV2EYFQ1AlcX4Lry66Csc3ALuGXxunrX+FnwfvFf/5Xe7Tpsfvz0uVi8Pp/f5n8qMGE2uS3tpvW9hWtXthNnwDkfF0x2t8fmZfW8CQ3YqSL8+Jz5u6SyWvxlfvbuucjH0G/ffX4DWtYP4z+//bgoa7AecBf4/XGWUr378WNW3v363Y+/y2k657GPQBjQ+uOX1/VLLBj4+9A4WHzRjhz7WgvseVz5QPgf7Js/T9Vf4l4u+fIc/K6s3i++L3m25y9A32csOkDu98UCH4CZbx+TMi7evdaoy94v7ML13/3498S6ke+mWdy0/5Lcn56CI9/2gLdeLvnx/WP7fl4sX7Z9k/n3l61AwPw7loDhX5f75qi/J/uxs38lOgMh23zby++K+96E5V8WP/1d2/7RhPeL4PPbxs/iHsSdk/mfFr8+QuSnH7zfb/7w829A9D8Vo5Vd7T4kfMntIg78pv3y5acfmsftH37+6YeuAlHs2/mXrs6+J/N7fn2s8ycPvka9+/NcsP6lSIvyXiy+5dDi17L6P/VvHxdXO4u93+83nxZ/zMT5s1zMRnxd9OmCP2RjA3T9gx9/fPsNIE8BrOncx2OAH//xH4tD7NZlUwbtAsBN1y7ABrdx7s/Kn6MYgGvzQA2AfX7dxMCxr3EvKJ41LoPFL//XfSDpB/eF9tAM41+eAP7lid5fXlO+PND7l4+LM5Bb1jEAXIDTKnM8fi7sEOD1vCYA28ave4BTztj6H0A6f5h/zFj/yz8T/eUh5WM1/vLgofiJeyorzpjXdJn/cbZOn8H7aYsLqMsffLcDC2SlC7QJYgDWMw00ZdYDzJw90aRxli28GKAKoLDxIRt469Ms7JdffnHsJvpcPEEaWzy5rYHAgG/qLD58AGYFWRxG7efCd6Ny8cOvv/2w+J/FP5r1ED6vcQRk8doLoKGkKfIC5FaXg2EzBwJQt73HXvz628u5QEwBOAjsXBzM5DpPBrGZ+t5XT2sC8wElyIXjAw8D7+ZVWbcz7cXtx4UYLL7pCxadH83cEJVNCwi58gvPL9wRSLWBOd88WZSAn0EANsH4ftE1/mPVX5zafqiYgyS3218WB/YImKjMZnKvX8wEJpdFDNz/LQ6e94GQ+odmsf4q4uNCnqNxUdm1XUW1/VojsJ/7Ahjo63Qg3F4U/v1zMVOuP7vqkRpP94BBwDPua0s/zHsOuDwHOPAsKtqvY+yZL88P3qw/F80r7O36WYIAVcZF2MXeTAb//QqpJio7UMHM/gOazpJeu+C9duURg5vvlTVzNbDYPgqgZ1Gw+NyhMIIv/n+ukWZvMDyvcjxz5jYLTj6r5nOX5rJx3s1npTnrCUL1mZG/lzBfYeorWn8ushiEXD3+93PkY29fY54I2NVgK1RGfcgHgQX0mOU+4n6O47p+uPpz8ZUW3gMrHhgIDAAgAZJodvrXBd8/bXxoGgEkmK9/LxFe2zBDBojtRdU5GYi7wPc9x3ZToFU95+5rm0ES+HMe36PYjf5k1bxRINaA/AVQIgbZCKjj4zeofj79qvqfJj4roXnKo0rsQOrWDwFAD39WcAaze9wCBLPbZ5UO7Pz0EALMyKt2tt0B25e/f930a//WxU3czkD59KtfAZD+MH8/LZ3v+kMFohE4C2RF1QHvPvJojpoc1DlABxC3IAjyuAC8D5zycsJDoJ3PoABA91WYPiU+br8M8h/JNxPW14mzIfOcuQZYBEB1cGf8I3acvxcmQF4+j3is+9eR9m21WfaMnw3AQLDi16fPYuHjk++fBcXiq9xPf9MGvfv3OqUHg1/+HACfFlHbVs0nCHqy7lfS/QjQC3rq2jwI+MMTHT48oeHDCxo+PKDhT3KfJn9a/Hu6/UnEKzc+LZCP8Ed4frR/xdbrA1zBflibH/D56edC9X/HVrB8OWPDvHEjYPxvRPh1CGDDsAZYBQY/ibGZ+fQOsOXBBGAXPhd/DPY52QDRFOEcnE35BxB4VAQg8J+b9o2wwKOiBWt7c/0Y+h/ntmtWv/HfPhVdlr1/A+Dp//NebeakfA7oZm7wgMNBNdbG/uNqxrmytx+t35+7X24AyO6CXPg65IWMTzSdk2WOs78C2fdfWftl6IOQZv6KW+Cm2YJ2rGaVn83cXP49EGpo/1YB5fHDzj4uNj5Aw6z5Y9i/uGzm8j9k59PL7588834xe6SZuRd4eTZ/zmy7AakCVPyuLg/q+fKknr9V6ME2f2KnV6Fgh49MXrwDMW13Wftn1gK4mI0/fnc9UAZ8AZ7tnnvx59VmTHjQ6bvmx0eEgMGLx+D5xlxFAOp9qADSpPnGqt9d51v9/bfL6KD0eTB1+Wm25f0LWsE36JneL761P8Cbr4Z0XsEvOtDr/zS3XnOAPabMP8Ac8PVt0rc/qTj+28/f0eup85fY+479ezB/ppx/UEIsxE3zJLx5p79j+WMJwAiAV2dtf3fD78qUj6ZwVgYo3z7/hvHrG0gXG8i0Xwnz6irAcACgM1R1LQQgBSwIrp/JD5792/3Ga34T2aDeBQIonPRh2l8Ftk/ZtE8gFAHTBOziOIbbZLBCMB+1PQKGPRwmMcdFKC9wYMolaA8mA9cG8p4Q8uWZckAksaICeLVCAxxBYQ8ogeKeR5M06RIUCtsrxyYcYmU7v09N48J7Gfo0bPbit9bngRlPe399c0gcjBTwRmSeHxZaIo6PQo5aO5BBrOIs1LtqN3CWd/T2mU10dpQoOL+WQqzxxJ7djWHi5qp8trhGwEzuTq+X8RHllnCBejR1uLDqdrxQNhU2GLtmnQN2zCehoKf8kBddgJxbVRvgW6oHu4QNb+oazm/DoRm7yO5bsWLpK2yP6U7qIQhxlmJ51pTWjYVt2NjGcUvatCaqpupnZ+YqbTuLHZZSytEdsin2A3H1IG4HLYnlHk/UiCPTij81+nafOHGHN1gNm3GG8bi2wZXBRPUyCyvXmlypzRFlt82qZdCr69v1OpV+aKiqVfNKTa9POY/xupolLqYniI2GW7NJOxVXIzU8h7Hqk/m9ZQmMQ+z4NMJSdrpZFdI1Xg8cGvQ1SR6xKj5HqyVE0WtkSQ9Ly7zizEoEMZrpZ44476XT9lwA8ytDicW+4zC8Vg/0KJ3dFt2v2N0Z9W0id5JLakjnw4473PfubggKVbEUI93WvCUYUUwd2GivHAhvcEYk7K9X8uCKIqhhDC6QThyChHLo9K3aWfSkeDsi7knhesMvDn9gSJdlHAGl94irbsqTRhpsdBq7u3ooo93kK6KApjcdN/wsRM7hcaclDsfD63WhrQOUSPqVR51JdzJxqhiSfVPz3EbfsTFxiS+uHY5GiION4Pii0dp9Zq50VbOMSksLrTgzR6hud+vNnmSnlRstr1JB3jyN2GenZdNLF9KIB95ToIA7k7cNmTccI+60fN+K6gkb3XFPRxqSiGmQs/XlONjDcAuYCV9xhFzb24FPHb3tt96qvXiqyYfJXdoMrLILiKbZyvs7N0LxyGn0dFufDrUJS60Ns61swqHjNSiiIxzBK54wejGis5g3lEWlWiW7pkSNwtUlX54rNBEOyog6pbCFax5PDBwem9FF1s155CfT5Qr9jHOTv7T5arm7Xvl0aZxG1ogiUw6Ik7Pzec6ZWFNYo4cNg/Lz/z2Tb/jw3JquN5bLxDmQa7/hLxBHQWQBbdljoG+7MRhZHoeEvUDb0IBuemMLV4rkpjq90dkghUi9SbZRw1x3zlmslvjOkAnPuqyTibGOsMh01qrDGdgcbmYKXSmvafIirPRDTYcXmjznZHFym2KX7IZIFNiAOd2n7doxFdmNvJPp+vjexYqpKQoaqIQJRgnLuO+wbGpEZ1y/MtXETweal3qLs9aEeEuONiQXpaXQ+v3QWTxvKEmyz65DNV5hx+XqdSwNlXsipKDzyWSSpZ3TeX3o+nyk31CAL1gGLW0GN4lmL1XKEk1RyjMNOq4FsumWSXPQkFq3CLjgTnIYxAEZTywfH1k3W/ex0UdZKe+Ua9PBzI6qRPtYafRw97jVrrrIrbQ6tlephfnSMgbhsLNv49RO4xAwvhVIXs6fM8u5QMLqMqbV6gDv6yCBT6KK8L6yz+m1CMofuu5ER+nYpqm2F1HdcIw2bvqiDVI8O26TvREGHDXB1OpUj6C0C/tjG57kO40YOwpnBIWl0Gu17ggUvxMNuSmofTKpXNZttqkv62mitCG7Flwr6bbIfeNJmoo7edlqd92KmFzJMvza99bB5WnachIVueCi0FOUDDLWSqyecCPYOm1MqKVoYupbdyxw0rJURx2YQ2hcoZTYHI+4ysJULKRUNtG0RB43p9Ej+J4ZmCgoaLU6oUSKw+zSJIbSFtdyNJqnFZwj1f62zO/I/VrAIeWkUs+S57C4uALeGcd71IihQ2i5yaP6pUyt6ITE0k13+xPBSNLIOwjRjSsHEql8MKvYOu/GnR6gSzVHDkSxEwMpv+B1aBdaKSGt458ihdP5E8IrAhcyqAGC/JCIVN+4bTQK6VmkmJ17Pder3Y7Dr252IJIlvd5aQ1kq7fLseQYK8K4RiSmU0evg1JLrHnipbEr9ci8HK6NdzKKXvRNnIpNf0Jx175J6LOkbrCXpMKoKkjQXJb+f1NgtnJqCzDsJdyRknVR5P+7Wyx6b0GuwEerBORY9NZyXwjiigV5397iGpcLogaVMw2YcjxLHY0iA3APZK94qby8AKanAkixFq8j2bBHD4J7dq0PIsKlb7pbo1Amvh36j+uZU8/vdJk+FUKkG/HxZ91y1a8ZpLdTNZVCHTWam5tBsrPpKbPmRrGD4tNKPRdHnKYwgRc3ZY+Xk+00P53GvYQe8krWMuMaIfY1Jf9TlPNpGh6N4d0RivdaCG5rEIjEi92WYoWePuIfJMtpwYbrCl8n2lJ5zmlsKmXGleeEYicV6MwmbjnMJ+cCL5lGDAHMLlohuR9Dhbc4CKd4ZHF3CBsQwxkWhxn5X8F6hsUs3N6h1e1LgS7xBjKXnra5hlF7MWIMvt6wztoq4bnk/WN4u2vWUGBLL6R6LLfdcGl4uGQ7SxrrZoRhBLQkqBi6+nhOuk6WUZNkLNu6OtBGain3HOYJrcHSdkS4/crSWXzlPdOLl7tBqUr6PL9YodkzOGM1BvaSUQ/ZXOOPMgwatOUfnbgfdAlUU2UeRJW4JHOW629CA+u8W3vf3Al96thi5zX4H6Fc0KkTtZQ6Rs/BapCJh3EcxU3p/ZYQrrqImPePpnCLpTIR3PTye6oHrSY9TAz+85ZG6uUthsdf2iBxnrhQeL/CIbMwDqyexgrK2eaEaPh0K8tioexE6cJdhHXSqzh669JzKLXasNjA22CfzxkBV4a2YdmDOmHgnsuQQbCMeTYB30ZXK3Mrdsk8xZuor9B4qXu7ntkKZTWLaMsMKuw4S0DtyowE1MtipK81MMQ0KJo/7CZ4wq1lFhOjhy0OqFsUFY+R1e4DadXVDtFRy2MMh5aytqmPUWjj1JSiT5ZsVZ7LfbiMuZZA4capR724ul1OQb7LjDVsm0mbqAmZMrbJjwyIMzRpb6fFqr9U7iVuHdidN1+lcToOYSp6WW8c1LmZ+CkdYZO6SdKXw8nHlcFCkBjh7DralN/XW9laYDB1qLJdFuspfslqF0hMaHoX6eJVtnVK8O2aBotSVRI6wygPmOmZ8SScpWpUruTULXQuJs4y7Ucah51pa31Nr7SQtwMHOhyiiABZWdHWVdqfU2kwyWiaxbhsiK2145EQZ1R2UCtnOGh1dEu1x4OlMGvxM2O7Q9b48U7bYLC9jrB09YdB7I2HFeJuOvcGpINoRUK6Z0i6mSFViL0p70DGDFfbj2i2kaNnKGHlKietF6vwbmXaWn1vprtPUUmQ2BR2JvsI0FW7r0241pQnSDxd9TPQOFlatVWIi762PGF2W1FUXGVOSRN0qr622hoTNfqvLmCKalebaTOwq21gI6ywU5ejuHmHGOUVdGWKh2+fXC9aj0Ik5kgfdTOvgtBHS+8mzGX/fSJvAOyc37AwL5lLL66Rre/OuyWw1IIZsHKc11vqCdjZ5WrfvzMpAjlMqLBmt6e9xW1HMVGlVL9d4OgmX7V2RO26TkwD/TjS6z6WtfY4vyWoFT5zVJdzuoF9NDwkV2Jxcw17ekxriN60GWhUzvCKHxm993hfDQkVO3oQPFHRKPJixPFNZRx16zmrihNfU5rheMQJe8Oia4Q3Po4oJda2uNQyFxSxSGxOqZt1m5x7JyVin+6CZ+Oy2VMRGgi+Z2VTxrpnwy4lhNh6jr8ZNxU6+7TWe5o2kr2vbSCOxoWfx5hQJwk7etVIgbNgxLAWkNvNt6+b3XAvVbaORBauyy0PBYaLJCn00AsqMsZ1mblZjzvlXkqiZ276liLLvE5oKihpZOYZ8ZLFYRJCTTJj7KRe4TXCxDh577cnD+hTQmrEtz62x88bBHfUVD4CIUlFTqwYLJB4Wp9XZJjuxuchCUndSnE7E9kJ42sbs5ZWqtef7ji61IxEFkGDgd/u8Tqvr5cTfaLK9l5FktQaQS9/sLQ2K8W3eBHDK8okqHYv6DpPJdiRyK+vXoPkyBj6XpcTiZHVL7PEzQd6XanCRtfZUtXCYak5Abb1sjfkY6m9Au1zfCTiS7vSZWVK5Fklr1/BOMl27d3o7FJu1ly5ZM0xkUJE7pucUt7Ltu72xcnQkO1FtUuISRUvEvVOuaRyMCCun1PkwYFB5pRVOxZCzd/VkoiegwFKsZkt2MJzI7Pl2vag1hq1glTu7ypoj3VQCncFV395Q7a7tuoGzO9W9w+ymO1uyi1srbAKoAeqem71zQOl9wEW8UrXSQieFUkW2vq2cQVgpdcejN/7SG9eeZrpcxWzQeArXdqU3oOAj17uKX0nDiWlutxImL2VibymmY1aJCp0LzS/kdM2k9JZZb6wQtNTnAyAf09uuE1iKsnbdCuL1ig+DoheTsVumN0wlCrOkuuKgeLB135fJxkyVprYOJTr6PnPw4Hypmjh/3C+Pg9PEpyvR+eu6vIRdvdFN7aYiOHpPBlFMmF1Z2SVlnkMnHNppyr2e8WBn2tLn0ZT7vNnD+wk6KqgR3O3rGRGVKevkyE8pjdTPVBAVJqrplZwa1aYSlmKNEaC17tO63XLu2a+2/lZ1qQgRkBtUO0izaSh7N7RYaaPbFvS0SkzsSSNjsToKb41dXWHOuN+zGlBwO93YwxkFndR1VW/3ASRvhnGjGudQ3wpYa0MKMtFof72vJ7/l+syImdTLJ/tGbmkYLq7NNbmKXe+QRVKV2RrOLlN9tYUmizyVlHa3fLzEeFbmoFGRR8gp2gz0wTyFMsYYtza/mrAlF67ykiSUvtBSoj2TY9vLy1gziyokhYBhw43AoSkfWI0H9X0ANTVU3q5xthvPwbEO6HPAR5PD8xKFtD52Y7CRj4eztM90Hq9JhoYU1cBy15NEkItxWKx2lwjB6zOJaZdtACsdHmpCZ0IlI4lBihA4tuLygNQ3pr6zDau7wip9yQE4Jb3nCCpI/9Kz16cGJfaKixBJlHM5KA45gV+uaJwz/DxZwbu6lqlDxN5Ueg/Rqxr0MCgWH44NtcbRie478j5YuXwv7NOQjWvJjw+tlUFq661QWK4xq2XhLgd1d2RHcMs2BJpBQhVUyEpXFPx0VK/rOyj78pNYFPeV0PaoZHv5lT5zy618QRvvXt7KFeyPZrNsPB5FjnJzvVVFceU31UqvhcNZcYiJp6C14/j8ORxQB0GkLjL3hOunexe/aI3EkfuNCRo+Gho9TL3yhG0xJa8ol+GIQX2c9KDAQHynvcsH4ZTImu8webgrQEGP0k5vhwanBZWUS3uhV/Y9g1rbdr9HsIyV7UsMLS8JsVp2o0VBfb6+74vIt/iss7DN0mqEA8ohMN+QWdC5EwsNrtI4Wn0IVmgESP9GEBIK3a7YVl6vhHp5lT13KXuIF1c5zpKjGxK3fW4VvrM1sbG7EXBK+Xl4udcAwQHiqpPhyK3nX8YrkhjO0vfUfbwBBnLL+5kv77JOS7cdtBl0PatxT6SwmlgSVYfbtj5QJmznR9ke747DktfbyUeVm1uM1+Ts+BCbb9c5b9f+csP5xuai9OukP2AMd7pqE9wWma1MXBMeJxWaBJUGdcMhmlChYC/GlfcGWyBtvgkb+uBRDJ/3BgY25djv+W45WIg+Lsu+OZGdi69a1W2W0zHwKh1Tjka9rqSCCJRAUhD6euGVHQWq7t7uiNLAlJ1RnamVMe174Q7KW6rfDqcsRXrCz3cTCp3xYRcgrXi2Nc6gNz275Ssz7zSTpDE7XGbKbVVtE7bybgiC21QFUU5SC+3Vr6jAT5eQXK4Arl3oIx3jG/ci7Cz95J3s8oy0jYrAKHuxQE5lAtaoxbZHVr7JXBu2kld0A4uqVfecYK1BjMCbtcEuN6h1SjvvOLbRbSMJflWskbEc40zVB3s/MFjBFf26AMXQajjGDSqoorX36/VOdprD/bBrO0c3AwniVtMWalG/cw/UaV0auaUMJ2WdyuUmlWFvuRN8+x7wVGkmB7pbejvhjq966DptVxwPO+l1lW3XZNPuME/y0wLNcP5SOJdYWFM0yqe+4AUtCYPScvL1vDiDTG5pIjB3t2vUyOZqLwDIHkhH12UN0zX+TpJyasqUYTuy75fbHjUzF0MY55I2VL3fU6CNYW+KfT7aeU8ZbksUuFV0GpaSgy7vAglnbq13L9Yujbq7vD43MIhd9awRAetCeyXdKpRI0kmywqxl5tTMhaWKjmBy9UhiCHbBKyhu0Yoa99gqCxkUyvvddNS5VZkcuF2TwUmnMhMRWVuWumMJDnF971M10BRXewOlGcLYDzEmTrVQ65TR4QzRt5CmUArAwn5DdO2tCywZc7l2wiBTHCxKNaFTicct1SRyY2wOo8ogK9TxO7m7BmSOonlwiOWEvpOB49lYIW8n/chBIy/ted62mXvu7AEoUtlR3uddd5ec+hKEA64eDmHrDby4VvqWA5V63493RtmcEjcHqS0hHZYVVHXhdx4N0zqixSQECHKje3WrnOSl4cmqs9nqR7yVmZXJeUFGbAMrweGkt465YV8rDLni6ZHcQYOiiJEBkVNwVlUrgPhQao77TYlhYuck9+2hw5JT3WExScS7kqyqvU9qq407HyEUvJ/dlwOyRJoBIVu92QYR2iSBQ7VDZ0g91rGFvvVFqAIVLT3xDmjxiaZSePTa78peseQ9qnSE7mBHGDNZfttdqFCDKyEM2dIIiosTyYf15Xy/rq/roDq7cIetS7wjlRZH4FRSBNH3dtZSLgGetpK9W0V4kB3dNA2MEuOyzkBI+EQuqYPXch2PQXXRTUk8AI9C7gElkHgCDUZI39Zj0tYBR04rkdpuxCDE2CkctJt4My3mAhOIBLVIoh9jCoKEPrmIWBDuOAqyhpos0+PN3wC+7Y4QN5X4kh8ictOJN8EiTGtA0GMjTKcbXw/ehmGYv7y9f5tPmV9nxf/yi2rzidD/s4Op5xnS11dPHieHoDv59Fjr07+u0s/v32o3Bgo9D9+arAtfR1V/dfT24Z+9aTDPHp/vfn09f34eqbd2OL8R/RYXXte09filKbPHiydghtM181uUzayeC77/ePT5ByOetx/6t+U8NojnEXExv1Pie/FzyHwZvo4j3795rxehvmAk8cWvq9nU19sLwELsI/wRe/vtfwHJ0GoO2y4AAA== -->
