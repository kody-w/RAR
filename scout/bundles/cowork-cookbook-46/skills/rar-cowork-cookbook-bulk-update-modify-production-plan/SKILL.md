---
name: "rar-cowork-cookbook-bulk-update-modify-production-plan"
description: "Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_modify_production_plan", "rar_sha256": "c54a6c354e8015b7badf4a57adccd982605b388e3fe40bf2866b3a373797cd0e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "field_and_new_value": {
      "description": "The field(s) to change and the new value(s) to apply.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity / company to run against, e.g. USMF (sandbox first).",
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
      "description": "List of production plan record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 c54a6c354e8015b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_modify_production_plan_agent.py` first:

```bash
python3 bulk_update_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_modify_production_plan_agent.py   # or on stdin
python3 bulk_update_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_modify_production_plan',
    "version": '3.0.3',
    "display_name": 'Modify production plan Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c337897eacd1f3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_and_new_value': 'The field(s) to change and the new value(s) to apply.', 'legal_entity': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'record_ids': 'List of production plan record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when modify production plan records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to modify production plan records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM production plan records in a given legal entity, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these production plan records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of production plan record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) to change and the new value(s) to apply.', 'name': 'field_and_new_value'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many production plan records at once in D365 F&SCM and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateModifyProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_and_new_value': {'description': 'The field(s) to change and the new value(s) to apply.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity / company to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of production plan record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOj1pblX1HfimjbRWaCmJUVFdGSGAQSkyQQ4HyRZgYxikEMbv/3PkjKwc/56tXr6E99Hc4rwTl73mvtc+H3N6dr47J++/h2CpxiwTtZlsRBvXAKf7Et+7JOwa8ydcH/C68s2jpxu7asm7d3b37QeHVStUlZgO3rqsqSoFk4C7fL0kWYBJm/6CrfaYNFWy6YsXDyxGsWGEksuP952kqLqi79zpu3L6oM6K4Dr6z9ZpEUQEiU3INikQWRky2Cok3a8d1rQ1JE4L5fj+/rDuysg3sS9IvZ0oeRYQmMr8DSO9jpBuBrAAzP86RtHzuBX87sSZjUufNQ/nWrE7ZB/QF4FgxOXmVB8/bx17+9e0vA57ePv795mdOAS28b4J/+cEwq/SQc1a9+qMANsB38G4F11QgiO3+vghqYkYNLfhAuXt9+boIsfLf4939Pe6eOml8+fioWr59Pb/N/R+BdG8/Bc5o28BeeUzlukoFIfFiss94ZGxCxtquLOeYNSEwRfXju/CaprBb/Od/7+ankQxS0P396K4EJD9c/vf2yAOH69AYiCT5/mKVUP//yISv7oP75l29yms69Bl47CwNWf/j8+v4SCxZ+W5qEi88nld2+dIGkJlUAhH/n3/zzNP0l7hWSz8/FP5fVu8WPJc/+/Cew91l6LpD7Y7EgBmDn24drmRQ/v3SAiggKp/CCn3/5R2K9OPDSLGna/5bcX5+C48DxQbReIfnl3SN9f1tAL9++yvzHaufq/1c8Acu/qPsaqH8k+5HZvxOdJQVo1C+5/KG4H22A/nPx6z/07b/a8G4Rfnpjggy0dO24WfBx8fujRH79yf928ae//QFE/1Mxp7KrvYeEz7lTJGHQtJ8///pT87j8099+/amrQBUHTv65q7MfyfxRXB96/hTB16qf/7wX6NeLtCj7YvG1hxa/l9X/qP/4sDCcLPG/XW8+Lr7vxPkHWsxOfFH6DMF33dgAW7+L4y9vfwDsKYA3T3CZoeff/m0hJV5dNmXYLk5e2bULkOA2yYPZ+HOcAPRsHqgBYDGomwQE9rUO1P+c4dniMlz89r+8B7i/917gDs+o/fmJ15/zB659/gbQjyL57cPiDCSXdRIlBQDX41pVPxVOBOB51gqQuAnqO0Aqd2yD96Ch388fZjj/7Z8L//yQ86Eaf3tAdPLEvuNWmHGv6bLgw+zhJQak8PTHA4wRDIHXARVZ6QF7wgRA9jvgeVNmd4CbczSaNMmyhZ8AZAGsNT5kg4h9nIX99ttvrtPEn4onUGOLJ501MFjw1ZzF+/fAsTBLorj9VAReXC5++v2Pnxb/e/Ff7XoIn3WogDJe+QAWiidFXoD+6nKwbCY6AOyO/8jH73+8wgvEFIB/QfaScObTeTOozzTwv8T6tFu/RwnyC7kBeirrB7cl7YeFEC6+2guUzrdmfojLpl34QRUUflB4I5DqAHe+RrIo20UDirAJAc12TfDQ+ptbOw8Tc9DoTvvbQtqqgI3KbObz+sVOYHNZJCD8XyvheR0IqX9qFpsvIj4s5LkiF5VTO1VcOy8dofPMy0zar+1AuLMogv5TMRNvMIfq0R7P8IBFIDLeK6Xv55w/6B0ktvmi+7HGmTnz/ODO+lPRvErfqYPHnAFMGRdRl/gzIfzHq6SauOzA0DLHD1g6S3plwX9l5VGDT9L/y/QyTwUL7jH1PIeDxacORZb44v+bwWh2fs3zR5Zfn1lmwcrno/VMyjwYzsl7zpLApIeyRwN+m1q+INMXgP5UZAmosHr8j+fKRypfa56g19Ug8sf18SEf1BFIyiz3UeZz2db1I66fii9M8A548IA9YDzABNAzc4S/KHz39O9haQwaf/7+bSp4RXmOAyjlRdW5GSizMAh81/FSYFU9t+orp6Dmg7lt+zjx4j95NecElBaQvwBGJKD5AFt8+IrOz7tfTP/TxufwM295DIYd6NT6IQDYEcwGzhnqkxYAltM+53Dg58eHEOBGXrWz7y5IHfD0eTGog1uXNEk74+IzrkEFUPn9/Pvp6Xw1GCrQHiBYoAmqDkT30TZzUeRgtAE2AOQABZAnBaB6EJRXEB4CnXzGAICxr1n0KfFx+eVQ8Oi1maO+bJwdmffMtL8Igengyvg9VJx/VCZAXj6veOj9+0r7qm2WPcNlAyAPaPxy9zkffHhS/HOGWHyR+/EvB52f/7Wz0IO09T8XwMdF3LZV8xGGn0T7hWc/gJaDn7Y2D859/4SC909afP+t998/xsLvJT+d/rj416z7k4hXd3xcLD8gH5D51uFVXa8fEIzt+431Hp/vfiqOwTcwBerLGRnm1I2A5L8y35clgP6iGgATWPxkwmYm0B5w9gP6QR4+Fd+X+9xugFmKaC7PpvwOBh4jACj9Z9q+MhS4VbRAtz8PjVEwH9UezdEEbx+LLsvevQEsDf47R7SZhvK5qJv5ZAeCDoawNgke376A5Pz5z2dcdgBQ7oF+iMr3zjz3P5Fx8YTauWHmWvtHCDyb247VbN/zuDYPeA9AGtq/6lIeH5zsw4IJAPhlzfdV/mKqmam/a8ZnSEEoPeDOu8XsfjMzKwjp7OncyE4DOgM0xQ9teVDTZxD7z4B+P4MIdMFf7Zp787Hw5+aXGV2fCXxkbLYB7Fw8dr5ug2Bm4w+1PSjs85PC/qqGmenwe5ZbwDNbVTNSvMYPJ3oAxrtF8CH6sNBPErf4uQF2uOUALKyb9pcf6v06b/9V6QWMObN0v/w4a3j3wtV3Dxp+t/h63AGxfR1AH38tKDpwtv91PmrNlfXYMn94VtrXTV//YuIGb3/7gV3P7H1O/Oavhh3A/plvfjwZLASmeRLdnPIfOP2QDpgA8Ols6LcIfLOjfJz/ZjuA4Pb554rf30CLOECm82qS1wECLAfA+b6ZhyYYAAlQCL4/Wx7c+784WrwkNLEDBlsgwiNwh/QwAg9oZEm4lOv4Ie4QlON7nr+iURIhXIymAywMcMQNUZokXczBKIxaUZ6PBEDeEzo+PyccIHI2CQTjPUCf726DS/7Lnaf5c6y+nmQeaPD06vc3l8TByh3eCOvnzxaGli58odzxYMImQg+2xe1PiXHzV7JKBHay8xuR4ccxrtTW6tg9w16UisvOlWgzaMxKawwV1JwPq8Nqsksr2XsV2lQthZLiZs0W6SSmEwHJmJq7TWBQd//o1INhN3TSdyUiZjc/Sq1TFWRSbgT7LGXL+10uOOuk8uodXvo7HkETW3RiXlSoIaTv1/M9QUbPleW+PgltcafiFXTI3BUe3FfkNaebckSl1liXyQnTW53YCbYdCfnRuaEC1WxEvaPPlNJCCj1Ig2cmLSGg5Ajzt8A2InxELnjvb+pJHA6wqCVja9fGUaMlHBkUuj7FXm0Kp1Vw1hAz9qaV2cHl0ukOCDCVQgh1UHLXHzwYUg5+Uibp5hwdLSNvmriXaOPAnfL0GNttX8ciGWc0t6k81wy00VS9k+zBTKjeJYYby+OhjHmB8TMqn608bmxJNU7VJN6avUn0hiBOxUE+B0o6GVpXJRuFvNsOKdKn06G+rl2kMA9XbwpyaWXcuBDJES1Gpq1ciXo/OtsdAem0boM4bwq1h6K9KnDb6VBJzfK0d7dcZySVI4c20zUJduS69dowQXAcbpSpI9X01IDJVz6zLzySnu2DYCXnvWx71Lm3hHSZRneZrKyVt09G+UKL0lLKNRc3UXqP3jUPaoTLpCv2SKz2laHHK++611GKpyHUUov8sOI2EColZSRuRzCs6axyow7ysdkqTS8WBHvY75BWL41dGtDBaF3q226Q2GKtmCedzKjlkie46Ma3a1blYSGD+RhWyoDlLpJzrs3kqJFG5PBL6cYjRnm45Gt3SFGSvGVWjJStUB8MyzYK+e4bbp5a5yY2rwcTv1yV2Nzxx3SpXsUraikYG1Ho9j5WnHZUObllRn6waC7vYpIhTEO96hR7S0o0OCfW8YxPjbqBIPnMS2SUEXB7xeHdVcaZXaCEuVUcBgXlB3x/JZV2Kjmyj8+0Y8JxSHNYMVxrr4CicasM4wriVVo5YI0JTkuxmXD2mnCVUW1Fa9kMWF/6xKU6k0LqsuX5YGtU3182dKwlyH1VbHfw2kmIA4Ad0xVv0N7IeVLkVf3iYbZzblMCsV1JZJFJu8X0qWybnSblUmcie2F3VxAuMtVJ2DDqcEFVudtVzlqfaMfdjj3XWKhdRPGSEmAp6Lf10N6hJeJN1s1yDfYYLzes5fc67q+d/OoimaUd90Y1MJkOe7QR10xbci5es8fSLu/Xy7qlQsjilR1qI6PV3u3h2E05B3EnC7YzkzSGrak6m2t1AEhBCis+zIZyo13up0t5VIPc1ZDD2LZScxdEMhr3Iw/Z3H7rV2mt9BpUY5KGeFDbCYqgEGuiukPTTjCssB9HKkDq1c1Lui4cq01iAjAZzaZAbL0q6mjDSCixFDipRjOqoUtPjg9CgVj9uqi7UEcuqp3vLqnJT+eeWslhcl9X7r2I79ay1PZYbNFH8rJehgd5ynG0pxFJ3BTUvupVtm0Yo/TEvBwUGY7XhmVdIS5DjoYQj+UgK0EWFdkWMvmOK417Ye9WvNS7xHS86DzLFTV8OE2Fcz+r1/Wgu9pZ99oDDU/XzBmxiDxWNqFF6l0LTFLcBqG2DbO0s1aMfPGRYRWsQn4od8qGj4XhJns7zyGjq9l7dRHQ4lDuUXkfM9qR0hOoqqEVv8ZX2Q7akJazb0/EKhK8EFCLrq7LTogMkuu03SStyePV2N6E/FaN7Tpdc4VU3U2SEpf39Hpzt3SqBfbpeOZg98q7+jkXSs/npIq4LI1DoWK1gKKbDSnc0LhnbUVcb0g0tzTrcjBDzabOnczmsb4ehz1lorqel1V/mXJQ9axd8ElEmYSMIl1jNoQ9DlXfUsdSnrLuInFpkZ+nbaAvUxRWrikc3hkka6QiExsJik638FgZJafwu4OEXYJBI+vNJucQygvU1Y7xTtRtlW1YBBbKA7kvrtQKJ2AIZv1yfydG2jzGlFcpdFLRRJWG29qK+k2WnjBcdTOST2yHveW3Qed4e71GC2jYehqLGqHmgpGwDgS54HPMsC2hVxJVgWRQ7itzXznciVvmSrSyrxoaaUwStZsi5dXQKq8EF16FuKP2zLa+OmKETEbZ16t6qrK2Yk161HZq4XL86PRbbpzIs8FUFGLpaI8Ql+0SMXwS2lqNcUerYbW59utNKgdBWmenE+iHFtpsjIyc8N1O5ndnxaExX1JTfZREsUcOKEwJvpyM+iFZn8T9TozS/rqh7zBzP+Z7NZZQJF8nHpywe2nFlPxSES5yudkd2FK2YCW9eHgCI8tlT1m+wLG2g1JkzSbHzV7cbQzxsicPnqZNEkZBOp7e4svtxFolyfVYIerrqor7vdYao9MJCdxCTR8dCEPZrS2yEIiUE7BxW9FhtJSyeBCrfX/eK0aleddp2N7kpNo49w7d84qRACQORzdxNc1ak6PltOLlPgX1gefoKG/2ddQJbCOZtn+jwKGh63FhOkZiZNSuL43GwIZX0xo9R4iD1t1vO0IyieWl5TRK5no3z/DVpT/tCtV0YHO9YqtpMrOcLkiHykVdaeUsDpPNGSHLxFttfXkrsxvH3Lrj2XDoSdgOFZYrTWlVvG42YtrXW6HOtEjbjCmZQpF85ji12eHpUotPNoKtsexOHVlxxZdb0MswarqJwHd72MoYNuAGAr1atyPKGcxtB0H3pk6oMM77SFAmlQEzVmMeaYGPN9fUVAvK2i/DjYNtwnqj708R59Ir9TrSK2k1uqqlnHaBej2wxrDkeoZ2zyqlgfB5VXLpr4y44T15ENjbRdqE4a3cby9TyzurhEkO/abKVtczJ59Ni1CRwEN2nHGFpVQTyOZw2PAJtQ8cdjPdZacXCTQ7tfGRjev+ejZX3DEVWDRbJ8GuPyorMd7V4slncficmJsr28uu6ADih0lMXBtbIdpIq/psF9AoGkq/rtYIKx62XVxWh5yBNQ0t1R21O8qoA/EQ6TYwtFKbW+yl5M71mGbgvTBVXWwlV3qhXK4EIxIes9yN57u4cVNncGtfL9AugrG7slWS2pOMvXY/nA/i0ev4DSeWa+RQkLhUYe52U+S4X7Ms512QglBUcuNdDS3O2hQ3OW667hvY8iqxSUIHu7G3FMsnUhOPEOEecIYZBqsQta5Z7fJjIvrm9pJZ7Z5TRUFSDo3EA6CLtjS9Es/5ZqtD9G3JBQ6YeQ/eWfe13bDZ5/TW3XNpZTMUPXZCIVQNQroRzgK02k9RE1rLVbVq8iNlLs9WyiYsipi3gbnEu1t9idXYy9PouhXdgDqmB/K0XNEr2F2e0LNy4XNAMGs1YQcGgywO3WQ3oSSWGLK+Eofar1wcV1Z83iPplt4WvdKuUt9kN258DvcSZ9dLfWPqxZVkaqapp2l7uK3K0opDnAVcFosHF9kkJ9uEypulJylyk9iY2uGgy8ysqxsRz8rzzT7lobUJ97l5bq9CaCzFO4oMacF1TWOIeHyC0L3FDxeK31ZtrrbtIIrrnFwnbH++72By13fTRjisetv2m8y5e9INQjQB+IXY0x07LjGsMJ0AzZJWbiDH9RVcISfMoJUjDWiVcSbq4AGsGNNYsdL6sHeTek0brFyuDZ0dGpPQGrjpRPhSSYgo0gUiH5q1iBOguippnQa+4V+Tfnm9DAFjHcW7lKIJt2HlgOjatIhos8cZlToyld1sIRu7eZXZBuxZxloJ5CLEzgPRTfKeaKfL/XjtDF4i4CE7iJO+1xpL8jkjYBE3jtg05OKN1xknUEJ5ezPuMryRnSHPed7jqVanRUe1vSoTqLuq+bVv5yclRFoAwWsJrpanEjdyfefimAoPS1gm0/vI1jeL0QPZ4XQtltEpt+vAlsH8tuO2DY+O3G0TITa90orzErdWx4jIcTc12imlN1V8Kskjo3P+RRHgwBMUnWOmmt0QfomweT1OJqG7mCznKRaqexfwkFDz/LnJ0TUtim5+u23uqduz10unS+AG6YpHkpDdSzfauKZHNlrg9/A2trWemvrYUU21VdbRQE/nQhd4pLPwlGzl8xWDg3qJH0HxyLiBYhlcrC4XIo9UY7izcarp6e0qXMh7ByPRWbpSEB96XkToNovRuHLa9muW8HmkuPIk5Bx3jFZfqpRrT3BnJupKvx8P/NEyNxxm1CO+3DN8Zzhxy3ErQp6ENID3q/B26SJz3DJ+mhlJkIYBmD30kxPUulBtiZ5Ze2YFn/kAMJe1RvWh09uuXx1NwdeXN5U/Xm4HdlQyhwlsTBeuuo9aNiLkFNajQehe1Quc3EupILvlEQAAi+l8OBYdcvajiGGW2GqAtW1HYgdIwPawsC6KZSRKic+SsmuXKuohR8RgGY1yr9rWyTmJ9IgKM5MCDEllSIml0UZqHPg4B01WcHUqJbpiCVd303Vpq2PnnSePuBxJdKlfVvVKgYtapqmlQuLu+chgu6w8mrUeygiJkGPYGThq0pQjDV2RO6jYmmEbGEOAXHUGO0fYrSXOE84r/qReaiZ0dgiYA6X+4KHTZc8J8AY64bsyrnJwk+pq667psL/E3F5fYrfwfujNaZfeljeIkcFpjOJuPbFb0nWo9410os92Jlo2ZZEmzmhX3dRXx+awVNkxSG23PkOo6R8Y66ZkMGDxe40xJn48oxlT5Cl03B957H6jURrUvpAEPFP60FrUpMvZ1OxVPhRQvILh4Q4lhCHJ+SklugAeQtrZynfLCu+yMYUChenydZtvTSlt4zDf2HSQDHcB3zvavUqYyB2vnUDCRjlZFVEoJHq2+mGHSDucSdPN5NG4BZGmNPGMk9+si634y3PjZpTtU+glol3EMnomKpcQtfeWxPV6YXMpPweS3FJwJea4fMZKI9v6mM1vdBY5wiRsmkUYd3rqmbmPSbsg8DO/GJVDJgD8NiyqwQ85XuwMEcNc/mzcTzmCufhNjCcCOpzSkEpv6tIw6v1ENmHTI2G/Lc7BmhGjzVmM8DAMPAWlpAnPq0jYiJVDDpuLdkXoNDYo+2bUN8i07xkjK3tveyJXJorjNuqP6iW4YBfJuq4nGm1I0DeseSc84YzHFmUlxrDLB2HalbsKtE9+aT0iFlilsXoVeJQs73tvXPq2g6+l3WUtjYG5Rpt9scYZtDmZrba8ithoT+w1QXYuGrnStV/GOEFo7iU7qPCygmjPME04h1wK1xQJHHERjFsOoYRd43ILKuwiG0tVOUZh2e0ufqvnKkRqVAaGVDwCc9iBGpOkmRKIQG+Ky9/IbtAm79jaiu4tuUm63v28cauzMTnKymUuqsVR8iCtgq1Ytzna3fe26g71AKm+lA6bzGt718qnDS6jvXgjsfWABkltpQcKizGPyFTEcYyhcArrwigOgrjUmmRuUb6kSTYfp/uRksg+X4opv7/5KCN45tmS7mZtW4GlRPtYKc27iKxuiqXt0itMqrle7jh7FzdqsC6h8UAmo0xovgvZkeHmrCopmD+dlk3Irxx6oNpWrC73pbikpgED8y5CSRKNEbBDtCMIcrLPfZ9ari4ErsMrsaNQGlkaHlWTV05Nq5asL8s6wUEPr/IbXgo9Jo95uGrvSHc4FZ15Wl2s4wRtlvEWYKCm391kdVqONOkb9UXluQtpXLvGKI4oWnCK6tT+gYf9zRmyjlReHwY6JDiEx8u9PtIRGWVaUR+8ax03bDkdQjLbYc2x4O5LIrDWRuNUIkM3iHi0K2yr2hvlACPMxtxCa8XW0s5Xxza+MeKuy8zNcZTjtEnoJDWvG3gvrKGd2mQJdVQ5sQlSKPXRRqonP7oYnS7nQcNUElHC+f5unVYyHqDRTjMPWy+JvK0Q6qJwaF2aldqlRkqYttrZ1WlV6Yd4oHyYnbgVyyOAaOGc25BNu8d82+7U9oCA0+rgCvTBJ63LEe+WPuY6IxOE4zK9uXJn3woXyo0klcGhurPs9ArBB2va3BgysabdzmqvAF/ISWynTA3pm6FLrbdbCs4JvjowJiK7ctrexuAYQdn9ENqd6GJ4RAaInozmytH2pd60jH7fNDhhkaR8FnRdp1pTq9QtOJoz+TKFcJJuE5AuaHm979yVqe3GatJM1D4qGLQ3V+aY7sCBJ9o08E7dT4cLw5RXid03GVJ0x/VExDa3pmosxuH+fg+mel9y+BEzOnpjm4ehLHZY7dYn6qIsOyJ0O9ZHj3JvBMxguIYH4UyHJaYc+OWV27W8T9/OsQD7o0f2noQJLGPqtg+RaHWEl0zbSJDPuTsiQm5LClH3joxKgQhH7ekiyAiyiaX8cnVW6D1wzrLvp2dMKfvNFUkscJSgEknb+hYFkknmYbhalxtG7l111RQXKnC9YuvJcjFth70vHFyS12nZRiGEXIdLDcm4u2Roq6SkmaXmX6BdaqxCjOVWlEilh1Pd3RpsjGltB8nbHlehUAwp6bLb3xts0460KPMEzu68cD1EaJMzfo6aJsgnOJXJDsa7rkkaGubD26NkUATFTMSNONeo02qHkAntvCNM93oBZYCBmcMy8RbNLBSbJDEX1aIbMyu0m6ZLaDwdMIyntrVpw33Sbi0LP0P89ZSe1msn86DWl1i9Z0EbGFwqrlIZO5K0kiR1SWBX96SxtB/bdFUIaDQJDpqVNbbbQDpzumgrpQhOCqGZlL+r3aZH2Qtl3qE2qLfSQfU0bIUPLhaISl4GzHhFdaa18cK8V9jRG3e43DdYUxmsIUn93vFuEYySq3oX+zA8mf1ND7ue4z24LW3oJsq3qybU8gGfpmbHLAeTV0tF3FfLIm6xXehC22B5zCeX1aL1+m1+RJkFr2e8/8I7ZfPznv9nj5aeT4i+vDbyePAXOP7Hh66P/4pRf3v3VnsJMOn5CK3Juuj1KOrvHqC9/+fvCcz7x+erWl8eKD8fiLdONL/G/JYUfte09fi5KbPHiyNgh9s184uPzWyiB35///TyO0dezzI/t+XLl/lKUsxvhAR+8lwwf41eDxXfvfmvd5o+YyTxOair2dXXmwfAQ+wD8gF7++P/AMq7Qnd7LgAA -->
