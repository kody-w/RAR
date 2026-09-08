---
name: "rar-cowork-cookbook-configure-analyze-revenue"
description: "Reads an attached configuration Excel file of analyze revenue targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with a befo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_revenue", "rar_sha256": "fd4ba8ab3dbbb62c5205db478d7e7c44d3be5711fa69b159ee2a7235b40f9a26", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
