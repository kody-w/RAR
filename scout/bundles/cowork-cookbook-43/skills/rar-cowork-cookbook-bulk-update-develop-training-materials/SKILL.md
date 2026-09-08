---
name: "rar-cowork-cookbook-bulk-update-develop-training-materials"
description: "Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_training_materials", "rar_sha256": "027e5370d37b37a5610af9d1e98e487fbdf14c18461a2cdb1955d35803787826", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_training_materials`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_training_materials_agent.py` and in the RCI capsule.

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

Develop training materials Bulk Field Update — Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
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
      "description": "List of develop training materials record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 027e5370d37b37a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_training_materials_agent.py` first:

```bash
python3 bulk_update_develop_training_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_training_materials_agent.py   # or on stdin
python3 bulk_update_develop_training_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training materials Bulk Field Update — Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_training_materials',
    "version": '3.0.3',
    "display_name": 'Develop training materials Bulk Field Update',
    "description": 'Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf',
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
        "upstream_slug": 'bulk-update-develop-training-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-training-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b0210029a45f8d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-materials'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-training-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of develop training materials record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop training materials records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop training materials records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf', 'example_request': 'Bulk update these training materials record IDs in USMF sandbox to owner J. Lee — show me the dry-run first.', 'inputs': [{'description': 'List of develop training materials record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of develop training materials record IDs and want a reviewable preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopTrainingMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopTrainingMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop training materials record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopTrainingMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpuMbCICEAKkaGuzQRJiEasQkiCjLJIdxL4vOfXfx5H0IjOrorqrxubTKCxMAtyv3/Wc68/57c1qmzCv3r68aZ6VLRgrSaLQqxZW5i52eZ9XMfjKYxv8Xzh51lSR3TZ5Vb99fHO92qmioonyDEyniiKJvHphLew2iRd+5CXuoi1cq/EWTb5wvc5L8mLRVFaURVmwSMGDKrKSelF5Tl659SLKFvsxs9LIqRcYgS8O/1PbiYsPiRdYycLLmqgZF7omHj4uaqCdnQ8/L7rIWjSh967pfp5Gn5RFkbRBlH1cFFXuts68nLVwq/FT1WbgntdFXr+YZ8xmgVFWW89j/BzYXYA5nZV8nOVmYBow2gfGeoOVFolXv3355S8f3yLw++3Lb29OYtXg1tsWmKw/bN0/7Ty/zBTfrQQiEisLwNhiBA7PwHXhVWDFFNxyPX/xuvpQe4n/cfHv/x73VhXUP3/5mi1en69v878TMGE2ucmtuvHchWMVlh0lwDmfF1TSW+Ps0KatsjkUNYhXFnx+zvxdEojDf87PPjwX+Rx4zYevbzlQwZqj+fXt5wVwxdc34C7w+/Mspfjw8+ck773qw8+/y6lb++45zSwMaP352+v6JRYM/H1o5C++aQq9e60FYh4VHhD+B/vmz1P1l7iXS749B3/Ii4+LH0ue7flPoO8zI20g98digQ/AzLfP9zzKPrzWANH2MitzvA8//yOxTug5cRLVzT8l95en4NCzXOCtl0t+/vgI318W0Mu27zL/8bIFSJh/xRIw/H257476R7Ifkf0b0UmUgfp9j+UPxf1oAvSfi1/+oW3/1YSPC//r295Log7knZ14Xxa/PVLkl5/c32/+9Je/AtH/rRgtbyvnIeFbamWR79XNt2+//FQ/bv/0l19+aguQxZ6Vfmur5Ecyf+TXxzp/8uBr1Ic/zwXr61mc5X22+F5Di9/y4n9Uf/28uFhJ5P5+v/6y+GMlzh9oMRvxvujTBX+oxhro+gc//vz2V4A/GbCmdR6PAX78278txMip8jr3m4Xm5G2zAAFuotSblT+HEQDX+oEaAPu8qo6AY1/jQP7PEZ41zv3Fr//LeSDpJ+eF+fAM5t+eMP7theHf3jH823cM//Xz4gyk51UEYBeg9YlSlK+ZFQDUnlcGkFt7VQfQyh4b7xMo6k/zjxnxf/3nFvj2kPW5GH99MFP0xMDTjpvxr24T7/Ns6XWG7KddDiAzb/CcFiyT5A7QyY8AfH8EHqjzpAP4OXuljqMkWbgRQBhAauNDNvDcl1nYr7/+alt1+DV7Aja2eLJdDYMB39VZfPoEjPOTKAibr5nnhPnip9/++tPify/+q1kP4fMaCqCPV1yAhrwmSwtQZ20Khs18CADech9x+e2vLxcDMRmgZxDFyJ/pdp4M8jT23Hd/ayz1aYkTC9sDfgY+Tou8amZ6i5rPC85ffNcXLDo/mnkizOsGUHThZa6XOSOQagFzvnsyyxvAuU1U++PHRVt7j1V/tecoARVTUPBW8+tC3CmAlfJkpvvqxVJgcp5FwP3fs+F5HwipfqoX23cRnxfSnJmAiiurCCvrtYZvPeMyE/NrOhBuLTKv/5rNJOzNrnqUydM9YBDwjPMK6ac55oDBU4AJzwajeR9jzdx5fnBo9TWrXyVgVd6jHQGqjIugjdyZGP7jlVJ1mLegp5n9BzSdJb2i4L6i8sjB/T9udOYuYXF4NEbPZmHxtV0i6Grx/3PvNPuEYpgTzVBner+gpfPJeMZqbifnmD470FnDWcijLn9vat6B6x2/v2ZJBBKvGv/jOfIR4deYJya2FQjIiTo95AOHgVjNch/ZP2dzVT1c/TV7J4qPQNMHKoIEAFABSml2+vuCH592PDQNAR7M1783Da8AzMABMnxRtHYCss/3PNe2nBhoVc0V/AozKAVvruY+jJzwT1bNIQIZB+QvgBIRqElAJp+/g/fz6bvqf5r47I3mKY++sQUFXD0EAD28WcEZ0vqoAThmNc/uHdj55SEEmJEWzWy7DUoo/fi66VVe2UZ11Mxw+fSrVwDA/jR/Py2d73pDAaoGOAvURtEC7z6q6Zme7qwRyFuQpilIWXDbeXfCQ6CVztAAoPfVqj4lPm6/DPIeJThT2PvE2ZB5ztwVLHygOrgz/hFBzj9KEyAvnUc81v3bTPu+2ix7RtEaICFY8f3ps334/OwAni3G4l3ul7/bHn3413ZQD07X/5wAXxZh0xT1Fxh+8vA7DX8GGAY/da0flPzpiQ6fXtDw6R0aPn2Hhj9Jfxr+ZfGvafgnEa8K+bJAPyOfkfmR8Mqw1wc4ZPdpa3xazU+/Zifvd5wFy+dAsZkHkhH0AN9J8X0IYMagAlgFBj9Jsp65tQco8mAFEIuv2R9Tfi45QDpZMKdonf8BCh7dAUj/Z+i+kxd4lDVgbXfuKwPv87wdm9WvvbcvWZskH98AeHr/7E5uZql0Tu563gSCMgK9WhN5j6t3EJx//3mHTA8A5R1QF+9DFpYPZCyemDoXzpxz/xhqX4T+svvBVdaDONzZnGYsZv2fO765R3yA1tD8vR7y44eVfF7sPQCQSf3HSniR3EzyfyjYp8uBqx1g6sfF7J56JmXg8tkLc7FbNageoOAPdXnw0LcnD/29Qn9irj9R1quTsIJHkS8+gI2y1SbNn6kMaFHVzc8/XBg0Ct+Ap9tnbP687IwXD6r9UP/8yBswePEYPN+Y+wzg3YcOngXw+umDH67yvVf/+0WuoDV6cHj+ZTbl4wt0wTfYX31cfN8qAae+Nq/zCl7Wpm9ffpm3aXO6PabMP8Ac8PV90vc/wtje219+oNdT5W+R+wPrBTB/JqP/trlYcPv6SYhz2H9g/2MhwBiAd2edf3fG7yrlj23krBIwoXn+1eO3N1BCFpBpvYrotQ8BwwHAfqrnngsGYAMWBNdPWADP/i93KC8pdWiB3hiIQZakh2Mk4mKkjZEWTqCI5W9c1NusvdWa9G3XR1cOul4RqLV0XBvd4LiL4WsEI9fkekkAeU+I+Ta3l9GsGb4hfWSzWfordIm4IFWXK9ddE2vCwcklYm1sC7fxjWX/PjWOMvdl7tO82ZffN0sPNHla/dubTazASHZVc9Tzs4Mh1PaWsD0KN/iGb6Ix4G96VJyWLtZ2tnvUieEur+hOajJqyqzBoS7piSPi60WOk2BNBikTsMTRr3k4hmvCZIwyPkoNL2HLUDX2RsbHk7km7+6wmtbnsXOJY3sxh/bEH/jMC+Oja406n14dDfcShbl4x+TCclknDTQUkTAEaXBkCTLfOOXhwIrWDd6uLMcSLrTGEle9PAtifpjyE79p6Cq7GhEB5iy7YV2t23sCCao1XsXQKI83bTi4G79jVzhdJWKeZYShRW1zOh+0PLtvdrZU1SovnOuNP9ZLx870UQ/r+q6W6qaQo+hu3ytx7M8uWrlXKd/eJknAdsIhSyXGO5kx39ayaQ2RHKXLrZnuLOHWwjlqdROCuiyJ4Mogp7YLOTDUcm5TXwzKsWiBay5peIBPR94gLiPtREoml2YHcehK2Lt4rKU4WV+IrE5qaD2INzk0Wi01dM48pFbCZVvIFbGE05YX8RJ6kLxrKFlsjKlaomfltMMdnbsdiEqQ3IJrOaQT+XInDY008Zmxx29iAp9I7EQnThBfDvaKCoRmdavxO6bnh7g4OAOAUs1Vo0O00UxQKRpJT3rJlmsT1/Y3M0kDQTxSAszKZ0jAPHkqXeYmriXcDE0SPTX0/hDhdB4jYdJt+/rIcJLCxfbNGog6CkZFWwssuz9K4h4GCaDmnjcicnuCrWDc3OTCQZe5z5yT8mzfoZspwjB3IiyFqA+HkNKYxLTpgnNPWOn0goFzp7Uq2eE1bQ3LXrGKUKRm6KiQON5rGnf5c9x5ZaWohchyzkFdG/eIhSwB8tU1xdWrdXPtdhRL0VJlIHxT9rtG0rFAcJvlxUPpgpHdm3yJkiuHSXiZmSejHA8Et4Pxk3wszvgosDUbjd6dWel77lStd/4tZvuTQG9CZ2S25iaFThTSLTelvyuuJ5vlC1ziR6rZt+uVgsA3WuQLZUdNzDawmUOgMHvw/6DaemQ2+/P6xq4vXmbwaHisyD6DC0X0j02j3cntmluxFbxy/MHeK7aMXoTtoJ3MrWDKvSmm1RU7+LtuFCXZ5gpodTQOjnBXAlqz76dVEG4m14aAQ2stK/KDh9nwsXZ21zN/SuKsMZwsx/dNukK2d4mPK1WVDUujkoZlWu2KHFX2KK8OwU1Bue1eGa5LZd+yyUot01W8PCQ9gwz1JG93/vKUGo52zPtlBzMW49eoKJY7YzhSZav1xzguD2etWWq1yGXaZdhnFwgnC0WSBMHbLiHzTsXmQR3i7RWu4CliadZNDAnHlitosisNjsXaL0cSl/PweG0CbJQYMye5De0juFPue6WnGc6HUpvS6+kK9gU+CEN/ji5bXbeKbbt0tpW68xg/ys7NZtQZUrNOyY2idFUvl/ApSypHXeNu0ZS3M+qaeqdsHC0oOdWiL1pPrWptdfZZ+swI6ylRnbK1zP0U5eRSi+hw1GjX3WLkUI+Qkzj4PUf89m6W9vpqE52B5x0mddQhNgzh0G5CvdsfbF7etjCab6mGGKqVOJFnGi33h9pSr6UgugazY9ensGUOxLaRtCEHKS55/bU+74+bo9BXtjfmKwlfkRhziPK+913saiVMO9GTstmd6Mt5H8Aducb7WxOPubG0zOF8Htg2agVMGHe344oiUJLlcSzOwhW+WgtMsbRReXdE7DUUnWQBE+/81tjJjnUMqfPKvcaHVGXyVAL8Z1M7jAjkAwDB3K3iqyDfVldhWulX6iw64U28y7kwyjzK3UYmYQVrZaRXJLhLFXszoc067llroBOeP6CM3GFOcYfubm3urzopuwfQWBd6Tl7RKh+E7RHjgijfx2eKM5JNg6hrc4ktvZ4YtWPixtv2iPZQcjmK1qgu1+XJp0DR6Or+7rsVk2yiDSbIab3a+nEr+KZyD6OLiGc0kaGUJinZklTuyOToRaATqRRl8u52xqVjQec45SPRySVRNq9pzciKcQX5uCKb+65KDfZ86cMArlxYTm+3adhA7a3DGQi+dUO32cPXqu2jCuGrW5eGBlXvKppZ4goc4JFeX0OGIOrLLlzq4oWfWhWjRelyWzLGripv0X7a9neCFKhs3wdT110dioVY8crFsdKIly15PoaNGkiHSNsKueNAJ/PinrfBjXDvh/CQNEJwDXpUzMijfRdzx76ndG7gGKWnWjvc+aPsbhUyY3NGa61qh/a1dfYHfoLs2Bowc++jHm9vVc6+WkNe8t1hIDhhJxuqxRLJCo9kX6qV3JEQzPM5XsnVZdEnjp+HF4E+xaGC4VfUD8O+1/yTqhl7le71dHtmaoyA3BZnDW55mKTI2F3YiOuDHoFq86oGJE2dR/TIymDrmBxW+kSg6MhzfF3FAlGvCbKsii13wtmGyzFhnXJOH6wkWhlAO2iFu9Sj6YY5TLcY5F2eMytpdO46Sp1OsI1aIy3QJSvktXSODztZx0aOXrOx0QoiTgtiHd8OCbHmOF28Lu/GeOYPiG4Sl5N4E3KEPjmhQxErY1mcr0jnV9LRoNQRinqk5h0DG5sEa/yLMxr8dI75/FIZGxG6jJx/VwZkhcyMvTRCbzS6c+16VlFaQtBJ8kA0YXw6xi1KdFuCP9/S9qheRBjlOSN3PVvadfQOLpDTYUPsSuvgKLQlX6MaK8+HcVADny+SI78z4oSl7ZpB+jLkBF1V+2N4kqhBjHSU7+Ooph2FyziLbH2NLboAoQadgW0RJrZmFHT1KZwEZgUJbNUiA121xK646RIK8HCL+efDnQrM1EuvCrmK70a0ZbbZrk1ZqHcuh0NTbzeSq/LH3rnZCCQJEzJhZg0FpuivZBpVzfsNU8V948DyziwxbeTti0gnNLlCdqpXwCq/hqxEOQhH1BRG/qiS+3SdwTcuZc4brBO35qXxzTi8YFpvWiJ+49WzxsmFvaxPvltcxjpSVelOO95K1Y/Lrc+bx4LqmTMMQF6oKiYc3WxvRZALmTzFcluEHK2bvlour0UadNxRDQFtxkNieYhfUEp+RlcTTd6SnZ05EkTDPrzRTuXVmniEWa0zPrqa3dE/kQOPxjlznaAtb5rHVAC9cgBpUtAe2nIibmd2A0/BPZdv257XpaOa2Xp1bKktnSbjNlKHRNdQ0pyYaUhAI5yG1b2MRXyCAvpgE5FQpqquMhcqjuJuNMnc47xqqtLdjj9VohrKop0y9yLs0mWnAlYbSP46CAgu7pKu4yNGOhKZNiW3C7kXEloS9jTn+DsjJx1uKZpUwDhQqY1+X/LDrb8kQ7iEtww0XcQGPUDUOgPNlMDbZ2qgaJwHkCfV4URyYi+mNy2ygyNXACJsqbBu9zS1vYlUX+0Dw8+pVaRSWH1Lpn3E2huRgbnoGLXJejddT8oEG5ftNuPJrChwTvWpSpwy18wuk8KspfyiaPWGyD2zxwuMUKrDduzvtJLDeWXFcL9HDwOjLfNg34ZG6hBdtIfjM0mRY8pozr5GcC++MxHD56nq6SoBE8ZZwtCIZwRFb9u+lCgqQJtQurU0a6GE0Q56ZfHDxnbajTYc83LidqvpDquUi+Ym6Mn3jlpvumsUmdfl6O9ISqHkptluuWpPYko2GZhrtS3oRSe0TKg1WmDRZS2fGv+g2IWCr6I+HHbeabxy5dQVKtXTKrJ1dQOqLclvMD6RMKnYgI3Pgb/75Z6mb2p/D9NrK8YnWdsnGiJX3EUSZFwKxUSNbCOW5eOOMXAV9BZbK7uPqb+Msv1kFEOv6+F1zRfniCzaNNgIm4hRxMO0djJ7jXuwcsRL47o7sUppC8et5+CrvpSPh9oQXebSHY1934dRF3EhKXtWQjRdU/qd1G1P1rBMy9RhyEaHeAsrnDCu7HA6ObZbpBrbjWVq97oNJckxDTP3dOgyD5aPXQ476dm06oLitRV6y04Rg9iymzcRGixDGs6tYJCpzUnE9sZaYeNRbe9sJGV2TqdXjDn3N5k+6igjJSd0ZWQwTsWkqrNuS3EH7Kxrti+ofnK9OlvPnVx8U/R5oIq5Vah2O+F63MjnMl8SardiTHwq7shuP0k92LqAXtpdohiyktHselvXlbUEzd+AIjS5u996yXP6sNOI+1Yth4nz/c2yC4P0ApXWrhoqA77B5PZuhF0ydEaoq8GuvEsy2bSjGHllwHJRLI/HfapQTaQ6huT7oy+Q+IUP6BChKRm7U+VwJ333KIUtmRb1pRthSAvOacxYIWEnZI0E165HQ8vPMmi1v1b4WXKYbnlOTdatecZ1PYxMFek86NYVcleq0B/yizvlJn9OEN6gOVVWWFf2j5G67pGruqQ5XeJc3SXpVXETlL1VrrWyvUV3kuO7TL66x0u3X0O3BiJpspgKpmQOVd5LZnsiUuduHAIH9PgWuaqp3S5WQn8p0MEpOiWw7Md0zdTmYKfTLtGgzlsilizrDnNhWB30BC4t7tT20iIbHPROfOHLI6K4MaIt4axXZLB5VlP/lOhsj5I6aNiS87G+4Z3s2ownFK6plbZ7hoLNhEJr16pujhTmA5lYGHfflPvKbU2vxgbclwCQkaYntk117aXG9AZCbxTzzjG4a6PnOypDkSanuuQRyoYx1UtZ9r2LtRLVZd3+orXSUrZkb7LboSDueKbcLhLmSGJZT5tsLd+N7sLw8Op4qq9yBXynNa6ooLx893eli5QHpu3rgZfFu25fwlPNoYY+btLiXJ2XWOAKe4PY+eu8TDiPlMl96Q0XSD/dVu4NSQsSdLUJpuKhFvf+XkEYdxv3liUoNeOReAZvRhweLsSgd7vDXrJBtsBjQ9lXSbSNm59d92l07KizeUijFi1UUC9SipdyvT7f/WKLyvSahosTaCpKDJaTgFiHDceEVaQQqqyy/PHsbUiVx9B2WyuMWCH9kXDJ493qJnHIK/g60MbhWvJMoLNiO2KpJBtEMfCBaTjnwS+geNXYyIB2Wxcz2W19NCDK6zoP3jmrerUX4dZQ0jV5JOVYvIkqLjA6Z9SrKl1l7IXHMLs5O52eIpi9KvliwiFBi30yLpWNezkCOq19B+xyyqOlWdSeD7ZnPiB833PkJSlO67QIONcsLGLYXs8KugfdAmmWl6qEbmaX7CXl6Ow0YnOTV4S5PI/K0tOxpWjcqWm9LAnf23O3Je5w51VoZEakF3pBh6JXu1eFuFZ5eRcTMUD2DEt4MXnbDJqSToXVSVBgxftiinn2Ep5XgmoiOwsqt4jBQ3TmIIYWrohpj/cu49x3HlLjxe6GwjScIITr+21Gdl267dm0bVUmhbzlATAHK8kHlD62RGY4zsTAg8i09q6TfHcMbsmmMIsChYnT8uDSMCdgleReeMnF3YhP8f0R8no85dPi7tmosRy9O4EmmwPolMcqPd2tC7Kc/JvSSNfLuETvt2rpReE+2hMbg4ZWPWus5Wst5UefHdNlUq7WHI7Z5BkP041lXQdM7/20k6yx94ioTAq1JZuyrvrz5OFQpyWHsGQt+yzskettjxy77f4uYRStoXsBo7LGlPdUHfjwCdYyfSy5QAxJhGWZi39hXL7YkwZR32uHasiAybqsgMMV2wlpBDHF5jpCRdt7Gw8f1rvIPMEpBJOa1DpeZwnaxI7QZtr5wlDmuXPF9krvoZtprbTSurMyjMhT01OipMkQWhjvlyL0Ny57yxsoGXYAXZFYajnP7+U1p1uZtrukhH+XPM+9uRZ6xqOLnFikxrsIibbDgBGlYjFddyvhK+XhJzIH/lLdIeV2KNdyUM3pxbLHcmJlh0dx7Ab9TpbKpN0hyOd2oEU9Z+Go2YiRI9nk1xS8W1qXrNyCBFsH+rWt1ulwZI6ZHB+GzZrVlPuVuVyEbQ7HtOPsWOg6uPn+jkDHs+/xJGNdjExlkyLZmreWJKadCS+z1mg2E4kvQ1bdS8RmV3g7StXLNVVX9UHZaKAR3AMe28ZmE9+k7QnylRZWCEPJU+S+Lluxz+ULwFHSVUBWFt422SIo10xuug0KrCEvNkB00buNaFzaUmuW2XmdXKJYCshba5jxHYIFY9qWZyIyJpY1m/t2coiJb6ZE7CBab1Kv3ltxfXbMxiVbItRP94vJcj1sYUlXY7QEtsUb1joOpgBJ1EEvPT083qJlr7cbF8oDwjq6oDj1rJCwsJis/Q3srLxJRivXmnrf2txUdiwmFUaYe7SiCr9sl+FmsoXhEKzwzdksV5NLb+MwCZrYJQRWoXhupVhnx9/j6GalbKhkp1yPBI0lghU6UosfNznuYkSBupgPu0HXjRJBEP3Rr4iqWd49arPEC7vNvdwNJi+k/AGbLmfMYu7XhgnLKBTg7opa9lojMVPKJG+QDZZvltB2XHaQVmWOIfhxdL6KFKLzibhsG9vOYt+68c6mtxDZ2FBgM2bh+Hm1i6+7jToec4xUfKGnVi6jjDa/qbEr6aVZm/WG2eVdtCyd281h8pVFNi5PUL52r0rBsMoTfBhypaL22cY+3RB4bVywOqu5xqqBUWuX3Wz9FcoeVJJcn+DOyOsKuqs0xi5NxM4CVRrW+5S1h/yA2bxnRk1aWNGmQdZELbZde7+zVwTqV7AFGcTmWl13WY8tza5x0xVW1QiJ9dj14PF+kR6a9cTY0R7F68Jjln4n5J2CS/ayaXHWxhQ0MzXm0OpkQCANGwS7HBCeboeSuNXP/WV72frF5CEyts1XLSE3KxSJeZnlPPdoQlIuLumGt46bcOWDFj2O/VuO0VmrHwjkRECk6DZ0e8DgKmunezQhtAQ74hJHo6kp2GBVblCKuMoSmpUX7LYO13tRkMjyoh7OrLRj7sfcx+uOwPGbMm3w9S5jq3h/wljQYWDqYUA1HjkEiWPDJ+zWR4wjqZv19mSDmEDy2G9ImCKWYd93vNpT1NvHt/mk+nXe/C++/jafHf0/O8J6nja9v8ryOG/0LPfLY60v/6pif/n4VjkRUOt5ZFcnbfA62vqbA7tP/9z7C7OM8fl22ftB9vOgvrGC+S3styhz27qpxm91njxeagEz7PllJK+u59d6HfD9x8PTPxgEriz3+WKKV31r8m/PM8v5fpTN76x4bvT7ZfA6zvz45r4Oqr9hBP7Nq4rZ6Nd7EcBW7DPyGXv76/8BmT3uQlMvAAA= -->
