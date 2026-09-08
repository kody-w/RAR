---
name: "rar-cowork-cookbook-configure-plan-workforce-development"
description: "Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_development", "rar_sha256": "447f00a007972ba9520a53649b13d0cb68472e8dd624cca35acea324cd7e5d68", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_development_agent.py` and in the RCI capsule.

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

Plan workforce development Configuration Bulk Setup — Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per plan workforce development target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 447f00a007972ba9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_development_agent.py` first:

```bash
python3 configure_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_development_agent.py   # or on stdin
python3 configure_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Configuration Bulk Setup — Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_development',
    "version": '3.0.3',
    "display_name": 'Plan workforce development Configuration Bulk Setup',
    "description": 'Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14a5789061ffa81a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan workforce development, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan workforce development target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma', 'example_request': 'Bulk-update our workforce development plan config in USMF sandbox from this Excel file — validate first and let me approve.', 'inputs': [{'description': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update workforce development plan configuration in D365 F&SCM from a spreadsheet, with row validation, approval gate, and before/after output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanWorkforceDevelopment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceDevelopment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5mJmATkixfRIJBACIRASAJnRZoZxDyD3PXf+yDpZqafXd1VHf2p5XBq4Jw977X2ufD7m921UVG/fX7TfTtfbO00jSO/Xti5t1gXQ1En4K1IHPD/wi3yto6dri3q5u3Dm+c3bh2XbVzkYDtTlmnsNwunS5PFvC8oatdfeH7vp0WZ+Xm7KFOgAQgJ4rCr7Xnfwo3sPAS74nzBTbmdxW6zwFbEYvPf9bW8COoiA5Ys7La13cj3Fvzo+ukiiFP/86K309izW7AZqKinRV0MHxa133Z13izs98uzktma2YEPi9LuGrABmLawy7IuwKIPizby84Wfxe28zfHBRR+2gxYE4WFrndnAWX+0szL1m7fPv/7tw1sMPr99/v3NTe0G/PS2fjnlq8DFy7vz3HffgQRwJQRLywnEOwffS78GqzLwk+cHi9e3nxs/DT4s/v3fk8Guw+aXz1/yxev15W3+T+vy2eBFW9hNCyLi2qXtxGncTp8WTDrYU/NDDBqQrjz89Nz5XVJRLv5zvvbzU8mn0G9//vJWABMe8fry9ssCBOjLW93Nnz/NUsqff/mUFoNf//zLdzlN59x8t52FAas/fX19f4kFC78vjYPFV13l1y9dte/GpQ+E/+Df/Hqa/hL3CsnX5+Kfi/LD4q8lz/78J7D3WZAOkPvXYkEMwM63T7cizn9+6QA14Od27vo///KPxILKc5M0btp/Su6vT8GRb3sgWq+Q/PLhkb6/LaCXb99k/mO1c7f8K56A5e/qvgXqH8l+ZPa/iE7jHLTGey7/UtxfbYD+c/HrP/Ttf7fhwyL48sb5aQy613bmjv79USK//uR9//Gnv/0diP4/itGLDvTbLOFrZudx4Dft16+//tQ8fv7pb7/+1JWgin07+9rV6V/J/Ku4PvT8IYKvVT//cS/Qb+RJXgz54lsPLX4vyv9W//3T4jzD0Pffm8+LHztxfkGL2Yl3pc8Q/NCNDbD1hzj+8vZ3AD858KZzH5cBfvzbvy3k2K2Lpgjahe4WXbsACW7jzJ+NP0UxwNfmgRr1DJVNDAL7Wgfqf87wbHERLH77H+4D8j+6L8iH39HafxTE12+4/vUHXP/t0+IEZBd1HMa5nS40RlW/5HY4Qz7QW9Z+49c9wCpnav2PYPvH+cMM+b/9M+K/PiR9KqffHqQUP/FPW4sz9jVd6n+avbzMIP70yQWM4Y++2wElaeHaT8JoZnJoirQH2DlHpEniNF14MUAXwGfTQzaI2udZ2G+//ebYTfQlf4I1tngSXQODBd/MWXz8CFwL0jiM2i+570bF4qff//7T4n8u/ne7HsJnHSpgjldOgIU7/aAsQI91s8czHQJwt71HTn7/+yvAQEwOSAlkMA5mpp03gxpNfO892rrAfESJ1YvEFoCliroFDLCI208LMVh8sxconS/NHBEVTQtYuvRzz8/dCUi1gTvfIpkX7aIBhdgE04cFIM+H1t+c2n6YmIFmt9vfFvJaBYxUpOCf2czHIrC5yGMQ/m+18PwdCKl/ahbsu4hPC2WuSsDNtV1Gtf3SEdjPvMxU/doOhNuL3B++5DP/+nOoHi3yDA9YBCLjvlL6cc45IPAM4IHXvOt+rLFn3jw9+LP+kjev8rfrORVu8Zglwg7MDoAU/uNVUk1UdKn3iB+wdJb0yoL3ysqjBmfy/wejz/oPUw87z0g6AJNy8aVDlwi++P95eppDw2y3Gr9lTjy34JWTZj5TNg+Us2vPGRTMMA/Zj/b8Pte8Y9c7hH/J0xjUXz39x3PlI9GvNU9YBHjiARTSHvJBlQFbZrmPJpiLuq7nUAO73rniw+zxDIzAXYAYoKPmQn5XOF99tzQCsDB//z43PIqm9mb8AIW+KDsnBUUY+L7n2G4CrKrnRn6lGXSEPzf1EMVu9AevFkA6SAOQvwBGzNEEfPLpG34/r76b/oeNz/Fo3vIYHTvQx/VDALDDnw2ckW2IWwBnoBIe8zvw8/NDCHAjK9vZdwckO/vw+tGv/aqLm7idUfMZV78EqP1xfn96Ov/qjyVoHhAs0CJlB6L7aKoZbzIw/AAbQP2CQsjiHAwDICivIDwE2tmMEACBXzX3lPj4+eXQsy5nFnvfODsy75kHg/fqnn4EktNflQmQl80rHnr/a6V90zbLnsG0AYAINL5ffU4Qn55DwHPKWLzL/fynA9LP/9oZ6kHrxh8L4PMiatuy+QzDTyp+Z+JPAMrgp63Nd1b+OIPCx2948fEHvPiD7Kfbnxf/mn1/EPHqj88L5NPy03K+tH/V1+sFwrH+yJof8fnql1zzv4MtUF9koMDm5E1gDPjGjO9LAD2GtR/Oi59M2cwEOwBoeVADyMSX/MeCnxvuBX4fQI5+AILHiACK/5m4bwwGLuUt0O3Ng2Xof5rPY7P5jf/2Oe/S9MMbgE//nzzJzUyVzZXdzGdA0ENgVmtj//HtHRjnz388IPMjgHgXNEVYfLTn48HiCZNgJov9Ye6aB6/8FfC++Hyu9nfIn+nKfpCGNzvTTuVs/fPAN4+IfyCKr/6M/F/nAP3ZLubP9PCAi8WMVYAW5qPpk3z+mpdaMLb47SPwswOAn4EMH7AlcKXzm39kXeuP7Z+NOTw+2OmnBecD6E6bH3v0xcLzFPIDlDzLAZSBC/LwYfEkNdC+wJE5RTMM2U3yoK2/tCUFdZd+BZ4AVPizQdzMp48li+eS9xHHDh+ws/jZ/xR+Whi6vPnlPx6mgWM3iIVTjGBDH9dF/ogSYMKm/Uv93yb9Pyu/gOFq1ucVn2edH154/eGRjg+Lbwct4PXr6Dtr8PMue/v863zIm4v1sWX+APaAt2+bvv0Fx/Hf/vYnu4BhDxIAVDrL+m7k96XF43A4uwBEt8+/Zfz+BhrDBjmwX63xOl2A5QAzPzbzNAUDBAHKwfdnr4Nr/1fnjpeMJrLBzAuE4DgZLJf2cknSJOrYNIEubQJb4bSDYN7SdVYUTqI+5XkrFHddGyNs17cx8NkjfcJbUUDeEzW+zmNjPNtF0EAkTaMBjqBLz/MDFPc8akWtXIIE0mnHJhyCtp3vW5M4917OPp2bI/ntCPRAiKfPv785KxysFPBGZJ6vNQwhjo/CzrS/wleCjqdQOqd8abRt3zrWxYkxw90Nt6PFLEmUuq43WiwJfOoak3490oXGMSrNqygP6yfMo0iZWl8lt913dAFmL33SZDQ45HLQq1snOchkqKrmybX6DFk1S251FAkTlZfoUCdLyS2bpLqUPnFdaqWYrgzKueApf7FiB6YJG453ch/r62os5YCm7nIsOLrIsg18uSiXVIyvHXUKtILXrzDZSbBQnQk/dyijOpHu2oWnmBIPCidfrXHJbc3ounFjooO5UIKP0qkxdIjH0tVh5AlITk67653MIjNySqv0b0stO1PViWHroYEmVb6EsR6icrSZtqOxdPR8NBqSOuub+/3SQfTR5xLa7/cUMIAcYH/KD1iNwpCCn8m7r2ORv5QdqlGyxN+cuuy6HeLdUYQpwtNOMjxwRifKqbLZ91griqtLZ8E9aDC2ZROSZVSJYXvmFNOHfRlTwnQOIznaRnrvb9Zrl5i0PCA5JEHD9HzaRphbusuzc1P2ty25ltq0OmBpAyn13VnmV7Pj7xAb5KJVCokomi6nrqGrq+liap2iZQh1gyYXkXT3dzya6Jsg9iJ5k9EWxK4jDpaYdmDYnewgCiYLoeojhx6UQLuyIkKPTwovbCs8KRKEy1R22ehbUVHF3KmUUC5UnLqUdjLd8xOjwk4tscp+JUSke6TSfU415miwu87cCrnk7Gv35Ce9Q/D+VEAWxxSipKP7WtSO2MqHpGqX7B0L0tU7Y1UC5Vga77P3gSwzs8evW/gUo9rNLvKyam2u4Y+EmPMBtcRSej1QtuFBuw1XXtaFvUQLmziHin1h+7V+dbrqHO9119JcidzsGqukK1rU1TCw1piwE/BLeiiCexL14YmqIJG3r3xJItt+3ICU+pJgC4mSDbiiuDdDuKOksyXQ3Wmzy+w7arKn4S6rnCe2d1WpdqXlEd6J6omSPd5P7I1Z6uCccKcuuev5ibkZo31NDDlZqpRvq2NJyip+iz21jiEo7anrbhA9V+c6+6ReuNJjWlIssXYUxPy8Y4WLvcm84pbXNOgvRQkD5nSbGgSlmJgaKykJDeHUNVnP7Qml2FXbjlbQSZGQPmMS3RIvx25zNjKulBmJUIJTwYiUkGeuhwUq72I8VvBLfJ3HOG2hhCuIIWqdrOwiCPdEh1nCknoWgeqrcW/dqtz4knasR0k8E5xoKNwoxvpKGHbmlShz3NeGTvesMSBuu0hLrJ09ZbYFQ8fCBJh2skYUQtOt07lXOC0jujUGvRF1onbuZ7a4H0I8N+uw2RjS1ohwcw2vr3mWUSUPneku2VNayEDkEFuXQ2ghmzW6Drg1J40Y7dl39Ygohz0ibgiVaNPBtEJJFlYecevtc6YcxkBXSwNml+smns6NoGX3PcvDDSM73XVdqrubv+yW51TcpbzNh+uMMWiPxLOQoNpAMzZo2HgyrF/xepLsFYmbouRvluZw80WOZpbO5MgudkAEsb9VMmwlkGREbWi0t/igiDvs6or8uUwPpoExyjLHDZuo93JRcnGhREK1lBA4rLp7ZiLkqr7Z6zV/G+Gc8Cajhk84uSwQcVdBPj0ExB0ZCrKlxaGhiHCrhpxzN9KLWq6kiTxnxCm+0KOI990qj8Te32nlcXRugSAfd5EnTk3LBRRBFJrUFadJFYGiTSlLkXDExDRRQxI3DtPJEcLy4uZFccWGphETq8Ih1yZh7KhR5Royx4LglFuuXxLR6q/oPeivFkZkprZjala+s1SVwJbclcnBOvnS6qrp2VSyaNpfxvVhp7ECdCK3qsDnSWkklKjszVptZKVE+cY71ow0pF5N76RrcYYrYhJblz2kN+2owFxUk9fLHnGbEj/zW7pltjSK1hKHnnaH9K5IQWbBgaCs6I6cbgyTp0gmBcedpRZUtdRv1A3NdKd3C1oJo0ZZBWggdNxQFR4NDeHdzpq9QCM9XAUYCUcrH4ZQCaFyGI6OZ0KmslLclWDUuJthyJbsfjoeyIggXE/i6922Qgwj5fij6+DqcBfYdn9WOeSujKc2IYT4vj820nUkRvWmb9eULkxLc1kl+0bSWFIv4hYfths2ptXCdaNIE511ZW2mEheuEiQYLlcKxrXbVrs4O+6c0Kk0AVZvLB+SPsXCm9V4lWNSjQos6tmDc1fbOCW2J0XfmUSwtUCSirNGn24UczR48UjTGrKRQc2TbcTwaIpOgiDctry9synbxS8tNzWGBHdRTjKixfOcvCF5fi1Om/MQrw++QDssbJyaRA/vUyIv+eAGlYgAWNbz4+RWmlc/ZVHODEKT3R0bFOEmRdWPCHHxxiIYnJW3zU1MvmYcZigRMjQdwxpmqVN+6HaWgvRneiqPWrpJtAt9vgSRCfHbIMN99prKosHAlciuKFe/aMjZZA9Gw9nL/bIL7eWtFLtRmsDIQvUR3MH8nnf7ddExK7FzNyKoHlbGIoS6XUat0SDU0B1moP1tJ3W7diN7e3xaiXKBnGRnjWM84bIUe8OrbZsbUB84rWSGmmmGgyHvXCuq4rpCc6oMLORkxFrk3s9k2Q93MFpVdnLmCFFSplNR+ddtB3F2XPhZhcsnk6rAcLI+dcGNMcND7BJQJV/OLn4ztL2mNM392I9htPKWuwMbCXJY7xFluEsXkt7HZ7MMXcvJpcPWTFKLVy8b37wkxZna342tfqvZvNyETCpHh1GzhzQab1cTSgLuuinZbRFCtQovE5Jn1EbL6P3WhBQXs2wr3tfTcYVh9NWwycrG5NEeSjzI/bbrDiyfNYURWnhPFwSqSH11oCsFSsW17mEp5OU1GMCEAx5lhsNmQRkm0hCYts5MW2wzRYbVLJWtAZ/YnaXFFpuoxX0p+Xs+aSYd6S/xcDsx0qjF+CFDWfOQkQNprldFw95Xh2BnxWSYrVZrO7R2rnDkDlsiF3oJvlDhQdpydYAz+BYxArHTN1m6Mccl2pzkMzklWexerWF/027m4Za2+uEAL91E1nNlKDrnTCTDtdqWkKi6kSRu0vGsMUt40raJQlK7yEaIkySRUT/0JIxfDDtlj8dUThzrViJZjoYtTSVUZhwuMcmplHuuEk1Uk3CSLrerPqBE3vfEwVaOqZE6jrXVE/mCxHfCQUk+NpeMfcZ2rr+G0ls2QmRGI5v98bz3sZxcHypKZ6qRqzwoaivWrySldLHEGVJ/tW9pzxG7cJ/dSr+935IT0ReQt+uQSragY7k3xTE/TnFAtk6BSlnJFYl5Rff7jlWP2Pp6pHAmYvZrZ9rcjol+kz2ku6/S3V5zW3pgKEm9BhvdgmvFiroJ00QwChBGb7CerEt7LubI2GMUdhs6AS9CcVmJfV1nm5DvN7ZqxEsEOh66sQ0UrtBofRytFQNFk4es5XLfoqPjXx0EUnJYkPqUM+/cno6ZBDMsPOvl5Vk7ddeh5pAzYkbKGIN5W7M56V5XicAUGYOMNH9Zn8fIXU/MvYJKxy0CaXNbr5jU6db5CcOSyLhDza1IxKnYObVYq2sSDPwJn9GCL9EFiehIEaCsdpeQYAeLZgYxMTgybJpNdWnd073leppvSZlN0wiX99Mk3y1JSR3Zwvc570QuIq7UZa85AFiX7bkEw9kFS2NUR+3NUgmcrdLbe/l63awZxg4cHZVORwrRj32rxjl06RD6hAqbKzXdnGp1QryI49h0JG2dZLkztd0kWZJFZbVdHi3ek1Mr2k1dwSzXnbRuDNNIBg02Vfx+U/mTWtLMlrCP52YYamvNLE3oejRYrT1uDwdOqnhoL2S3joWS20ShB4Rboua2ZFfrjnf6HXa7SlONt5cdBCK3N5EY2Qrthb+y+QXn6xQmrKGECqyNWNCDzjkldR32yQRvUcdb0comGxmOSDjEKiWXN5GNjtT4VgrQgWimFgrJmh2ve/eeibzAmdCECzp9i8/YREWph2YWM1JGexXMnsLBgNAQSixsWRjbYKYZeArZNiRvJGtM7TrOHBWlEu4BzSuoAB03SJ5YncToJ+sSrpelnO+nEjketItAukS+cQop82Izgk8crHopz5BLCnZ3S9iEh7I62tLxGGGJfMeV6l4JHIAbHBrvUpwe6zyNpjpk6B45XvQrCil2gjoC2h4vYGxTer/zV8nmFO96CVm3VdxC/Hqn9+bFr/UtdJYlySvPVV2eKbVSzoHUZYrm+ZkAwxvPL4oRvtn70nAHsb50q4MWV7FRT5u1SpYVOhms7R+JNtmgTWjphqHcFNuDdQvrmaFCkeOItEV4vNTC6V7Y3SGfNlZRSjVqnyydrvCNx0YkC7nE7WTa67MRGD3cSllt2YqUdvCOMrdgMCOQ3b20io18cXaCH6y6RM0GhrjxTHKeLtyxJVse0vbYmV6LiRpdKgTAmnYbUPYmcf5qpU1rns95Vr0EcmPdFR4X8YuENLF8uuTsAPgoHc2tFt0wOGqOXHjkzzoBH2WyGgNSR0W/U7kqh2JL3nOJXIj2LS3uXU5H3JlPhNoDJxEssjLKLsh6bbZFfjuwQWPv7iiqWgLr7M+r8yFPfGdKrkofrBzthuaoWVhCpjUHrj6XZFoqgtBm1/M2aDc0dipRh4B2V9Ly92Rzv4hXJTc7xfPG1XW8Hi1tbxzA6I0h6y4S4dig/VamE+/IxPD9WNJeW9R1Pmajs2kFGhdMMDkUPUyVom0H2vkQk5iwNIigUb1xWfVxIHp3RN7wiA8XOCSuVuE5XJ4O/pKSjpBcaJUhXh024lCHLuCusg5Th+VtsVrtFRLzRb4FRUL1bckg9NKWIbqe1uEYcBp6QdbJ0uaVHXRgbVuASZuGhys0JtfN1m/PATxhkIJz14i5n7Z7CIqCrmBD9oTv48thqGGR8mXNwDJ3txMFUofBsLeMBylfLse8HmTmiCa3k3ffUOxGvDVJLmyDJrmt7ksnRPbnuswCmd74rXvdU57HrlAxLNjtqFc0auDOnRNESzSXKGweLQzWTAQqiT7Nz/GqW7ucaZ1IdeWTZFONyT2u9h0Zydy97ZvsGFoRlzR2Dc4ErIttkdXuANm+UMNVds+EYKO5B18d/fOtN1MNagVdT+FLjxWOE4trTtxpBCPrO57y1ZiWIVI6FXQfixlTSCgiZMIG2YTJxdnk57pALynZrJGL2kzFQDO2QvqxRgZYcb6uFEsbJmoj0z6EN6MEbxC30PAQJ834vDNKMANpoZsJxCGih2gZuccVm3O0tCPP9Kj5WV9ofa2zZ1nwhN3hcJKyYZMMBY9QSy8cvEbE4P0x4TIkF+4RaRTV2V3iZaELCCzD6XI+b5hY3fUFtxlFTaMzcY/fi/4q7PVTSI9Ska10XnDvDbXfV9nQD5jgVts4Iy+2bAUH3WUFrZ7oi0K37emIWWcz3vfMxKVFtwv9lT5cTvahIfO+teyIYFSlsrA627ZWjCGD4Fi52/qmkq2SVHTJorypDMZh6w7bCJfNcqPeSITkR/dgB0h0FSGybK/bqlPnP9EtiQStEqitwkwJVwMKzqLFqlHRNjpaUVQK0zAK5wnhaoREs32yEaVSWe1rvN9vbhfAIAXcctv4coubCFe5WyypXeyXB56qDqXXHyWPZEAaLfo64A5G9Je+xal6ZSI1ydMHGfavmulBNKfSKw89XINilQb8Xero6ygM0FFDyiAawopSV6gaWsTdb/uzj5nNaVxB52zsyfC2A+N9wub6YXW9lu7SU9wuNzp4fUXqgi9T5cClpYR2yNU7+hBS5RhfKRIyVulKE31KPQZVQtkbmMLPsKkQ6R7J6EPKYpkZKsnNuklDrqvXtX8LYjThB6lHy+3VCDJEoFaQsdGa9cq8hQlGjMdSwCxTg3hqagVj2soqwZSecpr/GiCffUtE7jCOKQfVJNJrc4lWO5HCeRWXYxxzhJIC/uA66i+z0WvsvXBQps4xEVScYDTrzQw0IIRG24FDUs8mDqwoVo6+JQ8kw5Hn0L+zqDreS8M3V5xpBAg8GtYVN5xzp10hi0KN+35sIw/MvjHpg/OAR1S85whCWkke7CnosrjfuwsYlaz2rpirYLmSjbTY2vSdk/kAJZy11R5N5HQxKTJtzINzO1l05ZYIOSkXZkImpdJHZUwR+DzSbnFji+lg3cCwuA+8TnKEJTiVU+dYFyCfkWqDKhlDUA596eAr5byKi7K10Uj3E8zf5rLDBqxC3OV6294rjKtrxGNgqZdOhy13JQg4uuyPEIgrNQyyBetlboFjCptc0hicw1Z7bM/syKO8LVxzhH3YrVc3ZiBXor7zmv3ApXZ/kd2b35bt3juSoZASHWFNhU2oEq5ukPZ8x7YHmN0FVwKNZQPC7U5yj6MA2af8IoC24CM70a5HSKlcmNRJhW9r1h8hc7PrIIKd0DZAAFTjgpvEOiIz+HWXi2jnQnmenJyrtaSHipJNWoyZ42VF3JZMcjn4x/WuzAmG2jMM6W3ru7mju2WGKfSNO0nQdr3jcGoViFie1YcOhY01VG2Tgk7jSiiMfLArDXFwaKqrCIzj+Q6UgA2OXtnoB6cp7ml7E28PELz27oa9l+DaYNuJBoMCgfOcGzBElFFV5KDT9brWzsLZU2xMulp7eEe6I1QGIQ7bkLu6X+rLej/45PpegakdLMJKhTpQx/7uKNKoqJmpN7qn0q04uCNh0Qq5KeOWaLHjqdmTemFSJ4i76UnMMKvUhG6ezF+PvKZuzpuE7fIW01bUIY7rIsVqRz/ylDc6VJmLWUiKFzQpClVgIYPTL8f7off1A3G8kp5QO9SE8jbZYbDRI+VhI4Ca8ynbc3K+v7sKSxw3Eot2FFYvZSGsrNtyi4+mbFSxlAlgJj2cNJdUXOSGdzA81riyZjF8HR3U5Vbos/hk+DtCy3KqoGuNOjeSSQextr8aLoSOOCXADElt7JtFaQzDvH14m2+vvm41/0sPv813mP6f3eh63pN6f4Llca/Qt73PD12f/zWz/vbhrXZjYNTzpl6TduHr9td/uaX38Z95aGGWMD2fK3u/Q/y8O9/a4fzo9Vuce13T1tPXpkgfz7GAHU7XzE9qNvPDvC54//Gm5zelc+iL2nftpv3aFl9fN0PjfH4+xfdiu/VfX8PXfc4Pb97rkaqv2Ir46tfl7OvrKQjgIvZp+Ql7+/v/AqlXqu5BLwAA -->
