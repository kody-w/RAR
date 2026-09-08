---
name: "rar-cowork-cookbook-configure-define-project-stakeholders"
description: "Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_project_stakeholders", "rar_sha256": "f7fbcfd00c663b9328084c1eb21572a5cc73eea67f024d47fbfca7d850cd2987", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `configure_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Configuration Bulk Setup — Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per define-project-stakeholders target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 f7fbcfd00c663b93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_project_stakeholders_agent.py` first:

```bash
python3 configure_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_project_stakeholders_agent.py   # or on stdin
python3 configure_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Configuration Bulk Setup — Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_project_stakeholders',
    "version": '3.0.3',
    "display_name": 'Define project stakeholders Configuration Bulk Setup',
    "description": 'Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa26369efc01f75c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define project stakeholders, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define project stakeholders target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies project stakeholder configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirmation wo', 'example_request': 'Bulk-define project stakeholders in USMF sandbox from this Excel file — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to define project stakeholders for many records at once from a spreadsheet, with pre-apply validation and an approval checkpoint.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineProjectStakeholders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProjectStakeholders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per define-project-stakeholders target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6mKbXYBvdMSwSQgEQghJiHKHix3EKlZB3f7vc5D02lVd1T3dE/Np5LAlOOfknk9mGn59c7o2Luu3z2+HwCkWayfLkjioF07hL/hyKOsUfJWpC/4uvLJo68Tt2rJu3j68+UHj1UnVJmUBjnNdln50qipLgmZR1eU18NpF0zppEJeZDyiC02ESdbUzH1h4sVNEYGdSLISxcPLEaxb4klys/ueBVxdhXeZAhIXTto4XB/5CvHtBtgiTLPi86J0s8Z0WHA76oB4XdTl8WNRB29VFs3Del2cms/iz5B8WldM14EBYAs0qIB3Y9GHRxkGxCPKknY+5AVgMYCds32Wt83cqQNng7uRVFjRvn3/+64e3BPx++/zrm5c5Dbj1xr90C4QgTIpAf6p/+K79bK8MaAz2ViMweAGuq6AGLHNwyw/CxevqxybIwg+L//zPdHDqqPnp85di8fp8eZv/GF0xC75oS6dpgWU8p3LcJEva8dOCzQZnbH5jiwb4q4g+PU9+p1RWi7/Maz8+mXyKgvbHL28lEOGh8Ze3nxbAUF/e6m7+/WmmUv3406esHIL6x5++02k69+FmQAxI/enr6/pFFmz8vjUJF18Pusi/eNWBl1QBIP4b/ebPU/QXuZdJvj43/1hWHxZ/TnnW5y9A3mdEuoDun5MFNgAn3z5dy6T48cUDxEJQOIUX/PjTPyILItBLs6Rp/yW6Pz8Jx4ED/P7jyyQ/fXi4768L6KXbN5r/mG0FAubf0QRsf2f3zVD/iPbDs39HOgOR23zz5Z+S+7MD0F8WP/9D3f7ZgQ+L8MubEGQJyGLHnTP710eI/PyD//3mD3/9GyD9fyRzKLvae1D4mjtFEgZN+/Xrzz80j9s//PXnH7oKRHHg5F+7Ovszmn9m1wef31nwtevH358F/I9FWpRDsfiWQ4tfy+p/1H/7tDjNcPT9fvN58dtMnD/QYlbinenTBL/JxgbI+hs7/vT2N4A/BdCm8x7LAD/+4z8WauLVZVOG7eLglV27AA5ukzyYhTfjBOBs80CNeobMJgGGfe17IfUscRkufvlf3gPzP3ovzIffUTv46j+g7evrwNffQHvzy6eFCYiXdRIlhZMtDFbXvxROFBTtzLiqgyaoewBW7tgGH0FOf5x/zNj/y79E/+uD1Kdq/OVRl5InAhr8Zka/psuCT7Oe5xnOn1p5oHYE98DrAJes9Jxn6WjmMtGUWQ/Qc7ZJkyZZtvATgC+gpI0P2sBun2div/zyi+s08ZfiCdf44lnrGhhs+CbO4uNHoFuYJVHcfikCLy4XP/z6tx8W/734Z6cexGceOigeL68ACeXDTluALOtysG0ujADeHf/hlV//9rIwIFOA8gR8mIRznZ0PgyhNA//d3AeJ/YiRy1c5W4BCVdYtqAGLpP202ISLb/ICpvPSXCXismkXflAFhR8U3gioOkCdb5YsSlDIQSg24fhhAcrog+svbu08RMxBujvtLwuV10FNKjPwzyzmYxM4XBYJMP+3YHjeB0TqH5oF907i00Kb4xJU6dqp4tp58Qidp1/mov06Dog7iyIYvhRzCQ5mUz2S5GkesAlYxnu59OPsc1DKc4AIfvPO+7HHmSun+aig9ZeieSWAU8+u8MpHVxF1oIsAZeG/XiHVxGWX+Q/7AUlnSi8v+C+vPGLwWf//rP9pFvzvGqC5X1ocAJ5Uiy8dhqDE4v/nDmq2DbteG+KaNUVhIWqmcXn6bG4qZ98++1DQxjxYPPLze2vzDl/vKP6lyBIQgPX4X8+dD0+/9jyRESCKD3DIeNAHYQZEmuk+smCO6rqerex8Kd7LxYdZ8RkbgbwAMkBKzZH8znBefZc0BrgwX39vHR5RU/szgIBIX1Sdm4EoDIPAdx0vBVLVcya/3AxSIpizeogTL/6dVgtAHXgD0F8AIWajgpLy6RuEP1ffRf/dwWeHNB95dI9dMYfLTADIEcwCztA2JC3AMxAQjx4e6Pn5QQSokVftrLsLvJV/eN0M6uDWJU3SzrD5tGtQAdz+OH8/NZ3vBvcKhCkwFsiRqgPWfWTVDDg56H+ADABYQDzkSQH6AWCUlxEeBJ18hggAwa/Qe1J83H4p9AzPuZC9H5wVmc/MvcF7kI+/RRLzz8IE0MvnHQ++fx9p37jNtGc0bQAiAo7vq88m4tOzD3g2Got3up//MCT9+O/NUY/Kfvx9AHxexG1bNZ9h+FmN34vxJ4Bl8FPW5nth/vgsnB9fiPHxt5jzO+JPvT8v/j0Bf0filSCfF+gn5BMyL21fAfb6AHvwH7nLR2Je/VIYwXe4BezLGQ9m742gE/hWG9+3gAIZ1UE0b37WymYusQOAmEdxAK74Uvw24ueMe4HgB+Ck3yDBo0kA0f/03LcaBpaKFvD25+YyCj7NM9ksfhO8fS66LPvwBmA0+FfHublY5XNsN/MkCKwPGrY2CR5X7wg5//79mCzeAb57IC2i8qMzzwiLJ16CxiwJhjlvHqXlzxD4VdLneH/H/rliPSuGP2vTjtUs/nPqm/vE31WMr8FcAv4oEvvHEvHAisUMVKA0zKPp4p8E2aIFXUvQPqw+Cw/KMyASgGIJ1OiC5h9J1gb39o/S7B4/nOzTQggAcGfNbzP0VYTnJuQ3QPKMBRADHvDBh8WzsoHkBZrM7plByGnSR+36U1kyEHTZVxAbABP+KJAwF9XHlsVzy3uH40QP0PmwCD5FnxbHg7r6r4dkYOwGpnDLO9jfJ3VZzF0KEKZu2j9l/63T/yPvM2itZnZ++Xlm+eEF1uAbTGcfFt8GLaD0a/SdOQRFl799/nke8uY4fRyZf4Az4OvboW//heMGb3/9g1xAsEcFAHV0pvVdyO9by8dwOKsASLfP/8v49Q3khANc4Lyy4jVdgO0AMD82cy8FA/QAzMH1M8/B2v/d3PEi0sQOaHkBlZAKXS/0EcRbLnGXwTEaoQkPDVwMJSnMIT2PwoPAWVIhghE+AXaHnkP5NIl4PsbQFKD3hIyvc9eYzILNUgF7fASoE3xfBrf8l0ZPDWZzfRtzHgjwVOzXN3dJgJ0S0WzY54eHIdSlzpQ7ahZUL7tL07C1YlsltSbxZKz6JEU8ebjubRahMNriV0aiSGLmHceDtWdKQ2B3TLIi43pp6jtTE4RDofitnEME6K4Oo6Fi4a7YwEWoThuamjieylQ1yRW1Z2SjOu1PVlSheOqMqCIT092Vb91SUJp0os1pVyNHklJuPLzGe3g89QgllGlk3sJbniwjdIfeJGxfXlNkpLG1G8tlfoR2N7emrS08NXCY7M62SxiXg8vfotu1vUyr8eJvqlyxK2mT180GSTxVSaHzabsNkkmhizLaX23HFp0VbG5anwzcYkPTnayosnPxNuN2OBFbSVXzMr5tTTXWkGyF3C+HLXQyOmVoashaH+NULWp06VvuuGxzKr2HCbnDqObOMPSZaJ1TlDXITfRdazcuTYeOtqddJiZ82Q6pYyKCBg3pDdy0jyPOTgd7tV6ToSNLaUw1qTqUm+UgYBNBaamdDlB8tbeyXB17K/MiS76kRMEPvKulyumIlkdU0GmjztPAyld4NllbBO0VUmjPTl+prM3ZeXoxAWaN6iZoiWgXopsUSRp7P1qlachWxMf29ZRDZ1AQhqpufbldU61BsGPLCg4bjXtV1+uJo1W8lTpG6Lce1jinlFAOhpZ21bjZJeq1DLJob8g1AWJHZk5Llm/KFDlpYxXdhZCHlUPtMOzmhqWTukcLpYBaUTZ5LbHXxVZxtpRtQnTsVmV43w/CPq62Y5fEFR/agXRLb2PmJ6IaitdLlLoYb9hR4xkUuZRjoy118W46WCeQt8JOrrak8gYp9iudoNWVth6aIOmCDGWrtVaVIlQ53DluHZbtMfdc28kxKQ6uXRnbWlJ6ux1v/YjEPJMqHo348c2jon631yB5Nx2Iq9FdDkK/l+HRuPEyUfub8x7b6gl9Wut7eLtsaTu7nNBzbKe+JB4hdRIGeLz6Up6tUHuLBmaurbNbzsW3fLvlybYPAhsSrpjF1usV5iYgYe/wPe7hPFLHfhS2m2Ux4ZAHx5eew/xRDlbxxkjFrKFkEsmqMyVd+Ph8OpzW1WZqUn4V1McbWaoCyQMX9G3Byr3qJNVG4RyGSs+sW8gtrxEQhEimjNYmdznYbrYXO3pMykY6eFFLbBL9IIwbNmmqIeACvuq4ei+bg2hpSxEXUUI25GbcIeGlMUODItaVmEMSjtWZqaCYH5dyK174kpRY1Lvuj8J6lEU53NtViAX+vSxLBGdtLDvS8npA2ltwatA+64XEwEam3jgAV23IxsL43K3WdijIalPnqwFDhEzZ66nHK+sErbj18WbYiU5XZ89Ru8wscXjKpVNImgaRh/xG5nU6xUUe86+9MqIdFJeuuvf2HjDr5Rrhlni89HQNoAHf5r42wJbqH1NWvaXmiJeimU+1IE4dS7vdUakEe3VGezyLNxtDDJooyvcexLh0kV/vTnxItm0iEzaUt3es2WMWNeDRAdqIZLxhDHIZL7GjsS865qYauH4E0aR5yF1wI86VxMTfZ1MvDmxtKt5w6yKzUsUUnY5nvxKk1VDHaladelw+MpJ3rxnmdEYUVi5qunamwu59/RqN5jnKbyQtcXChW8K1l5CrMm0z1g1YH+9kvgv3ioUean1khamvLAEeYvqk4rXl7Xhl8Gn/vs5XSKaMkAZPRR6l49LQZQBeBzVP74roC/543hPCkO8pVWt3fGEMYQJCk0+GxMhLP4trZJhikUhl+2rxY15Lu1WoXIRg0pZ4AE09o2LJnrMO7iiQJzlMXD/c+KOknpBdlO3S0W23545P08MyYefw48k0iesUJ9lKyWxmyJtd2Zq3k8daad+EFWrySs+7gbbuI59uFIUbymA3ZP6lPy2HMj6xLnYcKCgh7H0sJZMRSitR8XVTQmmvcGlG5yVZOQfmRaaEDFlGh+uhptN1SNolw19HkWc89bpjKPiwl3A3RihHUZX1aX8J+0I7MTBtJcvrHaWbEPZRezcppr5xsp1jS+MN22xYUGn6QMDIAOT7IVZw2asy0d9XarFDBG9folp4sSOls4NNR0trGvOPZ27LC7uYtocoIAesNNaaHTHc2dZ5V0WZTEN4tfSC+H7Qtivo1J1MccDz6Ropux4XSoVW21YnlEvQqCIIa9kTJjS/2yuMuxqTcD54UB6GpzZhe28pXwhYXp0VXLsNpCkQewMRZVFgjCy9OUhPtjG3trJ8FKWNsBZ9zqHdI+G34qGxeKaL2zhPc1BJ4Au3KkujT247jzZR/HwjikvEiMWJO1zSnO1DeMfWG920uWvB2u7aOHM0v54O3v64lZPziE+ayK+POH1YjTc6jVZMl8OdtN1J2G24TnFUrhz0dne0rbzaniGc0mRDPUxEvbnVBKhTN2PHq/1qhMxjIx4Ic+M0+LJLA9lQAM/tub9Cy816UJ3jjt5gmTxVhw0Mo1A3iLe82XJ8J/ZyKK621kFT6bDEGssdzs4pLhC/3ke0nvNbcpUmIHSW8G2nFqvUw8trY5CcGK2NXZlgscmgFCfes5oVuMuQcYkCOpWLthfParuX5ehoalkw2Ui13sB8X2UXxOBJJ2cO19Twi+uaPqyrslfo5WHrQI7hgUksCgT2ct0FCrkr8HNGYIa7adNjcMplEjbLtYnYByGSNm3n6gppQqbTW52zWY1+lpyUnXLOVhQImvU1WXkE6Hy2Z43OQUc7rI/TcRK5bn2W1gq9RnrY2cT6BmW3iA0zGX5JuDbRMXmPSXF/83vMTvz4FClXsq9xlYBwBCqjlbS7xpW/xLYkIYvMPUm32gmmkPaaXNgrfBFCUuGOBQcFhUwTQRHj/SBn68EuoIvNN1ts3URa3N6z8iTVuuCiOjIckuMlBs2oo/l8cUXkrZo2Llp2G3pImqMDCRWYwYSqo3WM7W4q68XJ+XAuO1Lu19FYiqNlILxZ4emFsa1gczTu+9H3CraOiDKTNWKvQrcm2+VoYkR9cBQRsyF38fGiujLmaTf3jkMZzbXH4261nuxil0u+gextAQLNCttkm1u1LqDDBot166qabXCcxo5waReCYXIltUdXLQ7mLp4qaleUuosz20rtD60wrkOCbFYsue9lrkize0CFx1TplhZJTHx2XrX80VL2uWxte4S9y+n1IJt77mZ56B3aLg87dy3abrE/trtjSwVhytL1XVEKUamgtQOV8rJXsGwVyD1vU2WHo6tmXEo795yN+GlnFDlwCIZfquOFglN1064KCLco7RbcuLN8ztCohZQdsiYT1lHhxg5l584bNxVFDlutPiL2eonj0vYSDYx33BZBQkmml3bTKd9kp3JdKktb3B+ko9SJS5HifRZZK2gZXKIaoLynQHx2bI3lzUs1R8AwXyJKRtRuGCIX7OreicelyKwCCNIpevKaopfYcqU74ygwEbw6Hcg4A22sLZS6WrFZa9kBeo8Ryd07vTSsq24X7Rvet4c8Hw/Xrc8GRBdRaXsrwo2UVLvBJ5QT55566NoM9s66Eya1N0QDvVvo+X7x1jgfZiy3k87IieIGFVX3nHeo8/CGGaRhaDynbZVBOG+R6kJElrMKl9IWCzhlqw32uU2N4nLTtHAnD1Kqn1QSN0tYYaQ2g90dml91HVv17qopmuM2dSJMvULM+YLlegqLpFCfke311jn3zfGM4+EFTpex58c5hTeBApPpuXCoa4YIKssft0a7bdPTZiACwzmEq7x0D6vK4uo7aNzkY8aw4vFE7g9JHeVXXtUj6exlUXLxWYe7bw2uPYuCM+wlQWqWoIvRnM3A7VtrL5EOfWwHAym9y3JEyribeJTV9tlw9WyddS65Fa5ud2s4sbZjhZoRUxlxw1SfjhUyhNaRErqBadANFrvSsawxA6S8izJw6JwOF1FbJqu2XFUmf1wW1U3OhGxqPKbj3DClVhyCJbsWFCdtqMCMxVdjf7oVaRgXJCU4/WHgxfJ62e2YqJLPbDuN7iZQIBiSe6I/Lpf7yTnz9TY7nz0vl67O1GSajpj4xSL51Ani9VBzNpe7jm6WSKitJQC6qOejvEOfuuZg56ogMTtt3I3WcdvvJ5gRr37DK3nFl2XGivEezCNLd0P4quBfC6rYlTK6rrhCUIcIANYpc2TdI1DP6q3SBVM04WCFpfnGobpnFwPMGriBERwHapjEoyhZko5MmvveuVpM0Ca0nLDesiRXoPcI4dbDl0mxieUmyfYSl2iHJZHgoA0WLhKrFcSYINvwUnL3tIpczkVuy7TDanbFXtbu6eDxxWE/+GEbrJI70mLSNa2g1D7ISbLEj8Eud/1BWgoCOtHoJAFX8icrHCsad91To22KcRumzGa1K2q8DwzR2/oaz2/9LXWZKoXs1PWFIwRRLbJtpyZnBjQLExgLRe+04np7wKx0Fx989FQpo2yerpFvSgfIM80tZF9Qi1eIdRIPwy1dcfKhTQfHEQkhGjDyuOeu4oXolxK8DwaLOW717LQdiPOdO6GZv6Hu5tG4qDvlerrp5wRamhivmTePOZnUES2Efq1qN/SYgrFJ34Eh9XIzC5BtS51DA6e5+eqdhnO1cz2DmIwAV9wtLVFdXGqCYOfuqe7XRbbBST5sURK92r2XwsqW8dqlj5nVEQz3CF5YhbdfqczEgIgbu+DI+KJZIRPgjucGzClW3dwm5Hg+11d9uaK9FPMkU4pRjOqZLYQSByPsbVV1KQnpvG4qOmLpm3UxQR0TCntfMpdrPeHOBXFU4Y1dm70t7bEklbFN1XQCZTfBdVwGDV5PtxCLtwDg9T0ZjSMB3c40hugAoSG3FRL0JnCgewfmcs5cuaEz4qLXaQj3tQVzYb0+OemqRlEY2sADVeZFHHctZKEwG5AXtjcu6LZzrNTrDnbjJIwuEuLyomEavDyukCIFIucA+FkridtqU1BrgeBHc03Gu0ALfblQjRteJaetbu2wClP8oOvwiKaE03UfmxuNZ1xCJQdykjhIVkNsDfs6FTJmolHlFY/ylEabUWQdQsevvm8HATB67FvENoZWVTuSApeLu4Nx6w/5XjRpa9WL8LJKoT5fmkGoXU6rAaWgbI/s2pslKVhoby2612sDg1lDWO/P15G1U14maZ1zXWY8FQbVJ5ucLRUMlfJ1hoqb9OyuCq0usXNF9Tx61puxHBjW3fm9uWEKClFqmFNjMOdt14Ee6jlxDZNLl8reRfUbe5PejomZs/TOFKCsgYbLbd9smM09Dpq83WJE2U4nRMQxMrqlwu6axxKXmQS3vyC8A3mCoxYhh+oJ6LyY3uboZeCut1Vx2kCOGDGwpTOQvrYs+AbVE72HePog1Bs5g7ily9wdMSP0xrm4QXPlYJbQ6eWyUnWo2zPAKB5ymcJoS6GZKBMajZ2icCPky+7OTZ6h2jsAEAmUG3gxdev8NDVY0+9G5JqvPGo0VavuXIq8VuUIHXLtDJd2dRZ3yq6eIm66D9f+HqOxb1gErYyTikuVFEDdFd7Z+G0ysB3ZCM2dLM75FfdXR5UWyfp8m3pO16j0wGyP5/UmCOl8J5VlbpWgBwhUymMN6Shb+2W4M7s1Z7MwdIViKh5QQ3Wvg4ntmgS6oWja6GSsGEtmYPGOdQKmu4NCEDC6k5FZMZkm3rc3n4buK9tf3wUYpUMM9FUE1AW8pfZaTU17NjRWAp4c6RhSloPetczQZu0ZgjXY9O/weBq9iQmPG1nRJycaEAU+EPA2sKutT99XncIGmsmvjkUNGjQFa+3SJSn03F7oi+nWuSQjhS9vXQ8rIc+hcH+kUoker9QaS64DPGrR7r73qtwWUO4Wh+fuLllCKRvLI9OhEgoGK6nP7t6FDTqFAFFxQBSDKbF1aLDddrprMQi2veLuj4EHZwKL5AfdpwPWnK6cZvuFWHYpE3gHjl77F18hkXAlN13apijUeC7uR+dzddSigF5VOmnizcmjM9odYJ9Vkr5uKFG/rPdK3m+oyKWPCoRymI4PpBjYAaUe9et92jOm3QeJe+jHEXTi2bqw19t+mxAQ0htKOq2admjxe1y5yeSg9RkvuM4d70jtaNgJwCCZGYemja5WcyGBU3XBmdBEsGzg5748GxHeMlWDkstrFoK0nfqj3wYHuxvL3t+ZR2WDeDnHaKEM+61MUVnkHPDTOK4ZxZNLMW0FpOBUGnWWFWPi47nqbnlmBiIZnMONd6QiK9jflXsfLrOhX2quqR+uU3Strqg6hsSpm/SdGfROyq5hyFNrXcsjNUHog2dIZe81bNGyo4cQNcVQMBLeeEHQa3vjY0nPrk8JY5N3ZonhznHJYSi+pUKkuGXblK4j+nyeLD0gqIbIGKNw2LtJ5TfiWvFpiFU7/3KWpJFj0bTsYs892iG+onwJANr5Dl00pQsYYcRif5ISl9ges4RlNPZiytcSaj0Kz6MptGyRmcCYdGE2a35/hoiryBbn3bjnmXGi3Qg02qdOIOE2tdyGRM/+piRkPQuv6U3VrUC5kEuq8rdLNjxca2+VgiYKjojjFi1iC2rKeulCmkw1blO2TrPEw05joKT3QynWMxhKqXSPnE0YKwU3G/3laho3+UBzpqCRqIK3TQMaidsudw5oR3eyRToY6VMGJVyZmpyqTjs3Yh/3zWR5tX/vLSi/9AW1BG1xsm69QjL5LbbUVsE6d3ebWx/wjI8w0NKp+6l1C6Ekhj2U1PuU3/DL7MJM+Y2tNxulqKLriMCjY0Z0YGkHMtB8hZ+yu6QHecg7fBtrB/l+9HVhKCUkSvDg6h0gcm/VhlRT9B1DHMIKoS6k1sFW3+9xZpio4rANsDQQkgo/CmBQgK3OtjhrlIbN0OB9pbFHNUA2N7WLCWuE6yK7wDqOD4rHdXtN8sIbswMolCPjuBE4hSBh/RqTg3GWmvOSK9HidrOsCw0JbZvcxZUr7lmW/ctf3j68zc9QX8+S/70X3OZHTP/PnmY9H0q9v6TyeCIYOP7nB6/P/6Zcf/3wVnsJkOr57K7Juuj1AOzvntx9/JdeTJhJjM+3x94fBD+fwLdONL9j/ZYUfte09fi1KbPHyyrghNs18xuZzSyqB75/+3DzG9fnzYcmbTnvDJN5PSnmt1ACP3Ha4HUZvR5ofnjzX+9PfcWX5NegrmZtX686ACXxT8gn/O1v/xtZ3vltKy8AAA== -->
