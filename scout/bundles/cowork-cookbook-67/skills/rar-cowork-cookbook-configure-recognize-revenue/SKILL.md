---
name: "rar-cowork-cookbook-configure-recognize-revenue"
description: "Reads an attached configuration Excel file of recognize-revenue targets in Dynamics 365 F&SCM legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_revenue", "rar_sha256": "08a8e45491f61f745ac998ccd7a2d76d2f5ad1a6fde8018123006600ad5ef48c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
