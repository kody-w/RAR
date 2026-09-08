---
name: "rar-cowork-cookbook-configure-research-new-products"
description: "Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_research_new_products", "rar_sha256": "c1a057efc7ae5d966a81eae9c0831d7891ac15e87b049d807d916f0c634756cb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_research_new_products`. The original RAPP
agent is preserved byte-for-byte in `configure_research_new_products_agent.py` and in the RCI capsule.

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

Research new products Configuration Bulk Setup — Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per research new products target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox or production; sandbox is required first.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; use sandbox first).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_research_new_products_agent.py` and embedded as the fenced Python below (sha256 c1a057efc7ae5d96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_research_new_products_agent.py` first:

```bash
python3 configure_research_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_research_new_products_agent.py   # or on stdin
python3 configure_research_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research new products Configuration Bulk Setup — Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_research_new_products',
    "version": '3.0.3',
    "display_name": 'Research new products Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-research-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-research-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '24f3c386f1ee95da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/research-new-products'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-research-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per research new products target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox or production; sandbox is required first.', 'legal_entity': 'D365 legal entity to run against (default USMF; use sandbox first).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for research new products, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per research new products target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of research-new-products changes, validates every row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, and after your approval applies the changes', 'example_request': 'Bulk-update our research new products in USMF sandbox from this config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per research new products target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox or production; sandbox is required first.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update research new products records in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureResearchNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureResearchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per research new products target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox or production; sandbox is required first.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureResearchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
