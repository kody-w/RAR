---
name: "rar-cowork-cookbook-bulk-update-plan-loads"
description: "Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_loads", "rar_sha256": "d3b1e2ee71fe630a462ec7d68bd9a84029a9c196972d21f5b6d3f2ad69c1a681", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
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
    "field_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox only.",
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
      "description": "List of plan loads record IDs to update.",
      "type": "string"
    },
    "rollback_plan": {
      "description": "How changes will be reverted if the update is wrong.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_loads_agent.py` and embedded as the fenced Python below (sha256 d3b1e2ee71fe630a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_loads_agent.py` first:

```bash
python3 bulk_update_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_loads_agent.py   # or on stdin
python3 bulk_update_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_loads',
    "version": '3.0.3',
    "display_name": 'Plan loads Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46fae0057797d298',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_values': 'The field(s) and new value(s) to apply to each record.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'record_ids': 'List of plan loads record IDs to update.', 'rollback_plan': 'How changes will be reverted if the update is wrong.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan loads records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan loads records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation', 'example_request': 'Bulk update these plan loads record IDs in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'name': 'legal_entity'}, {'description': 'List of plan loads record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'field_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}, {'description': 'How changes will be reverted if the update is wrong.', 'name': 'rollback_plan'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on many plan loads records at once in a D365 sandbox legal entity and want a reviewable preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan loads record IDs to update.', 'type': 'string'}, 'rollback_plan': {'description': 'How changes will be reverted if the update is wrong.', 'type': 'string'}},
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
    print(BulkUpdatePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVpbnV9G8jhjbTeZD7JAVFTEgEAixSAgQkrMizS52xCaQ2999LtJ7mXY53dUVMX+N7Ayhy71nP79zzoNfX9y+u1TNy6eXQ+iWC9HN8+QSNgu3DBar6lY1GfiqMg/8W/hV2TWJ13dV0758eAnC1m+SukuqEhxn6zpPwnbhLrw+zxZREubBoq8DtwsXXbXgp9ItEr9dYCSxWP/vw0pd1DlgmFdu0C6a0K8a8D0k7qK7hO+c+XmzYOzA1j5Oyk9gX9c35cwkaKaPTV8u6iYckvC2mPc/hKyihRdGVRPCbtSFDdx2bte3HxY3N+naBbixcOu6qQY3/zCzKoFWRTHfmjX+Rh/oGiVN4T60+/ASjm5R52H78unnf3x4ScD1y6dfX/zcbcHSCwc0th6q7oBOyqwSOAMuY3CznoCBZxp12AD2BVgKwmjx9uvHNsyjD4v//M/s5jZx+9Onz+Xi7fP5Zf7PAErOJukqt+3CYOG7tesledJNrws2v7lT+zupW+CfMn59nvxGqaoXf5/v/fhk8hqH3Y+fXyogwkO/zy8/LYBdPr8Ag4Lr15lK/eNPr3l1C5sff/pGp+29NPS7mRiQ+vXL2+83smDjt61JtPhy2AmrN17AwUkdAuK/02/+PEV/I/dmki/PzT9W9YfF9ynP+vwdyPuMQA/Q/T5ZYANw8uU1rZLyxzcewPVh6ZZ++ONPf0XWv4R+lidt9z+i+/OT8CV0A2CtN5P89OHhvn8soDfdvtL8a7ZzPvw7moDt7+y+GuqvaD88+0+k86QE+fruy++S+94B6O+Ln/9St//uwIdF9PmFD/NkAHHn5eGnxa+PEPn5h+Db4g//+A2Q/pdkDlXf+A8KXwq3TKKw7b58+fmH9rH8wz9+/qGvQRSHbvGlb/Lv0fyeXR98/mDBt10//vEs4G+VWVndysXXHFr8WtX/q/ntdWG7eRJ8W28/LX6fifMHWsxKvDN9muB32dgCWX9nx59efgOAUwJtev9xG+DHf/zHQk38pmqrqFsc/KrvFsDBXVKEs/DmJWkX4P8ZNQA6hk2bAMO+7QPxP3t4lhgg5S//x38g7Uf/DePhGby/PGH7ERJfHgD9y+vCBNSqJgEw7OYLg93tPpduHJbdzAmAcBs2A0Anb+rCjyCJP84Xi6Rc/PJ9gl8eZ1/r6ZcH7iZPjDNWmxnf2j4PX2dNjjM+P+X2Qa0Ix9DvAdm88oEMUQLw+APQsK3yAeDjrHWbJXm+CBKAIKBITU9M78tPM7FffvnFc9vL5/IJyNjiWb1aGGz4Ks7i40egTJQn8aX7XIb+pVr88OtvPyz+a/HfnXoQn3nsQD14szuQUD7o2gLkUV+AbcAlwIkAJB52//W3N5MCMiUot8BLSTSXz/kwiMMsDN7te5DYjyhBvlW1Bag9VdMBlF8k3etiEy2+yguYzrfmOnCp2m4RhHVYBmHpT4CqC9T5asmy6hYtCLY2mj4s+jZ8cP3Fa9yHiAVIaLf7ZaGudqDqVPlcvpu3KgQOV2UCzP/V+891QKT5oV1w7yReF9oceYvabdz60rhvPCL36Ze5Cr8dB8TdRRnePpdzVQ1nUz3S4GkesAlYxn9z6cfZ54+CDRzbvvN+7HHn2mg+amTzuWzfQtxtwkdvAUSZFnGfBDPw/+0tpNpL1YMeZbYfkHSm9OaF4M0rjxjcfetS5jK/WD8am2e1X3zu0SWCL/4/7n1mE7CiaAgiawr8QtBM4/R0zdwNzi58NpCgH3kweKThtx7lHYfe4fhzmScgzprpb8+dD4e+7XlCXN8A+xus8aAPogm4Zqb7CPY5eJvmYenP5TvufwASP0Cumi3qg8yZbf7O8MNTn4ekF5D+8+9vPcCb8Wf9QUAv6t7LQbBFYRh4rp8BqZo5Yd+8DCI/nE18uyT+5Q9aLQB1EGCA/gIIMRsU1IbXr1j8vPsu+h8OPlud+cijDexBvjYPAkCOcBZw9swt6QBsud2z+QZ6fnoQAWoUdTfr7gFXFR/eFsMmvPZJm3QzOj7tGtYAjz/O309N59VwrEGSAGOBVKh7YN1H8sy4UoBGBsgA8APEUJGUoLADo7wZ4UHQLWYkAEj7FjNPio/lN4XCR8bNFen94KzIfGYu8osIiA5Wpt8Dhvm9MAH0innHg+8/R9pXbjPtGTRbAHyA4/vdZzfw+izoz45h8U7305+mmx//vQHoUaKtPwbAp8Wl6+r2Eww/y+p7VX0FeQY/ZW0fFfbjExw+zjDw8QEDf6D2VPTT4t+T6A8k3jLi0wJ5Xb4u51vKW0S9fYABVh+500d8vvu5NMJvMArYV3P2z+6aQEn/WvPet4DCFzdhPG9+1sB2Lp03gCgP0Ae2/1z+PsTnFAM1pYznkGyr36X+o/iDcH+66mttArfKDvAO5rYwDl/naWoWvw1fPpV9nn94AYga/uXkNVedYo7edp7SQJ6A3qpLwsevdwScr/84wQojQHEfBP77lsUDRRdPlJ0zYw6qvwLfWcZuqmehnlPY3Lc9kGfs/sxLf1y4+euCDwHK5e3vw/mtMM2F+XdZ97QjsJ8P1PmwmHVu50IK7DhrOmes22YPmP+uLI+q9AWo1T8N8UeB5ux77Pix/enhFVCSF4/N88JcpEGNm+aL0AXo9xTmu3xyEBj5F+A/kKh/5vMoa48ti+eW9+7CjR9I8GERvsavC+ugrv8GEKUMvGoEoJpP3+X1tWn+M6Mj6GFm2kH1aab/4Q0uPzxK74fF15kFWPJtipw5hGUPBvSf53lpjqPHkfkCnAFfXw99/euHF7784ztyPc3zJQm+Y2kFnJ/LyJ9agMWGb5+la/btd/VtqjyfK9Ojk/4zaam6vecZKBoAn723CWDOajANPkvPoy0BCXhrqjL+DpuH/KCEgEI8m+Kbjb9pWj3GxFkiIEj3/KvGry8g5VxA3H1Lurc5A2wHiPuxnXsuGKARYAh+P3ED3PsfTiBvp9qLC3rh+U8omIeEaBhSSBSS2NLFSTT0qYCkvYBxaXyJMi7jIwzJUGiAIhHhkQEWoW5AglWXpBFA74k5X549ECBJMFS0ZBg0whF0GQRhhOJBQJM06RMUunQZzyU8gnG9b0ezpAze1HuqM9vu6zD0QJunlr++eCQ+OwhvN+zzs4IhxAtR2hspBy4JJulje7tMjo7XbZYdZjCCXRycvThu6IseL9mc1KU+k8eq94bzBTVWgsbulhZ8MjEZJui76pchkYv7ktwPjipy9Rny1CLa4QDz1Z0PN6XlT+tcSG7IRG+3akPb22bLmVF9Fdp8l0oYjPcp4L1MKsdKxipSy7Q2skEoxSkNbZGjShxmmSiRQzh0Bvp43VNZnW2z+A47RVsnjXUY6VzLclQWiJoOS1G/hvZ2RHbqlq7aOsNWHj/oU55khdccyczbw8Lx4GzybGucr8XRuG7qcD0lZ2JzaicJz7zrqfNPAr/RVPTgjoXmbrsTp+bFfqlOfDEs48kIyeKWrghMGALKuCK+U5OQjtVomGgqRk0kxNAW5W8y4nKqlA2IyPJ4IFFeIU5X5C74F0spDQGDWU9yc5WeZNPvdIVZbU00cs+Fl1qZI5vqVlBvG3Y7+o7BnXVHz0/njDmuFRoHd/BpXWrDBtUZW8pGtomcbTtw2+3+7IgCQugoKhLFXZUZ0FPDdXC/Qklh+dtVh+tlu8Pobl2z+mivan/S2e1us15N2lXLkMRwRfio5zF2TzRWD9qDtxfEg8zLZnjHwh6uAtFT6WA8XWoEuRYJl9Sn1PLdy1TGxHHNC2JfpsYlaspk2porZrtsD5Z74mHTbvaVEe3v6DnbkbUK2+nV4fyrhOTEtTzQ6IaqnTueRPY+si6WJazlw7rI5MojlPOaqsKVhaqJARnbS6yNbeBiNx3aGaopkrFv5Ot7diERO6DW7FHs4o0qnvwYLgrIEXj+QK1UBRnGTaVtbwEvFmve22Zcsx81fKLOgW22Bmmlkk3lJ5lJtTQ8y8Xe2raXKFEiupK0Y02Tl7RnE2oKV108hAxbMiTvC+YYnSz10h4jWcn3DE9313K82rFjnOudTOjs+nZGyz0kFZeLSN/yyy1I4puc0pF/h5wkKPg0syU62JWnDQJfS7yMYCvCr0ZDLteoSePwTsLHKEoxVL8F5Pq4SvB82gM1rE1o5qCXbe0jIYjFctpG/Sq/9zZAsOxo0gddL6OhXqckezqOW7WHbeqc0Vs7VULBEouVj3BklGbi0gN6tHga18aGvPQqf6z2LrE2zZI95hRN5Xcqyv0dF2I78yrkt6ApNidsbeMiy7V3fdR9lOvPvr9qbkUKb0lda21VuoJFm2fLtT+eOQel7ux1Z5e4TjtYP1Q+OUJmh8kiw8NQo/nVZqkplILjG6o1xVAvbhIaQl65vNj3/OjAZ0SST7daX9ImqQB38mRy30iwHhGSdltDcgiJ4e1eEXZI2n7AMhoX3tshK4tqk25qmsD25uZIFnlY2QcvkK6SfbtMq9JtW8qnW/cmFc1ypfN54FmUBJ2mrB7UpdLYMSsr+2m8+FgcCLgF5/4YBMsxz3PZzVao6nPeRodCBDL2Fn1Uu5CjTWVnDiiib+kkP8AhemdR/m75jRTvYnxbno+ZSA3ndIXfS9Fpr7CKH1CcPRr42UVVBPU3bDAWKn502PUyl6VL7yaIwrmGcrot6WHVUdTGi+9FeqRdi0xitoOjs2u5lO+psJLpqcu6cFdGJRTQTWFzkrlTlO1WZm7cGJ1F836fJJpZkV5p9s5OuZlDwEdJZIhDfAs6v/SN6168Zzik4ycA/e5S21wC3xitRK+vIVOw2NmWxgt52m/rCR/jlR+BEuNgbN1v9h55LPx1K1pVJtaHdbKujmp6GHf78nxZk9EQadpQeKa0OhqbS14zku41m7sL7ctcZs+XY5zLwAWtd+zSVSWU6sXdOtC+ZevEQSEwoZdedKZ4T99MFroXq0biSZAHxlXmvSlf0/wtjQ1W1Ri0dZ1CwvxWdO+ndbe9dV0G6SKRhMp2natb8XiOJASNdk1BHQrucPUOnO5n6q7KrtkhzTjooGtla4XJbScnoMtPCTimiUxH+3McaNhqxUPDMsrzDRNFzTpHYIj2h1t7h6GUspqeTpqbfHGiJD3FMedlK4zQqAuxdTVfcJorYW+k8960Cojgvf0esaMTwSGBSe/PhCacUPm42VeygFPIwHPe+W6utC1fO9Jet8bKk7korlb0NHHS0BbuOt1IYySjggQ1vGvfQB0oAs7l2dZV7npuQ13CC+15TRQqfTflVeuRB9CmnMnx2F5RIrndGblSlsFd33pWHdpxd8z9vmzz2Ds69i1gY7LlSanbbRrJspeV1kEsa+XFnZTWgSiB4kTfO3UXn67qSr61CgpTas9VBrZdD3q4ESdxZbWSkdwTxoENbEOtpdv1bJrsvofH1Vo8psv0IAiKVhCTtcaDym1HrWwaKqtumqDUq6M3bIf9NtlPxuGQTOpqGrhYUnngFBM6bnmoQrnkcizV0UOEVVZzlJVfLUKsr9UFhrDrmG8Osq3rl5Prybig1kOmMPhuc1va50k+yOexVbzlSd/IbL69bqDD4OHthGyKU782yk0HcI4X2STJTM/OqXaJJ0bi43Lq3nIuobcyFuZepsj7Tl/fcugYlOhdPqRcyMLSfTAEBRjS10b5wOi1TTRFXbWrJd5KLiQaft1T5ZWRqoseumg9LcerQ3fsRSP3azx2GL3YDMPeMtl+xCXrkNdrMhv3gzDxrXt2L0Gx3hoXkeICdRsLW2S9UwkyKzP6ppmUvRVAP6Oxl8N5ibFYDlP7tcwUm10BSsxJwixZ9Xk4sdQz7kj8KThw4imPpkpNCTKp5A7SvdW+w73ruSS6BNK5DSpt9jEBNS6HD/i22GtMpudptq7hwaOZXXpQGZ1BTbVCTQEyC9naq0tGEDAKE8L4GLZZx1m9yW0vum3Fh+1yQ2qahLrJqd5jjXEyZFZzq+Lq500+cHIPYwXbX6+7atqTSmmpV9Ft4uqM0aLqMw3uNK7tDpt4xR85MetBMyLueXmLWEsxngLSPCiBvJ90M8O95TAOJuuyYqz7hLa7+op3sQKHOHDx5lCZa9Ou4GkT7aV0LGp02PqOjnv0HYJhPFv5lSZ6IOovuukt7+ESirHWbOS92pW0bhwuiLzMYnpS8XrZkxjp6BRN37O0EiDQXGubg3VhitQyuBOyzQwhTq3WV7LWmdr9uvALLTmIPXnd3UuJYBujqaqkWnNBCCDrcDgLzHIQ1FwetCK7HRMmxpwbr0zjqZT34aCJkHGRDWfVuzV5IM/h3sEdfMOme09YEzVklConmNmyLmxmbPza8w8ZwxFhjl8uq6iFo43Y65wpnnBUIlnQSV1DLoNUKQfDnb61rOp42Hj8JjuIUwCv9VOquJt0Gh2ssc4r6NBF0W5AGb8rN21wTKADv2Fh1Iti6RTsibvmOBlPE2RO2ApN6KDHTWtZd3MrsywfMvTxsIRUWE7DPr+pQbzbtwcBNDGU4A/KfhwVXEyOZ0/YEsyqi7TCTjmHoM+WOFjEcSnbjqfHrgql5O3QqlDGIiW3HqwdxJ6q4TbaCHPzfIFhiWC0l7yMlfrKos9mu0SOZwk0u8d826b3XsAkT+ULWZfVQ99M1GbF3tYJCzXTKoVOfOxp2KlCqI3IeH6vGfI22k5KMZYOdDlQ1zgVR1+kq3Mbdoh1APMGLaBxGAfeiV8FBoRBnl6OPYUE5/MJpUm2y2g30xp6CRCtxBFpXTp6x6do44sOcV9fdkK2yXN1tLPolESgEyBXh8Jg6v5U3TPzuusR8zzt26vVQb1OrytRytQSqYVLNd3UBuU6N5EvXi23SlYLhieklxHed3xzjzYnoD/kj5AVgpaO34Ghr6gwgys0py50am9hIxIMPOj36LqoxpMj+GJtqdX6fPdSrrmqhX5xnU7nJNu9BUohEMetS4Wht+aJqvEFi/Tv7BBcC423z81BWUcGTlLpqVZRw9VNq0S36W4LgDnkdnkawpoC40Uk0ocTnW+3CYs4pX1ZC4oSVER+xe6mE8Xc+TRywBBubG3OjkRNxMY2UkK4X8/rnkfxKdxUt9FPN9zV7+HdKtqJYqqQF8K+ckm/PF9Ngzo3t8rwiuJeeMOQ73a7zD2IySm7rvGmRbq9F5x2tOKyKTIWPCcXFADEtMNCiMTXdw1xXC3lINS+eBaEVCTJerVR4seSrfaZHFwAWNWiBcFXOeINdctYCOeURw8AR4cdT6tQyeXN3SqHtSGemUkKpkBo16y0SRC1VCRFtw+GthOF5ciuVqjplb64aX0cux93J68gr2Tt0RHSFHvJ0q1jmW2QkegojyjAZCW4aC7by2x3Ryj/0i7pRuwVhxQZTens47Fzoo62urOVI/uU99p0xQrtlUxNaSqjCjRGHOgPdqRLWT7JsTJdkCdp4ynmhYRUVZSZ8zHSOvp0ujW+qllhnAebtVQFMV6Z+ulSSSPviaCtiYGriWsQbO+0j+JrBLuJNS8z++u5d5eRvpPVAD7yxoEX7wO928bh6pDjfZStJv0EZ7f8Kl6d0e2YPYqsbni+5fYVRSreecP26l3bBMtrlKFXCbq5MnXy8LIMOVeVdhV6bSqXMcaQQgkgKn0vt4ypd1nf3W15aKM9heolxg+2510G0KVEzbETPO0UeB2ZIgWDKUS/agdPHnOmdo9c1zTQjswv+I3YYM31ePWLC7FMztONbzADjsftmhVOROn21sGBhYYvinRVuLQa9kmfMXePrvcDWCXcLvJ2Ir8ktaK38Ttzz3Ts1IrXKtAxVHIcvxXEkykW5jLE+xWGT0J+NM8Hw09ox6pKkYACEzXZUEldb2WC0bOvEgyKcfi4NDoKcxwQfOglvWdHmNsKKAq6SZRG6fUhCQu+CmhW32is6ccuU0wwbDAwPA5Q0hy3ViPTNNTBo0a7pTbsT9RQ2fewMqON26xVts9lb7q0YlmjCgQwqZNtEAmWChOHTB84t3RCk0+h8oLF/J65Swy73vBxhuxEuMrulHnzViMveuyWDKht6hEDV3adiaN4t3c742S5LZHrLj2OpHgUeTXlRSksIVnA5EYPk7a4Q9RmPwfIADsuBFGMdkvSlrzrSMwoVN8AHOEgeZWp5/2ld+JeKcAg1kRM1Gktc/TMrrlU6LArq04xht6oohF1yDqy03sh8vjl6JsJexZWW0KVTIoaL0fsXEQZonJcpzWOtdmSG2hDF9udtzt0gTN5a6g614QZu45zHTHpLk7hCN2nI3pPs5MQFYxteri7gh3QojqiIlDiQVcEVBZdhqWHHbmvCIVX1+wFuRcyCdEgG2u/ODYpiI86Jk8xX9ax1qzqUWOZRqBQkFRZiUvnyRi3UkqxWmkw14kBjUXnHbJygBAwryxbmqGxuw9bK+7kimTmOuTh5FMibue45B+uSp9dOFjzdurdrVuFRkZsO3ojqhRN6WC1xAbLGw0mbn9c20sGzYtN6d3UirgqxakIS+1cHtNmDcaV8Mgc9/zdLVyTSSXT0xg/XKJnjPeOTDjU20nScaVCbh7V34LkJrsTyl6gCGtOR6XBUszSmuHS+/al8bBI5HQXQjxlReHX6oiIJFMkoDlWdKo4MtvsKAJogTVfMs/qzri26k6V9hwYOvU17RnoKY9ZyN3BoA9M95ad6fqNwVcpVaVXZQ87HJJzxQUZTuxypBioUjmG8ZDyjuokekTOkIh5gz5ErK1E7Q2DQ6dLS4yURPvce/chiJBIWHOlKUIAXaSu93SIK8pzhjL2BO9GdbdrQkQJQJ+rmZhSLztpWKI7/aYv85xIVxQYiUexsECydJJCUc2AAs3N63AyqmXjuHl0KwpS0FEqMqijRG/RkrxF9+0uPBCQzg9qxzoyN4l2LmX6VWAcTwjOWmzrbhl2BuMJ3kgRvnNkRW/Zh/uI11ZZ6CmJtNzfE5zZ49YNzlbFcq2U5rI6XdvJwKrm1p1IdVPbdntM6T1HjJvdeF4X3W5/x2utW5Zt3SFxJwRH8STm4bJrVS2DryGRYNh6cEIxiNllunRLvFqzB3UpTTp+hNerXRdrKQMa3+LoRFjO43SIwPg5hhLF1aYtPa1i5oh2Xp8N+9Q70PzW7K6GklChuT4MCtqgiHvwE2JoPKM+kdQROnYtKC63o96GeVpMCg5rDS/WXqqAoSQSJ1VklG5X7HZWt6P2uY8hrGdlrdfsFCxaIqur7posWQyU43dECUQJD1gGhlttG8kVe+3MW8b5MBq52Wgyy8TxDPNARCsfVvRsDeLPpdOUwc5Q7jWoJVJlT7CFoZMrl/PiJIeulCthWjuIIp8OpKk6WlTHaqy2dpUMhk/gnCZyjd1kG9ANwweoGtsDmQ0GgDrPUvLW2Zqt5PWQHbYHekd1eUcag4c5nElEdtAjzagMWKD4EI+s2mO4Jk+wkd2A2ujoq3dZ4B3s3JE4StjwNfXcMz1t0N2dr5kUqUIfA5MKbcLyKWtP67riV+e2ExEsZpll75IUm/eBkfDSRbhNKwwTTrFAjsvDPkIhuMS521bwMjSiznqH+ijZV7dT7SD8KNsHpYEky9fOaL8k2B1hLJF1q9onOMGXPBIbCHTMbGYHi3lAydReOTZ6PwwyB+8dSBvHTIdgLqLc7W4LV0tOGxk8EAlc4P2IJS4o7XIBStuOatiSHWgutvLq5q5UVEJPy17qdXhqi3CwrkjW0BqSeZTn9QGKawkEGs1bM0qMemOa4nQ/GSEsZ8oNvXfEuCZorQtrDdtQAUHZxaa3qPiwJKQ4XlVOVFreRVM5y7zZnM1FtekvdYyr8J7UOxxZZrIubcJge4a0SkWFTna3zAWPcpbOssipMKHsrTW5NEiIUoNO6NcY3JT9PU3uS0GDfRUlkOTe1VKMXxmEJY+6hpRXG3PoC82rikZd7f3alLSVmG6riGgHkiCc3Z1h6FUpNRlvYBKZMs1+PSKHEdYJ22hghDE4BO2lKoT21UGBsF1atbsADlxFrwuCZ1n27y/zY9Y8fHs4/S9efZufI/0/e5z1fPL0/l7L4xFm6AafHrw+/StB/vHhpfETIMbz8Vyb9/HbY61/ejj38fsvL8xnpuebY+8PvJ9P6Ts3nl+ZfknKoG+7ZvrSVnn/9kq117fz+5bt/EquD75//7z1dwK/zG8/ArXm98a+dNWXt3dFH8vz+ylhkLzv6sK4eX9hO3h75+oLRhJfwqaedXx7JwKohr0uX7GX3/4vLm20U/4uAAA= -->
