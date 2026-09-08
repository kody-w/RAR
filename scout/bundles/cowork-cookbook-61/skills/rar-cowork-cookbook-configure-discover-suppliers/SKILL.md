---
name: "rar-cowork-cookbook-configure-discover-suppliers"
description: "Reads an attached configuration Excel file of discover-suppliers rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval, emitting"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_discover_suppliers", "rar_sha256": "7b9f35a2767e80857d483309ebbe8622e6d29d18a65a6a71008d154e4c181c27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
