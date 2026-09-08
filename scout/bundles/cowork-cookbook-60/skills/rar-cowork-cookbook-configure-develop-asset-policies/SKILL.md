---
name: "rar-cowork-cookbook-configure-develop-asset-policies"
description: "Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_asset_policies", "rar_sha256": "847f4b834e96f36dc7a0592a1deb01535962c9aeb95ad4c8ce504aa30f644884", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Configuration Bulk Setup — Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per develop asset policies target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 847f4b834e96f36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_asset_policies_agent.py` first:

```bash
python3 configure_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_asset_policies_agent.py   # or on stdin
python3 configure_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Configuration Bulk Setup — Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_asset_policies',
    "version": '3.0.3',
    "display_name": 'Develop asset policies Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6537fabaf2f2dbfb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per develop asset policies target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop asset policies, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop asset policies target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf', 'example_request': 'Bulk-update develop asset policies in USMF sandbox from this Excel file — validate first and show me the preview.', 'inputs': [{'description': 'Excel file with one row per develop asset policies target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update develop asset policies in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopAssetPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopAssetPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per develop asset policies target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVrLmX9G8N2JsX6oKxE7d6IgBgTY2CdCCXI4yO4h9X3z93+cg6S3b3fbt7oj5NKqokoBzcs8nM+vwy5vVNmFevX1+0z0rW2ysJIlCr1pYmbtY5X1exeArj23wd+HkWVNFdtvkVf324c31aqeKiibKM7Bd8yy3BtsWVtNYTui583I/CtrKmlcshMHxkoUfJd4i9xeu13lJXiysuvaaRZEnkRN59cIJrSwA31G24MfMSiOnXmAksVj/b30lf1h0VhK5VgMWgO3VuKjy/sOi8pq2ygDr98czt1nwWeYPD0UsvwEqjXkL9CqKKgcL5x/JzLIJvW9s+6gJAR3b8/PKg5+7Zi2Ast5gpUXi1W+ff/zpw1sEfr99/uXNSYACQPnVS1WPf+rFzmodXlqB3QmgD5YVI7B1Bq4LrwIsUnDL9fzF6+r72kv8D4v//M+4t6qg/uHzl2zx+nx5m/9obfYQt8mtupkNbBWWHSVRM35asElvjfXvjFEDV2XBp+fO3ygBm/9tfvb9k8mnwGu+//KWAxEehvvy9sMirwC/qp1/f5qpFN//8CnJe6/6/off6NStffecZiYGpP709XX9IgsW/rY08hdf9YOwevGqPCcqPED8d/rNn6foL3Ivk3x9Lv4+Lz4s/pzyrM/fgLzPYLQB3T8nC2wAdr59uudR9v2LBwgEL7Myx/v+h78iCwLZiZOobv4luj8+CYcgFYC1Xib54cPDfT8toJdu32j+NdsCBMy/owlY/s7um6H+ivbDs39HOokyEP7vvvxTcn+2Afrb4se/1O1/2vBh4X95470kAmls2Yn3efHLI0R+/M797eZ3P/0KSP9TMjpIa+dB4WtqZZHv1c3Xrz9+Vz9uf/fTj9+1BYhiz0q/tlXyZzT/zK4PPn+w4GvV93/cC/ifsjjL+2zxLYcWv+TF/6p+/bQ4z3j02/368+L3mTh/oMWsxDvTpwl+l401kPV3dvzh7VcAPRnQpnUejwF+/Md/LOTIqfI695uF7uRtswAObqLUm4U3wgiA6RPkqhkz6wgY9rUOxP/s4VligMg//x/nAfcfnRfcw+/47X19ofXXB1p/fUfrnz8tDEA3r6IgygCiauzh8CWzAi9rZp5F5dVe1QGcssfG+wjS+eP8Y8b2n/8Z6a8PKp+K8ecHfkdP3NNWuxnz6jbxPs3aXUIve+nigMLjDZ7TAgZJ7ljPSlPP1aHOkw5g5myJOo6SZOFGAFVADRsftIG1Ps/Efv75Z9uqwy/ZE6SxxbO41TBY8E2cxcePQC0/iYKw+ZJ5Tpgvvvvl1+8W/734n3Y9iM88DkDLly+AhHtdVRYgt9oULJtrHgB1y3344pdfX8YFZDJQhIDnIv+9WoHYjD333dL6lv2IEuSraC1AZcqrBiD/Imo+LXb+4pu8gOn8aK4NYV43oAQXXuZ6mTMCqhZQ55sls7xZ1CAAa3/8sGhr78H1Z7uyHiKmIMmt5ueFvDqASpQn4J9ZzGchtbI8i4D5v8XB8z4gUn1XL7h3Ep8WyhyNi8KqrCKsrBcP33r6BVSg9+2AuLXIvP5LNtdcbzbVIzWe5gGLgGWcl0s/ProLJ08BDrj1O+/HGmuul8ajblZfsvoV9lY1u8LJH81E0ILmARSD/3qFVB3mbeI+7AcknSm9vOC+vPKIQf7PG5nVH3ofrk3ihQ4ApFh8aVFkiS/+f+6WZrOwm40mbFhD4BeCYmjm011zAzm79dlzgr5lAbY+U/O3XuYdr95h+0uWRCD2qvG/nisfRnmteUIhwBEXoI/2oA8iDMgx030kwBzQVTWLbn3J3uvDh1n9GQyB7gAtQDbNQfzOcH76LmkIIGG+/q1XeARM5c6WAkG+KFobeGPhe55rW04MpKrmJH65GWTDw4F9GDnhH7RaAOrAJ4D+AggRgbQENeTTN8x+Pn0X/Q8bny3RvOXRLrYgh6sHASCHNws4+3D2DRCvefbrQM/PDyJAjbRoZt1t4Hmg6fOmV3llG9VRMyPm065eAdD64/z91HS+6w0FSBxgLJAeRQus+0ioGWtS0PAAGUCggiBIoww0AMAoLyM8CFrpjA4AfV8B+KT4uP1S6Bmkc+V63zgrMu+Zm4GFD0QHd8bfg4jxZ2EC6KXzigffv4+0b9xm2jOQ1gAMAcf3p8+u4dOz8D87i8U73c//MBB9/+/NTI9SfvpjAHxehE1T1J9h+Fl+36vvJwBj8FPW+rdK/PGFBB8fSPDxHQn+QPep8ufFvyfbH0i8cuPzYvkJ+YTMj6RXbL0+wBSrj5z5EZ+ffsk07zeQBezzFATX7LgRlP5vFfF9CSiLQeUF8+JnhaznwtqDWv4oCcALX7LfB/ucbC/I+QD88zsQeLQGIPCfTvtWucCjrAG83bmRDLxP8/w1i197b5+zNkk+vAGs9P6FqW2uTukc0fU864HcAX1ZMz8CV+/IOP/+4yAsDMVMoVkE+UdrHgVegAr6r8jr52x51JI/Q99XDX8H2Lk8PYHXnZVoxmKW+jnYza3gH0rGV28uGX8mzrdK8gDsGZFAJZiHzr+qKw1oSsD1bN5ZVFB9wX4P1EIgdOvVfyVL4w3NP/JXHz+s5NOC9wA4J/Xvs/BVY+ce43dg8XQ6cLYDLP5h8axhIEGBErMzZqCxapC5wFh/KksCoiv5CoIA5P0/CsTPJfKxZPFc8t7AWMEDWBbfe5+CT4uTLq9/+K+HaGCYBraw8wFIUNXNn/L81rP/I8MLaJdmHm7+eebz4YXC4BvMWR8W30YmoOlriJ05eFmbvn3+cR7X5lB8bJl/gD3g69umb/8PY3tvP/2DXECwB7SDAjnT+k3I35bmjzFvVgGQbp7/K/HLGwh7C9jdegX+a04AywESfqzn/ggG2ACYg+tnFoNn//YE8dpfhxboYAEBGqd83KYx3GNIHyNdh7IQgkGtpevZyJLACIZEHcbybIawXNyhHY9AcMvCEJ/EcZrGAb0nFnydm8BololgKB9hGNTHlyjiup6P4q5LkzTpEBSKWIxtETbBWPZvW+Moc1+KPhWbrfhtmHnk/lPfX95sEgcrt3i9Y5+fFQwtbdik7HG/ha8IrJnmyiCE++l292wWMibTQ2/1RQiYgEi7dVzvg70S6+heHYw9YfrbPl2xB0H3ZIEZO7IqizgS0zCmCAqJVVll95JItVUO+d1VO5jUnReoJTegWeqL0rFwSh2S82irh0azj9cWWmEr6K6sha7sQuvqlePYGD4M55hrbZl6zUF5N47MTlX45HrcZBQqu6vhEl+Gc5uIoY9UHFfDF0+e9MYopG6Dnc6r3IYpvLpWxJZwMnu0y2BgtvmZiVjRzlTikimDeg7wE927EqpYSzSG7Os46UyWr+6nQ1qdWrdMlhZBV3JtTJtjV+vITco0xt5hJzvmMuvsFXbqjfpkDRe+h5VLFVHKdWIgN7PKqYHo1s+ks0qU1315VvX2fCV0W8kxMZM54bSDJmGCh2StqJPOgXmxlOTGpt1BEUYGPrinIdsJ9zUvi6xYc/WOgiSCux2wvNdkQUlzV7lWQm5M2eGOcssajs4WKa48xL0h10alcd7ChxaZKsKLGuJ6uK+HjjR06RjdaGHT7CTk3sfiEeu7dbESLmXi2nckQLueY/OwnNy9sLSdSTdFpcQYcb3aSDFnB+YmH2RXwQN8Q6EhRtfUiO3LTWIpMtIf3Wq0Sj0WXRrT+3wXL5FwKG7sShpLJdHM0pV7wI9eimh31MnavBDWVmV05nwWjn28S7WCJtORQU+HLJWYNQdPW+14jMPifDHP4SFvGbMe9eZWkrgv8HhvRA2z0U1jy3qQF/mJbSnjwUSbIYDLAjVzc6/d9cMuwwt4Cwlh4QWXE41a8VU9H8WwukXHBK1YEWl4j01a7HauED3Gx4iQmmM6XCrUPgoSP2lxxRwTf3m5kOGk6hPJ3Ymje8SRVrlNy7UfSUrI0ievV3e2EvaWS8hHW9kyuZWRjXK52GufNyVvsw+IKuHaAtnn9FUO8pW3KTy/rptD5dTY6BQoAVWGuml0eYP3Z4rBOkyE+6KGN+d6hMfVJoZSKSNvcC93XHgmKnXvHpp8lSDjso58fXmiW1fMd/RYF9Etd3E4K11yOilD4uzy7Wra2j1XUUKuX+Fjs5lG0ZRLgYwS3CuRrb0fEe0k74VMP4VnPLlpppoPrB0grlrzYeC5tz3s0Mxpcvk0MIxgjWN+pV75mDhtJpGSx95EnYjqN84mhbYYnnhFYg4eesa1MPZEWp3GMLDY2JI1VbZXh50NTaMcRRPqEoSLc4e7Jiw3EWYoQgersaO0l9Nou11TDCmWJTBJ9upYmTddWDtDTQznYtoFeCbeQ9AGHvd5tWJxhzu06c1caUxJndUDfUQ7Q1oC0ybqEdoJII22J/MYH1Bm3W6NieF3CC7Th9sy6/FzKNY87t6qzlq3impcjW55hLjTqrvzWre1o77SdnR9lM0KU1yPr4ij1NhL1tItU+dDXpMmAutGhct0CtqxnQAN/cRURtmZRFphRcMS+ElL1iIUMmtWxdJLQHU8ycrEYXM6hHfaMpPuiDd3bSVPxDay+j47iqsebY9ueTDLDVGJO7xQgivRbEp3hx7qrOU9f32TzZ117Hj6eqaK0Sfd+8GLTqxxppsuxI17FWiYTWrJjTAEpWO9MiXU2pf6qGrs1dhhOGZ0BG6c/M1AkKPhB9F1A6lmZITIPjbJDURMmBatb1o2mkf4lC4LqQy3R3S3jA8BZV4EINChNwrVaHQpG46Xk6VEOOStKIzKdxOiGco9k9LDfqWIx8mrFBLz2ts2TlVXYg/hwQ/x897RbbfamWNqSoWriKYaxuRFsYUtjsbCNgalpxh3+/N1X6esvlEnKjmYTihtLokJrrvaLxS9WVXM1UPoKlBOtShyVe4oVwsavOocbzWXbasT1zbJfuxv6TiF7hTdtdTHCsbJbihdT71l1oNBcuKe2SaX6ATXDqLbzna9LWphx3cTNOAM5KysrX+tdzKaFBwH+1vbhomJ0GEGdABVRR8SK83qMR5GK72nqcZITcSxm4smHQKmvXbFkB8TLWdO5arMQeQEcKjQplVWDdIrVwc+XVDD92yx1c0i3GYspOBHqcCtXLtbJRhiyjgL97o+jEGs8onoH/GCYyOEdxqEjPes2W1kNkc6CxSJo2WRZexzm/R8kghHhbI6Uul2r1Bszfe2mNtTj4UCRTeuFlCXaF0uG9SFWmt95fqeuXNocIo5Z7ieTgOlVygqsLx1tXeOYymmtkuq4Wbc1wKfWOaZcvkDxB71nbju+WV9AFgq3tNYsGFshIk2D4jdmYuT3UkSnEOIr+KgaRJSHNWwcc97gt0ZzW1YBf6Onu68gcby8pTR5zUOsGqbLSlLxVc17kZjL2TcQB4LsRe3BXI3qF3LLNs2LDg3AU0KKda9PkB72d+3jCGJEbazeoEWyi1ZxMpeS4wzl14KHrJ3wPzWiafFdHVHr/mOgpWhhc+S0Ep+2eywvSWsihZYlIC54tZey8asGDHI0ZAbGUW4eJMoWKSfJBeASWXqYO6tBdCaCKs1eYKU7kpPuqVsLitOOt/Z00aiC68IrwzdNWdG31ZlvJKl1OpucnJGWDhvi/UR1VaTmY7kPRnsLEzxaFOUrS4vYamkuJ3udq7JsyxiZIfE3J/EItmY5SWSjPTqxZtD1qhGYN6m3X5kdEculyls0NGVPkyT5BBaaQjxqb7RfTUJp1gUaB4/IaC/1pJDemqF6bS+by7bjUhvkQ62dqG0W/IVIvuhPtUaCw1XWyjlgbYw32uSvDPP27QkKZIyHN5jUnvDHjTQD1E3lzmPt4izVtkKy7cg/ZbrNeZy9ybv9VMnd1NNyJWGm1REusc6PdNpZOaQUlS7lWA6gbrWUkxH9gYqC0m8JuLN0au4455u9ahSpM3yJo2FzFLcxj6OltnUiH2Q2kBKAzaTcoIOfcktLXunlJxQlJx/P2yGbNuJnnnKAzbidP2Gra5BkN8JJTjKUFmmarqMtKBT9ZN1G/xMD1n+MnoZf8lohpCEnD1u9/SFxoqpYJSjwrdHmltd+mofiLdbDou1fdzeh7RCGxE7tmA4kCAYxhHeypuNXe3XqKXLNeYhTNcJGGoFhC3RMj2Een6IA0jX++oCkZfNVYIZqBi0Ui6RysJxNXH3LR3wQqQvd6nCbhK3vW6Crjkd0QPsYUJwbsRTR6l+a57soF4apQuFTckg2TJt60Ns46FHSg2j2btTi10Ug8u6ZW+HKDlRoeEshyHynA2ZbRwjr81ozDZrXsMrCpSYjdfu05PhmxKxQfQTN4nERte8huZRbN1N5tny9HFy7RsdZiI9CGbCYUykT8c97hzl3NhfkRXJnehjuFs3R4PBqzy4+ooumyWObo6rhqNsxWBOdMGTFcMe8f2Z8i9ljNmXyq9CmsYkOln76NncKpKiHi6sOkziKbAoVFs7RsMm62WJbtm0nCTfxSHQu6tNsl35W+XKZiJV1Gbmk+vjai+nxDrUJdJ2r/bW2iGHdg0zAgdKCe+KqxbGHFw1esEvqaCzxEZvrA0ZGM6oosgh3qYtezf25ua+TpAmrYZB4WF+wMQwJiLcpdjxQl1EeW+KN3of9TSLX6QOiQLUH6Oaoc4Xix4nprmMB2M3rUVFgeBKSfeFSyjlwbLFW7M7Xnxq6JZNDTlgTroxCoVSvidtwYN2Mo1i55rhBboLgyRyRyvUQuNU5Oo2s4YgytmpvyZeVNYradpRqWASUxztboi9U9UavxQmPpyJQ6veBsHq2ctpWIfH83nnJIcB+P+24UMaUdfbJXouqzxCG+Em7Zf9iXKb/lrpFKeFCSvVg3xbHjV96xFhjFeEdNnI5crwm2x90ZSulNbVHu7uNN5iVUMysp3WLN/F7Nkk1/h9KEAFB4ZFicjhUphHy5XWuoWRcbwyVO7esIu2WVZSlmkeJVJn4XRp9JMJ5t+CHkvCBf1eCychVSsYUqOUrQ7Jnm0mqgoi+WAwHdG0Yaef/fi2vLWBwumr0ciR3LP3MYAeNeLGEofsLUtWxda6pbv7hpEVWhkv7NTqNwg67qElsb+f9JNGhq0vW6l5RhnQfvqdg0AFsuO0W3At8n7f5EtmKTKWcQEYs18dyptI5uOUmJYAaRKZ56sluRmtnA8gptAMQ1yDRSd0KosQUsnBF3pTLXzmyDDlFoYtxs3zDr5bUnNy+jw+X90D3q+d2EMHFu3L8Nb2gAMMsn0gT5IbNZGh7JN+zPuGDTSCq8H8LIQMckHiey6qgnQ7cSfZuFIijdIR3uF82MErNJFM5nw5NTqG7V1JWSGSey4ojcbl7V4XaJpbl6p72I+8KVQYnLvcyLO8YS7ZUNV7/2ZcMghmO8Yw9HVQIsPpVg2r6SLdj9TdTFYOytQUnXlTm5xyFi/WVSw6oIW8ROqtspuxP9xB/NGYJfM940O4HxjXCK0ImdmrEmxdh0iPL2rglGBavU77Y16vIj+PEQUa98XdzLIa3gs1qezMCa2OsDFhrEPgEhPx8hUlnP7c8yc4jHIEWo+QM2INttWt/RFJR4P3htjmc2pppISdaWfKXA9GVmkALggmxX39DKHXCKLkZZx0N1S6X6+OtyQLAFxKnln8mSJT7uj5vuh151Qb1VwZbII8OTvJLLGE1tLN6GtaPlHyxGj+plsDlNkY+yXdC8ALpUq1m/S0LOD8dj/XGO9eocRmTm7ZbzahvMcMszgwpNaLBmFsm9ZbHW6tGg06pdtXBtsQSkJfqG3YYo2282PXsUm+MEzIdrchW/IcpGAA1yMVwvrLjpbXWNXBcFPBUafcK1Xf+yO9hCO/V3RDZ/vOu1cbKpQRk7uALgv0C57me7pZ65G5lamE3HX4ZstI9Rj2aresmLvBisQRFdpdG+YM68QDBALqnsD67e5YjeWuxVuNH86r4VZTvetyJGoGVw7gSwlNoqMQ93svePKoNajeevBJ4H09g0hhFK4uegzumwNMXY3r1UhQofbFQUOcsPRdRYvHeruXkSw67xgwbiw9Ccx0dlWliLQHpWdVt5vOrlOrWLqrgLjcGVHslgmjH2xntyXUINnG7LCLjQGH9shE1YU63H1BE/jjMikP9UYqmWJTo7xSXbW6kXpyLbZqvQpG5niRKbkSme0yS9zlfbM7ynDsJtONXEMFCVglIoZyQqXfVDGUtcjZGKR6Q7IQCeWjyGW8okpUMix1JK1yrdvDRyvl23tsbNexsVtPF2RlQ9ny3jPB/gomLl2b7Cla90x0lEXIc4T7kiebxC9LCIK6olpi12S1dATh5IN0YtJRIfEtqTvbdL9kYNEMqBjEws09oVso7YnkiJyw7QQGPmLK2Btm0NbSUx2iIFVClFytMdWjo6wHWbuXkubKOTk2Z45Ksm29otEsdVovRVTeuB7PddqQS6JH7UjfBRPUsDdTpAhcQfEdObZsCPmXrZlWxWjAxrI5pBt7OVR2RuicajmTbR9hUcwzRSZVNJo6zZZhDCWk+LLJnVslOVvjLHcGeTOh26VfRWWutKZD2ypurmMeIg+kq8llub/LHs8NU3Ja61285GBle5GrLSt5OFdQJBSbnrxFmBIDqL1s1FtTX7sMvXRcmco+3Q29VbhTiBI3zRlo58oSWU+r5eYqFP2Nlpeuei2YUW+6i4cha8NY0hemccK1d0pcsfHvJelQHdIKZNZe9dsFTiQrAmAzRgeOXK5QhDj59oVakrkqWIq6HPItqm3cErYc80RbDBRQCgMdiGSLnmso47DUDtwguBnqmEX8eQV1brSpt711jy/ToTzcrTuk+tIKH9nissP3DeScRI3pwEwVHkC/TAbHIYT3a74q4Z2jh3fQjHL1FZPsJb68Z64+WoeC227ZBA7r64Yzu0MUY1jkDWkMSc02Gqbj5Tyt03pIDdgqibuEHV2KZG9sayDkuaeFY1RmO7uxaUFhlhwpH47DVq4rxxS3PU6UMLuP4UiymlFkpq6hk/q+RhPU8q1tTej7FNvVEpOCuZD2rdY6N8VQpXTtiujdTSxihPanUyWZuyW1Ue1dF/ZozVhBUafygCHSrncxKB5tmtGkLltLRFeyKKhvmHe7QpiSrAVTSbVB8YeWsKdumEw67uxlJFugKPTc0soSeZVTRZ+IfLbPm5ObKNIFESc6po4IdR+kcX/Y3BJ82bpkz4NJPd/eTmQhILYL3RNo6TQ81aA2Z/NgaTyhZE/s7rtwGUcxP+62vrCPET5SvO0dFiF3q5Zp0EHQXcVRMORIZ7WmcXR7m0qHKtADJlW3KRvs8/7m83ibkK1H31CKAFX2YO4Gm0zVXhumld/cNq7ZbtZxxFUaADQcLQYQ5w2ygpq1vSUCpCSo5UGyXDTw9nDg6pedhCBcKKfenWQmwbMMhXFjA1NznLsjkbnn7G20O65ck9jnUsr6NsPmHN/0ZsfXMUp5N4fP3c1Go6/0bX0MSXi48veqTZAu5xhJLfImBJ0SfUkDqGZFeBmufQMekqtKdkyEVFNpNz3iI2u4auo933VD5uBtOHXUOlBqbJvl18OutO/9Wpax7FR5qE7iughcU1QXyqB4n8jsuG62tHpAu0ytl+UyCOkDE96otd8qJQCkFN141pVM0MRMsUneb/aHLBxBvltx7Y0MHA8YcaHyqKEgOj85e5jj8vHMsYre+FyZrc47TjCms3Zj7WJyEa/j87wk9y6JIjF32DoXWLyN+1wd100hivzQ+8kOSWJ5qrD43l7WA3YkUVhuwnWLUXB1JftsNWEbBfZklcGia1FtAzpnkh118SQQz25/lUOId3YNJbra2uDrlX6PkSs3XRQTkjqYdiD+GLgQmxsZ7PJXTNuXB4HGJx1SmYsG+/5Bi6h1BFrKG7lvcHwL9ypzSu3ziMgsy/7tb28f3ubj0deh8L/8atp8YvT/7ODqecb0/o7J49zPs9zPD16f/3WRfvrwVjkREOh5OFcnbfA6yvq7o7mP/+yVgnn3+Hzb6/1k93l23ljB/BL0W5S5bd1U49c6Tx5vmIAddlvP703W86u1Dvj+/cHlN4bzod/jgPdrk399vpP2Nr/WOL854rmR1Xivy+B1VvnhzX293fQVI4mvXlXMer7eUQDqYZ+QT9jbr/8Xs2h6LcsuAAA= -->
