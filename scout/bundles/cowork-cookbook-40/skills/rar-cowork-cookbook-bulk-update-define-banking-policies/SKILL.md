---
name: "rar-cowork-cookbook-bulk-update-define-banking-policies"
description: "Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_banking_policies", "rar_sha256": "c05360197b71d925c3d7f61e82c4f197faa9d393dec97f9ad91ae8966bf4948d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Bulk Field Update — Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are written.",
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
      "description": "List of define banking policies record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 c05360197b71d925…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_banking_policies_agent.py` first:

```bash
python3 bulk_update_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_banking_policies_agent.py   # or on stdin
python3 bulk_update_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Bulk Field Update — Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_banking_policies',
    "version": '3.0.3',
    "display_name": 'Define banking policies Bulk Field Update',
    "description": 'Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc8d9e79ccc812ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of define banking policies record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define banking policies records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define banking policies records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work', 'example_request': 'Bulk update these banking policy record IDs to the new value — show me the dry-run preview first in USMF sandbox.', 'inputs': [{'description': 'List of define banking policies record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of define banking policies record IDs in a D365 sandbox, with a preview before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineBankingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBankingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define banking policies record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZOjSLblX9HEM5uqemQmIBAS+azNRoCEQGxikZAq27LYQez7Uq/++ziSIquqO7une2w+jTIjxOJ+/a7nXA/49c1qmzCv3j6/aZ6VLVgrSaLQqxZW5i7ovM+rGHzlsQ1+Fk6eNVVkt01e1W8f3lyvdqqoaKI8A9PVNqsX1sJuk3jhR17iLtrCtRpvkWcL1/OjzFvYVhZHWbAo8iRyIq9eVJ6TV269iLIFM2ZWGjn1AiNWi/3/1Ghx8WPiBVay8LImasaFoYn7D4sa6GXnw0+LLrIWTei968jM03aqsiiSNoiyD0B001bZvJq1cKvxY9Vmi6LyusjrF/OMh0FA2IeF5TezvUVR5Z2VgPPZTj+qUmu27DEYGOsNVlokXv32+ee/fniLwPHb51/fnMSqwaU3ClhtPMxlHqZST0uVl6FgfmJlARhYjMDbGTgvvMrPqxRcAs5ZvM5+rL3E/7D4z/+Me6sK6p8+f8kWr8+Xt/kfcPLD6ia36sZzF45VWHaUAP98WmyT3hrrl+FzKGoQrCz49Jz5u6S8WPxlvvfjc5FPgdf8+OUtByo8DP7y9tMir8B6wGPg+NMspfjxp09J3nvVjz/9Lqdu7bvnNLMwoPWnr6/zl1gw8Pehkb/4qik7+rUWCHtUeED4H+ybP0/VX+JeLvn6HPxjXnxYfF/ybM9fgL7PdLSB3O+LBT4AM98+3fMo+/G1Bgi5l1mZ4/340z8S64SeEydR3fxLcn9+Cg49ywXeernkpw+P8P11Ab1s+ybzHy9bgIT5dywBw9+X++aofyT7Edm/EZ2ArK2/xfK74r43AfrL4ud/aNs/m/Bh4X95Y7wk6kDe2Yn3efHrI0V+/sH9/eIPf/0NiP4/itHytnIeEr6mVhb5Xt18/frzD/Xj8g9//fmHtgBZ7Fnp17ZKvifze359rPMnD75G/fjnuWB9I4uzvM8W32po8Wte/I/qt0+Ls5VE7u/X68+LP1bi/IEWsxHviz5d8IdqrIGuf/DjT2+/AfDJgDWt87gN8OM//mMhRk6V17nfLDQnb5sFCHATpd6svB5GAF/rB2oA+POqOgKOfY0D+T9HeNY49xe//C/nAaYfnRfgwzOYf33C+Ncnhn99YfjXdwz/5dNCB6LzKgKwC9Ba3SrKl8wKAGrPywLIrb2qA1Blj433EVT0x/lgRvxf/gXpXx+CPhXjLw9Cip7op9LcjHx1m3ifZhsvoZe9LHIAh3mD57RgjSR3gEJ+BFB75oM6TzqAnLM/6jhKkoUbAWwBXDY+ZAOffZ6F/fLLL7ZVh1+yJ1RjiyfJ1TAY8E2dxcePwDI/iYKw+ZJ5Tpgvfvj1tx8W/734Z7Mewuc1FMAar4gADXlNlhagwtoUDJvJEEC75T4i8utvL/8CMRlgKRC/yJ+Zc54MMjT23Hdna4ftx+WKWNgecDJwcFrkVTPzX9R8WnD+4pu+YNH51swQYV43gJwLL3O9zBmBVAuY882TWd4Awm2i2h8/LNrae6z6i11ZDxVTUOpW88tCpBXAR3kCfs1qPgaByXkWAfd/S4XndSCk+qFeUO8iPi2kOScXhVVZRVhZrzV86xkXwEPv04Fwa5F5/Zds5l5vdtWjQJ7uAYOAZ5xXSD/OMQcsngI0eHYXzfsYa2ZN/cGe1ZesfiW/VXmPXgSoMi6CNnJnSvivV0rVYd6Cbmb2H9B0lvSKgvuKyiMHmX/Q4sydwWL/6IeeDcLiS7tEUHzx/3O/NDtky7Lqjt3qO2axk3T1+gzU3ELOAX12nbOeIFufRfl7L/OOV++w/SVLIpB11fhfz5GP8L7GPKGwrUA01K36kA9yCyg4y32k/pzKVTW7z/qSvfPDrPYDDIHGACdAHc3p+77gy6iHpiEAg/n8917hFYbZGyC9F0Vrg/AsfM9zbcuJgVbVXL6vMIM68OZS7sPICf9k1RwokG5A/hzyCBQk4JBP3zD7efdd9T9NfLZE85RHu9iC6q0eAoAe3qzgjGd91AAQs5pnxw7s/PwQAsxIi2a23QbxApY+L3qVV7ZRHTUzVj796hUAqj/O309L56veUICSAc4ChVG0wLuPUpqzJgUND9ABpC7IjjTKQAMAnPJywkOglc64AHD31aE+JT4uvwzyHvU3M9f7xNmQec7cDCx8oDq4Mv4RPvTvpQmQl84jHuv+baZ9W22WPUNoDWAQrPh+99k1fHoS/7OzWLzL/fx3W6If/71d04PKjT8nwOdF2DRF/RmGn/T7zr6fAIDBT13rBxN/fALExyc6fHyhw8d3dPiT6KfVnxf/nnp/EvEqj88L9BPyCZlvCa/0en2AN+iP1PUjPt/9kqne7wgLls9nPJhjNwLq/0aH70MAJwYVgCsw+EmP9cyqPSDyBx+AQHzJ/pjvc70BusmCOT/r/A848OgLQO4/4/aNtsCtrAFru3MvGXif5i3YrH7tvX3O2iT58Abw0/uXtm4zOaVzWtfzlg8UEGjOmvkWOHuHwfn4z/vh3VDMEppvSPkCziemziUzZ9vfQO2Hd/p+2fpgph5kL4Ci2YRmLGadnzu7uRd8oNTQ/P3y8uPASj4tGA8gYlL/MfVflDZT+h8q9Olm4F4HWPhhMbuknikYuHk2fq5uqwblAhT8ri4P+vn6pJ+/V+jBOH9iqFe/YAWPav6vmfWsNgGhBDdm9nonr+8uBlqBr8Cp7TMMf15qBoUHpf5Y//TIDzB48Rg8X5g7iaJIHut7FgDlp93fXeVbH/73i1xA8zOLcPPPsxkfXsgKvsHe6cPi2zYIOPK1MZ1X8LIW7Pl/nrdgc2Y9pswHYA74+jbp219XbO/tr9/R66ny18j9jvUCmD8zzj9vIhYcUz8pb47zd4x/rAI4ATDrrPDvnvhdn/yxP5z1Afo3zz9n/PoGSsUCMq1Xsbw2GGA4gNCP9dxSwQBRwILg/Fn74N7/zdbjJaIOLdD3AhkOssIIBCXX9hp1yeXKwdy1T6DeZungPrjsWxbpYiTmeg44IS2XRC1vQxKE7eMkvnGBvCeIfJ1bx2hWa9ZpxliAQ97vt8El92XPU//ZWd92Og9YeJr165tN4GDkAa+57fNDwxBqe0vYHgUTNldkNAbHc7KrDKUp1hfCKKSKdXtxm7LT/SaEVttzExfrahW1+rgznJ5RVIaklGVMTr6sS0ysqolMZi5W3fIdvV3eIFtMfQXPHFdUxI2dHcuzXqjXsVWP/LJVC3snN1q1q8cS2tUQGkXKYKs2b+QJDMtYh5f8kY4O+zi4mco+uvX6SUXU/bE9VbpClzu91guh2NsH1Y5GGF515h1KJycTNkZ+TusbvboYbTPyNgltfAZXQ2OMbn4RCtKqOjqltIv8wr0VfnSWLDezh0uqDo1r89RRF44xmUtjGvmML5WIGrdm2aH2Jdg7NdKpXCCF+/FsFc5ITwICO+PQbiKdl89T5Y2oTLt8sGF1FNq0TLje+HqztGLcg80lnjV+J5ppuo9oRWMrp1DSQTbKyWEvQnzKxXVmiCbG2Bu1SNRzUrXqEngpETrFvU7SUFyUpEgpen/lu/01FYrBFc2Y7+Wbci40WNYGRnZWR/fADkmeeOWRyxJyzLtIqnHGgvo2nqq1N1KpCEkCYyPygJ55neOTs0Fpl+N2TRpaGu6qwjomzBHe7kZwIuFxeBL0BBQZcWB0OdgUR2mj2ucjKnQHxfU4hUrhwmVtceMOVligaJFGVJQ4uqFd1DGLV5c9s2OzQEPXlcOw6m2VFbdYr1J9q2zstawx1XIXZ9Rugx4SonaP+3VhDI5+NJamvrqsjjDMqYSlEPEx7UOe0cq6L2nl3BzzVhNYo+Ig7rAKSmEpFzscU7hi6UZO0ErjFC2bxBCJEl4et8C9p9NVDFcULEmb9qqx5+X2ZmJ2dDkR56BkG9Fi2/OVuYA+q0+S5brMnAip9nIVlINmszY7Ytox2JxvNLxj4ZUqH4tpNQZZfWiXsLuzeVUZtt1UMG4MHw8AJqS0xyV5w3JK2iyX0rS5pIIgRUrR7juGRgi47zEHF/PNRdywVBmDn+v8c2HK65Hil7cBF+6E3GrXPdEnE6giOPU3N7UilqtUh08UlyFL39cx6NA77P4SdXgyqlMvXQtIHwub9i4yyu5aZ328tlZKHY7kFOz5lOt97qrQE3br6e1wN1Bhm7OZs9rboRrdqrq+RrYZrA9XR8SsQJAKLra0+MjQRtLkODIel6EabAJlG9AryKU4nuDSfuf2UUcz3rRL+7qjMF5Kb8hNbwdpYu7bM7tHIP6sTq5ehJ2hsgdkp4YQhRp+QDIsIh37OHJGM5Yv5jpr42gcL+2GaTbeFjdU6aRW2gU6kOPqQB2k7CYVMIKPmF1p67itlWIseTkPcqwJoqPEAum7ae+cg0t8pk6UvM0GAUMmlk1Ya2XqFXJDTreYbZ1Ky45+HlKUorqVnLuw2Zo6wo1dtBW445nHpf3KanaKYlo2cQ8m84KyE3zZxcfAYIu9uvFGgW522TDshmhwUGN3zBJlhXYGX3AFxWm7ZIf5nQVzU+oKF+9+knkyK+CV1R2Je6rB3vK8NVWqgM5rgjk5O2oz9gcX9wfgP3za4qK71ndNyewRS1TTTiS1lD4QqgbtUYJqJG3I7bSWjuNlYkyzJI+YUFegg7SkccinktrtMBJOExDSYTNtTjuXNegldlDXMuAes74RXno2PGRzWvdCuRrFODvKW6WRcYqWiDXcrRpl5FlSXp+2dMBC0DXWI+7IjeyBnLC7uhMZ91AhgTZu97v+eBCqW8/GKCWHXsow9SaqrqOY8p5ikT19i87sENsx5akhX9Ct0efFgbnv0DTe3WqThhUMztPlWuLjgudqbsjD/Cy5mu2uueuY5kLhSsebHMXEUrqy3NWMd0osU/owcqu9KTXpVmPl9RrcdClhP7b9tt5fcVizknhvHk0PpbvArZ3jkWpzR3ItaPDW51hS3W0nGPtOSvixH9JxCt0puoepiZJ+JiyJenk7WUE96Cl1XJFscomMTSxbhVQz9B1NaaHVxcn3YWK3XTXIcn2kpaPcq7gKRQpRwfBFvIYZjMMc6CkPt2SPxaiqKEdmPNu77VaqI1OhJl+5nfu8Ty7kpU37KGcPG0Q83Us2Xd5xxmEMs1oB2F+qdnILdUrUVwiVtzt+w7D7/egxyN6MN3yFIJtc2p5WdIbIR/V0Daj+Ut50tg8u90tsOIcim6zxMN4psSTUWm6zOlXEVpci6nYy2msw2SMjONMYYqyfXDmcOTMFzDuxxFBTT9K7/bbkmFMU1e6Aact0ueMUy7Q5B5D8VQ2SbIrrHgqjHEGyXdDZ+HWuVw7Pzet22WuUZjMiPfnV9WBHehBcXbEHYLTquI7e3jV2CFc0U4lUJ7A1XRAuNyTDrWuqKhpP+crIGeG2N9fni5ZqAL1pNYPOe/mEhtbGvvnEcOpRZi/GB36Fg+Yz4Eb1ptYnLd2nRddHAmyyaHq88IZ8ci2LoaBdlNaxNOAKt0bOq/F4Oat8KzDo1ctLLvHiq+dBdp0XyDG9tsyq5KU1Xe/Als+KUZtFyQ4pQoruCMBIfTLcqWMPe+gmEfi4k/hTur80d2Q6G3EI0VCqg2oRmunq7TEhguU6WZVpUbYaglSHcsmqSAHb/WW7zTPJs/B8bQwcYoRa2Cw1Fw8T0osLnwrKNLwxvZgvy4uAHkfI73MvqCf0MIn05R4pS9q7oozI1ipFh0fj5Im6mIhHh9rZFJuN/MRC6wwJCRuXttJ+C6OTLAeXay6sd9e5j5GiQSAkUT2sjSDbI2cX4J5mmzV57Tn2lhXNHYKORb3fhdt7Yh4k2Kat4I5CQX9t813CcVi1IWUB2I2d601YcC5OisjJMw0skCjXuUs0X6KaJtl8LcY7azdRV8GY8C3k3zQ7SjILOAbIuQV3I99eWt46pNMI5/Qq3xX18SDFQUC0tqixEcYTlshMriaVE1yXe2ubI5K9s8o1Xt7CbRNXid4TDI8VDdehCY2vZD3sVJglRS7flhTfGxu46Ju00aS+PUkDbfQCH5X3sICt4HrCuj4Vlu3xFLe4gPMQDK2RSaubVM+l1gYtbz54iHfHRr2Utk6TgZYvGg9H3IghTdrmuLzE2IxrSBHO7twWMoiVjJ9Ck/eWNG1EJ5Qrxe0lcbYAjdvklAp16NgxIjqe4WeeX58QmyrKoToldZS2pbrmUhkd45JHtnW2H1egyw4woZLda1oHZIpaJ7XZbBFz0oXlYGW8XjQSd1HzvWoqoVWsz9HtxHWi4HgWnx+2zH0T8q5MVzlrmcIRP8b3oRvMy3S/lMgBbW7lKmAdSumcGnUr0dlpA8frux1zZqO1XHQ87+VEQJ3KQWePDmdWHhRp137JUidYp4jxgLKC11vmFpfQLjn2xPVe+KdRidvMx6haX1mXA5Ef1DLrj/0G3V/YwY+HgLJ4PauakchTHbNIOVvvpXYydkrtIOdG9XGKKMdI0k1IzbTUpFxz4Ac5F650JgqQu5T0m7Q2p11g3DyDu/mhxC+n+xDZu0Q2z9ep38rwbayd82UT5PCFVWiMx64nAa4NpmllnstNOz6xMoz7sErvlxAf6u1d8Js0h4swM5EoaQgmy2uSKZkjtL71QtNZlX2QQfrjBOOF9F2Ftkoc9H519thj0xKwQmktOUzqxrnhp6KQNzcmNleIkgf0loW2pVb7Fy5sjbW3zIh0BzVxGUVoVw1TeDuF/OEoCRIf1HfcikXn4svW5aLZ9E1mdinKj6KUCOi4rcQo5HYjy69gW9jkfLDG+Fxdn+sEQKkotmzhljjY7u8JWDbXy35pOXvFUOsy3xz7WyaiIqvkhyHo4xO2uSMuS11PG8Jgc70xq2Rg6mlPxpvdurqk12XR39q9gia8lRLYpW6VPTOQy+R8XYtlSXvUvsMtpDxeytXe87j1Bm/hu0vc1H00xnHB3c+uy3Lmqa6W5tITPIk6QycpiThqGd0a9URFjq+YRYqySjwxmHgTfYqSSBrpTY6ET2u13cJeffKMPcAbQyvIkCgkIctqGt+0iilJLQQZOO5zdCoZuTLukVzTM55EdJ3DNgJLr5DpWjBNug56x6xNCF2ttHPIUymnD9YSldyLVAVrYzQv0VWMVbpPkL0Ftl6JuScVn/GKILAu93IjVJiijMp6QnRMbJp92W6RvXgrzL2NRTvlFPtZKDQyzI4UTTsX0GdypdkxO0t0Ne8a7Mnt7soZRaE3R0jQtnoX74miIBWcmbYEMcnwCVb8fc9OgMUAZPtpad0ObnE7kyQE9yMEuLerV7Hdx7vtsS/XnZGPqZlDgPd1SMxc2jxCJ2SLyKdePmrSHjbOxHkNmZzAmOVGO9ZYFEKth5fowGpgE+uhA9rYGVMU7c4IRDlUibs5ruzUCG/ihEU2sWcCi4QRi+FINij5K8yxhnitUoRKD2XsEG7DIaqGt+VpCf6zOLsVXWfLl3afuuxAQE0U+2s7d5urGXnu5iAHCKS34Tm0SWYPB0SCkPoI2QTSoL5GcAgCjQLjoYHN5DiqsytrraoYdq4ASmgHefLSSevcEbaDvGpH92xaFze4EsT6vi0unqhqDU2ERCbkF/fQOnVKkKO3E8duMMyiWjeodYMQiOZd9yrekKvb3kjenLb9SLqs7/bImF58iMgRQbqXqzXEOpIzoTf0TqhdAUF5ZNzO2lRmWwRbNqjOVZoXrYtGDGWw2ZJA/21b/jI7FFf7cN7791UMlNQrh5xStqs0GUpBfaC+SQ91ZSs33kgZ3IJGdCOWjKoW2dArFg7DB6yD2G55DHBuUyMdvLJhdhnUVyRqMol0rxiRs1Eg1hftuL7cWQYe1/vJsKhVdvc15qjd8WLS9dz1C7foanKbkjlV3/A7kd4RatT36wbsEn2ST6WhRBOwIbhMAWnYDD+IU5X77LhPT1h50O5GJjYjltJyPl6HW3y9XqseBhAANilYrWehi/FHypBjHXazal11I0ZzcsM1dsogXbtExtvuMKbH05DQkuLRXLvHMK2Z0CUCgQa2k9uWvVvx6EVow4YrNoSzs14m5EWRr1dF20u8xPHxiavi3pW6ztybbnoD6d3v5MuyIU9BVUR4MF5zsiYtFPWFyDiGaZbIVKG7+UH0RZuHD2uFt21ZVoMbdEVNqQssYeW0Bu9cRb2+cUbpRKfLdpSFAylJ61BNtPpE8BlDKlojLPEcX5+RxkzUXjpRSDGk97IvHJYTLUr2pZ4QY5i2JU3mrxtnRYmEp7NK0lnXGrnxxKbxy3oDQZAoYL4vMoEvac4kCZtlzTnTVb4BQOHOFiZcN6tUgsOru0P3ngUT5217PJx1Te9gJKsBtCJeRzhoMm0k7Lw8hnbAV7eJCfP2lrqrCODcEYoy/eSWVjjRnRvwuTkEDVOjKMLbvH7p3JpPhl17FLHMSZecg7JUg4XS+YyL4oTUazoxvdEfDxKJHaZLqqy9yehX2OVy921T6y70EKN6Cl1IS7Ew/IIUYtCj6wy/3aOVHSa4QhbRajvSCotkyPqgwtck2EKWAp+IUjcMNFaotYOP0SG/FwrXmVQSU2k4dNctMqzh4SRSE3lFM6KTCciUbmSO2ZncOdfzwa97rIdM955hxH6p31pLCJb+4LPSdtJSSGi3h9qzPPK+ywh2SaI4BA0K1hUyoru73UqqllmB11CHtEqEDZa2gfLwPNHrPtRLNuYv+ZmsJRQ/S2h1vnqcYbnV/dJ0uu31iu578eYqkDVhbwhplRwadgPvKSw1AiGOVvdjn2mKSXt3P2rjuD92ki5COSQdFRzd1CC4lGSbvNjd01BTarSPdtxq5Xm5wV39UdWJ433iR0N0vRu3nhTA9yZbO1V1YTSSxzf4rsPrCMcylt8YKYRrS99IBy/whIPMjJ0lo+luhEnFG3SiUu4hI/W0Ra6KyTE2QSFft7eDw/jlnVzm8hBCB24ShM7U7htIsWGznjrVbS6rvbMKT05lXxrM8i21KTwmoRCUa8AmNwwKrOmXttZJMu9h56Zcime/gpnLoKXxrToYyjhMt2TjpmhRGRKfDS1L3lcy5WXLZMq6ksXWkda6xL25n1QJzhI45m7hec/wsa9jiA1gYrXZjBJvE+RVkBNlh9DuJST0IHXtVlKtgrRUoWqLwuhC2UyykU2cRPfUAVrVvtVNTEnZOuwFE52RDDjbbODhskbIlbQijWBrw+M5WTUFrSJqGjGGRlwVbnvb9GIaOjdpgOHCxA4uOhhHiDNjxgvEIiHGKsalu1TpFeYc3K6Bj94ybBDTE6azjbrkZHdThEmhWzP7QyPrpH5Pj3AzOkTvOAq3Y0xk5dLEshhgQNnWviaEpTJtC6nDSvmCYuR1oyvbdVyfLkV+oG/iikWxNNwgtE2sxayVzgNzKLY9TWPK7hTsygHTt7okw/KaOtEHO0a9A883yxqtnLWIjF3URh6ky9korXBrqpoO3XblUByV27UM13tqcyg7v95IYklULV+tJx2+tqnvmjefb/A7vLKYUW830AUG2KC7/q1jhDs5HnmsJ2QcUpktwPUD5uat6Hut60oWdtRvFSbk62gzos0BkuGxzrwaKdG42ihobK8Pfuu2uFSSo0j01WCTUk9W6XW6qh6s59x2OSUrNVkvpcKLVEwwvT1EwPQpKKbMobCEw3fbM41t0szhi+AYyXQh5MJGFpbpEhcPe+wsdWybhLcev2eNroQNteyTghsMV2H6/IDEUUqyq4Qch06OtmZG3psc7SF45cLLK3nxgqGrkgyT4wtJcptDorf5QUOGtiZHiG5jJT6F+87RrF17bXIV4VWm35xD05d7SGm7wNgwTuDJeKf5Zbnr5FKVg3pb3n0IJuQICvvmDgBr17k7HSfge+9vqJvbITyyZ7bb7V/ePrzNz5FfT4P/nXfS5gdC/8+ePT0fIb2/YvJ4ROhZ7ufHWp//La3++uGtciKg0/MpW520weth1d88Y/v4L7xUMAsYny97vT9pfj49b6xgfhf6Lcrctm6q8WudJ4/XTMAMu63nlyfr+f1aB3z/8UnnH0x5+/Ycs8m/Pl9Ke5vfbpxfIPHc6DliPg1eTx4/vLmvt56+YsTqq1cVs7Gv9xSAjdgn5BP29tv/BmII7/rULgAA -->
