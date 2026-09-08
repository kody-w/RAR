---
name: "rar-cowork-cookbook-bulk-update-collect-interest"
description: "Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_collect_interest", "rar_sha256": "0afd6b436f0a4e61e475e5a6b6cfdb45f4abc8a406fbcaff100570780a687e5f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_collect_interest`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_collect_interest_agent.py` and in the RCI capsule.

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

Collect interest Bulk Field Update — Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
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
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of collect interest record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_collect_interest_agent.py` and embedded as the fenced Python below (sha256 0afd6b436f0a4e61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_collect_interest_agent.py` first:

```bash
python3 bulk_update_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_collect_interest_agent.py   # or on stdin
python3 bulk_update_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Bulk Field Update — Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_collect_interest',
    "version": '3.0.3',
    "display_name": 'Collect interest Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5d080f8f07eb2bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of collect interest record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when collect interest records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to collect interest records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf', 'example_request': 'Bulk update these collect interest records in USMF sandbox with the new values - show me a dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of collect interest record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field value across many collect interest records at once in a D365 sandbox, with a before/after preview and approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCollectInterest(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCollectInterest'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of collect interest record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G894Ptq6oCsVM3bsQgQAiQQCAkJFwdZfZFbGIHj//7JJLest1d7tsdMZ9GFRUSSebJsz7PyRd+fbPbJiqqt89vR9/OF4KdpnHkVws79xZs0RfVDXwVNwf8X7hF3lSx0zZFVb99ePP82q3isomLHCxnyjKN/XphL5w2vS2C2E+9RVt6duMvmmLBjbmdxW69QAkcCEpT320Wcd74lV83i8p3i8qrwQBYH8adny9SP7TThZ83cTMuutheNJH/rhE3C+H1w6JM2zDOPyzKqvBaN85DsNyrxo9Vm4Mxv4v9fjGveKgfFMCsEkztgGDHB5c+0CTL4qaZV7qRnYezAcBy/33Qno0OgLH+YGdl6tdvn3/+24e3GPx++/zrm5vaNRh6WwOTTw9b2adp4ssysDIFYsGUcgR+zsF16Vdg6wwMeX6weF39WPtp8GHxn/956+0qrH/6/CVfvD5f3uZ/OrBo9kBT2HXjewvXLm0nToFzPi2YtLfHGjixaat8jkANwpSHn54rf5dUlIv/nu/9+NzkU+g3P355K4AK9hzEL28/LYCLvrwB74Hfn2Yp5Y8/fUqL3q9+/Ol3OXXrJHP4gDCg9aevr+uXWDDx96lxsPh6PPDsay8Q57j0gfA/2Dd/nqq/xL1c8vU5+cei/LD4vuTZnv8G+j4T0QFyvy8W+ACsfPuUFHH+42sPkAV+bueu/+NPfyXWjXz3lsZ18y/J/fkpOPJtD3jr5ZKfPjzC97fF8mXbN5l/vW0JEubfsQRMf9/um6P+SvYjsn8nOo1zkPXvsfyuuO8tWP734ue/tO2fLfiwCL68cX4KqryyndT/vPj1kSI//+D9PvjD334Dov9HMceirdyHhK+ZnccBqLivX3/+oX4M//C3n39oS5DFvp19bav0ezK/59fHPn/y4GvWj39eC/Y/5be86PPFtxpa/FqU/6v67dPibKex9/t4/Xnxx0qcP8vFbMT7pk8X/KEaa6DrH/z409tvAHZyYE3rPm4D/PiP/1jsY7cq6iJoFke3aAGQtgAwM39W3ohiAKj1AzUAFPpVHQPHvuaB/J8jPGtcBItf/rf7ANaP7gvqoRnDvz7R++sLrb++o/UvnxYGkFlUMcBeAKU6czh8ye0QYPW8H8Dd2q86gFHO2PgfQSl/nH/M2P7LPxP79SHhUzn+8oDg+Il3OivOWFe3qf9ptsqMADc8bXABX/mD77ZAeFq4QJMgBgj9AVhbF2kHsHL2QH2L03ThxQBNAG+ND9nAS59nYb/88otj19GX/AnO6OJJaDUEJnxTZ/HxIzApSOMwar7kvhsVix9+/e2Hxf9Z/LNVD+HzHgfAEK8YAA2lo6osQE21GZg28x0Ac9t7xODX316OBWJywMAgYnEwM+q8GOTkzffevXzcMh8RnHgnMcBGRfWgq7j5tBCDxTd9wabzrZkTogLwrOeXfu75uTsCqTYw55sn86JZ1CDx6mD8sGhr/7HrL05lP1TMQHHbzS+LPXsADFSkM6NXL0YCi4s8Bu7/lgPPcSCk+qFerN9FfFoocxYuSruyy6iyX3sE9jMuMzm/lgPh9iL3+y/5zLP+7KpHSTzdAyYBz7ivkH6cY/6gcRDY+n3vxxx75knjwZfVl7x+pbtd+Y92A6gyLsI29mYS+K9XStVR0YK2ZfYf0HSW9IqC94rKIwfZv29fZvpfbB4dz7MLWHxpEXiFLf5/bopmTzCCoPMCY/DcglcM/fqM0NwnzpF8tpazqvMuj2r8vW15h6Z3hP6SpzFIt2r8r+fMR1xfc56o11YgDDqjP+SDpAIRmuU+cn7O4ap6uPpL/k4FH4CmD9wDYQcAAQpodvr7hh+edjw0jQAKzNe/twUv78+Gg7xelK2TgpwLfN9zbPcGtKrmun2FGRSAP9dwH8Vu9Cer5liBPAPyF0CJGFQioItP3+D5efdd9T8tfHY/85JHZ9iCsq0eAoAe/qzgHJI+bgB62c2zLQd2fn4IAWZkZTPb7oDCAZY+B0Fa3du4jpsZJJ9+9UsAzh/n76el86g/lCAPgbNARZQt8O6jhubAZ6C3AToAGAEpmsU54HrglJcTHgLtbAYEALivZvQp8TH8Msh/FN5MUu8LZ0PmNTPvLwKgOhgZ/4gbxvfSBMjL5hmPff8+077tNsuesbMG+Ad2fL/7bBA+PTn+2UQs3uV+/odzz4//3tHowdqnPyfA50XUNGX9GYKeTPtOtJ9ArUFPXesH6X58osPHFxp8fEeDP8l8mvt58e/p9ScRr7r4vFh9gj/B863dK69eH+AG9uP6+hGb737Jdf93TAXbFxlIrDloI2D5bwT4PgWwYFgBqAKTn4RYzzzaA+p+MACIwJf8j4k+F9oLaT6A2PwBAB6dAEj6Z8C+ERW4lTdgb2/uF0P/03zMmtWv/bfPeZumH94AsPr/w8FsJqJszuR6PsqBmgGtVxP7j6t3SJx///mcyw8A0l1QBN9Q0w6AjMUTWOcqmRPsr/B21rQZy1m15yFtbuseKDQ0/7iX+vhhp58WnA8QL63/mNovrpq5+g8V+PQm8KILzPmwmC2vZ24F3pwtnavXrkE5gEr4ri4Phvn6ZJh/VOjBMX8ioVcjYIePav2w8D+Fnxan436z+LEGwXOKAWxd1c1P390NkPxX4ML26fQ/7zVX/YMwf6x/euQBmLx4TJ4H5h4BkOtDAVAM9bvl9Xf3+dZV/+M2JmhsZiFe8Xm25MMLPME3OAl9WHw71ABfvo6Z8w5+3oIT/M/zgWrOpMeS+QdYA76+Lfr2VxLHf/vbd/R66vw19r5j/w6sn0nlL/qChcjVTzqbY/wdqx/iAd4D1pw1/d0FvytSPI55syJA8eb5V4lf30BN2ECm/aqK1zkBTAfw+LGe+yQIgAbYEFw/yxvc+7dOEK+1dWSDLhYshu3AIxwMJQLYxnxi5WMk7uM24RBu4DkYHmC241I2BhOB49pBsIJhnIRJCrYJivTx+e8zT4D4+mxdgMhZGeCGjwBj/N9vgyHvZchT8dlL3w4sj8J/2vPrm0NgYOYWq0Xm+WGh5cqBENI5SrvlBYb0sT+rp9SO62SPen2n4AarYr0mSGXOjP4QYuvTNc4G6WBbIle2sDiEAh1vETbwJPLe3Z3ifpOVTpqUqdnVWH8V87q6E+12BdHEzsn968HY8entzNzPaSVrbWQc7ktd7jbaGLsX1NdH89RNdIVShoRmviynG1ly4KC+dDKkLqf9cXfRy/ZsG5sUgob0GhMSU1vWyawpjZtWy9IuY1knJkbfx6tzqx8ucmSkelEZJHutqlrbibmEUGfndnTOJnEybrpuXW6n6pKtsUuLpHp5CbMKNyne0JPMPIfyseEz4VAoWthJDi67u513r+Rb5vGZofhwaGgmnMD7/VHyOO2aVyvcy3cw4V8gRCtHGnwPxQj5DhIiSsma4n2SjfNVK0hdaM8bWxd4f5ee2QliFV+mx4t+HVEGOzbHib12/kpwomN80bm9zMrj/a7VToi1JjcWpzLtTf1MXLuJL467sD1RiGiX5m1D8Oga32lts7+FTUxgvdBL6Aij+22ZHAw7RGlpdROVfZ/Yx/NBWBGhGpz3qaCb/M3aUYeCTca1Vk93w1FOcdanTnK9I5WBaFNx9266EzKbM1bTChFSAomkKF6iSWucFJloXDg8WhVrx8dMsajtsRfF2+pUHxU58bma7XeNPcjOllOVPQcpMV3CVNuflTj2tchZVunRLM9Hg+gpy8A98u7AKemJ3PKy3e6uW9E8n7OzqxFdXa/kqXb00DiMsrnft80xOvk6OZBSZLVFwPdHl8E9ybhrAXpybiZbWDCjUdck3lL2diQiTD9fh1L1/A3OlOa6sOGxsAczbOzTuhOMS9Xez/H2GMMAtJQoNV2EXp0jU4/UcePv3SCy94RH4BN7o0NniOkbwt8vBQ81120YmxLKSjeFnbCKXodwh9BVwGKIZeXV0uxNyjXEqTtEZ+7A3SUMpECvcPzYIPDSQyZPyu6oOtjesLL18GIyLdSGEG1B8eQEZtL2B33LEEFAJrQCDW7ORKtBVjeW6F3VtGanOr74KO/GHnyWY2rF7VGJSS5EL/XRfovF+1V1oKE1DzF2jO9uaxippHw5Xjl5fYzK1mjqiJ08IsyFm32+ysnZK2P7nDCb5RB1GNWrWMhKI7fGNpiUYduGSQ/6UF9jzr1cQr7OJpHcL6drhieotsmkhlK6hCcyI87qeM8UYsXKrNTHUW6Pm+MWWCCxkCLSCX5RbyhzUVXxAIJDlInBNhsDSq8qj5DyYClVU9LZmK2Wgo2hVgqr5yEyazsKip2w7QWY5N1NWurMsWFI5oodKXqPrgu0seTyTmnpOLL7sI4ZjqKvm7S17KlmAPpERepglXAOek5fOzsx6rvdCTMGgpiuALttF7n7AYGzbH5e349Gl7O6WV6SeJ0wo4a1a0OmSxfr7EMuShhPJSZzomkSi2ocazQCjjGk9bdBSVKOrZoViV15xebZtiignjlhkh9XPeNh3rDOd1jWwWcAe5JzEnYFrCXrtUee9owMj6m7cwqWODNp1NrjqVpf9F2GneTu2ICUn8IpS66uLRDhmqGgYIObLqksLeoqyIm9ti9JQW13AdpaTkmLI2iTNQEND/J0StVDIQg+zVJLnCW85Y4jJjhjD8cjKHK9QNOJl90tUic8c6kOPiFHDMfQwm1NSbh5HAurVcT1lSuE+2Z0mLbopXO+IeSShOQdKwpqqpjr8MQt9xqrRalEyHp+HZRpT8fKPbjgS5q+UYFF875wlJC9ITq2lAiG0+Bse602KWrHp7tLrqnOlvm9Ft9GQYwKPAnZpW3VcCSmHo10V3dd5JtaYCZdJlFEO92osj9PrUL2vJILcYgjG25C2voSr6xuKJiGdDAlaRriskSM3S5NNrKFOEFeIl6HlrDer7VxItcHcZ/np+PJtoJwOJKHhrme/CV2WEfGHkU7WmKWl1bIHW2ImPF+YKulmgX5nVw224rI0R0+XKSSdEuVykoeL2/BkbyG2jq6HUlMdVJCiC2bL4X76pQKZ4bZ5hHJOhqPrALNAd0n6Ys7SMiQ1fla9Gp8UCPl3DMH3u2LVtP88M7nkcQKUJwf18xJCDSs3CfrlqOaeswT6C4OUbHbYTpXyNeLYgi8Wh/v+Z5B8zI0xrpXLxeHuY8Wxm6GTHA0zSJv/qnFe+o+CKmdBIcelbiKrvaoSJmZjEXiFklvxRFxk3ZfSEqtLo8Fk5ZW62teniN7SxARktJR36j3/omqj0WIaUosMvgeEninSyHH09ejVnO3M48JlwOsR4xecgXUiiESMtNYV5Ot7tzNieAhmF71gdjCxU08d94ZVc+iJ20sWRE7rfSM+HBNL9s6H5uTmOqosWGx1mLRSlyze/t8OImm6Q4Hitq2E3tqb6f7mYvJUyz2bhRcVWrwD5dxc9m0p4SVCxhJIxy+xbyPH8s137VtJcjn2Ep3runEF81wmYK4xs3GbDnf2QkbJozpmDm1EnUtRxDsTYvr0Xi5xeIRq5AlYfGVJkJqW/I9osfTFRGaYMQi497YcoTY1S1RdoOdxjdctdr9OmYIacqzaKfgB19Z88fCsbDzuN2WsHajhVN83bSAL4OdpO9IaSxdSzuYtbzhmD1rJvEB4f0rjNfnUWK2GaqlIrQvTt06iCWEFbObkSk0cigjDOQ9I56ZA4wH6i27FhwZ87CFodvhqiz3mRjR6FWRcbytgCaKg1xrbM/sd9SIBBc+dpijqLnEuWUgk0LNkxCtBB032VPHtaSXl6XpCz7WdoVpbJecvjtp9moFg8y+SLvwZDV1E5rttJZ0VXHDeL2S7PVhS5qJJdlItXZ1a9iAVD96ZZUIa6ulDgjT3uXejsLLeGC8o5JUnG7k+H6V4E0kRPgSjnHfhDqjoXeuLPbKhbds0rlf18zuVqaGJnASWjZiB6/YylKNqDOWKr2HeS9ibyTcKYRLXtCTZNDjWhSP5sZi8eNB2S5vQ8P4B8Rv7VPaKzSMWtC0pEZZuh8xq8WW3b5cxxMHGUi7Oi5lnttZEHuDb5Ye3chRMyShNxFoJXG7/EDTU5gU7jK78xvxWJcrZKdpt6PQbKS64jkAwbu7KbEIrzs3eO8eTwHpB7WIVaejdCHViC04PhzL487iEbQzmYvUKTkVyhE9UOcuOyRxdLqRGQq75QY7n921vcrg7ERgYXlt+/6ahQizm3ZwpF55yQjG6nTGK37im4E1B06Q0a3UmPcY2x4HIcbw2jF0PoLIa9eh5GoZXzXzmtLZFuZdyjzs6Y2E8wh3SP2jqLMJezYKeMD5TdWbUBn6Ibe+pR2jU6epaxsTSg4TkcDCRkZhkcPlcjvm5QDdZKeJLw0ieyKBjzrtKpvG28B3Ysh0z9rsL4pwx1eutYova71cZ+fgtPa1A7ypzxWRHhRi12z4MuDP7j1yC9gUjxFJ2dk5meyQD1Pci7AEoe7WsUYCjR8sPV9lJ+8GbaK6PllYpC2RBmMHlRTWpyZNvaa/SqqA4xzV0x0NEYLbFpG4o0EXSle4sHMP8vI2wgHDBBu0OegUinQXS0XO92bvQnbQ1J2fTqG3VKXGD5OtXSZKK+wo3AizUDunuTIcCqNnDZjJbfZsqkqH7IoplS1u6RlJzHb3QIe6E8NPgqjvGzzl15Rf7S7rG2mWmWbWmbEtpYY/sIKN+57T6etzF/V+gICzwfF6gMpmN9Qt3Ol6m4uFdl1S7kEarG5SCLq+ZreIq4XrGPWNymcWG3sd250MqSqkCsm50xZlyx7j0c3IuHG+P3e6x+VLWMk2siM44aVcGUOZNSssvyXhqvFw77y2xMyw4Y3SImiqLuFALI89A2UxuVQOeOgqiJamFmNPZNGz903pQ/6oOFXJBSMf1xqj8obispsk76rbeFGTbazkTkRkKrox+s2Svx/rTKlJuLgmEM5kTnBLm3otr1aTOVqH3e56Xhmu2NqJB9MlpNHaDrOs3jnuEF0c93Gq0fsQtFgMbJfhnWUTBd6EWOOYSxxHjn54RdJr22VjU7lpi221PomLXcDC+CHm0SoT8SmQZAMk1epOSTFmZ7mMkUOtQMsrNmCXEZv0vcULg1xMeltWdSNmjuhPgSCrtnuvQQeXnuBW7zWGTqdpvF7p7WSwVwe3033irYw+nvbyil3xJW6WLnvxTD80TpgmECf7Dp8CLEW0wSlS4dIc0UFeasrufibSCU7y3luymXGp/UgSTXsJr1d+Tss6rrotw+WGiLOM2/KRw5UrnrHl+1o3CdBxkPaGjdsEmxRkW13Xd7oFfebavuJLK3GKZq+JhKCzrDBwml3AN0R27tt1ni1XhieGeoJASw6KttqKvozSdIePlJwqWmRYW0ONMrgwud2pGO14UwQNaKAuk5q5B4cim7EISKM+Nx0a+h62UafQN/wCCROU23SdkZxwbmx9bqSxpU6oHewPJSdSo6L3ro0e3KYsQrI+TmVSlt2ScC+GdTgfIWc3BF5mI9NIkfxQde2BxSpCu6+dCJZX/rIEvLNt13kFWNFN7uzNiOxU1ZVqY/vQ2icwtPDKtGJRsu0uYX+GCPSORHijxkFbrYnYl87NmZIp20AL8z7VVmB2tCbD7Qkc4FV/VdYJhWplQfGXM3odJdehDqcEyVaQNy6PzHJXnavluU9c9Hhp/Wpi8ijfBizujkRSOQVieWgn3rk1pRwshxcMrdDgHMM2jRZAtINCm4pORIn1K2UDQfIFc0Kh4SIBri80HA4AMDH5zLjHM7pRNqBxRHZq3SWgT1tmsswcCAFOyEHd08WNo6AiayqRP7hDwByPV0gqpqEjyz1NKQKunMZ6clEivOaqPla9560JRKxvgqLVJ7uzUtWk+mEUdIFTOmFDUBBcTK7Z2pOFXlsnTBhCIMQO7yqya8dcNVSxaMmM6w4q0o4WsxkF9TjcaxacxyfXyYsbiTeh1S0L0r961HnT4xjNk6bKxectQbTwrVo2Qd0jgcxahrrXJUY5SgzlB62vtKQ4YUMTi/ehtInV1mTyFXmLTFLKVtUdMTeYxyq+6rLxSGvmnrQynTwgoBlEGCvpJ2q1H32/r09d6VYGFjmkGJ8HNutEh79uwSE4rXEDI+6aqDBT1GaluoLcU1JWxLGc2j10Cl3C1TCili+cySKhESBDLXBdtEQ2Al/7iNvH7uGYb8a82ck2k9J+3608Nb+gU7QkSVxTWeqsjNop74cewKGI571fJOeD6yVca6H+JoKN6wV3pvsphh3PUQS1g3RVTEoYg9sKB8ffwml2tc6iN+s8rbbMsKclZyeVgulRiVpH+7hPspVLwuTB9AdbwLmmGFsTVYTJMo6w7MKXcx7u0CTMgySpWILNB4poMqs9SCpN+9rSiepL1tTBst/g1aQ2oBtayb4Pc6FoVyq1odBlvSsa/WpHQ8PXPb1JR5qr0mmVkSEr2pFMWBxIsHVoageygEBD7W00Q7hSW25K5MJOVHgVLUErrZo+b9IhZ6ANxPX19VBWp25wycp2V+BXoLqTF+iuu5wOB+4ODgAHp4xLKcKDC4fmSkevBC6+JHRwSC7b+4ae3IY0fRSFjslACV7uU4N9utBq6hn3LUV2cCvKeXvRL+ZV3y3Xq4hNTr5h7vYb85LgudyddTjWS6RVTkS60ZEjHQ2iMVSXgasvLQZlJx9vR8Ld+pa/blku3VeyLyqnHUEjItE76/t+zK1Gpx3eGRLcvZiM4BTt8RowDXsLrDQ87bVdjNEaduqhW5zBoHR3gOGIetSrG9RT4HiS3f0CkAUcGlN8PMTTjrNawACmsysPFjh7cAKEXje363l3ze89YSxPNLm5tNHSZA6oti6qG6kOmrq+rQvupsDNUt4IdggJW0Cke6r0dWLbY3QDuVIIxTu7GVlqx4a0iTROW3e94dgUIwedGW/XUJgJN3/bXRoZrvHV5JtZ7gzp2FB4cJLv57RWrvRuq9wuA+GYZqPBiCFgJAG0U8jAdhTfL8guw2W8uzNIJZ3QtX1Z0kq44a9Kpg9KMLQg17thd8VunbOKa1uDjH69svN0z5ZkM612Qa6AE3I7ZmlMbPDl0RNtb5iaFb+t2pG2UVW8EGje4utMD2Bn5ZwGCUpMEqZw0PhwPeNA4yrFu3Ktw3oWc6cjcT2IjEX1+ywGtT1SEH5BmWEVnuSluIsTP6zLlMCn5Kp0SmmUuR24XQNJKslmmNxtsXtKtP4ooSS+yxC11+MEyZGlJPW3oLME79oKm1u8ru5uFnmOiwdZjCBRsI+VhOoJ70rbed4Ik3DgoVGVwEHStpk+cw6655Png7LLlm0vOfnJDQdM3+/DhhsEca3WHg9vJ/TQLBmXjUxsf4mQo+N1B3O7bhU3wUWsVmMuhZLWF2oCtelwi9WEGSOCWgAc8NdEuK+gnSwvczKWl9AGSqpj15b1JVpR2nbZHHvssAxkcPYwt2pXo+tmXMqKQGKbrRswQ4jUWeJkyOVyP5+2ylmxUcHBHaoqdjUUYZlMU1BkLVduucoVs9h2a7TdQW7lDZWJK1KTXOJ8aeuVqUTLKfZiQ+q9MuOQ7W7bdftmrzR405c0CmFYqWXqnj8UFiwxMdOW5wM2Geszz/AGetJxNrA4C/bBoamwl5Inj+ht2G7dDNpZrFKqx3VbEio3aEEq8k22nyr0lrTnzRoyCIFUmkgBxxqouBBUyibQVgHHbbUh4wveCaEbLtNiOvvkChNo7LIfRs7FUkz29K2RFGy2XRct17b2QF2CoAcYUzKkuz7mAcIKXRYbcgiz98lYWhSqU+dautJQpJEov1+qJUZtIYY982rGWlrIMG8f3ubnwa+nuv/Sa2TzU5//Zw+Yns+J3l8OeTz5823v82Ovz/+aOn/78Fa5MVDm+fCsTtvw9Sjq7x6dffxn7wHMK8fnG1nvT42fD7wbO5xfTn6Lc6+tm2r8Whfp45UQsAJg1fxOYz2/9uqC7z8+svyD8uCqqDy/+toUX127jt7mNw7nNz18L37eni/D12PED2/e6/WlryiBf/Wrcjbx9V4BsAz9BH9C3377v8249zBiLgAA -->
