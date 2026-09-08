---
name: "rar-cowork-cookbook-configure-plan-projects"
description: "Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_projects", "rar_sha256": "ecf37b51851485441da2ecf2adcacd884bc4bd61630fc2d12a2ec082af9cbf48", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_projects`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_projects_agent.py` and in the RCI capsule.

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

Plan projects Configuration Bulk Setup — Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
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
      "description": "Explicit approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per plan projects target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_projects_agent.py` and embedded as the fenced Python below (sha256 ecf37b5185148544…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_projects_agent.py` first:

```bash
python3 configure_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_projects_agent.py   # or on stdin
python3 configure_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Configuration Bulk Setup — Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_projects',
    "version": '3.0.3',
    "display_name": 'Plan projects Configuration Bulk Setup',
    "description": 'Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af',
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
        "upstream_slug": 'configure-plan-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e63b1ba96e9defd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-projects'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per plan projects target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan projects, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan projects target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af', 'example_request': 'Bulk update plan project config from this Excel in USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per plan projects target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update plan project field values in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanProjects(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjects'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per plan projects target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjxpbmX9G8HTG2m6piX1QdN2IQIJBYhEArrhtldhD7KsB9//skkt4q+9q+3R0xn0YVFRJk5tnynOc5+cKvb3bXRkX99vnN9O18IdppGkd+vbBzb8EV96JOwFeROOD/wi3yto6dri3q5u3Dm+c3bh2XbVzkYDlblmnsNwunSx8zgzjsanseXLiRnYdgqC0WZQqUlHVx8922WcT5gh9zO4vdZoFT5GL9v01OXQR1kQH9C7ttbTfyvYUwuH66COLU/7zo7TT27BZI83u/Hhd1cf+wqP22q/NmYb8Pz1pn22ezPyxKu2vAgqAAbpVAOZj0YdFGfj5fPox+t3D2+rswxwdLfNgOgLP+YGdl6jdvn3/++4e3GPx++/zrm5vaDbj1xr389XXgn/5yD6wCVyEYLkcQ4xxcl34NRGbglucHi9fVj42fBh8W//7vyd2uw+anz1/yxevz5W3+Z3T5bC6In920IB6uXdpOnMbt+GnBpnd7bH5jdAO2KA8/PVd+l1SUi7/NYz8+lXwK/fbHL28FMOERrS9vPy1AeL681d38+9Mspfzxp09pcffrH3/6LqfpnNm5WRiw+tPX1/VLLJj4fWocLL6ausC9dNW+G5c+EP4b/+bP0/SXuFdIvj4n/1iUHxZ/Lnn252/A3mcSOkDun4sFMQAr3z7dijj/8aUDZICf27nr//jTX4kFeecmady0/y25Pz8FR77tgWi9QvLTh8f2/X0BvXz7JvOv1c7l8T/xBEx/V/ctUH8l+7Gz/yQ6jXOQ9e97+afi/mwB9LfFz3/p279a8GERfHnj/TQGtWs7cz3/+kiRn3/wvt/84e//AKL/SzFm0dXuQ8LXzM7jwG/ar19//qF53P7h7z//0JUgi307+9rV6Z/J/LO4PvT8LoKvWT/+fi3Qf8yTvLjni281tPi1KP9X/Y9Pi9MMQt/vN58Xv63E+QMtZifelT5D8JtqbICtv4njT2//AJCTA2869zEM8OPf/m2hxm5dNEXQLky36NoF2OA2zvzZ+EMUA3RtHqhRz0DZxCCwr3kv+J0tLoLFL//HfcD8R/cF8/A7ePuPhPj6jta/fFocgLiijsM4t9OFwer6l9wO/bydVZW13/h1D+DJGVv/I6jij/OPGeN/+QuJXx+LP5XjLw/gjZ8oZ3CbGeGaLvU/zb6cZ6B+Wu4CVvAH3+2A3LRw7ScpNDMBNEXaA4Sc/W6SOE0XXgwwBDDV+AT1Lv88C/vll18cu4m+5E9IxhdPCmtgMOGbOYuPH4E3QRqHUfsl992oWPzw6z9+WPzn4l+tegifdeiAE16RBxZuzZ22AJXUZWDaTHkAwm3vEflf//GKKRCTA84F+xQHMx3Ni0EmJr73HmBTYj9iJPWipAXgn6JuAc4v4vbTYhMsvtkLlM5DMxNERdMuPL/0c8/P3RFItYE73yKZF+2iAenWBOOHBSDIh9ZfnNp+mJiBkrbbXxYqpwPeKdKZvOsXD4HFRR6D8H/b/ud9IKT+oVms3kV8Wmhz7gH+re0yqu2XjsB+7stMx6/lQLi9yP37l3xmVn8O1aMQnuEBk0Bk3NeWfpz3HHQYGah6r3nX/Zhjz+x4eLBk/SVvXklu1/NWuMWjXwg70B8A6P+PV0o1UdGl3iN+wNJZ0msXvNeuPHJQ/13bwv2uu1nNDY8JUKJcfOkwBCUW/z+3QnM0WFE0BJE9CPxC0A7G9blLc3c47+azoQTNyUPLoyK/NyzvoPSOzV/yNAYpV4//8Zz52NvXnCfeAdTwANYYD/kgscAuzXIfeT/ncV3PVttf8ncS+DD7PiMecByABCiiOdrvCufRd0sjgATz9feG4JEntTc7D3J7UXZOCvIu8H3Psd0EWFXPtfvaZlAE/lzH9yh2o995tQDSwYYA+QtgRAy2FxDFp2/A/Bx9N/13C599z7zk0RN2oHTrhwBghz8bOG/LPW4BgoGceDTjwM/PDyHAjaxsZ98dsO3Zh9dNv/arLm7idgbKZ1z9EmDzx/n76el81x9KkIggWKAqyg5E91FHM8RkoKsBNgAoAWWVxTlgeRCUVxAeAu1sBgUAuq+EeUp83H459MzQmZ7eF86OzGtmxn/P8/G32HH4szQB8rJ5xkPvP2faN22z7Bk/G4CBQOP76LM1+PRk92f7sHiX+/kPp50f/2cHogdfH3+fAJ8XUduWzWcYfnLsO8V+AugFP21tvtPtxxkRPr4jwu/EPT39vPifmfQ7Ea+S+LxAPyGfkHlIeaXU6wMiwH1cXT8S8+iX3PC/QypQX2Qgp+b9GgG/f+O/9ymABMPaD+fJTz5sZhq9A1x5EAAI/pf8tzk+19gLaD6AbflN7T8aAZDvz736xlNgKG+Bbm9uEkP/03y2ms1v/LfPeZemH94Advr/4iQ2c1A2J3Azn9tAkEGv1cb+4+odCeffvz/UCgMARRfk/vuUhR0AGXNPFfv3uTgejPFnSPti6m9wCn4/IdabjW/Hcrb2eVib27vf0cRXf4b5P5rD/pEGHmCwmJEIwP98ovwnXmlB6+G3j7DOpgKOBct8wHjA6M5v/sqW1h/aP+rfPX7Y6acF7wMsTpvfFt2LSedO4jfY8NxssMkuiPiHxZOvQD0C2+fNmHHFbpIHI/2pLX7ex3WRzx3BH+05PJ37zZz/eDQpDXDXKQagpAYt0GsnQEi8Z//8p4pSkL7pVyAC4MkfNfEzJz+mLJ5T3vshO3wA1oeF/yn8tDia6vpPpX9r7f8o+gz6rFmaV3yeJX544fiHx0Z+WHw7WYHgvc66swY/77K3zz/Pp7o5ux9L5h9gDfj6tujbn2kc/+3vf7ALGPYgB0Cxs6zvRn6fWjxOg7MLQHT7/OPFr2+gkmywlfarll7HCTAdYOnHZm6sYAAzQDm4fgICGPvvHjRey5rIBh0vWOe7AU47JMqQKMGQBIF6NgbuYbbn2q7HMITjEo5HoRSOBC7modg8jDCYHSxdJyAYIO+JJl/npjGeTZntABH4CADJ/z4MbnkvH542zwH6dq55IEX4ykOHIsBMiWg27PPDwRDqwBjtjMoFuiDMYF2FWrbOBe7TLVs1yGDaO+FugAOb7dFnJeLCYX2LzU62FGXjq5uoECBjC90PuAy7mC2KqXykz6bTn1HjTrCp2zlqFui33bTMaCn3Ce6uqah4hI7MWJV7YnS0U1PRSiPU44Efa2Rsh43dUYIOE9gSXiPUdiNQuZBEpFRbkrFtprO/vqRFFhoHXhmCrb/GRsMkqq6Hx5UPq/B6PHeD3O/au8Ldq2ZbbDBtgGLRrE5hWlmjssREexCFtd3LS0Xy40lm8iLcXyzbEuw1fKhaj/Sdi8pQ3VZWt/bV3VQKcrpeJUHNiqjaTDo1JoPDN2rjFWG7tZ3N2QltfktBgZRCUK+U2FLPif6gYbAaBMEa22CZk7r3SvCc0zaGDnbj1adtI6xVNb5w11J3VVzhnGqfnlNe8XltnZ2vTkrXbGC23X3Py+Gt3hDLfGKWFryNkiYzR9M+KSh52gCPB2lDYBvLakq5yloOsuy0QLDEv5wFbCtil4L2zxOCFVpvehbHTeqmSbyoT63j3ZGgFdkfx4Mpj8lt60Uee/b33Dpbni1ym5whofWdrVYhy1hjxWvBOntBFKoQ7RmauftsSx8puJlGvMyktNyyyN6269iOp/P2ykjmsLkW2NG10GN2F9TiOJ61c4pOtwML03Zha5pCSQWt7pepfIE6gbywu9gS81q+Krl3gJrWKTfBuL9Lt5Dkxy4uK04/tVJVVKNnxSLjCDciSrdu2ybxiZB0qctOMRG5Dq8px7OaxX5WoUV8N/gkdg142kMXQeGHKsKJNNmmVzmqD3ZUp2cWLa8is916HVaeN+22TFKkbNxsyHKsZupK3Yr7fmBP8HrrVJJKKnwhwLtLtxbX6AbSIoXZes1GimNshXJWs+MmpEFXDd5jQxXECHpanwsoQ46MelAmmLsF08282Zlt7AV6u7SD8/KEVn7pTcxFUDvDVJcuvE5h4gJHHsFg3m3fXaVugiy9bweoXhK7Q3yx71nANYnQSCYU7TMjy624M9RKLnfx8abSW/Z2oVC5sw8sdG1hWcGtO1tPYhEfkPDc70mhEM3R2UedHrUrZHQqJMaE85m0Tnt/ezqd+XK3FwkNvaQsfhT2Z43Zsf1awNmhEEiCE0WSd0aKEeoQtS5WhikCjvjMqlxt+2i5rLzj2Or9leKEUAq9ywpR7xNS7coLsoYuyzx37c09iLxrFzLKqkGb6nwqZZ3Jo7tPW2d802qdrmJHur/XF65W+whJzujEVRebH1Nx3e9WEm/ZyJ4j9zF8vBAmwyCCJudGEyBREMusWK5SR5epU2YK9m2726wRWvdRNFwtb1csZO8hlYjH4bKKs00xBCR03rXdRbWtG9TtiXIMT6dNnteuTra5L24llwsvQnEad/clfaYNUQijMEitFZsfXGjpqF1vqamxLSVcUxENlhnKDndnxRtte3URuPx06AspKcpxkF3JvV47zrgt04C4YCK2spGdwBKIE7jhfXvOBDI6a8LJ3HjbKks6ajQ12eXXliNXwW5n0OoQXvKu0IqNqOo845xyZQwoT4qYpDGs44h0UgTtGgI/NSXmJRf7ijAswXixZ0H7fVV7vp2eqD1dohOMKvheYnqw6zwQ5u2tuy5zyJaD1CVNpGKT1BS5odgDYEBjj7e2yvUSu1Um/CS0ZmI6Oykx+Ik+nllDPclOox2uwL1IDUnZIMzDrRjQRF3etEq51Eua2uXCBF0JYb/N9vppn9lkigjDST7cTMTj5cO2Zsiz5gjrMN9EW+8gcRounE8tE9objb/UeuGkVr6u7my3VxSJPhwpo2JL/Gb3hHTj2Ti8VtKtqC6ZjvpNVp1cDm2vIoodU2XpaGkWL/NU6VW4nypSP2iDma/MOFMkvRGC/G6f7K0RGfCoaIx/3IWDfl7RO0W/wRZzbHb4ubmqmFuuVqMNweecInkFJs85cRjRC3NzhFpl0jrcRnlQ3a5huHJXMrTf0REp2JYs5ASApKOJmundwYkNOF+uGueis+tJG4wmQaV4qs1GPt3Xg34zRQ4dpet4RapGAhi5Is06bo4Ww+3XfIbsdnu2uK5hMTs1tLrqg4CX5Qm5lfWWn+RKntLTZj8kXLizyOKIQDxZ7yCMS4/Jee3FG3U74PeCJC8QIjPxPd/xp+5SHE5RSniutDnKE2vdD+n+hGQ2EpNdFAlIkkGSJOSCwAGA764Et+TptpHpfpWJwt4lhHgvSNzqOGwifr13m2uvdWdvuRtYcdtVPLOPdqsbzrgrf6BFhBfPDnc6GwjLKnawF/htHGLjpKnseKyX5mksGAVRKU1buoN/1T0TE+l1uRK4XZUC9eFwSS/nAce3KxZGT8baQdfX9BRz+8vOMYjEOuyD0IQRlUdcAm1u+yrlzFITqfiinVikvO33y4pPLhuvgddkf0+qpKm3RYvQG/O43lxM3WP6EFWzaTArI8qPR2d/X/qZuZPXSSajehdXnZqsp52Tubhg7A/uak9XgDOPpOY7unhiV5YVssfdlrGuVXjBtn1pRMMpiYz9HTvRWj7GzY2Roex0MwSlra6SLBtrzIPqQbWziqkOedjWZLk2m7RbEeoqVkmybijBO13iUgB4bVjk+Zrmy11Y6ka62bEBh0INU6c6ua2WPsmGcomdt03RlPbx0myZuzOx+yqOV6xyHUxL3tfesVS2maxkQrFTPUovDcYmWnWDcjhCwlyaXwFgxipWXnFpqLXlEtvHy/ZoU7XW1/CW0GjMb64srzvTEYOd9RET4jM7jG1sw+1dMgwtN64XQ1dTVlYacncYiaXuDY6+sU3F1w+6oA9oSvCcy+39kUXsUpfKWyWZpuzI3H5zjJo11BuGKqSZ7baUcBH88HCpDI09YlgagbZcmtjjKWR2d0Oyqr1nJWt0vzqqVRUGtAqayyw4nI7iep0gUrLWhqqgE0HkD+LNEirrUnYbxlJyY6cjsDAUg8qfx3N6E3vIO6Tl/lCoB+3MYKCI0MOV4XZ7csWZ97q05QtZwEdRq/gBGsBYRoZ9m9E63OedZ/TmidfgfHWQvU2DB8iyblU9Xq5GLCBIdMV5+8t2xSTJyg+Wx2TXTTm5nOLoqDniKb0aTX3COexYaWsr4ZA67IhpS8mXU8Ix7b2idmF9MkqdcoOjbImmdz7Wd7nghbAig1a4lOoSCSzKRpfeHSIUfC3bxS3AcLs0CRp4L/QAN6SyPmPbrNgX3f6EYVWeasFmQiN1ypxJ1DaZaYbuvRuK9OwcOG95J7i1FuiaT3bLfrnvSRtgkxlSV7IcmyWpHo2SvxtdeGT76wY1ha1xGpfHEzolDCoXhqWOExINrTY4k4VPS36dIoi8wrELxJ73+7oa743sE2TGy+V6e/SpdCsX4bm7h/BaLyLtYG/Oyi2b2qVgSnAbQ0x/qeE7YAxnjdmtG3orDPHriOErZypYhdfPwbZsEuKOm6i8ubLWBdX5hB/2MLF3BQ33kIt7o85UZXM7E/Q1yxOuTeCEZ0vZ7ea6liuaSxsB6FKRDlUn3YnOIjYu11exU87Xw/F4sOWACPA9JGL2Njp0vKJ0yZHiBuVGGPuOWU3uxYdP4iaooKYEXY0LXS0WK5z1MjG49HI5SsxUluRFVHzKEvF2R5D1MYpseE3jzsWiCQWOFcqZ2gxizhcm2mvZ4J/3dMRrjLjN/KM8lLKI8uJp5EEE1ZpiVxsljr01L2i+4JwPeUNcxyWPmkbKA/7M7uHN5VabIyQdaHYlHdZutSrsO6n0a8dDl7rEWaEPsA0+GA5F7Vs2E5beRu477MojEohm0UGMxcThxcYurh3hsuKKezQxSee4G9YZfjjGB+5Ub2CdR2EGqjWT1CExHIQx4QF4y66Z4I6pXk667p4wqYL3zDpi6Vt3mljeWxZ26cCkX6Kyk1dGCtFjF+4TWQQkTIxmTV57AHsMAkQ7wbDbLu+RiDRrLJAb907Kuoj3aOVEhdG0OiWxCMLuojM33gQE8ftDcbbVXaxNFQFgOr+XHp4MKiKCKnIyR+jZM1TmMLUS6Ytw9oy1sZc3Ky4C2H+EVveUhLyJp/JzuEXPEZ/z7CnUiRE0yrK+Q3B3nZuF4vCHg3c9lSulT1CuLjiUEgdjXxGyV5rUdHQDQWhPZG1bsMjb/SGIKfEAQLVbw4Gy8wAHEcppYwmbYQP6ACjUONM54ypImD5aoRv6zjuWbyJBsttGGqZzQeCq7A60ZEbhUhuC7vpu5w8nyiD5ExwH2ymLr03ddkpYil6AS4crJIfoQCmBmR1orh+NS1N0BHUKArFk+oI+upqeT8pR4JC1kbehvzMSV/I2d66iLvgWP0Aj425DQRe30aaGvAyZ4MhVHFnyDoji75druz4bQlRG6igc3IsjZttbuzquJQ5Br00X5+pRTW3qoJZ1Haq8FJwGVzyuwhU8NPat2Isnc7l1EMFWCmRJbeXEhcmObWyTvSvyblfL1MqWdeN88tYRZfUD3YpQk4nUlsTznN5U7lIDx6D7DpuMtVnicMZAoNdCe9F2d4RiRZGC6PzdEXeTgNUXbKenq05OYKeeQlBb2LDELhRJqWST70l8e6v7rt8RbOXUol2iVGszJX3d5Baf14LXu7eYa3LDOvX1vjmdJJgoCktp8K7F+altA7sHAGKfg81pp0kTP3R2P0kZba+CBtbMG1prdkldloO7Q62iS8SlJ8GhV603K3A+Gjc0ZjEeKOsCETGJUzYIbEoH1I7xfFkCRNoSGKTSbTbdCLjMWBTJvbPj04WYDT1vYCK0Shv7qIWxtqIcCS4gGL5j8DXWD8BVIYAxHJKOIRbuj8iUwV0BGtTQr2R7cEcDS1exrt+ES0vma8o0IISG5bwXwrheaq11Z0RH0MoNyPsBZg1zQ2/7aejprQrFS3BoNFGLsvKJHS51tO5g6bL320zRV2mirOUatw4Rnu1U1iymUoOmBo+WxriECycv8rnXHI/sVYLhxAMf/3I1h+W0VoxRLJcYxa8yYhdbZc9Vhnq7GynRQJTV+D1G3f2iJU/oHaHV5ID4t+IoyUhQKiem1ysDg3ljHI3zYeQsgZNJVeIdGh1OuEX1nJqxhYyheSWk4AyTnA/rvM0LLItI14yOuktVd411dlpvbJY9jdg9wzctYe3Y3O8d90zcgtjtTltmr3mNISfVPj6cN8OOV5Y3gaKv457aaOwUdUna0hRR+IcLAo7L9L7L+O6W3CQtOWzWE7DLgTTFUiWHQ2HAPRuyJQeW8AfZSC+eyNlqtPTNfml4AazTeN/BNQ9c2K7GQaAJsugDsTZzEM1VDVWBJKlTzyh8kYX1RE/VkTcuHqzJag+bvpGb1aj5m6UvHgq6VRqDxRNrPZFKfJW6pF1XpKG1Ps3nwJ5iS7aBxrtQW7nnuAtpS3XSeooykjOLcPJb0OFyRER4GLGhxo6NIL+RrlldjwfYPd31EHK1oXZyqFvtbGZynD2MZkW24zzPsRy8aLNgqP105Pkk55FJWmMYr6AkdtazdcEVcbWucVzLB5plmSSAy2naGiFmMJfofqNUN+7K07pp9DKmTXk5sVLG2xDUDph+W7X6FSUvyTQ5OOd1LuOPa8vbDbw+QS7WXdxiakPusOv5nnDCDdNVUr8mB4vZonEgTHB2UrJ2Cdlcrtxgv45J32QKeBxQvwKhvWHdEks63CAuhLWlcJU9jiW6MpHc2WJ9l/SejZrrWNuB1hUafYRL7xOR04OSETidVsFk6k3qg0KjN9h9ElZx5iTBUahO5JVGLHcH6K08QOQx8CPRPcOXlAxX8r2OMn1U9ukaq92IT0Si1/fI2lWIDZlyBonBsrgu1MSnJEbOC1G0x1reGp5GM0V4I1zoTq3vEmQfrt422NQ3l8Q7etW0ZuGw1EoxnSmHrxVZKeTdoCj2xAeOhSn+fROlfrbH9zhRnK2GZ65+FKvLsR3xIuBvGc6QmQeBYwy+UZAOutlWeoXunTLR5hIUhJpBKKcH0gatZI32O8c/rklYEc22ways83rMEmUT40F7GWWcTjPtTT0XmpsMmQ4Nlsh3NJod5q7AYyTypi4NCiWtjJBNGN8um+K2Gi1JQOHcG3HQxJ0NUvEvtXBFSiYLORvVuet6wo2pctOdY50T0PadteKSk1vQlE7Z5JGSVIsDU+FqVJxafUnxqotVzdH14FsGa0y5opcYwTv6MI3NHbMJanNYaZMASnhkxQDht/fb7dDhMCxDxHq3g8KAA5hOhlhxUa47Y09htEmfdnZM+3R2WqKGl5324o2CbNKppeDidtURzqSKv55w09sccRLZwg3PNrRR2EVyuu9udq9B194p0PaqYMrEkhro6XdnlKYYZuJXNBKaZzIUuVIlRRTPuZblHZvW8251HiapYPcij+ubfXiM7/hNMDoxKL17w/ItQDQ+TKhlrWUHMhGjE0OrhmQOGDTkunb2gtYPpeVZU6I2Ag1yc5FCv1jK8DjGfdkRcd9DAVmhDl15u6WIVzsYbc5bCAdwAlmcYelL+651F5ouLgFbODdCUFU8OTo+NlLEKBeUDQ4jxHjtg1QJMrxVoF0wNrnfEah9NyCJurfLuMdF1KXQfrXyrRPRQtn1jI+qtdvolxJJNraVgPJdglLCPZsuk46D8MaBbvGKH4mW28uh011uOecARLmFlZlxMG/CZbvjV4OHKi2FIsl2J6n+UragbbHDBFRI16s7o4+Jb5q8Sy3JDZ1Grofs2n5SrobTQjAFDtzbe7McbgF+43uPSCl7IHRZsswdmsdLf8jd9WEThDmn7MYEMY53mu3K0VZCohYbf53DsBasyv2OZo/WBM7+E1UkSHY22GsZSDCyoSl64tTg2mh8kORY0kshzPCabjfI2Aosy/7t7cPb/Gz19Uj5v3p7bX6A9P/sWdXzkdP7+yiPJ3y+7X1+6Pr8X1ry9w9vtRsDO55P35q0C18PtP7p2dvHv3jrYF40Pl//en8I/Hy83trh/O7zW5x7XdPW49emSB/vnoAVTtfMr002s0Eu+P7tA8lveuaYFrXv2k37tS2+vh5Uxvn8TonvxXbrvy7D1zPID2/e64WorzhFfvXrcnbv9RoD8Ar/hHzC3/7xfwGKfGkIwi4AAA== -->
