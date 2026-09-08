---
name: "rar-cowork-cookbook-bulk-update-develop-long-range-plan"
description: "Applies a bulk field update to develop long-range plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing change"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_long_range_plan", "rar_sha256": "4c636a3deea075d862b6926229c3b9d0502408831929b01f41e6259796853453", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_long_range_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_long_range_plan_agent.py` and in the RCI capsule.

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

Develop long-range plan Bulk Field Update — Applies a bulk field update to develop long-range plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing change

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan
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
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox).",
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
      "description": "List of develop long-range plan record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 4c636a3deea075d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_long_range_plan_agent.py` first:

```bash
python3 bulk_update_develop_long_range_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_long_range_plan_agent.py   # or on stdin
python3 bulk_update_develop_long_range_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop long-range plan Bulk Field Update — Applies a bulk field update to develop long-range plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing change

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_long_range_plan',
    "version": '3.0.3',
    "display_name": 'Develop long-range plan Bulk Field Update',
    "description": 'Applies a bulk field update to develop long-range plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing change',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-long-range-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c37f5f991e942e45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-long-range-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-develop-long-range-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of develop long-range plan record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop long-range plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop long-range plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop long-range plan records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing change', 'example_request': 'Bulk update these long-range plan records in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'List of develop long-range plan record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of long-range plan record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewable dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopLongRangePlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopLongRangePlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop long-range plan record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopLongRangePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9HpfNgWM8IvKqJBSCAkZiSE0hVOZhCjmFG++u99kGQ7s8pZXdXRn/pmpK8E5+x5r7XPhd/enK6Ny/rt05sROMWCd7IsiYN64RT+Yl0OZZ2CX2Xqgv8XXlm0deJ2bVk3b+/f/KDx6qRqk7IA25mqypKgWTgLt8vSRZgEmb/oKt9pg0VbLvygD7KyWmRlEX2onSIKFlUGFNaBV9Z+s0iKBTcVTp54zQIjicX2fxprafEuCyInWwRFm7TT4mhI2/eLBpjmluPPiz5xFm0cfDWTm7dtdBXI7aKkeA9Et11dJEUEbPLr6UPdFYuqDvokGBbzjodPYQl8raq67IEeNwBfA+BnnidtO+/04tlU4GwwOnmVBc3bp1/++v4tAZ/fPv325mVOAy69scDl48NX7unnAbipz1tV4CTYDv6NwLpqAsGev1dBDVTl4JIfhIvXt3dNkIXvF//5n+ng1FHz86fPxeL18/lt/k8HHswet6XTtIG/8JzKcZMMxObjgskGZ2peTs9paECuiujjc+d3SSAHf5nvvXsq+RgF7bvPbyUwwZkz+fnt5wUIyec3EC3w+eMspXr388esHIL63c/f5TSdew28dhYGrP745fX9JRYs/L40CRdfDHWzfukCKU+qAAj/nX/zz9P0l7hXSL48F78rq/eLH0ue/fkLsPdZjS6Q+2OxIAZg59vHa5kU7146QNaDwim84N3PfybWiwMvzZKm/Zfk/vIUHAeOD6L1CsnP7x/p++sCevn2Teafq51749/xBCz/qu5boP5M9iOzfyc6SwrQu19z+UNxP9oA/WXxy5/69s82vF+En9+4IEt6UHduFnxa/PYokV9+8r9f/OmvfwOi/49ijLKrvYeEL7lTJGHQtF++/PJT87j8019/+amrQBUHTv6lq7MfyfxRXB96/hDB16p3f9wL9B+LtCiHYvGthxa/ldX/qP/2cXFyssT/fr35tPh9J84/0GJ24qvSZwh+140NsPV3cfz57W8AewrgTec9bgP8+I//WEiJV5dNGbYLwyu7dgES3CZ5MBtvxgnA1uaBGgD6grpJQGBf60D9zxmeLS7Dxa//y3sA6QfvhffLGci/PCH8ywu/v8z4/eWB348q+fXjwgSiyzoBkAsQVGdU9XPhRACxZ7UAbpug7gFUuVMbfAAd/WH+MKP9r/+C9C8PQR+r6dcHHyVP9NPXuxn5mi4LPs4+WnFQvDzyAKMEY+B1QEdWesCgMAGgPXNBU2Y9QM45Hk2aZNnCTwC2ACqbHrJBzD7Nwn799VfXaeLPxROqscWT45olWPDNnMWHD8CzMEuiuP1cBF5cLn767W8/Lf578c92PYTPOlRAGq+MAAtFQ5EXoMO6HCybiRBAu+M/MvLb317xBWIKQMogf0k4k+y8GVRoGvhfg20IzAeUIL9SGCCosn4wWNJ+XOzCxTd7gdL51swQcdm0gJiroPCDwpuAVAe48y2SRdkCsm2TJpzeL7omeGj91a2dh4k5aHWn/XUhrVXAR2U2k3z94iewuSwSEP5vpfC8DoTUPzUL9quIjwt5rslF5dROFdfOS0foPPMyU/NrOxDuLIpg+FzM1BvMoXo0yDM8YBGIjPdK6Yc55w8SB4ltvup+rHFm1jQf7Fl/LppX8Tt18JhDgCnTIuoSf6aE/3qVVBOXHZhk5vgBS2dJryz4r6w8apD7k/FmHgwW28cs9JwPFp87FEbwxf/P49IcEIbn9Q3PmBtusZFN3X4map4g54Q+h87ZyFngoym/zzJf8eorbH8usgRUXT3913PlI72vNU8o7GqQDZ3RH/JBbYFEzXIfpT+Xcl0/Qv25+MoP74GPDzAE2Qc4AfpoDvpXhfPdr5bGAAzm799nhVcOZtQA5b2oOjcDpRcGge86Xgqsquf2faUZ9EEwt/IQJ178B6/mLIFyA/IXwIgENCTgkI/fMPt596vpf9j4HInmLY9xsQPdWz8EADuC2cAZz4akBSDmtM+BHfj56SEEuJFX7ey7C/oHePq8GNTBrUuapJ2x8hnXoAJQ/WH+/fR0vhqMFWgZECzQGFUHovtopTnxORh4gA2gbkFn5UkBBgAQlFcQHgKdfMYFgLuvCfUp8XH55VDw6L+Zub5unB2Z98zDwCIEpoMr0+/hw/xRmQB5+bzioffvK+2btln2DKENgEGg8evd59Tw8Un8z8li8VXup384Eb379w5NDyo//rEAPi3itq2aT8vlk36/su9H0FbLp63Ng4k/PNHhwwsaPnyHhg+PafH3op9ef1r8e+b9QcSrPT4tkI/wR3i+dXiV1+sHRGP9gbU/4PPdz4UefEdYoL7MQX3NuZsA9X+jw69LACdGNcAqsPhJj83MqgMg8gcfgER8Ln5f73O/PbEF1GdT/g4HHnMBqP1n3r7RFrhVtEC3P8+SUfBxPoLN5jfB26eiy7L3bwA8g3/l5DZzUz5XdTMf+ED/gNmsTYLHt69IOH/+42l4MwJ490BDfANLJwQyFk88nTtmLrY/g9n336D16fODoV4wG/izM+1UzdY/z3jzVPjAq7H9R0uUxwcn+7jgAoCNWfP7JniR20zuv+vVZ8BBoD3g7PvFHJxmJmMQ8DkOc587DWgcYOIPbXmw0JcnC/2jQX/grT8Q1muCcKJHfy/egaOx02Xt3xHZD1WC0eALiHL3zMsfFc4g8eDXd83Pj3oBixePxfOFebIAXPzQDpqm+ep+80M93ybzf1RjgXHoQd3lp9mN9y+sff8g7veLbwcjENDXUXXWEBRd/vbpl/lQNhfbY8v84Vl83zZ9+3OLG7z99Qd2PW3+kvg/8P8A9s8c9M9nisWOa54kOOf7B84/tACWAFw7G/w9Et/tKR8nxtkeILh9/oHjtzfQPQ6Q6bz653XkAMsBqH5o5iFrCTAGKATfn2gA7v3fHEZeIprYAZMwkIF7JEY6mB8EDkwR/opEXZJGSRSlPcylfZiAURxerTCERmkXRkIcCUiUoCmaXBEYTmBA3hNWvjx7D4gEd0OYplGwFoV9UKAo7gPBK9IjKBR2aNchXIJ23O9b06TwX74+fZsD+e1c9ECRp8u/vbkkDlYKeLNjnj/rJYS4JEq5xuEA1WRYEpooHDMnIYrSKomhGWveHyQmte/JRdCmFZMq+sHOrklnDIbZrW2LCe2KHgpIX518TM6nqzsd72h8PUrWek/dyL5etVaG4tSV21Bpa99NU9KrpqLysN5bu7KndW7o8akfd5U47gVqp9WQhnf0cnlp8Kne4Wla43Za9KflBCEKdDjtNCFRjpOhylpiRLpI9RsMdthNtoQoOkzGEFopZzzT660HUbxm6JuTshS4HPF6MT0QhhtLGL7c+oFxsBN1651vJpGFSbx3/HM1cW6dK2mU7baoFehS6qi7M+FWtzMYsKZAx0Qe3tyzPN2rrexB29yqaN++TMV4sssIs8hreVtfBvtig3gp55pcKQJC0KoL6+IEhUU/plMfuHkcHUsGwy/hVmxQUTfEs7veZcx1ec+QrXRfrmV0PdxPgWlgA5U4YkFBAVkJdbK381ywN8wl4tNLUnbX9eT2Ol5IuTUeO2XfMMpmdbmnalvgRu1oN7G9hq03nrK1rbnYeovqa/xsU4F1xbG+rTWfvnWmOqTpxoWY687HhZy47mWm3mtShhEDeyGYnWUiYp4mulsaMtGU6MFENboWfVh3ox1fDiLkjiwsYe2ho7n+4KGNcyrxydDltBdvOynKsnurslFiWoOo4Ildy8Ma2qvbm8WaNn4Z6ygkmlOr5NkZNu2ywEtvmR14Jy9TvkqIdX4nzzuscqGVfi5LDPWm/Xqdtutp2qQinS9v+8zFEA3aCW1W70K2yTY6LvRCkxM5FHsmpFwtvtLC89Fljvm1Qde7ANZHDpJpItRWTNngq0xRJSg+XtcwYrjHVqs1tN0x51qsT/Rpr3M3JU2aTE4yq0Hpk9U5bKxM20CSwtg5ki1CTNxeLoYRotPzeplBTI+m3KAfNlQsTTx7WeZONDkqpSFqHLhlcz2GnH0IeDEi6mIoiCw/SfCO29sOe7N5hrQRNh1EhrgdaZsq8EaxHWQ3FFfmXFBd2F2W8f0c8oU0qKKwWYUhZdLrbiVs77vW1peQpSkWV/tDNe4uZjdiTHoitlvrJqY+3he1r+GrIWdXMTMdcwiLNkIi68eUjcjLmCJtBe0Y5FabMeVqvlQY7aGNd+nN2B6F5LTdRuR1w3aceSQZhWcJJF3S9/toyoPisIqyvjrDBvW6gr2XsnVCL20ySrTQR45muHgYOu1Jqi3CFgjKitEQxi8bSJUdQV+WNh9XfJqaubG6TsayWV1Zg6fMiRpv6hW0MuO0Gwfvl2LqyZ3lNwgVutxB7pXDckKG7n6wL8ZGtMaGIFP4kmqe2eiDZdw2a+e48lg1Otwxk98X4Sm5FfVKLxnJvCetUVo4c9tdcGl3V/j+Rscr/AI5illrp3VwP6jxUDMnWx3I+zmAG8/xkg4JjYpel1t/k159dZWkpnrYcPxhe7+Z0+Usq9C2ssQLu2N3WhbxqulBF7cJDy580vWSwFQJlqHDaro5XbD31+dTwEtCD46Xg5hH8R0Th3aklzZHq6gtxNfStbe1hgdXfe0h5JXdOrbZbalBP+0ghG8cgzqs186BZMMcdqrhaneTj8sE5R4cbl1uhlDBAiMtaLOhsbJdH5zEQgcKG5GiJ5FYva+i6YoWkWpxfsGbGT6lOLNCKHZ3wO4FjaOguTYuXMvMej+4OJGI0q4yTunKpQrV53cRF9FQylgaU+asRrWOsoYFRoQPmGa3RXpyFRO3uPvSsBhdOu1clfYiCvcgODb39lG7xmNR39eMjLpgTHcRxHcvRZqY1W4lGGWc3lKokro2lS+msSfPppEbZYVmvcWuhfVJiJasOU67YdscJwdZ8cqdymTbZw/88bZiGtG1l4aTpdsz3q1u2zOgLXtz5Hxt5ZIZcaXPB9HJLkx/OLK9nI3TMObTPfbvyTXOzwjmF3cSauBqOMJdM5oUuydAn1nJMbz28GT6VCaU0lG1CxO644C9tybX1/lGcI96TCzv05Xs+hNNr1ZUsSJuTU9s/ZCnmiklhn1ZFDmE79r1juUbpiMiojmHtyHFrRtspSeW1ySVWDaRwMo7a9nDg3zy+o1tXa+h2zSMTehCoaEKrgmAb1JTxPvjMeDgrJfdMdrsuYwMNZxg14kGb+DpcFLrS8ntFQa+t7fLFTuyMZIigyGTNNakyqqz9n5qibjMSxLaMPd64x273ejX4365x+7KEpXXtXqxA9ZgomrN3H39vJUsrPXjmDGDDJ34rcCt+bMYLHFagCN7gqU9LRxQchN6nJaSx8NN6MQ9qRSNVsurfjh0Yr5XY6lY50zkLafNfk0ztlNIO0WqSE9ykhM3kDQSbFu/Dj2UZ03d05Cti2ytbnsdNBMyeqMZx4nj2Rva+sv9SVgfpc2keafChvYTy623GR+z+2Ot+GdzQ60w/gBrzXpoIhK/NkJpHrnzzo2R1bUbT8Wudw+iHNnBlYO3zKZO0H3aW9BeKkdDcuUK3kyrtcZmEXvxnao2IN4xx3LUvc2SlTVZt6PkejgMXXYJjcM9OYssm18uDX2kcCsSVkjr7GKvEfhYaffnasx7uyqdQ3lT9hbc86W1DzuCHwZ+x9VF595QeDyxO1jSYfNyWMG7VQX7As1rkX267db7pdHs7hlJ6XiqiYW5lDxRo024vJXiaqh5ps4MMMI62f7IGLIvnSReYrduvE6nCtvQWUGUyQaQEadqxRI9+8mOR3dLO+PsgJ8Ot0Nz2SDi0XBucl/T4iBT6KWxGVo172cUc7epyQJ80wgAuUuUSUqm9UsVZfm1ERPuilCv08pX/fGi7izjEKimvBFiZItz0vm86zVwRj9m3HE6cyLLR9KQrxGJZNQMOeaEeEFrMdDFiLd3qBGIVaKMRLPqSAZQ79pVroXBaO1ZzBlODzNqy14JLL060pK6xdpyd+BO5aU8hLeySPejQV5UDt9lQQ7Hy8netymt8LJKUIUWRBlzBEdYor1fdfmW4SwcOetNFlsmuH7XAfC4mnAlM8Q08yHqm5xSl73Z7iNM3Mc5wVAwUggUi9JLk9TFe1Z22hR4UnbS1+lq0kKC9ywquKVxBh+WgYTvSE6uplE3NvE+8mskHYZjLUVO6mnFRg5ag6yvEbEEIR1Zl/FFyGyha8qgSZngh8i7MeIWJtIrptMRfspE5QaYW2Yg4cwax/2V3Fh743hsZRc7cxTVGK3ii5TjMqv4NHVVnDkTmVGVE3mEveNac9C3wjUWzGy3SfDaATMrebxpm3NZHy6jGjkH1Fq5l5uDMoTr+aGH0Ifrjj2q2d4xG0zWWZnA4U1TBWAYP3LcaJLHabUR6sFaVpEXre8Cb7LL7gYNVsZ3Bnse+cYzjn2pGJPY9+5o7ZpRyRRSgQPCT5ri5CKJcSblMrfSI3mjhltzyVirN0ulOU8HeWCcGkr0RF5GO/fgbdB2YIV2Xy6PW3NzFk/rkLn5Q+IjdkbAKm3ahnFOyZrhwrI05XPWCfnhsIG6oYJ3eN9m132/2gk2YtvdKLmkmNGu5LUGu88OBrOiTG6pSwG8u8R2x3lMQzUomQgWegzX5KAw3S2JmfM55FYAq6wOGa/3mi36VqSNLRofIwHSvX5s1auALM9yf9hanjiYd3GaljmeDzsBDJaMILLS1Q5gl105Ey0fMKUK9L2F8MMSU6J1fmVxMrRRQ+cCiy2SSbye7zvON5UEzvgrFW9Yb71v0X4Y8gFX1TsrV7EnBBeVV29t0zIXNbI2O7cyJWUiojq8TmQgYCh0O4kGOIbs7NgcHW0j3n0zgdfrY6mJGxrDEUqPrQ0njeOQnkgi65wqt5clFGGeA9PcSbnKQw2V1RHGzmCGmPZ4gnZwfxDAaQTU6tZaRgRxTFuEPBxXFwzCc4rz7yVGZ5nIOibfTCSs5bFDWVaOyX4bV7Q+WXEZk9FFPt43gXpIu5OjZlcFk0XF76QiltPDeTdKZrGsmVHApphDo1IlwCm3bvk2RbogGG6phfMejoKzsol2q9gcEPMaSmc4CTxC3F+dCwtqB633fLjZyf05tbYJglwQmhqiWtXlfIzDtnGtCxdGVsYKvuZAWTwR6VY5l5cpt5w8Pw9QjQy6qCHo5QQmKvxMr2SijrCWzptQ26nOyeKv4Y3SbV3pdLpDpaa5E6eKR3b42eBWzI7wBwi7ClPnXjkuEK2u5po9dIgjs023UzyZSdt7kdR3XI+EKebaon4TTXll9DA6XeTL7WKJ9A3DplaWp2NnkT6uicM2vdD30q7MC9xFHFwtQ8Hn3T2pUQO82/fcicMcObxVZaq0Xi1u24zbB/GtugsJPLGAtFW2ZzdrYbV11r5JpNKF5fTyZiWKLydHVidE4qzvbJ3fNEse0hQWHCwOxYq/5Ol22R7sMSHPSuqdq15rAlOL5NvBSvKcGrYIWclrjzRxwb5fo/x+Ffb2COozqdowViR8q4xSYDq3IDazars8XQwypIhwTzg5bVb+duOYFy3u/bscD55zu3ttW3Z0ZqC7K1L1EO7V3EUNk6V7GEM/d2AT8ajNWPeduiZS0nU4p0LMUwBVHcwL93VWI1XRXEkWPirOVr1d6sxTlwHozF6/+j3P93XS5+rZhnzt7A8wWtxUHPYcucBOrr+8NPwoUttbf9ljCACfHpLhWwybcecgiu+u9op425bdBt24h7riTa9ux/ulDrK48TUawI+RdrToXynIZiBI46hjfTwf/eYu3OvIOW8aWQDH9K3FVsI8iAnVFYXk5ZLOwlVSopJEidoyPId4HbD3yWny/XwAxm5r+cw4WtmdMFFwPG4nWbI+3XPP9nfC+XwdqrtxYG6huZd9grwrZHAPjXELSwIupPnh7nqe3ZGm5F5PAHArK1B8cGI4Umfab1kC3dQrftS2MB8HGcSvhstd2DiiFKJ86blEP2mnlip1rMyx5N6ASa7yh+uKwM6n8xUMG+nZH1lKLZyzL8fRaAvVDj53p50gkuIEWyG9Qahz7/OFZ632E+7Q3XS5CQZ8uGeOCld7yCqQkgpjptXTTYlH/IVJgpAbFDT0sgscYCNjRkfWde7YOrllrnEQkzs5wq5rrFA2uAm5f7KVSObbXt/RPQU7/YrxGvyicELQu57lrPE+GwitHROdHNJ75SGJd44GVb8rfSNPyLTWpJVdxaEPzmzWMWc5mRaxzSUiNbG+36vNyHrkkbGwZLVy+EZXIMqxM8+KKGjFXVJsagpB3vMDWl2wVQXGiCaZaECpgEzE6bwxA3pXE0IZhjxzhHHVM250Z8csJlHqeiKr5rCSR2zP3k6dlxf8+V4JjA4GwhTxQos6wjKaWburO0gR4RwSW+jSZpui13pNsJRhTYHG3cFhc0PklGG3tMei6AU7uDl3acX9WlDIQ3kftndxcNtRR2KfNXHICBDpzBUC7SM3tbm5p/FWXyGTKWTlIt8qtdqX4vWo3OSmQxzlxtEH+8jbtjOubEknvFYj6YCuEgKcF25goM7pwzTaSMRAjkp5Y5mVeL0LuBEftgKqny0rVvf03q7hdR0MLBGjoZ1KPA25SE1VCgnlskFjmNmrWCedhLDX7sug8K8ZRm4ux1Ga6l4DYHkQGdMYoFO3rlv1tqOntCBzlD7R4XaUJKyWsMw/bgi5xTbVXV63cKfeMNIxxmCIXWiDjXx+FGSTWPlexDmdvfQdxCSSk5I5+EpblZHqFY06GYHaBVCAQs1mNbUUA4VM5N4ljSf1Rm9tsxKquNfbkTIYOwup4/VwU+/GFaLD3XqHsn4+ToYL4yVcU7uGWa4hx7redI4XVtFR6erVScu4zCwMRMOhqBeulnI5HcQSSjeetxYgfvQu8rWE9mYYiBQ4g+A5LGd1xl/OiuXc+cuS0s+SHkz00tU4myOrzvdUltndjmCa9NG1gNY6nXNNeL0a5Wo88Vq5rPu8v4Y558jdfsntAbCvUzcYurtJaXSx16QcQtZKa24SbItSXe46YPbL7oHFFy44NbcrItzs96eskWyaE+T0PJCuZbUajJo8TpHb1Jao0HHlICjdPkYORH9j0FbcYIpzpr3NfX1TeJMh8x7HvHb+O3kUGFhGjry8C0WcuYGBNWW9EPb3RWHe0OtNSfLs6mwJyPB3jj9WMgGGT2VaOZgS2ttO9VFOSkK4R2WY4TihRStiOiAUrTHoMsmyS9uuWdjIE/NokC62Yy5L4GPiedy0WhJgzBoR6LiHdod0GUTAUxIfU5fu5cqsCzAN9y22V+6bjDop3HhyTx5Nmz2WnBEcIN9WaPmM7q/5bolNHjl4krrbcFYykduxNbOlc3adbQsmbPXOVFsMKxULoSBmZfYMlTaaVZXC+iIRPEIV4gpOXJKSik4+xZxQbYb1GsM2XrS5jXeDMeVmeaZYbS24ERJQotyiDUqoeelcznd8ZHxJcCneW4EhB0JIJkQ0uN020kmjk2jFIZpvQcIRtAe2Oa0IMQyVqr7eXGQsQ3i7rHfNiev7sfBWfDL1JMK4Xm8vtS5gGUwYFPvS70uLbrITGBN15Gxa7ZSjAT2RCqWG8bSlzypumf3ZOTl3veMQm/f1mh7bs9Icer3It8EhrPJtu7ryZsIhBDhM8LmlHso+COQTmnfLLQb0mk243qopFR3h9hBF69JapoBvZZg9msOJPbFudQ9gpWBLvCPFlkTgVFQEKaD3F0gsFXTTivyei/EwY1Zp6mEltum745aEdRJaSn7Ld4dqCSrDNscLmfDLjj8H5OjCMDcEp2ACRzV1S9L3PX5ANYjtNhaN7MukilFWNjNYWI+ggFeHnoIciDMjeWLL+5VW7i6sXzpp06zuRqcuZRamPVGOweSg3eQLUbUIoqrxUpKhk19UHMMwf3l7/zY/fX49Q/533mSbHwz9P3s+9XyU9PXFlMdjxMDxPz10ffq3rPrr+7faS4BNzydxTdZFr4dWf/cc7sO/8CrCLGB6viL29an085l760TzC9RvSeF3TVtPX5oye7ycAna4XTO/ctnMb+V64Pfvn4b+zpU58mUdeE7TfmnLr4/9kmJ+7STwk+eK+Wv0ejr5/s1/PXD+gpHEl6CuZmdfbzcAH7GP8EcQyf8NkE8lOgkvAAA= -->
