---
name: "rar-cowork-cookbook-configure-recognize-revenue"
description: "Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_revenue", "rar_sha256": "08a8e45491f61f745ac998ccd7a2d76d2f5ad1a6fde8018123006600ad5ef48c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_recognize_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_recognize_revenue_agent.py` and in the RCI capsule.

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

Recognize revenue Configuration Bulk Setup — Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
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
    "configuration_file": {
      "description": "Excel file with one row per recognize revenue target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; default USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 08a8e45491f61f74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_revenue_agent.py` first:

```bash
python3 configure_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_revenue_agent.py   # or on stdin
python3 configure_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Configuration Bulk Setup — Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_revenue',
    "version": '3.0.3',
    "display_name": 'Recognize revenue Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0b7655ff0785f56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per recognize revenue target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; default USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for recognize revenue, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per recognize revenue target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo', 'example_request': 'Bulk-apply this recognize revenue config sheet in USMF sandbox — validate the rows and show me what passes before writing.', 'inputs': [{'description': 'Excel file with one row per recognize revenue target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; default USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update recognize revenue configuration in D365 F&SCM from a spreadsheet, with row-level validation and an approval step before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRecognizeRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per recognize revenue target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; default USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
