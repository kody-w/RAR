---
name: "rar-cowork-cookbook-bulk-update-manage-service-assets"
description: "Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_service_assets", "rar_sha256": "21d9c860946217703b2934a6bd280d422532b2e43f88a73e846ac691317df2bf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Bulk Field Update — Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
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
      "description": "D365 legal entity to run against; recipe uses USMF sandbox.",
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
      "description": "List of manage service assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 21d9c86094621770…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_service_assets_agent.py` first:

```bash
python3 bulk_update_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_service_assets_agent.py   # or on stdin
python3 bulk_update_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Bulk Field Update — Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_service_assets',
    "version": '3.0.3',
    "display_name": 'Manage service assets Bulk Field Update',
    "description": 'Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6378f6d8a7b1d43a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of manage service assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage service assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage service assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval', 'example_request': 'Bulk-update these service asset record IDs with the new value in USMF sandbox — show me the dry-run preview first.', 'inputs': [{'description': 'List of manage service assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many manage service assets records at once in a D365 sandbox and want a before/after preview to approve first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage service assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9GZ+WRbDBIgV1REM4OQBEISCNIVTmYQ8zzkq//eB0nXmVnlmiL6U1+H40pwzj57XGvvC7++WW0T5tXb57ezZ2UL3kqSKPSqhZW5Czrv8yoGv/LYBv8XTp41VWS3TV7Vbx/eXK92qqhoojwD28miSCKvXlgLu03ihR95ibtoC9dqvEWTL1IrswJvUXtVFznewqprr6kXlefklVsvomzBjJmVRk69QLHNgvvfZ/qw+DHxAitZeFkTNePiej5wHxY1UMzOh58WfpWn4DAHKOxVH+v2cby7SKK6WeT+S/JCZOqHKZnXLzorab36A7jVtFUWZQHY7lbjx6rNFkXldRFYMxv8sNXPgQ+KosrBLmCrN1hpkXj12+ef//LhLQKf3z7/+uYkwA5gOwUsvj5MPTzMPD+tJB9Ggt2JlQVgWTECV2fge+FVQH4KLrmev3h9+7H2Ev/D4r//O+6tKqh/+vwlW7x+vrzN/1SgZxPO3rTqBpjqWIVlRwnwzacFmfTWWL9Mm4NQg0hlwafnzt8k5cXiz/O9H5+HfAq85scvbzlQwZrj+OXtpwUw/Msb8An4/GmWUvz406ck773qx59+k1O39t1zmlkY0PrT19f3l1iw8Lelkb/4elZY+nUWCExUeED47+ybf56qv8S9XPL1ufjHvPiw+L7k2Z4/A32fuWgDud8XC3wAdr59uudR9uPrDBBbL7Myx/vxp38k1gk9J55T6t+S+/NTcOhZLvDWyyU/fXiE7y+L5cu2bzL/8bEFSJj/xBKw/P24b476R7Ifkf0b0UmUgcp9j+V3xX1vw/LPi5//oW3/bMOHhf/ljfGSqAN5Zyfe58WvjxT5+Qf3t4s//OWvQPS/FHPO28p5SPgKMCbyvbr5+vXnH+rH5R/+8vMPbQGy2LPSr22VfE/m9/z6OOcPHnyt+vGPe8H51yzO8j5bfKuhxa958b+qv35aaFYSub9drz8vfl+J889yMRvxfujTBb+rxhro+js//vT2VwA9GbCmdR63AX78138tDpFT5XXuN4uzk7fNAgS4iVJvVv4SRgBb6wdqAIDzqjoCjn2tA/k/R3jWGODlL//HeaD9R+eF9qsZxr8+AfzrE72/vtD76xO9f/m0uADBeRUFUQZwWiUV5cu8LmvmQwGkzusBUNlj430E9fxx/jBj/S//UvbXh5hPxfjLA76jJ/KptDijXt0m3qfZPj30spc1DiAvb/CcFpyQ5IAVAAMlT7Sv86QDqDn7oo6jJFm4EcAVQGLjQzbw1+dZ2C+//GJbdfgle8I0uniyW70CC76ps/j4EdjlJ1EQNl8yzwnzxQ+//vWHxf8s/tmuh/D5DAVY94oG0HB3lo8LUF1tCpbNJAhg3XIf0fj1ry/vAjEZoGMQu8if6XXeDLIz9tx3V58F8iOywRa2B1wM3JsWedXM7BY1nxaiv/imLzh0vjWzQ5gDlnS9wstcL3NGINUC5nzzZJY3gGibqPbHD4u29h6n/mJX1kPFFJS51fyyONAK4KI8mem9enET2JxnEXD/t0R4XgdCqh/qBfUu4tPiOOfjorAqqwgr63WGbz3jMpPvazsQbs30/SWbWdebXfUojqd7wCLgGecV0o9zzEGbkoKcenYVzfsaa2bMy4M5qy9Z/Up8q/IenQJQZVwEbeTOdPCnV0rVYd6CHmb2H9B0lvSKgvuKyiMHD99tbOaOYME9eqBnY7D40iIQvF78f9wmzd4geV5lefLCMgv2eFGNZ5TmxnGO5rPXnLWc9z0q8rcm5h2o3vH6S5ZEIOWq8U/PlY/YvtY8MbCtgCUqqT7kg8QCUZrlPvJ+zuOqenj6S/ZODB+AKQ8UBKEHIAGKaPb5+4Hz3XdNQ4AE8/ffmoR3VwE3gdxeFK2dgLzzPc+1LScGWlVz7b6iDIrAm93bh5ET/sGqOUwg14D8BVAiAsEF5PHpG1g/776r/oeNz15o3vLoE1tQutVDANDDmxWcA9hHDUAwq3n26cDOzw8hwIy0aGbbbVA8wNLnRa/yyjaqo2aO99OvXgFQ+uP8+2npfNUbClAvwFmgKooWePdRR3NmpKDTAToAKAFllUYZyCrglJcTHgKt1Hsk33tr+pT4uPwyyHsU30xZ7xtnQ+Y9cxfwSuBs/D12XL6XJkBeOq94nPu3mfbttFn2jJ81wEBw4vvdZ7vw6cn4z5Zi8S73898NQj/+Z7PSg8Ovf0yAz4uwaYr682r15N132v0E0Gv11LV+UPDHJzh8fCLDxxcyfHwiwx8EP23+vPjPlPuDiFdxfF7An6BP0Hxr/0qu1w/wBf2RMj6u57tfMtX7DVzB8XkKsmuO3Ag4/xsTvi8BdBhUAKrA4icz1jOh9oDDH1QAwvAl+322z9UGmCYL5uys89+hwKMlAJn/jNo3xgK3sgac7c4tZOB9mievWf3ae/uctUny4Q1gp/dvzGszK6VzStfzlAeKB3RkTeQ9vn0bCsHnP07A7ACw1QHV8L5kYflAxuKJmXO5zJn2j6D0wzuBv0x+cNNMZVEDHDbb0ozFrPxzspt7wQdYDc3fayI/PljJpwXjAWBM6t9XwIvWZlr/XaE+/Q387ABjPyxm39QzDQN/z36Yi9yqQdUAFb+ry4ODvj456O8VYma2+gNNvXoGK3gU9Z/elQNa1Q8Ke2ew7x4GaOrrk6b+/qgZGx6s+mP90x85bb4wdxOAAh/nexbA5qfd3z3lWx/+94fooAGaRbj559mMDy+ABb/B7PRh8W0MAo58DabzCV7Wgpn/53kEm5PssWX+APaAX982ffvTiu29/eU7ej1V/hq537F+/+L1f9ZHPNj+wXtzlL9j+uMMQAyAXmd1f/PDb9rkj+lw1gZo3zz/mPHrG6gZC8i0XlXzGi/AcoCjH+u5qVoBYAEHgu9PCAD3/vPB4yWgDi3Q9wIJCOxuHQKDtmsMgXEcQm1ki64tzHYRAnLXCLJBERvx1qhPEBaOesQasxxsC6Mw7vqI7QN5TyT5+qw3IHLWCPjiIwAj77fb4JL7suap/eyqb3POAx2eRv36ZmNrsFJY1yL5/KFXS9heIbg97m/LG0QMpsFWkqnnqGW7XF0dh0sps8PdMMlDhhA3mlMjSWDTqYiDNlz3d560MVZAaaXOtuCiGZWnHCGydlvZ3PE0GGLqyxkTr7rueB8KPGM0jAOtlX6quyhYlzG91/VCtZWyVaWOI8fI0VBPHfVrN91tlLjt0NSTpISTdjbk17dOWsnL6XBGEvgU5tgoNhpdePvNvscQqRHuBKyuuGi1xbxVId0pacOEhxCCJU1eCS4CO90ulgTLng5KjnNlHSE63UsxdNKvMDoQFScm9IZrKuk6+Mnk7C68WNxu61g2NG6nEBLYkZwTCxqVaItAJSep3Epi+uJeVfvQMsNsPfW5uslS1XDNwFH248a5mePmiJrEikO8BuWm1XrdwHwUhfvzRGZ9WTkmeRvOe0W6u7tA6pc3qeSyJWdGzu5W1QUTugWdmyqrt6Obrtk8gQKUCuictrd3fnBiLu63mhTUaQkVfrZzght1qjcBG5eJeU6GY71eH+rmUJxj/aJyusmg6Xrjtd0aFVXstN0W2iQer8s7FQVxxLfUprkO1x1nnoe67ttgp+QUPbnNoU7OFx1bI9KxRLexUEqCy+oGS1Glm8BYQPA4EqKbAr23l+tRwhoHCs5mRVvROT2ahHDuRTGGr00LS3ePqel+31iDZAuMfDwwq2O0LSCi7bVjFHnnYL/U5KShi914tbxDQbQurGAj3Mbhanffl4fzqS7LQ0kEsOCaJduOYQoZ7ERESXkF3V7J7a6s1Qh1yqXrRN+0sDAhebYtmzNDQyzCiDJ5GS5Lhdld1Lpibm6kO5xGlnxTW2ybGJSe1FbPNghuFV50DTKpQs9GcQyPvqub8FU9A2CM9j5xvUSlg/JWrGf3C2LX3krVwzJZ0z5+pXIxixooNBmjXkrTydgyRFWiQ+tGV9PCsxrOWHY84NN6OeJO35epx1KazJDJgSG1wx78Z8grgpnVdiL0tD6eE0PZRPv9CupW9KrfhE11UQzBuUeu0jXhMvAIgZvExlDRUD8ddKay+yIUjUs7oGTscue82zr9kXb2cBuQjnEhl6dgb02o21P4xOfRZXlyZWgEs9zFjNpRNWG4o2AkwMxWY/U9rR5reJd3bLHfU1AVcw0TqXjvDiQ71S1zYkD4esUKJe/OWBOb9m1HsuoxNSHTbYfjJNRk6VzstevyB03OeNfkjf1J5XmI1cKWghz7dK2ocUdLiuhkAp6ltbvD2JagG+JAktfr8qaWo74Vtv0okPgxMo/pCoJy1J5GlG4OfjOWR2kdZFlDFlDCiDegX9BKa3SdCzqpnhWi0B1eOKC23nQQrKfYJO6MXaqmW+6cUIIxaplx9bUVs5YhqVa1gaRYoa4jgSYaI1SEqjreVTgsJqs2V2UsSX7MFzue8PM93Vzvw0AOUU1jMZPesEA4b0qeiBMjZq3+ss9b34F5P6l5Pdd4ZzXhR8aP7i4sKgrnDV0SJHcKcyr0QLvr24a9reV1v2UZ9bIN8bXR6ghlQbJAQnkmDWEf1YcdShOWWMXkRjNSYGev26pH72n8Wvpe6+PHIkC7qDoYJ0vpGOKmCbvRx1xeXeYIGZUbW2F6VJCXlwqBJnmUQtHySFc+js5meTphpWtAOIz3eAFvV5ioMAG23VKdMdB3XzicN8Fkn50r4xObTS4dqON9XJ9WbLop9mPI9wiZxHKAG/quizA3yBAny4tM6YNajE2MHQwedQ5rVTDp0mjygt7c44GKD2qnl6sj2sXZaPPr+LRUNfVOMfZFds4Xr8ivFz7gDlmEJVNuHBPbP4UnVrdOG16+sQHZ7y9H6bBnq65m4WLio8upIqU4cavVTuIsbW1tEGFLMPv7XT0dMyas9jd9D1t1IcIEv2nW+gZB7hKNXPa75K5IDmDibLf0utsGVxPqMjITo+RskUGeZu0u4TBOxyZwrl7en7TQl1HhvlJ7hGgR1DipzXGUaLB5zBRsuYw6wlml2cb0R2HAeFiaul3Z85aJrmvEEEmzIBvvgqw9lU31UErLRpNU7Urvd71PZiR9dG8Ib9BVe4uOG6rpmkTfHS55MOW+7ogC6nAmlyNlnQVSVawv2i4sTgYZSYyQO9eIGoTETK+Dw4NFFCfQ8n1Xh1vJg8PNjjRXsNciVBPHMbeP+wOCkiMqErk7xRttPLawiXnhUudvnd4TAZOTNHu0vLhKzmeoMJuQIrUEGVmBn3hW3VkEhMtKfB0P7K6v98iSN5zTEMsnyTt54i7jAiioGKJBom6DiOQgIoQuRo6S4RI9kAYSHERvb/A1eRyhasLonZM4G88nWo3aqRcxUEyswsuKHNXruEtUzdQxQbR6Jzokq+01162QTnWarbdcn2ralcNi6eDvmt1op+LdxyDYiOKzztwrPYp6L1ROsBOWym2UQw50/LRVQ0gSYgeFPRjn4kZf9m6DXLUSmg43JZ9YhLgHVEgO7llvQmuJpqddPhwctm+MczB4iXDvrKWcMGwji6dkqbsJMm3OsupR/mUD5xE3QvWVxxIwZGoYcWUcWN953vme+IzYXolmrVAke8mUox/HliFa8ik5pehU0XfugBbQKSZ4trQ4XSHLCGvYrsYlbohP27LPr/K131myuDLUDXOlh5sYByeKlyZhG5/Ts7Qc5EEFSeEMVTdsQU37XEEdcnaZKWsoRllScdR02vPr9Z7pUmhg/S6i5dsJhl2z2zXeBN/JQE28lEfxdXwxHIpmMrrlcQwlsA0Jy8EIehE9WcuADLfH/dRPKBcvA/Pgr49so0r47XZiTq7TyZSaIiOys7kDm7KbZKRF5drlLOFTlhknlVVzA5exWnTHd1jaUoaQ4v3KoLF8G5Y85YorCnYQ7XDk5LMDpUqasoBTfU/b8ZQgphFz5C6YRkOhWnpiYSgUW0Eo69UANzIOIa6GMRwYfdSTO98tm/FEnTpDvCgWgZp4Hbu3A0mfjlRkk6dzdxS8YGp6XUHa0j5oxHF7XdmrLbGcymN5zt0mkCdlM7T9tvNB6jjEHlJEU5H5swTpO5mIhVRNuLaDz6cRo1Zd6rAuk0HhNSvoc6y0EAaaPau6BiVVZf1a28HSFXZosektZCfePCpUEMe/Xim+LMdKCbgrFZ3NvmDqyDbRisMccp8HZJthlCiS90Mea5q0OVxOUaGdabgr9XJp9ISjTTHGIktIEKEoLzNbrxFAgkMsIBwi4CzEqxSxUWPqQuWlsdSwqDvSKZUsJQw5GWs9J45Voh1I4ljwS97i4VBBj/nV3GcnN7siMaQMwu4epUagDgIFM7iOWEiDkQfxZBzECnQIRqfUyNmhhIQ1D5uhsUt3pfEeg2VqGzS854sVN2mN4XPLC88meSKfW2xfRqasVeOGlflBS2PWVLeqD7OrgN5qHW/J2fqOJHy4pfShSMT8YhwV+bBrbbY6tENtlta5FnaVcNzoY6m2e5aTdc0kjqpjm6AY9qHmrw0W2hmoG5FbZLwtkfUEhZEra7Sxm+LVljRvbgACuD607RjdvVI4+iBJhVyJaBxxRLLEp65R9h7wpuy5J26A+Ibm9JAglR2VdbpNOKq1bV2oFYYhC6U+xi+0E+FyuCXJ9WkgueCsuBIi4piJLt1THJ3byK+GifKHoGVE196JPlThFsP6essbOpra9E7asfJ4Oayt3a0ZmuBABZ7PY/6ZdqRtdBY87rKzg1SiWEdBosA1pjvvK8J2dG4VsXU6+1SU4skNUyy/7y+Rm16qgDVP18vunu+6geTX9pKd8J0o3rO2uFYWYyU2elwX9+vhuoknEnXKLNtf7D0s7/YuYe1bvKLLQIEgl7bt7rg5mY067uP6hm7ydnV3l7bNhPHO1E98vcQOZBlat9qvMX1rnTMiOlZcwCTsZIahQZzvKrE8ePnotFcPlKQKk5ajFoFkIuL9SoEo5ZBbr8YbDF2rqzUsT5fNcWLargymzrMVoZXPN4y87C8yo6z9iGN6MLMeipxfXtog4gxu3Wtml7YZUt3gLtY8NsZ40EUf9nBTWbhoGyES5MOauUGtrDlRVMKhXOPTGZoIGds67Jk9XkLXbTZLbuU1rVkzuLPJ4wPNlAnkppNva4e+0V30opmlwEObXEZQceoyHtRDxCh4AMt3AVlaZ5sJ9npRTI203A2nSxZz57C1/aolArZrmO6mXKa7Q+YQW6RLKtvUHqJplq75vlxtsaiN1+UZzZMGDPR0e7k1XgRaOZndk52XbSUKk5wNSe4u5xwg751ktcof7wGHNOhdP4Ng3ssy76nqVF0nmVnvmDYNUG+TmfklaNIOOl8FHlE3YciZ1eZQIxvETSbF2XT99RRW+OreJ4KRS21yJyL7NJ4dPm1693TPvGPOj6kukMnpxvHdwABmB6xCHUmH26/h9L4NB2OF2KeVPa5IAl/vXFokUve6ooUC2a9OiVTgXULAXGFv5Rg6q8URjKjuJCICNVXpdoTaqGqzvZ4qfLrCw1E/1ttxv607bouY1U05T/WFb5drokqUYpvvWuGCaziWbE6Oz/Nep6XDKOfHQeHK68ZDGq0FqG4JUsM1sm2YK48jTgKuTBZ1E5XjBrGWpiOzd6hq6qq8TUy5PQ+aC6GY1pUekpYBi7gT0lCxj9CcKtQRFuOSug+WUZQwEFLh7QUxhNC0J4PzpVrJq0yx1+MNwZkqJZaJdeVg1D6MBApG6NDj77W7pCXj4Nl2YDLIpCyH7Wo1NMvhaqSymyZLv+gItyZNtZFsMHRiYPgMUgC5vX6V8PSOMKsR5yJQH+ssVi4UTNmE5DTaRtAxdDRV/5qjGGvxrbgKxQ3pxNAWR5sA8Kh1d/TW0ovUJPqDlhKTDUZBSKisaDpZCTOo5Ta9buwJdJfmwTgghGHsp9XlfhwMvLIzNcJbSm+VLvArvGvHTL7Ix7y1UwFSZAQZTZobefk8lDU9OruLY2d5jOOgilq+wD3DJTSu36yXnK3LTKQJGNZCcbVs/bpHfJK2LvJB3ZHH844kPL9tjy0uTuuhicSaKiwMBtNeDJNQouO7FK5KROfWLn30ZIeOxu1JP+BmquIKYmkowpr3fiLgw+h5fXedNk51WQc2LkbacEgH0WYNYZctw2AzrrHyJB7JKWzTQodXzvVYVNgZVK1BFyQmbuBhMK9LpuaPZNqlQ80zXagjDc+CcnV60N6eM2HMGqa0xGTrnztYdf2VgqNdu7SZ/iKfCW27d243sZ48eRfsqrVroDZBbFJqGa5dDobPxgozmdZkrtP53izZrgMccFGqjWL1GMNXJc6RzcDC8UbtodthlLeDtSsSRdsWuVKDCTa4tfAB4taTHo4WhpFNvOn0jmen7fnC8jc0Z/YkaitUi1Kcrq1Z5QJBOAv7HuZj/HG3Uia9PeLOyux30y292JYwKRo75NkFQfQttjezNYYWTtDDANHMe4TZVIKt7L0wURB5dWF6u1lldxVlyDrwVyoxJcamFFtlWFMbQVYvmqdW+ztunA9R5/TUJkC6DjeO93VvXxDfhYGh8Oa67GTPWy+r9m6EaLKU97d9e3VuGXWaqn7ZDr6ikhfQ8hxHsiLOlrOts2yHoVsN91fhHkU3MqJtSc50QyjbrOVV17eKhUPWeePmgx3GWS701KW8rSXQ33sIv/FKD0NLlhFKV4IHRsJzbW9nlDCd24Pgtbfj8ihuRxjJlwogdeZw4iTTU7cnMDwk905NepRmzUS563c8PkxRttx2B1JCuFM6LFWbFUvIHh0nyKgBU+MyVDjhkOuynG31PqGye6b6AbQ1W5lzBmxfKLeMjX0q0/XBmVZRjQjn2yitUd7F294W+5IfFSuEUmKzQqTORABVeW0gnG5gsI/QmhbtKy/ua5tg5S1CgTHnNAhmcd6uoH04ABd5E7/iENiONULnKKxuJNQ1/ThDkjV17ayG9YSleFBFwrNABTUmQGKiAc3L3U6sDbYstGu1NyQY12Vb7O49Um+toKjTw4BCe7H30WU82sT2jPrHVJuUq9foetHScbsd/b0k9tbhnlqruzmiqB3pw7Dzso4z4mSVBUwJK5LBMZM9YLdUvuuydkyOew2SJiLGTxB+n/bjThHMBINbl+4F16tywTTxi7+m1AJdyvbqNsZCh9oBV6+O3jXVa0lQeVN0TbEgiYhCJ3qUqCERhNUq8b0tepFONhS1Ibchx/JWOfIpQCCQdaUzusgWPeR4bfhFWV/uJVpu8Drzsmtr1bgjSIrl4GWe0eYqiDdwuDYsVdTLfMQ4uLkkK8u3Ta7G9ogykQXXoaWsw9U2IC4Kicf1SS9ygQZdMg/jaU5AtI3hh6w9agMjFGRP06jCngK2HNALeTmuVzJOnWjBDmBP2O0apIZsB++hscvI6LTU5Gw8btbWVDUdTHblUEiKaZQhzu0Ivuy8mlAOJVa1uwqfsiXWHJdYOXmaPwgdAuNx5WyIZlXfnBxrJ58XGLyLb10QuwMx8qR19pS20lwPDBuOdkIrB0SlW6aBjC/ZyCjR+1LIcG3KdAO2en0pLPtmGzUov/XTJMVkz7qtGyQxEHQ67FJJEUIkNnyrrttxq7AIurFwJrvZKykaaMNYX5bS/RyfSRJLjOXdPbDXnlWVo8bFu20MoypGyHRU5Qla2ecTS7iDTRSZiAS4qCNxnssCtbzez/ppkjvvLG+Mm+AylU2MCKvjPhgF/Yp29opjoNt1j6PezktrjxlD5HpvzHV3q02Uuo7CetdHU13ArHaQe8ly0mgtS0MFuH21mm69dWXanuOdVQlZy3J3LO8nsTru1xlkCu526/FKLYvLIsnCohNOqyU3nRh8RRCnniTfPrzND5Rfj4X//bfS5kdC/8+ePj0fIr2/Z/J4QOhZ7ufHWZ//A53+8uGtciKg0fMZW520weth1d88Yfv4L98rmLePz1e93p8xPx+gN1YwvwP9FmVuWzfV+LXOk8d7JmCH3dbza5P1/GatA37//hnn78yYZb8saPKvrxc+3+Y3G+d3SDw3eq6Zvwav544f3tzXa09fUWzz1auK2djXywrARvQT9Al9++v/BfJeGlzNLgAA -->
