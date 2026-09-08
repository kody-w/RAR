---
name: "rar-cowork-cookbook-configure-manage-procurement-spend"
description: "Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_procurement_spend", "rar_sha256": "2296c435a75e55e869091072c4fda9012285270053b5cfbf09a169e93d1e9fc7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Configuration Bulk Setup — Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
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
      "description": "Explicit user approval after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per procurement spend target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 2296c435a75e55e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_procurement_spend_agent.py` first:

```bash
python3 configure_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_procurement_spend_agent.py   # or on stdin
python3 configure_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Configuration Bulk Setup — Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_procurement_spend',
    "version": '3.0.3',
    "display_name": 'Manage procurement spend Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '739ecbca00efc4ab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per procurement spend target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage procurement spend, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage procurement spend target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of procurement spend targets, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes with a before/afte', 'example_request': 'Bulk-update procurement spend config in USMF sandbox from this attached Excel — validate rows first and show me the preview.', 'inputs': [{'description': 'Attached Excel file with one row per procurement spend target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply procurement spend configuration changes from a spreadsheet in D365 F&SCM, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageProcurementSpend(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProcurementSpend'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per procurement spend target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWJrmX9HcjpjMbGyzSgJ3VMRISIBYhMQihMoVTvZ9ETvk1H+fg6RrOyuzursm5tNcO1NXcM67v8/zHsNvb1bbhEX19vlN9ax8wVppGoVetbByd0EXfVEl4KNIbPDfwinyporstimq+u3Dm+vVThWVTVTkYLviWW4Nti2sprGc0HPn5X4UtJU1r1jsB8dLF36UeovCX5RV4bSVl3l5s6hLDyhrrCrwmvrDorPSyLUar154nVeNi6roF1ZgRXndLHZjbmWRUy/w1XLB/E+VlhY/p15gpQsgKGrGha5KzC8fFpXXtFUOzHmXNlswOzP78WHRhB6wsyzTCGgBn1XRzfaGVh6AC33UhGCn7flF5cGW33jAWW+wsjL16rfPf/3bh7cI/P72+bc3J7VqcOmNfrnqSVZuBd7pu3fq7BzYnwLZYGE5gmjn4HvpVUB8Bi65HgjH89vPtZf6Hxb//u9JD6JR//L5S754/Xx5m/8obT4bv2gKq25mk63SsqMUeP5psUl7a6x/cL0GycqDT8+d3yUV5eIv872fn0o+gaj//OWtACY8wvTl7ZdFUQF9VTv//mmWUv78y6e06L3q51++y6lbO/acZhYGrP709fX9JRYs/L408hdf1dOefumqPCcqPSD8B//mn6fpL3GvkHx9Lv65KD8s/lzy7M9fgL3PcrSB3D8XC2IAdr59ioso//mlY058buWO9/Mv/0wsKGUnSaO6+W/J/etTcAiaAUTrFRJQkHMK/raAXr59k/nP1ZagYP4VT8Dyd3XfAvXPZD8y+w+i0ygHpf+eyz8V92cboL8s/vpPffvPNnxY+F/edl4agR637NT7vPjtUSJ//cn9fvGnv/0diP4vxahFWzkPCV8zK498r26+fv3rT/Xj8k9/++tPbQmq2LOyr22V/pnMP4vrQ8/vIvha9fPv9wL9ep7kRZ8vvvXQ4rei/B/V3z8tLjP6fL9ef1782InzD7SYnXhX+gzBD91YA1t/iOMvb38H4AOQsGqdx22AH//2bwspcqqiLvxmoTpF2yxAgpso82bjtTCqF+DvjBrVDKh1BAL7Wgfqf87wbDHA5F//l/MA/I/OC/DhdwT35rgCXPv6A2x/fcD2r58WGpBcVFEQ5QCGlc3p9GVeCnAdaC0rr/aqGVztsfE+gob+OP+yiPLFr/+18K8POZ/K8dcHHUVP7FPow4x7dZt6n2YPjRnMn/44gH68wXNaoCItHOvJN/XMB3WRdgA352jUSZSmCzcCyAKYbHzIBhH7PAv79ddfbasOv+RPoMYXT4qrYbDgmzmLjx+BY34aBWHzJfecsFj89Nvff1r878V/tushfNZxApzxygewkFfl4wL0Vzv7DVIFkgvA45GP3/7+Ci8QkwNOBtmL/Jmy5s2gPhPPfY+1ym0+YsvVi7QWgJ+KqgHov4iaT4vDzLcve4HS+dbMD2EBGNX15kh7uTMCqRZw51sk8wJQMyjC2h8/LNrae2j91a4eTOxloNGt5teFRJ8AGxUp+N9s5mMR2FzkEQj/t0p4XgdCqp/qxfZdxKfFca7IRWlVVhlW1kuHbz3zAljofTsQbi1yr/+Sz8z7KJFHezzDAxaByDivlH58zBhOkYGycut33Y811syZ2oM7qy95/Sp9q5pT4RSPaSNowbgACOE/XiVVh0Wbuo/4AUtnSa8suK+sPGrwSft/MtXQv5uBtm2aLFQAI+XiS4shKLH4/3lqmgOzYVllz260/W6xP2qK+UzYPEjOPjxnz9kCsOnZnN8nmnfUegfvL3kageqrxv94rnwE5bXmCYggNC5AIOUhH7gOEjbLfbTAXNJV9bD8S/7OEh9mV2dIBH4CvAD9NJfxu8L57rulIQCF+fv3ieFRMpU7owco80XZ2ikoQd/zXNtyEmBVNbfxK82gHx4J7MPICX/n1ZwCkC4gfwGMiEBjAib59A25n3ffTf/dxudgNG95DI0t6OLqIQDY4c0Gzrg2ZwWY1zznduDn54cQ4EZWNrPvNshy9uF10au8exvVUTNj5jOuXgkQ++P8+fR0vuoNJWgdECzQIGULovtoqRltMjD2ABsAqoAOy6IcjAEgKK8gPARa2YwPAH9fxfaU+Lj8cuhZvzN/vW+cHZn3zCPBwgemgyvjjzCi/VmZAHnZvOKh9x8r7Zu2WfYMpTWAQ6Dx/e5zdvj0pP/nfLF4l/v5Dwejn/+1s9OD0PXfF8DnRdg0Zf0Zhp8k/M7BnwCQwU9b6+98/PFJmR9/AISPD0D4neSn058X/5p1vxPx6o7PC/QT8gmZb4mv6nr9gGDQH7fmR2K++yVXvO9AC9QXGSivOXUjGAC+seL7EkCNQQVwCCx+smQ9k2sPYOZBCyAPX/Ify31utxfcfAAZ+gEGHuMBKP1n2r6xF7iVN0C3Ow+UgfdpPofN5tfe2+e8TdMPbwAYvf/W+W3mqGyu6no+94G4gwmtibzHtycWWo8T4e8PxfsBoKUDGmKmvsX7usWMjtU8jkVeP7fNg1b+DHIf/Tij2ovX38F2pqwnEruzU81Yzl48D3zziPg7EvnqzSTydQ7UHy3cvPPOD0zzgPIZsWYSKWeC/ie884j7bDygZrDVA0QJ3Gi9+p8Z1XhD80cb5McvVvppsfMAbqf1jw36IuB5APkBR57VAKrAAYn4sHgyH+hdYP+coxmDrBo0NYjan9ri5V1UFfns0R/t0Z7O/bDmXXUNHLaLAaipAK++kgKi4z7H8T9V9WDar0+m/aOu3czJvyPj1yD1Iu//AFjqW20KihvcmIn6T5V8OzD8UYMB5rR5r1t8ngV/eIE/+ASHvA+Lb+c1EMXXCXrW4OVt9vb5r/NZca7+x5b5F7AHfHzb9O2fgWzv7W9/sAsY9l7Bs6zvRn5fWjzOmLMLQHTz/CeR395Ap1kgp9ar116HFLAcAPDHeh7MYABIQDn4/oQOcO//4vjyklCHFhiegQgMo1YOgS+t9dJbLj1yRSEUiqwxh/Bdi0JQDCOX2BpBlri9dHzbRygLXVEehbuoR/nOGsh7QtDXef6MZquW1BosozCfQDHEBcnECNclV+TKWa4xxKJsa2kvKcv+vjWJgGFPV5+uzXH8dpJ6AE7wqlt7RYCVHFEfNs8fGoZQcHFtj/wVqlZeIUlbwcmVQaqT9pIS3dAuW7a/RTHFNaOxO++9QDVuB0K77S2mSZvCZTZcxJ8y2r+tl+O9KAoddXHsRpvXimUD3hbvqJBOkLNK1WR/po5rQRNWOra9LS/by71Y8+pKwAUzZ9Ub2SQXxRi1Ey91wqQKOBuOWVHBnXXtiHLiDam50bfEcMCRxDgoR9PyfbPUhfLG3xMVWtNbb8yEVI0RFZ34o5kmd9FVUSG3opGF9lcpSZCVTuDGZUwQxfJPhu8PdAe3p2gpIGbJFqneM7RqJxqOrkhf053ozNeMkpuOqx6CZUu2TJVA7uWQsjVzqnz7KO3vENMlKKl1RmZWJzHkx/iSic15FClFF5PuslqjBOxX5PpkiDvMy4l2ckP41PGQuDOavaxS920llei12a2yjXiPFEvBpZJJmsPkSzJdNNW9TrcjgrSaorIirklTQl+iENtuGJOZJO4EzeExKehuijwvK0ynhpuWzqx1s2RudaquuOMeu1hMGWOJdzUYLHN9Ebl03BKt7scrnu8MZ4yGc8J4F2Yn4sxJGzsmS9TIuqikzrMXaMMzLG/Yy1teiZHtKkLDwnWI6MdjQeObMyNGE4JgK1+HEHktyaQ7mUNpaJUl8PcQkRX+wtxbuiQkRrHGLU/dmN1wu/CHVkh3Ycy2W7ge0RLp28KN5XGHGqF/79Xc2WJKanlW3HhryUbStXvYUUZemaVA01k3ZghTXNeHUl1pNq1jUnSDFGEQLsaoihIXR5x/GuQzy5ZuubqP1WWCUGPiMLowdW0UIcsenLN0FOtDn8swO5rM0WCxIw1O9ZvqjBwJ+mq7qdEpgqbxYqeaJRoffddYoroiAFiLNh0kbKcLexuv6y0FO7lJS3Z4do72laCp2xmmVdiul6E0stsbefWCyMInEz2FJ0AJ0x27ni3S0Q5T2ewh43Znjxdt2/P3jmVM9tp6J8w+UX1m7xx4v4S5TF/TsrSV4Vwb3ZNk2Ce0rOqODEALDiMEcx3pi3iVWoIdXXm22yBdwqLJ2cKInNHaqFBFK82rIiwuY0Nnm+O2lWLs6Gnr8xoKjq6ZyppPYpjdSUU0BpFA3ka3SY6YXZ2ZPZmNHB0dLmjGl560XzL22Qw29bowQgeWekaCGdsksb0RbNZ7k5WGvR4I5FBPJyYuZMU7Q/qFi22YKotbO+g16nLW8ax4bXEwFJRSyYOQ3ENye2Gg5W3NRe4qAyFe8RqxNhp1n/Jsf/U0X76uCFHpQMhQKC/YNWRdHMsZQf+7t6vE6e6dk3XSZuAkRpjlha2PtOWad5iS+oC/YvejTvmxnDE3ZdkuTcLjt+k2LwrNUCvcN/REQ6lYWDtnJ2gutYefRN1Rhjs8mom7Jltb506UqZr3rXlLCjz2AvNyTD35wErs+aoWzr1dWc1kdNVBwGlnZCIvXJLazYSueuQqkk1t4g5BIZ7iHCIj7vLRNVjnvPVTBQ2klOFrGt/i7GEXlBJshh57TpuAbXYh6YnsEpOl/SWMTuZtrTB6LPI7HWFQQx1CDSIi/paCuirpIZFYyEHTcBOrDAHf2QJlY3iKijQysYAt1vZpmHJO3KbyFonvo5AGvhc0GsyPqq9btj5Wu35P3HCNQ9cA2tjI6fenQolrWAe2YkHMET7OeRCvVLzUVuqWP+x0FaqqluI2lqtzK35lCzLA8DQ+jGZKQDa+OWRCgK4P/YGm4kidmF7aQ6GSWQNNgzLXvK5LesnJvOm213sJYiF7hWXOqsjd4Xy+yzctau37VY4C7NLsGfGwu3GtLm1ifuAZkPhjtFPR1bTanQx3uNe9cGYzBreoiU6zFD/q8nGTbXZ7AkE4wMSwKdxRR0SrA4sKSI0k6IlNzf5qaUszqZZTp55sZC3jKebs3UC3yibOEfoiro7CcV8tBQcepzPL7KJ639ZtyU7w8nw+Deu4X1vygWddBfb9qy+k5Z5sU60xB0gcfKNqx6SQblneZeVtU9P5nsWWJz9YlhepUXldu9kiL5RqIXP1/sBrdyHDpmHrTM55zcsMUa9SIcrI0HFXeBi0Rbius6NQsquJO3vJUNjnw3Yw1X4UOO5U6+dNv46lkNJ2fLg2x1jiNqsblkF9pO05fsguBGp4w7LwrcvF6QcboYTgNKEZfmPpkB46ylDrHvP91E5aeVkYHda2eJ1O2n28dTGxP++P7DkD4UBKDXOp9lQIIYlAXn+A7+cJNMBkZWxiRtrKuzQc1Ryd6OgDcN9fD+kumXTTbalr76IHjgc0V6o5S/M97EBxICvRHrJNwwyoS8T0pi8xW/F8x/SVeNpgyipV/OFgGOh4T7QePubGEcOXITJwKU3vN6VAYjGNKcLUHaHJ1hWyHtVRvrdec8q84TQIUYrI5joQA6vz7+OZunDHoy4qq7u4KgKBOLS4TDMsmpU5EXckbqGZcOF1ecs4PKQSh5VSJ7eAhZXCbPEi1C9phjSdFlS7lF7HNz6xSz9lDGfJivd5uG4PwWYgtpw+4vaqW2a55Uk1sTFFdlNK50HjbbajQheUi7IWo+hci7l1usguQzDw6WpFh6uoYJHpNHZPKPhoI8ctaVyFcYUHqMiIkNv4FaVvkSE/Hj3jfmcjmNvXaZYNXurts9O1obW84EFK7tTkSfeLB49kasgGxxgMHdsZzysDt6arg60aNMqwglArUTJJex1eapu41tmCNx1zXfvqaSjGQmELD4pPhF7j+/PJUbBJYA+k6MANO+3j+j7huotS/tJnWn93TDemm3ksi52UfRdu0FpyoiXZrbfXxHT9jcedAfac6Yz0OApzwswkHI5kb1rNbuGcBdi9DKsDDVeOdmeU1TRiobaU9knOXop94BpqMPWpIJB6bV+C7lATcb2/HXe3KsriW02WkucgHHNjSENldRc73pMAK5gxo440F3c8kFh1Ja+E50kTq+3pXN/D5bY9k33RXYQMHZWo81Td4ke3GxxWsreok1bsyqAksTiOHD8Vho0sMdgrsQE9+OdQMJmkZBwE8Vc0h2wJ8nanqrE9oPjOjWGYIqJ6uzF1zm5Y5i7d/VLBq7Vm3WSaoi0JgPNF2EehrO44/hhR+ao8Ne7QTUPOCHdsDC9WSZ8Tx0GjHRKdUbOUNkbqDBy37S6brK5T2k56/bgx6uVuKtdbWcCioNzqfHpwe/usX+qN2sJacz6yyrWpbWls2otjC53fRnaW8oG4zOPospIygAJZSTN8gIcEoRSba52floneqEKV1X4W784beeMoXpkR/cXa1xLOHUW9LlkLH3dXx7vtCqUcbY2Cm2rkzGo6nM+rzvLvYMZVdOcMJ5G5C076zjcDFkGp8yrrjnyyEYnL6hjlY7yNkqVGmOtqzDUm2+H6FaIv5/PAT6BHPIIId2IqhlvzIh0PtSEjUGgdtvZ2y4xXYkjCSlesu5cwrnbOGNFy/fVJaBUmjAVfibKdfd/WvLhLsGjSbmAO6DLjrPS61d5FTuDGiOiT5BANtr40csy+9UzCNnXcqYISCXc1W2+teHkituY9XCnmOg+uhohFKEi+YLsr2cX320N+NtD75ogLOJhrilx2/JVwbrmtJFL9LXZTrOsyGfVpTj8FdEtOqFQc1tQlbnL7PmXTVT7WhJSxXunguAIPOjKxGtQGhqtxl8qhoDRetozTUmsiMCDxRGVZTvlTTS73d/EYq2SKRYcdIQnhNsrSwkSWN+vScpjkqGOwKyyyCJRLr/C82PST5tVYSwudaLIdvDqeN6qz226yIhCP900bhrx7vqYmmZYTRgaOfR/wgg74mx26hUCel2QORod2sPpOzjE6jaVELhI3Sw+wdE1aVe51O4iiOGVFbcsSsXGnYsNVVdhbM5Bd42t0bcfHPDqsD5KQtCghDxV+OA/roOlD4nCElLZApAuJwGmwbQlUJu8mSen3izvoB3DiLtx+J2dxo5/21NKoj81okRAbQdrOHpSlHKuTZewrMTU8x+nz2MLBkhWpIja33GhGuOGCanvbXu3kdE1Gp7E4hV4ipHvc3JxLGR0sTNnxlHyMjuNNx8syT8AIjp0aAZxso9VePPLbzIXyy3HYOOKahVv5pvuCjNMy6+rOHh+L5fqy4paiSbCNW+mlXBmEdleU8+WEiKkadBsw3aNyWMAqj2qxf8krMsTXFFZYGLZeX0cPhjHcHwVHPIByvRwc9iBV9wghsCEBh5qwnjBBI3pAEvI5sMVrZNjsmUy32brbJkfJq3euvNlIBQFSZWiiBKaxTNxguXk3Tvma9Q+VIFUQ5yx3smO3weBA1yUNe0aBIvdDB2lIhOLbEiIbCx1o6MLHDbQKNTDMbfYroVO12kuKvl+hZ8amTqu9du+W3ubUj5eQ3d/1xDbAEVNj7JMee+0O2xwULaYu5bYTdxlCVbhSW4G5n2JGXFlQ1WSGhGPnu6jF032Uz4A0BFljNH40qGNf8nljDXdRPY8RPFBunJyvVxWFzqfCLnM+1BxFPwmIuN3ZmbiNWl0bVJEMELsZy0oT87aF8W3Ob6mYM4/4rW5G8xDkJ+zqrILr0WeuuXOGYLm9dFTb3307N5Cw6vGkIXar3XpnrAe82rkIJid+64hjdjLukB2iPdT7fUpiVxK2paFIMWsFjmMxdrJwduWsDnZIXFEPAydLJoWnqjgqhRPfN8uzYuSyGtYXWCOlNh2uo62GmIh3gl/Co7W7TLe8oYe+J/MTTmt3wrJNGS7XQ2XIwyX3w/VgNDJq3TP05o74wF115BydpJuuwI02LRXPpPa4E9EKi9gjfrvdawwA/84Sj0tU5q3JrVa0zkLB2uG8SawpOtXNUxjKbBNmG8HjdUn2TueKwFAYDjoqqtxDY5jVEgLRx5HjyBJMHcAwgFPrftLVXObU1C3P0G5zWDPdJepPSeVrG2/i4dFWDkylS1sqOwZyecYk6ZyzO2IzqszSUDYSv9JOa2NnZrxZT850C8zyGBg7j0qLEzsy99g9c3R8XdflsJ44bs87tsTi9pLgoPF6HK0yJ6ujBHfjHsxX8+wmQOvdsU92jTjJUyBp625ibSFw9Un1GD0Y8KAVW9dFKpfbW+aJk4bcvnJKLfsnxcLiM5krUJIa9xt1PWGmvSfOhhqTAXvbRJ6/61tsZ6YlclsTGR8IdNmcl2Hpaj3PZMONslZNeve4vrrEnHSvT8oKzwHhyjdoou9wrx22rB/xmYaIy/aAE/nhRnOsyNmsygj5IeFjPE7GfLuPmYgDBbxj2ZV6wfc4I2K2kGbLaH1AeheRknJV09Ym8i8BwDsDg0GH5b4Wq6oMeA9koh4ZweivnSDRWLnEoTaP1xTukVlC5Muev/B9vl8T17q7ZbCzC4/b7Zpd+ddO6lWz4dpbo2Mc5JvuWFiCGzbVkJKsGG0IGPIERFZPk8s5JfABq3NBPoEjy4E4LfGdL0B1ZZ2d0lZ2dHfr+MJeiscdiaHoEoy9xtHDScqgr3sWXSFbKiguYKS1+6yoyBN3A2NxJMXx7Upcc5NsbpXNUaQqmzRaaduu0xr8Trtg0rhxSZd1WBpYps6aFnnABbYgW7ZwnU4mJ2ejbC4yrim+B0au7W0Dx/HyoEPjWUcTWe4pgo64Ir9rg3fXxBss0ZXXb3Fw7ofywWSqyeysOm9tf7AbPK8aXLxUmHkjfC1DJ67ZHJtCvaG9B/sQre0hwEv2nr/iCDZQ+UlmmXZVYRAeOV4XbjsfqwNhgzQab1U8hq5wmg7aq+Jf64ChXGMr3JRtsLwZVYBe8eW6a4RyNwixdvQo7LwXOFRBrhvE9rThYp1GgsgSb5mhgs9BirttBTqVuoNc8Dq/GvHDirC3gjTm8FhAVCQRJdmJ6w19DK87yU+MkBaP6tByB2ZwtoUpmP6oaAKbTiWkS0f1dkDRmPCPZmZZ4FBxUqDDniSSmKjHYdWgFiTsbJdfg2nHXOHeelPv6MomsIgb/TFvzTslX6E+xM3NcedON0jYnvcxKmUKTuOronPbbW364XgYR5Q4FPB+qmNsyHYrvjnAQhVE8JF1U7MlWzzH0vVWj28NYu2hUbodyKstUxBGRngOykLIJjuzSgS+gWF4Z8qA2NjbAa4FTOqtAB819rxaM4kpc7l6O7ZeyYAzVOZM6Ma+ppkdNGLncKsxkk584mhXiMJF7wZtQVU1S7m+xOp1tDZypZN8cd00OVTqOuymllKXS7MNPT/JVY5rJzE4EJSL+aWxmpb7drluz3yqWRWn3J29hENVevB9DD1XJiSBUwnl1bJ6GM/kIJYbMtriEz1KmzWTpwRMdoE8FUNxo85IclUMlF7a27Hm2Mm+rkpU5mLYqbsgtFfj/dx7V+oqNiZprlFc5U4Ida6YbrUpmazjmc36MIlyf2MtnnWaDPCRHYv46mS3KzKSkJMmlmiMlh45VArRq/ABSWtzWxQae6tdARfVA4S06nIdpLU7rLbcdjOMIyLtD/WeHRAtyCnYF/sN4bKnHubp2p78brJy3ZS6/ML1BurxlQxGisbF2j1Fn3gFhaIV1+rX3rvvVn2fQNVdJvMuGGRwOF1TqZH7xHXa+AgqZmCSlRq4Lh1i1U4+y+2mPvHzIHEHcmI3luqcsOriuuVFcS5nvHIuTdehF8fwO7XF/J6ErNZc+tPlvl334FAJ48LasdDWHsnBHlRYqpGKRaBbKA88QspIDJYxKYZHWT4SB9zdu4NPwnuO9nvIMuPzeadX+UgivaJtlD2J6tczL6Hd6qQFiG64Me4dG36jDRiTj5kTWzsppC6igrfyjiz3CVLAcu6p8lLXOUos7BrB9hjsd23oV+NeOJEOQhGohbf8KSOt7bhbGfHxss6veYWHzsQdjhN5DUp078pSIJjOqiZPq2XFDS4F7/LpnmhNzwiePyFHv5GShEbk6nhauqRMh2oP7yJd5r07lw8pxHU+uTsRBhJNoEY2m7+8fXibn+e+nnH/C+/bzc+i/p89Ens+vXp/bebxTNGz3M8PXZ//FaP+9uGtciJg0vPRX522wesx2T88+Pv4X78nMe8fn6+xvT+Vfr4Q0FjB/I73W5S7bQ2OuF/rIn28OAN22G09vxRaP4wEnz8+GP2m8vtzvKb4WlpzLKN8fhvGcyPr8Sr5/DV4PQj98Oa+Xs76iq+WX72qnN18vXUBvMM/IZ/wt7//H7lcjmynLwAA -->
