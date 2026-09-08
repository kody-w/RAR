---
name: "rar-cowork-cookbook-configure-process-allocations"
description: "Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_allocations", "rar_sha256": "8ad63334ad8ce082abce0d3b49352539279898951f72d6265c74012836e4acb8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `configure_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Configuration Bulk Setup — Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
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
    "configuration_file": {
      "description": "Excel file with one row per process allocations target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_allocations_agent.py` and embedded as the fenced Python below (sha256 8ad63334ad8ce082…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_allocations_agent.py` first:

```bash
python3 configure_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_allocations_agent.py   # or on stdin
python3 configure_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Configuration Bulk Setup — Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_allocations',
    "version": '3.0.3',
    "display_name": 'Process allocations Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return',
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
        "upstream_slug": 'configure-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '133b1d3257617d6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_file': 'Excel file with one row per process allocations target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for process allocations, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per process allocations target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return', 'example_request': 'Bulk-update our process allocations in USMF sandbox from this config spreadsheet — validate first and show me before/after.', 'inputs': [{'description': 'Excel file with one row per process allocations target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update process allocation configuration in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureProcessAllocations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessAllocations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per process allocations target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8HTGZ2dgWArHIFRUxiF1IILEIRLrCyQ5i3wQou/77XCR5yUpXdVfEfBo5bCG49+znOef48vub03dx2bx9fNMCp1jwTpYlcdAsnMJf0OVQNin4KlMX/F14ZdE1idt3ZdO+vXvzg9ZrkqpLygJsVwPHb8G2hdN1jhcH/rw8TKK+ceYVC3b0gmwRJlmwKMNF1ZRe0IL1WVZ6zwWd00RB1y6SYsFMhZMnXrtAcWzB/W+NPix+zoLIyRZB0SXdtDC0A/fLu8XNyRLf6YJ2EdyCZlo05fBu0QRd3xSA9JfHM/FZkVmHd4vK6VuwISyBjhUQAyx6t+jioJh/Zgl45MVOEQXtwwRPYkDZYHTyKgvat4+//u3dWwKu3z7+/uZlTgtuvdEvVYPjUy/qq1qzoTJADyyqJmDpmVYVNIB9Dm75ATDF89fPbZCF7xb/+Z/pAAzR/vLxU7F4fT69zX/UvpjlXHSl03azeZ3KcZMMmOPDgsoGZ2q/U70FjiqiD8+d3yiV1eKv87Ofn0w+AIP//OmtBCI8hP309ssC2OXTW9PP1x9mKtXPv3zIyiFofv7lG522d6+B183EgNQfPr9+v8iChd+WJuHis3Zk6RevJvCSKgDEv9Nv/jxFf5F7meTzc/HPZfVu8WPKsz5/BfI+Q9EFdH9MFtgA7Hz7cC2T4ucXD+D6oHAKL/j5l39GFoSxl2ZJ2/2P6P76JByDRADWepkEROnsgr8toJduX2n+c7YVCJh/RxOw/Au7r4b6Z7Qfnv0H0llSgHD/4ssfkvvRBuivi1//qW7/asO7RfjpjQmyBCSt42bBx8XvjxD59Sf/282f/vZ3QPq/JaOVfeM9KHzOnSIJg7b7/PnXn9rH7Z/+9utPfQWiOHDyz32T/Yjmj+z64PMHC75W/fzHvYC/UaRFORSLrzm0+L2s/lfz9w+L84w+3+63HxffZ+L8gRazEl+YPk3wXTa2QNbv7PjL298B8BRAm957IsvHt//4j8Uh8ZqyLcNuoXll3y2Ag7skD2bh9TgBcNo+UKOZEbJNgGFf60D8zx6eJQZ4/Nv/8R5g/957gf3yC3oHn19Y/fkbVre/fVjogGjZJFFSAFhWqePxU+FEAJ5nhlUTtEFzAyDlTl3wHuTy+/lihvbf/iXdzw8SH6rptwf6Jk/EU2lxRru2z4IPs17mjNZPLTxQcIIx8HpAfabyrDDtXAXaMrsBtJxt0KZJli38BOAJqF3TE9n74uNM7LfffnOdNv5UPOEZXTyLWrsEC76Ks3j/HugUZkkUd5+KwIvLxU+///2nxX8t/tWuB/GZxxFUiZcXgIQ7TZEXIKv6HCyb6x2Ac8d/eOH3v78sC8gUoAoDnyXhXJPmzSAq08D/YmZNoN4jGL5wA2BeYNq8KpsOYP4i6T4sxLnCvuQFTOdHc1WIy7Zb+EEVFH5QeBOg6gB1vlqyKLtFCxzRhtO7BaiSD66/uY3zEDEH6e10vy0O9BHUoDID/8xiPhaBzWWRAPN/DYLnfUCk+aldbL+Q+LCQ5zgERbhxqrhxXjxC5+mXuSa/tgPizqIIhk/FXGuD2VSPEHmaBywClvFeLn3/6Cq8MgcI4LdfeD/WOHOl1B8Vs/lUtK+Ad5rZFV75aBqiHjQJoAz85RVSbVz2mf+wH5B0pvTygv/yyiMGj39qYNoF/YeGZ9tn6UIDuFEtPvUIvFov/n9ukWabUDyvsjyls8yClXX18vTV3DXOPn02mrNoM+FHXn5rYb7A1Be0/lRkCQi8ZvrLc+XDKK81TwQECOID3FEf9EF4AV/NdB/RP0dz08yCOp+KL2Xh3azujIFAV2BRkEpzBH9hOD/9ImkM8GD+/a1FeERL48/6gghfVL2bgegLg8B3HS8FUjVzBr/cDFLh4cAhTrz4D1rNvgE+APQXQIgEeBKUjg9fofr59Ivof9j47ITmLY8usQcJ3DwIADmCWcDZE0PSARwDwfVo0oGeHx9EgBp51c26u8DT+bvXzaAJ6j5pk26Gy6ddgwrg9Pv5+6npfDcYK5A1wFggN6oeWPeRTTPQ5KDPATIAQAHJlScFqPvAKC8jPAg6+QwNAHpfAfek+Lj9UugZlHPB+rJxVmTeM/cAixCIDu5M3yOI/qMwAfTyecWD7z9G2lduM+0ZRVuAhIDjl6fPZuHDs94/G4rFF7of/zQF/fzvDUqPCm78MQA+LuKuq9qPy+Wz6n4puh8Ahi2fsrbfCvD7FxK8/w5r/kD0qe/Hxb8n2B9IvBLj42L1Af4Az4/2r8B6fYAd6Pfby/v1/PRToQbf4BWwL3Mg1uy1CVT8r7XwyxJQEKMGYBNY/KyN7VxSBwAoj2IAXPCp+D7S50x7Icw74JzvEODRFICof3rsa80Cj4oO8Pbn5jEKPswz1yx+G7x9LPose/cGwDL4b+e0uSrlczC382wHrA46sS4JHr++AOF8/cfBlx0BJnogD+Zi9xUwF04ICM1tVxIMc7Y8CsmP0PaRhjOYvSr5V2wF10+89WeFuqmaNXgOdnMr+Ifa8Xk2z49k+1pRZnBYzMgEKsA8c/6gvrSvAvMw8ywvqL9gcwCqIZC8D9p/JkcXjN2fmSuPCyf7sGACgNBZ+30qvqrs3GV8hxhP5wOne8D27xbPwgWyFGgwu2VGG6dNH6Xph7IExS1pymLuFv4sj/5U7rs1X1i3QGG3HAGbBjRILz8A+/jPTvuHrB7F9vOz2P6ZFzOX5T/U41e35EQPIPsLQM3Q6TMQy+DBXKt/yOTrLPBnDiZoxua9fvlxJvzuBfPgG8xv7xZfRzFgxddwPHMIij5/+/jrPAbOAf/YMl+APeDr66av/7vjBm9/+5NcQLAvQTvT+ibkt6XlY3ycVQCku+f/dvz+BpLLAT51Xun1mj/AcgC179u5+1oC/AHMwe8nUoBn/95k8trcxg5ojsFu0vFxFEXXjk96AUwijgu+fNRdb1AMwdANQmxI8AdbhQTi4wiOecQaXiEkigdrx3NJQO8JNp/n/jKZBcI2RAhvNki4XiGwD/yIrH2fxEncwwgEdjaug7nYxnG/bU2Twn9p+dRqNuHXIekBL9ErZF18DVYK61aknh96Ca3cpUm4auMuLZgcp8HsK2lkO2/Vcattv6/KtR5vo3SwkT61Yk5NJIHNW+m8z1Lhwg4kBY0MER/bYlPohzu2oxOXDn3/uhmigTanXXq3SUIg0PthOirk4LbJFVc1Mb3rR6rZ7w6QoRzy+9mVevq2rossrCo9sWzX0MPlskFJzWb4w+EOq5cs5+HU5UWzlY9H+DJxIFszbRcmPrwNzjw/nmtTSzQ72AvHIYc1KRTWOb7kpiWJH9H0qtaZF+P5ybRzI1gKG8jurfU6X9PdIWXSvor3kzae1wYUnlmOpytqH8ShgbLN8ph4VVFkozLSU8/RTk+yCqu4PHNSdyc39wVLPvCNs5VzB86I5ISMQ8DY9covKhwKbvpmIxpEeLsuCVgNbzK2Q0xRvLJnN9slkHjQdq4biyfaCuNDWlS8i29vdYzUyZj2WySdXFFMlrB+tKnsUtrRaXuOT6frjZBTOx0gXd/aBznJNqRbsmtHjPbtcSu3k5ad9SzeX2oatoiYOd0O7u2AQxaAn/OdxUs5dPxumu4HsUxltUhVAFZCwK07eDpp0lRcbTX2o8Q/JVy+MW18XNdrVHPVirj4MNXlTBdRDK1rFwsJocuRDvw6DE0bc2FiO7XVAT45TpM4yWRuL6SgjeKlRNMQQ4x8YNs6TUxOy6b7VaeWqG3BtWMZyga5xIR0umHeTqu3J2M6HJVz33fjEdc2t1QlpOu9tTN1q1mVSdDpblOsg1rfSytEvIykJiemVyU5ctoJaUAG08V0a27kpWnVssJmxY8cP7GX9DrtICkc16roWCWXHeV8jw1ngy4dBCk1/Bxxjjk2lIa6XZ3hO03yd35dsLvWrzc1KtWTpKV7+IQtR9WUqrtCLzHqSKQEFSc+TcSNtKQsQtquRVCQh8RmTi2035wu8n5zc9Chl3MTM5ZHe69Iu9QuCnWZIVWcnQ9DS3t55YV9GSVppxOo0R9LuMvW+zFyizV8W9LLYXdb5qfDFE4Mw+L5HYW85dUPmJZIzVa6n64iu9+tboPKVs4EmQHOJ2KXn53cEbYKh1un7fKwjcLWumXE0h627p0vEx2PzJuJcRSv0u4pCY5Ft4Unz4FLkw1MzDmfgp15NplKOfFreWtV1JplTyZFHqkbZ6DUWLIYSKMcY9wJJ6mSWtmWnSN7FoUDaFtsd7d4s6krY+rOcSVv2YseOcqutLPOZiNWSBXpCqF3heMJWR6E7FYXsRg4cadOcqgv00HhUVdEnK7pKixfFWeId9aWzZGHNJnaC8Jgp8CrKGU3iWt3pyUUdqq2rHL0jydtt6lD/2C59nmbnwIOVQyOgaMpuqb2bqTFpUuYQx3cWpurqF3Kt10kc+tLlXBQTyK7I4Lu8xV7X1qiYWzW4pS642o48Mh0Y1gmpy/7+iTZgs31q5uxbSQ9oXb2VhI0D9q4h5tgHzJ1Vx1R5QDLy/2GOIveYAnwSNKQyDpJtBz4JLoiOyva35iSOmBHXghjzXMu2e20rph4VJSEOiXtYYfSp1repxSun2XZO6epY5DJPkHUM9ReCMQVtrejbbqn0ypQGAzCQYxCji/EZNqqtjEhihBDSguh57ZC/PTsnGCSwlk/8W3odKob33EyvYt6NMyXIF4lWofhwj4lruALnm5H3U5rQyYgMazcSX2qD564wVXD6JrTNbq008QOm/QumFhHDRqm6K1+FwbDZDVlRZ96GTdZT4yh2GaN9eRVl2rYYnfKXWG3M2Hh/moX99qJgXVYDCWM0XQ3rpj60vFZSgRG7i23ZO/ktAIyXxrLMOabRJGm/HRm+axeFTAtkUSy4ilrzWXJBus9MTvZRN6jpI5GkWrIHLOCuT3K452pcc5EeWbLeK6iZ5FwyPIcKjguPyxvOo4d9Q4KCr46I0p42e2PKVmn2pVhlrkJ6nopb6+RyCAe7wrQnazW8tRdBr/jeO4aLMc1ZFokJPW35fIqZyh0uGEC37RD2gx2Vtzy0aZaOmF5BFPQCMvNi5Rml7weTe2sZcOBwcSQzg1O7oqBX+dlj2r7cLSz/sxJML0uxpLZehdm8mWH02T4LEeb3WkwU4+69hjHXGFFsuIS3vUm5GvUkhRtNeFzf6MfjhR9oXJHP4DSo9pJdeDFZRFaGJHuBD6OzYt4ZD1hfUmCeNP7kBrdi7G+uYh1jntcNranpUdt4SgyqLA+pJmOdHv5IO5wskdOp/VwOcXYHk2ygstK8VyJlgwrm4N9qavtKkJQPmqHUCZkhL5hiEiN+/O1EGX9dFKWSGqk/KaNxmF78K9SQ9XUtrsdRWmbTr5tY3xOjZKF72nMCGiDgQo9RKlzzhBG7OAwG+34ybhOOM0F2cYNQw9CmOteTNu6vhVX3S60TbArjboaeU+VjsZ9NCYZr6tdEkvuSQ3PJWPk3G6bi47mjeieDDc4i12SzDG5W3Gmhaij8RigziG4pRdnv5pEuZ7uDi9UA6zeY98O0umwPE5TpXhX/i753aFgPepyocEcYMsbC99MZ5k/D9Seu9IGL0yVxSc15BgHDS7RbDxBCHeXi6QQrgd6mWeNyu6z8oJJezPDPbbBdg6fQNK1qDp3rLkks/oRPmwTCscI0N3IWpZg8jEx1X2RmAGMy8WGP0VrdRJtczn1bJMhxEjmmkwX2wvnXJW82lqqvrta1LbZZ6eIzg5IeYYdvJZ80tYkhN4zKauAonhErqKOyyeBY8IBC5EyvVyYTWJsqjWAm4ZPQL7aKiwpEnTz7tdlqOJjJCqb45Z2N611X5929l0QkXC/QTOME6ydEOMsNBlUpQgbNCj2MR4IwTrKDXebh1ic1rfjBWSnw6PA6obdknJpkPpWqkYDp0Xh7JUsGWa2mmaN03KjULDn5FpFZ7k1YFsusuXAjadRjw40rnVcXsl1ymdUYE78zQoVkNY3CVLoROl79MqgOyXio6SSPe1AJlkW5DDouLqAFVG9RX1aHBxET9cuvLzefMph8rj3aiHfKP7Rqv3W1oRI1PKtLZ0tXhagdOyo4Ci5qmxaLd3jbhtulsGOE1b25YBqp/0Bg293nTghEDlBjkjt7WVcDAeJU4dUQDSTk3K3uthed0ORguNLJM3cs8CVTbND3JOXTnzFVSUF77tkfcswSfALWuzutcQnzblrjrgRGA3HaXSpS1W1Pke8Te4D9SzWy13NJ8ebZw6Sj0aXrTSlLFqZcKwzbQCZKKDBbidYulk7HXXZpWEYF3FP7J1i4Lx8e2VqFg7s28FOE6fax3eJYPtzoB7XBJEgbA1yDN/pgWuncePAA7vsewUt8cGgcYEVAhZnXWpDDbx4WnN7gz6h1q7SyVtsiSsplA5n9rq/+aGnGJDdRhIxLYdrTW97E7SvPipwhm1Unrmk7a3PJgWSrdwtBYmCSfmFt7dGer0tk3Clw1FV2sf0XOMbqbXN9coRukpWbxdBqUzK6BXfZnMTUZHqwuM0b4+au9KWKTNyArYl90p6THHigChnvSNOJeHsEqnWeJAV+hCsRa/cShSB3ii2tWSBHiTE4AlvGJPeYen9KYtcpfNiGVbl8rxMi74+ybdWpwuHtwTfnL1xLYa83cBMVUYst5KaUIJ6vPFNL/AcZ2S5htmbrUOYSx5TingpMH1xyFtH4AToetrY6+ORa0jE0ss8cnxf4+nsDruaawv1QRGMy4rXWbnSyEqCoZDhMvdEbba+4ZTluqyH6zQE5xuvCOrOSF3GPDFBm16IKKq4U7xyBsqAx0iKpKBVtPO6Ik5hbVyag6AGpY7nONWnKrWDjxZF34gupzc05Upr+QZzRW7QJDu5jXHBbIfSgv6K7C+qWXbm/h7qNb/OIFK5t0RwQ4n1VLvcVnVO+lkw6sEszI5aBdbRvlPrXQcxrSHenTVOXvgDShfjmasLaWnVgarwYVEfa1KiRFnjoltomHuTzBMatFB4QkDyEYrTI69eJY1zi8Li20tdyB7WKYmCi8uDnlxJmThT4q69XUbQsV0x0HaUjNjoeE+jSQNL1nE8qHQVkxY0ZTFprJfkSG4urdfUISLiUcMZ3pWSpWkv3Nf5hQvud7xQThRsjUzKRPkKElCzPtctvtq6F1xvGjyTdvWkG1Ke7EHWias9F9l4uvf807q173kPV/JtJMwGXlH9mOJC2MQhOglFudv3MpIdEuqSnivL58txZYtnW4o3ouj6B941b+keqaPNxtQHUT1pgZMo2T26tkU6SoMEIwPVxbHSV7ecoIe1dCbSGF6BALLZjeETaccnfriGMSpeW8fprHjnMxi7x+XGwrYaolveTlrdEp+sKcIlV3KB7i8sT3JOfnMwcTeCSIgUBD/CO0HX75JhlooLK4cJPVemkhx1wvIzYQID59XfhlTnQTs5MSYRCVBG2triOOA3Kb7m4llidAoM7cdrc+3FhC7uVTqM+EEeoHAzYmzkGb4FhjVtfVLL/moWZVLbdyyHkgmTtnxoRJ3lw3vSCYAt79Kxb4fLVoVxb7yr4ZEkiYt1z45tChvevdvKrH8uLMe7T6F2O8NBhd+ufqHxPkGthO3YkJsJzlMGOez7XEHyJVGNUj+EOQchVgIRh1WWwTa+vwNZjxNS40K9c2z0vgqgegXLGXm/Nqtd6V2lQ26pTn5UuBsH6aRc5xOjCYGBSCsCX4bhjt6vDogMpsSDEvaIdlsHrh+HkTAWdBC7jUw1kHHiMRs3cczX0Du1NNJB2yo7Ut8Y2d0sM4m/mZBryNuyvuxstcxXoX3nV7EPRnUiPKSOwpFmzYQn/1wVWA4zx63JX0kboskSHht16+jDcA2n5RJCbuAmcugQtQqS23J0l0JAIQMY/rAJul2cu0RZlKTY/qQjBTMx8tU4qXixs7QthG6XdBHubMFyghz0+0e+dDV112NXiIrSEVKz4hoimg0RsBut9ueiysMDwwVdarmk729xROxEnj/BRn3zM0UILmtoK12VFCWO+2CJaFgvsx0Erw2rm7RI39LLemlZVpghRupdxwD1tkng9+1ks0yTS/pYgwGJPKve/lin7rDWQPxZJjkR63oX6xgkmWkgpPVxleKTdsMxaMPYpLpVQDGQxW2tisL1Tq7iDrWdUFAQMRH5uGkM/yKFRq+d3TZ3zf5qX6wY3p/X+CAxe2TbjvCmbeDw5pVhK47CtsATm4Q2cZgwPRdjp26MVHxINa3RdluHETcHDF/n6rLcUvcxybPNHV+XF+0CH1A49DY5U0cpcVRTneXuFbl1g93eJo8X+kxGq5247qoVs1bGnc65gQKXOePkRYjnEKRITYPew9UIrUk2WruJL42o6/DLYB3LPtPwhCAUh+FGHpkyb+v7ftkYjG34e1k5LAk6GF0V1s6hs7kUlkj0+1alUVbl75VwvRR12q2StZpl4f56Ez2xFbHOAmGG+A1pxv2JcA5NVt3VHqe1Mr73SX0gt15ASgRI4ot1MqCjKHQ6N2I7csX5OgYDgHacYX0c7LuV63YNikRNe9hoVrdMvepyam3cJBqZe8Siw4bjpg3TZPdV7ka86ICxJL5iqB8Ne1FYwiFZ6y530vkLKWzuV6l04sAmBNKRyuzmiTJB8Tl6visDeTlWjXnTvWXjBMS5128F4txABh1C6FbEK5oohA7GNSzG/JBptsx6V+qXiwDEJEx1wx8RloUcBO3bJgj2EA41eTbQNNxtaZsoJGKzv1oRI1f+rRWzUWvHCcxGKezQWZUjtxUa2kF9r9grU/keSSDsvaqJa2EW92i5U2JvqUOOuslcvSIDjIf5S6kYdy/Go+x0awTv2sQwW26kEJWuBCzeE2sibwdqb3LeAaSbw4o93HBrL7K4cZ1HVbzccYfSOSoWdhpWu/RqGfu4XJnGsJfKy0aAi+s90Y7Rfc9UqH5dN3IHZ23fydfGk83txck8dNe253TZycF4Hu/HTczIA1MjhHr3DDKqhNJum3Z73OhbwhMuA0qnKpbtj6oKhceDnh/zjSP30nK/jyQEXLZuT3Yw6OLWW6N3QI/O3UH3mQXCsUEyB1qv7oHJF+6YTx2JhQdJOmft4bJhBBAOI+6aZn9y7vur5y/p6cBvjt0xPx5Nz51ovffxa3cddJk8c96KVoY2USdfgFdktkHWIAw0vSJUcy+GK4yqY31CZA20LoWPbSyUW+2mHKuds7zWu7XtVUND0cSU70zZRa1eRvUGV+cOm5Pla3nJFdm96fcUbeCaUm9L2Tzn+f0sqJKzUy4FfAo0SkciW6G9cANtlli4ouJpD1NwgGNFykhx0LWYwrhut/cNgiQyrMf0lZ5NznkIAPg1Rd8HvK9BJXM7eeXmavkJ6Ndv1xXllw4naDKzYqM+bt0zdrtzhM92zTYYoQu36yFMnZBbSAv1ZX300kRbHai1tStEpPfwZRnprmXDm6GGgGFFmjqZGJawVGoq0IWWRwZyW44S/Z45r720sDqsgqFo23QQm0hXDMZDES3yRumRpUFDDZ8OCDyuGAT0ycdzsHLXtmqtUE+10PKWV5mt+25pHZSlakEtPxYItOT9+wE/KgB9th2yGTc0tuYYL6SqOCfr2EUQ0+LVs+D7soMqGoGOJopFO4McR2jVYiuUb0x6P9gEjTiZ24NF6CoQfawKE9Q5J254GNJLSQaCo8bYdboTe1jVq3B+e0q5WMpW3ZIFKfD5zmCplbQiC/nAWidWPcpnLt0t8xWq4iSYEu+tSZyzRkwCZS1Dxp11NT9l6gpXmPgUZiLbZzy2wqZxKSUU2myufooMV2vTLwkuaPanCzre78RV3wd4FuhTibJC5YggmLBwa2nCXTwlaL+TacvTYBG02PHa2Q9Ek19CAbUGJdz2J0U4WBUHEScOgafpsqckcbUc9B7HUYJB9p5oaMvpfLzVwXG79Nl9fD34LEVRf3179zYfzL5Opv9nr8XNR0r/z062nodQX15xeZwKBo7/8cHr4/9Qnr+9e2u8BEjzPLdrsz56HXT9w6nd+3/5OsO8dXq+Y/blNPl5bt850fzK9VtSgBaia6bPbZk9Xm0BO9y+nd/TbL9I+P2B5ldu83ng41D5c1d+fr4J9za/Rjm/shL4idMFr5/R6wzz3Zv/erXqM4pjn4OmmpV8vR8BdEM/wB/Qt7//X7h0SN05LwAA -->
