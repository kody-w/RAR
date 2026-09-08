---
name: "rar-cowork-cookbook-configure-discover-suppliers"
description: "Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_discover_suppliers", "rar_sha256": "7b9f35a2767e80857d483309ebbe8622e6d29d18a65a6a71008d154e4c181c27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_discover_suppliers`. The original RAPP
agent is preserved byte-for-byte in `configure_discover_suppliers_agent.py` and in the RCI capsule.

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

Discover suppliers Configuration Bulk Setup — Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached workbook with one row per discover suppliers target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Sandbox or production target \u2014 run sandbox first since this modifies data.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 7b9f35a2767e8085…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_discover_suppliers_agent.py` first:

```bash
python3 configure_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_discover_suppliers_agent.py   # or on stdin
python3 configure_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Configuration Bulk Setup — Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_discover_suppliers',
    "version": '3.0.3',
    "display_name": 'Discover suppliers Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting',
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
        "upstream_slug": 'configure-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93163706746f1f78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per discover suppliers target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Sandbox or production target — run sandbox first since this modifies data.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for discover suppliers, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per discover suppliers target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting', 'example_request': 'Bulk-update discover suppliers config in USMF sandbox from this Excel file — validate first and wait for my approval.', 'inputs': [{'description': 'Attached workbook with one row per discover suppliers target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal entity'}, {'description': 'Sandbox or production target — run sandbox first since this modifies data.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply discover suppliers configuration changes from an Excel file in D365 F&SCM with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDiscoverSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDiscoverSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per discover suppliers target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Sandbox or production target — run sandbox first since this modifies data.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
