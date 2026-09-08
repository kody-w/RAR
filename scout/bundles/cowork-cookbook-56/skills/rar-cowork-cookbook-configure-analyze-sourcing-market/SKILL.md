---
name: "rar-cowork-cookbook-configure-analyze-sourcing-market"
description: "Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_sourcing_market", "rar_sha256": "0cac817944228857c9bece93b2e9e3f99957243c8ae546af219a80f6ef16f74c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Configuration Bulk Setup — Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze sourcing market target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 0cac817944228857…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_sourcing_market_agent.py` first:

```bash
python3 configure_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_sourcing_market_agent.py   # or on stdin
python3 configure_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Configuration Bulk Setup — Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_sourcing_market',
    "version": '3.0.3',
    "display_name": 'Analyze sourcing market Configuration Bulk Setup',
    "description": 'Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be',
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
        "upstream_slug": 'configure-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '478ec18d29c0078e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze sourcing market, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze sourcing market target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be', 'example_request': "Here's my sourcing config spreadsheet — validate it against USMF sandbox and show me what would change before applying.", 'inputs': [{'description': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user has an Excel file of analyze sourcing market configuration rows to validate and bulk-apply in D365 F&SCM, with approval and before/after output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeSourcingMarket(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSourcingMarket'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVrLmX9G8N2JsX6qKHUR1dMSwCJAECAm0IFdHmX1fxCIW3/7vc5D0Vtlt9+3bEfNpVAsCzsk9n8wU/Ppmd21U1m+f3wzfLhaSnWVx5NcLu/AWfNmXdQoOZeqAfwu3LNo6drq2rJu3D2+e37h1XLVxWYDtbFVlsd8s7IXTZSnYb2fj5H9syq524yL8mNt16rczjSAOu9qety3cyC5CfxEXC2Es7Dx2mwVOkQvxfxu8ugjqMgd0Fnbb2m7ke4vV4PrZIogz//PibmexZ7eAoX/363FRl/2HRe23XV3MMrxuzzxmHWbxPyx6O26bRVAC7aqqLsGaD4s28ov59CH7U5zmofx3Wo4PlPUHO68yv3n7/PPfPrzF4Pvb51/f3MxuwKU3/qWVzz7VNl5aqw+lwfYMEAbrqhEYuwDnlV8DOXJwyfODxevsx8bPgg+L//zPtLfrsPnp85di8fp8eZv/HLpiFnjRlnbTAoO4dmU7cRa346cFm/X22PxG7Ab4qgg/PXd+p1RWi7/O9358MvkU+u2PX95KIMLDXF/efloAA315q7v5+6eZSvXjT5+ysvfrH3/6TqfpnMR325kYkPrT19f5iyxY+H1pHCy+GvqKf/GqfTeufED8N/rNn6foL3Ivk3x9Lv6xrD4s/pzyrM9fgbzPaHQA3T8nC2wAdr59Ssq4+PHFA8SAX9iF6//40z8jCwLPTbO4af9HdH9+Eo582wPWepnkpw8P9/1tAb10+0bzn7OtQMD8O5qA5e/svhnqn9F+ePYfSGdxAeL+3Zd/Su7PNkB/Xfz8T3X77zZ8WARf3gQ/i0Hy2s6c0L8+QuTnH7zvF3/4298B6X9J5pFsDwpfc7uIA79pv379+YcH8gAaP//QVSCKfTv/2tXZn9H8M7s++PzOgq9VP/5+L+B/LNKi7IvFtxxa/FpW/6v++6fFaUah79ebz4vfZuL8gRazEu9Mnyb4TTY2QNbf2PGnt78D7CmANp37uA3w4z/+Y6HGbl02ZdAuDLfs2gVwcBvn/iy8GcXNAvydUaOekbKJgWFf60D8zx6eJS6DxS//x33g/Uf3hffwO1b7X19o/vUdzb8+0fyXTwsTEC7rOIzBisWB1fUvhR36RTszrWq/8es7ACpnbP2PIJ8/zl9muP/lX9L++iDzqRp/ecBx/ES+A7+eUa/pMv/TrN95hu+nNi4oFf7gux3gkJWu/awUzVwVmjK7A9ScbdGkcZYtvBjgCihj4xPqu+LzTOyXX35x7Cb6UjxhGl8861sDgwXfxFl8/Aj0CrI4jNovhe9G5eKHX//+w+K/Fv/drgfxmYcOCsbLG0DCjbHTFiC7uhwsA44CrgXQ8fDGr39/WReQKUBBBr6Lg7lIzZtBdKa+925qQ2Y/YiQFChUwMTBvXpV1Cyy5iNtPi3Ww+CYvYDrfmqtDVDbtwvMrv/D8wh0BVRuo882SRdkuGhCCTTB+WHSN/+D6i1PbDxFzkOZ2+8tC5XVQi8oM/DeL+VgENpdFDMz/LRCe1wGR+odmwb2T+LTQ5nhcVHZtV1Ftv3gE9tMvc5F+bQfE7UXh91+Kuez6s6keyfE0D1gELOO+XPpx9jloMnKABF7zzvuxxp4rpvmonPWXonkFvl3PrnDLRxMRdqBpAOXgL6+QaqKyy7yH/YCkM6WXF7yXVx4x+Kr5i/cAXrxaHf53rQ43d0UGwJBq8aXDEJRY/P/cMT3sIkmHlcSaK2Gx0syD9fTX3ETOfn32naB1eZB/5Ob3duYdst6R+0uRxSD46vEvz5UPL7/WPNEQIIkH8OfwoA9CDPhrpvvIgDmi6/ph6i/Fe4n4MOs84yFQGMAFSKc5it8ZznffJY0AJszn39uFR8TU3qw1iPJF1TkZiMDA9z3HdlMgVT1n8cvNIB38OaP7KHaj32m1ANSBIwD9BRBitjQoI5++wfbz7rvov9v47IrmLY+OsQNJXD8IADn8WcDZH33cAiwDsfDo2YGenx9EgBp51c66O8Dd+YfXRb/2b13cxO0MmU+7+hXA64/z8anpfNUfKpA5wFggP6oOWPeRUc+o92aJAKiABMvjAvQAwCgvIzwI2vkMDwB+X5HypPi4/FLoGZlz8XrfOCsy75n7gff4Hn+LIuafhQmgl88rHnz/MdK+cZtpz0jaADQEHN/vPhuHT8/a/2wuFu90P/9hKPrx35ubHtX8+PsA+LyI2rZqPsPwswK/F+BPAMfgp6zN92L88Z8Axe8IP3X+vPj3hPsdiVdyfF6gn5BPyHxLeQXX6wNswX/krI/EfPdLcfC/wyxgX+YgumbPjaD6f6uJ70tAYQxrP5wXP2tkM5fWHkDLoygAN3wpfhvtc7a9sOYDcNBvUODRHIDIf3rtW+0Ct4oW8PbmZjL0P80z2Cx+4799Lros+/AG0NP/n4xuc4HK55hu5okPZA9oztrYf5y9o+L8/ffj8GoAAOmCdJjr3jf0XNgBIDR3YrHfz0nzqCl/hryvWj4H+zeMnc8fuOvN6rRjNcv/HPPmxvB3heKrP0P/19lEfxSO/WN9eKDFYoYqUBfmgfS9Hv2hrLWgXwGH2e6z9KAwAwI+KJNAj85v/plorT+0f5Rk9/hiZ58Wgg9gO2t+m5+v8ju3H7+BkWc0gChwgSc+LJ4lDaQu0GJ20gxBdpM+qtafypKBsMu+gugAiPBHgYS5mj6WLJ5L3nsbO3xAzoeF/yn8tDgaqviXh2Rg0AamcMoBrL/HdVnM/QkQpm7aP2X/rbf/I+8zaKpmdl75eWb54QXV4AjmsQ+Lb6MVUPo17M4c/KLL3z7/PI91c7Q+tsxfwB5w+Lbp2w82jv/2tz/IBQR74D+oojOt70J+X1o+xsFZBUC6ff568esbyAwbuMB+5cZrngDLAVx+bOYuCgb4AZiD82emg3v//qTxItBENmh0AQXEtd0lSjMEgWHLJUm7jOO7PoM7mM/4eMAwDEljBO4ubZ8kKDvAUMZeIgHlBygV0IQL6D0B4+vcK8azUCRDBwjDYAGBYojn+QFGeN6SWlIuIIXYjGOTDsnYzvetaVx4L02fms1m/Db0PPDhqfCvbw5FgJUy0azZ54eHIdTxMdgZlQt8IZl4DDeXY1wdMA+BsmuneIe+EDwuZae7M7jrU86tyCa/aumph+htLIUXah00Gyi907v8kG8rPnGM671lJ3dtrXN3d9FzXaYL1dD1ZX+VY2vEA9SOjW2zRNVcxNRkeawu8W6FnqGbsr3ahXkQxppI26FqytsKh+kRhcXj1RHP0YmP4zOTrh0J1STrHFVRjNhE1uTiKikPE+1v8F3cr0SYgbIgHgLIlZ3l+TZNXrim9lejEFqrXo2Wtx/O28yajpfTpJxTYxxKpTKgk5NSwWlF7tjcJEIZIutzt6KnETvbl5Retd4hW5+ulZIbZ9IoJHNlkKcwY64eoe3IODiwqG1MR0tW0KV/qcdll3jjRRuWneNRgQ/5induN5mxsc/7k5PtXBTt8ktMojGbqXRxVE1c0Kg+vt360h2PeIiGd5fM7gUZcy2H4By7u63UNq4pT66QwadSMzNF+3IvQpF1y+V1SnUtUQ5b9HxcMbf7GN5tZzNKGRl51f00MpozdMCOeU2bZHaMU5SLckyyD7SZsFfyMqKxbN1Ox3ZjRptLyEdWcsopY7Pqsu1ly6CdRLcHgh1FVrDZcNxHml4P3FLFW7mbhLvsYo19au1rGaa3S4qusuP+RkJZuD+IdbU+1RebkNU15yrj3SCroQp1Rju12zxjhOGar4NbNjHnXcb3Y5mfKuKWjxR+hGvlTBkyle7yPtrwxq0Zb6Nw9Ki0MXI9XwWrZJ2db8FWNRPXjWiS2ox7BFE63cpdOwzyG27F/UHgc/+gT6av5KvohgwgLCaZL8X90Cb7DKvZLaIJPpt1+PVUI0Zqkagr5lvPSi54VqHaPrjyhS7KhJ3sCGdKeT02m8RfI9ecd2hkFeCl1h90kY7YURquyzzyEkQfsTqQyPPGy07NUDQkW0SF7cuU7eRnCcmFDD4xqhBrfGrDFi0OsHyudjxj7UhI3cC0AEv5xFgWrcDrdZBQjn6vaHg1LqWqy4ReSQsp3F5MwRo3omKdRgop+2worqY47fsN6V6lmh9uakJyLHH2nI7VfAtdGTDFVVh3OIopkSOru4BiKX3dXaWzw+83q0w5+tzpmIOEWOsudzVL1krlvc8vdTZZHfHVVK5QgvO5fk1j5FLesChpXvOzLOONseTI/e3OoZBz2E/etb7axq7HwtjVwm2S2FJm7U7rg0LxG4UZp1HzrorscjklJj1y0g5oRkr3CyQtd3JOK0MdVe3AFHhOQltjuZ0EIqBi42ZJkUPxZH7kht0gc1fRCo+Hg8S2AwdT15wzgupIkRgkqaoyJuaa3Fg+tTZ7Mz3a60IOFGLcU+c2rQ4t25XytoFk3o0OMbw62w6W6YmZogMIxTTchEepFqHe6pxtuTKZnh261hUtcVvnUR0zJaWWpz5dG/vthOP32KKLEc3Ko54EG8KDCn1oyzmBozuLInv7HMcBy6D78URm5Y6G/VAQcZwXwgFv1T1WquehHCRrOaBba32pRM06XsotgipS1NkDIotyE+NbZlvgdRkPqSoxLppFbGJwBBxTd1Qy8SmuxANy3SuO69ElM8GtOxQb6nACSd4LXdglxWY03JLoar6R13pwD3b3Aj5wS1++3EvNl7ah09Mxs131SCFaOLzz7V18oltVJJJllZF73NvuOORcrnsBQVkvyk4KrxOYPtByxx1cozyrd5dVRnXDrY9jRq7WeHPNyT5MvLi/1AxFks1yoq4yn0bZGh77ZlXsqs39cuTJZL+1zVEzK0SjRi1kq2p9WXt8YqX7bnNXNhWX7m0MPwf95mZuFavnyuGM6QhVXbjTmOOtXhPyRebj0NnKwvkUWPrpNh7LjpX3F7Hz8mFEkpzHE0/Ik5MUYBEayBsM3plhdHOrc4bxbk96u3JVokaQxqanaHLpums22Ixk49D6YLId00myYx4idrplNEzW+xsMSThC+jA/EPCAebdT4ZunUe0nnTw0+z07jRt7KbfjMpWliBd11L5dhG1onae7y+3Wtm3fG7XXTu59JUOJ6Tu3m0GIB6HYYx3ByiVxo64H7XTVQ+9k9nlpcnEYc3K61fdEFUZgcNw4VcYrbJlIUthMUCrmqx2XF9jVkPqTi6dsvdS8mtwWV60/s/QOMkUANF1+SsK+ufZ4mKlMgZGTC8zSSTVzb9UsbynUB7BxCHlQ6FenbLrttpaGh4Ng87UnCMUt5sVVAx0Yl6zCw2678gtiyviVvB/WPcctw3plrM/GUdYgBXMi3DWbvQ9SOOHU/T70GVhmT+n62oQHq1fLdXpjBa7RS5EtjyWGCqPGUvsJNbzh6Ia16PEFBFmdKrelI9Spxq/YsjqcelubOuPmUTDmUuMmBeX5oATVbTqt4z1i8UpGl3c+LtbBJLKarYvemrzVbr4VI+8oMue95q+X6cE6beV8U08JDM+/mG/O1VHneATf8YgiasF6TNBloh/8+4Ef6404OP5dOIvcCkcmeWTq3RgX+9s1psScyKeVHKqBYJyaG97UjFdNK1ZJ1BWfReCwOR46pIJvZ3PjGxroXa6XDgu2+krvL8jo2evI7RSHPMTI3YzEwB5uoPusdzGH3aP0tMUxQg57aT0VeWdcT5rhaevGMv2rlPlxHiDUOvYFznBZTAYtS3VqLjczixmDW3emvgq0oTLUdWGZZHI+H/IyC0M20/yblRoFsbXO15hFY8UsVr7gn+F2tS8QO6S2KxgaYe/ADr1Mrypr6rupw2yV2w1b+LTHZZTJj45DBWeVO4wW4RTXNoZ20RptVm5MInfa11PLC44BfTwtixLIdzcRUr8HqivBA7eqsGQFm9zmFPg9knKp1lUeX3qH+rqOlnls9Mlx5Nb4ISkRxMuqa5yBWU08SOkavYVWOead5ao53UMWT5VpNG3kTdf1aG55J77a+3kb91orkYl839Kb1FjJAsnd3ZoStryWYsN6tLf5lXIM5WyQhJlcdbNdrkOuvu7M6H6AJEZVS82WN/1xiVdT23lmO9320MAfe2UT36oIODS09vi9zzdYt7XSO6EQGwiGabKPAlHpt/kUqOauRHyEud+R4rgEYBSsr7AQV8eQ5JapdDAQjWg1fz/St6BIVptTlY3e4VjxYut3jMWuDBtfSxtB0g7TBRsjaecom4tEqqJsoMoOL0hW3WIn/sLexPEEHbd7YQeRXbW9Yc24bavEIc7LE8dzRHy9XPb3YmwdOfWgBrRM7FqIN+ywXikXCLlQqTNSym49Vkh6kQZcY+4qJ3FWLwwZFdUrkKIjMoQu0ZrH9FoH7s7jhoIm6mLDXO+a5hu0eL7yfHG5gwRWxq0mGPIyNndLFgptc7UiOfOoXS/yhg43/vboO6KW7kLGS3zIXvUClQn8EuG8OnV2nLy9w4LYYv79Mk1RZB/LBvRUUCgnNW74m3zvAEiLpptL0Nx49txY486qVnsWv6XbTlDY9KxCA97FqxbhaJ6SEQO6GcvQ32Y1R7GR1w2BgV6k3qnE5Wk1iOeN45n8RDiEbJURGa0d0Etrg3235VUIHNeeycQRj9ie354z7tyfS6rt2U5VYWRbuJB0Oivh1CnrWgsBjjVlse9cxlIKqzORLYItFZIcW/RQT/UWQ+krpwrludZMCwOjlHY7pHmJOnQtIbJw8NHbvmlh4Opzx9ATCppQDJ2cFtQIciUayibbIznGSwmhKmuvUkEJXffoxuT4Qxw1Vn/yWNAHGWEknjhQcv2LoLZ0zm88ZFrzSLu2J8tCCzBbqN4I2voQLWNCim5bllbk7ORy+roQd01LsSV2OVcwv+xWjrPBWEy91US7kyA+NZUVfb9t9W25afnq1h6CUxQKMsWbQSvLVqxZjTbpFm2YNA5Glxz17pe2XGHbtZeG1k3t79wc5e1q5Ch86nYK6wXEzuiJU48ss5DrKGQHSgNCdMpZlpREH1CeVNkdiKD+LBd+eq9OS9DQGLSfjzC0Kar7Mac3Q7bh22SqM141TKYhOwkTc85RhTEZBOkgrK9xs45ALU9Q6nRrhHURUJ1KR427Pu441VleIyiToCLS7KvvW7DfmLsTqgQr83g0YmFDCEZjDD20kTgw4kNVnvKZmO6rsFesDJWjTEuS80bLM7S0eWhAihWina2wVixki902eLhXTts2uuZF6WTHMa3y7Cx6WiCAMOfWGwGhxhKCFQGGb5DOHq3OzWLxwKtbzT4xeMNykXKfLpZ8OV/pWJBWcXOyLdc/SkLU7YLKcaQj4Rn0SjGNkF+tOJFUJZ0alrsyYeubZZ4lJvJD0jtdpo5ZJ9tauirXmJEJeAv3zBHWaLFyNXlb6tUZDvPx5HpKYZhB2rqCKl5cCmmRLBXkbcev8Qg2z6YUKEgibDjsMKJOf9hcUUM6tQWk9Cwjn7XUv202kJtnETdlFo25ByyUuiuiRfleYQuc6PXIIViOts/Ehu1x5miAwcCiAwIWwLjBImcUZsXKjgSlMo/qEYsQoUNBQx6O0FYry4FS7WtMgOjPTFTXaz5fXtMG7C+rNi1i3yOqboiK3Y2+Hg0NYFZ9tK93MtgqLkaglSdCdnENIvzaaxzhUmrit0GJ0AlFbkwwT++IYDuZ+n0JO8rh4uXUEJMqLQ910ulbjKfIk4SYXXJjmP259HU0Ey61GVzlo2J3y3btHhXnRslL8VinWNIVdCPCwfFcw4wiZcXEOAD5hiWd18uB7HbhhSYJZtLN6ZhcEYirqQToXh+63EUrvElC7zDZSu41iO9oEOanvVicDMfEENM75Uv6shJOODxsLxgT2hSsnR2fTvikvwsHTFpyqSXJWkWpHH314NqH4fACD6dalOziFOiYDmkQezk0rcPpy2VU+8fJDDNMkSp/y+p3pTlLhiTnPqiKEiHhzFYdUKpwLXI3IHtpVTqSv4aikmHdtO+IS5YUsHFNXLu1L1V2bWj8JA0GKBMYIhdWHHv1RvX2Ny2/kM7EyStPtppxaQUwAkfAKxZaJXLAU7vtWVjvD/QdWtJ1WU8IHofKjYhcvW+1Jt8P10hIU7vGlZRFYODNjQ7VV8/BbxmeK754cDUfro6oUNvZMLY1qW2DE83kEk7ErHWLj/ZeWMUHXU4I4LhubCjVIeJNuOXb9kBGg3cQNmI+XBmbarPKp9n7KZHVW6PvpcTHrNTHmVw8QeH5uFTvXKLi905x9/dBL7YraC3tsHXmXrLK4HuJo2y4MvWWV1MwPRmqdakpNHLxTMvsrq3cRhJu4YrcbZDgLAohx9XGRhlKZ0hpAqqow7CVW5rVChMBCd2ShpZHGz1ATSZIhgyFqXu+hFZ6eNf23nW6esKkUcQwGkvQ4aIGbOxDOPXk6OodMRnKezrbp0f8SpvJRGNJyhJr6LwddkfvRu1IV1EPmr07ulo2qYm+P8dgFkFrn2LuiqmvD2R7UhmfyW7NGepC+qo6WT1FDe6mEVd42vFq7ZZXwsOINTV2bAT5Pm7lNeiz8dNp0Nubgw61I3sSt7OXk+Ps6dIuC9D4t1g83Q+KSgOcUtKzVLrWpLqy6at3k7pa0HXX8/FY7ruwWTo7whJTAaZ0ak9JHijhnc7pFjUqYDI07D2EibVcy6zg4zx+uvY+Q9moMtI6hRUgeyp8KtRLilxkvZkm2M68KcEo8na+QmflzvTiUkrFditQW0K5c2ST4PzZxx0Hv3iQsIIPgUSf0OV+n95gh2encGKUBOnIPO1ww724aaHZObutAiM8efGUL512mVE1lvrqLkPrYsvVu1Zod+YYaFt69EY6kJdjgkvnOOnhUQm1Ye+CvBFQ7hYF526QL4K1OeQAom/6fZ/slEAZoZ5NrFM/yiRZ7mMalFxo5N0C7yQ+l5fhcYzKJQlvJalUEZ+iGlEuhO3udKLlsksZ3zW4peRdHW1qoK1peZtgXbduhXc0C3CwdFYMIRvOVMDWjSkUEo8oivU490Jiit+vo5Nn7/E9TpQeWQtLp4tGdRozyisDIcEGKJp2jIihTnqaskARdmNzsS/XiKn8KVtjjidFSjsJsS7mTJc79vFKwqAPbxuMzG+ePp7OWwMTWp+MckOnl22insudvUlUnxkxVdamWsXw3XEJE2MMXakJvRmDNqQkfBdANyIJp9RNBMbxDYh297hOCghT1iLo0BHWMyrSWFW+cj11CFLT9b1sqtbuIsNPcV8qVGsIOI2k1frcThUuKDXqsTDodfxO0i8oCUdnpYdIj1rWvWrB1XJwG8hmR3YcDvGWEaciXCGWlFg7BYJ9eAlwXO1xKjZEr6p7Lgv0M+IGflu1inekXTojO/KAgFHbPvW+rvh10XUe5hlkJbR7t2Sii2cQUaLXSLFb6rxgaAKqCcUeam8uTBu0tmoLzh8gS9y0EMmN2D2Y5NwiFDeN96jKEpdNscY6l4aL0HQuV4Tpb0vVYtY8uz9TZIKAXnkH7fnNTSYKV2FZ2pPqydowHZLTQc5J+REUVaMYWhQUJV04e14LNSKz0jYHWhePulvqIXmk0SKSqa6kRxtaVvTdSe/traFzzfVoRvMp9gJ6BRg+4OVYNjiT9DvUERVEkRtTi3o+L8zphhbO5npUxKOHIWLiVUytL9GMZLEEkwv6NBVnC7X7MyRBfevFLS4xQR7mkOTbFyLBMgvDJ3WTb3W5AyeBhTTdyHgIcllu6Qpv4Y4sj6TZCYKx8nl2GzmQeditkF486NxRRESoEGmTciUhpsscry/GPiXcgUaqgsBC2jKQ1Cp3ckQdhdE4TH7iGhC5v9QHuaaXA4bYxCWAuoCWfEXf73Gmn+jCUHyQ9GDew49CZRHwpbteuMso9+s+xrtKZC+qj6xt9RYR5y1cF5kF6zjeb12u22uyG1TMLjiAHDlsVmKcLY9McYA998gltBCbN+9K2N6A6HBI8I23y4+rPcuyf/3r24e3+dnq60nz//yVt/kR0/+zJ13Ph1Lvr648nhT6tvf5wevzvyHT3z68gRtAoufzvCbrwtfDr394mvfxX76qMG8fn++RvT8Yfj6Tb+1wfsP6LS68rmnrEUiTPV5dATucrpnfyWzm13ZdcPztw85vHL8/nGvLr5U9WzIu5vdRfC+2W/91Gr4ebn54814vUX3FKfKrX1ezlq8XH4By+CfkE/729/8L5Wn6nSUvAAA= -->
