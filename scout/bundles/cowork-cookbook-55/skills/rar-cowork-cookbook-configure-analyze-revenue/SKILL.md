---
name: "rar-cowork-cookbook-configure-analyze-revenue"
description: "Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_revenue", "rar_sha256": "fd4ba8ab3dbbb62c5205db478d7e7c44d3be5711fa69b159ee2a7235b40f9a26", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_revenue_agent.py` and in the RCI capsule.

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

Analyze revenue Configuration Bulk Setup — Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
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
      "description": "Excel file with one row per analyze revenue target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment, sandbox or production \u2014 sandbox recommended.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 fd4ba8ab3dbbb62c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_revenue_agent.py` first:

```bash
python3 configure_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_revenue_agent.py   # or on stdin
python3 configure_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Configuration Bulk Setup — Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_revenue',
    "version": '3.0.3',
    "display_name": 'Analyze revenue Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo',
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
        "upstream_slug": 'configure-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af89d2dc5ea5060d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per analyze revenue target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment, sandbox or production — sandbox recommended.', 'legal_entity': 'D365 legal entity to run against (default USMF; use sandbox first).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze revenue, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze revenue target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo', 'example_request': "Here's my config spreadsheet — validate these analyze revenue changes in USMF sandbox and show me what would fail.", 'inputs': [{'description': 'Excel file with one row per analyze revenue target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'name': 'legal_entity'}, {'description': 'Target environment, sandbox or production — sandbox recommended.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply analyze revenue configuration changes in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per analyze revenue target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment, sandbox or production — sandbox recommended.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; use sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
