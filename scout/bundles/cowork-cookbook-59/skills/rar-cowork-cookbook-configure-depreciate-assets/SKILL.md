---
name: "rar-cowork-cookbook-configure-depreciate-assets"
description: "Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_depreciate_assets", "rar_sha256": "9cd3ac03ec9762e3126ac9bdc2a93ff4f79cdf1f04efa16e25c921ceac3ce037", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_depreciate_assets_agent.py` and in the RCI capsule.

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

Depreciate assets Configuration Bulk Setup — Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
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
      "description": "Attached Excel file with one row per depreciate assets target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 9cd3ac03ec9762e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_depreciate_assets_agent.py` first:

```bash
python3 configure_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_depreciate_assets_agent.py   # or on stdin
python3 configure_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Configuration Bulk Setup — Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_depreciate_assets',
    "version": '3.0.3',
    "display_name": 'Depreciate assets Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f8814a0be76e3761',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for depreciate assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per depreciate assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir', 'example_request': "Here's my depreciation config spreadsheet — validate it against USMF sandbox and show me what would fail before applying.", 'inputs': [{'description': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply depreciate assets configuration changes from a spreadsheet in Dynamics 365 F&SCM with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDepreciateAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDepreciateAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5kpIeasqIgGMUiAEJMQyFmRZhTzjAD51X/vg+69mXbZVe9VRH9q2ZmS4Jx99rjW3ol+fXGHPq7al88vRuiWK8HN8yQO25VbBqtdNVZtBt6qzAN/Vn5V9m3iDX3Vdi8fXoKw89uk7pOqBNv10A06sG3l9r3rx2Gw4iY/zFdRkoerKloFYd2GfuL24Ue368K+W8RFyW1o3UXCyo/d8hZ2q6gCh69YBMdW/P82dsdVHt7cfBWWfdLPH1Z3N08CIKRbhfewnVdtNX5YhUUC5LnvNxdxi+aL0h9Wo7vcfIqt67YCaz6s+jgsl695AgS9nzwmfQyEeCFYG67dqAdueOrYAmPDyS3qPOxePv/8tw8vCfj88vnXFz8HtgDjd2+mhOw3K+mnkWBnDqSDJfUM/FyC73XYggMKcCkIo9Xbtx+7MI8+rP7zP7PRbW/dT5+/lKu315eX5T99KBetV33ldj1wru/WrpfkwCefVnQ+unO3asN+aMvFDx0IU3n79Lrzu6SqXv11uffj6yGfbmH/45eXCqjw9NmXl59WwEtfXtph+fxpkVL/+NOnvBrD9sefvsvpBi8N/X4RBrT+9PXt+5tYsPD70iRafTVUbvd21uKbOgTCf2Pf8npV/U3cm0u+vi7+sao/rP5c8mLPX4G+r4noAbl/Lhb4AOx8+ZRWSfnj2xkgEcLSLf3wx5/+mViQxH6WJ13/P5L786vgGJQB8NabS3768Azf31bQm23fZP7zY2uQMP+OJWD5+3HfHPXPZD8j+w+i86QEyf8eyz8V92cboL+ufv6ntv2rDR9W0ZcXNswTUL+ul4efV78+U+TnH4LvF3/429+B6P9WjFENrf+U8LVwyyQKu/7r159/6J6Xf/jbzz8MNcji0C2+Dm3+ZzL/zK/Pc37nwbdVP/5+Lzj/XGZlNZarbzW0+rWq/1f7908ra4Gi79e7z6vfVuLyglaLEe+HvrrgN9XYAV1/48efXv4OYKcE1gz+8zbAj//4j9Ux8duqq6J+ZfjV0K9AgPukCBflzTjpVuD/BTXaBSy7BDj2bR3I/yXCi8YAm3/5P/4T6j/6b1C/fsfm8Ot33P76itu/fFqZQGTVJrekBMis06r6pXRvAKGX48DqLmzvAKK8GWA9qOSPy4dVUq5++RdSvz4FfKrnX57Uk7yinb47LEjXDXn4abHpsuD2qwU+oJpwCv0ByM4r331lmu4DsLWr8jtAysX+LkvyfBUk4DDAWvNTNvDR50XYL7/84rld/KV8hWZk9Upn3Ros+KbO6uNHoGmUJ7e4/1KGflytfvj17z+s/mv1r3Y9hS9nqMC6twgADUXjpKxARQ0FWAaCA8IJ4OIZgV///uZXIKYExAPilUQLOy2bQUZmYfDuZGNPf9xi+BtRrQAXVW0P8H6V9J9Wh2j1TV9w6HJrYYS46vqFgsMyCEt/BlJdYM43T5ZVv+pA2nURoNihC5+n/uK17lPFApS22/+yOu5UwD9VDv5a1HwuApurMgHu/5YCr9eBkPaHbsW8i/i0UpYcXNVu69Zx676dEbmvcVnY+W07EO6uynD8Ui4sGy6uehbEq3vAIuAZ/y2kH5/dhV8VoPqD7v3s5xp3YUnzyZbtl7J7S3a3XULhV8/e4TaAbgFQwF/eUqqLqyEPnv4Dmi6S3qIQvEXlmYPfKX711sjsftfIMEOerQyAGPXqy7DdwOjq/+fWaPEILQg6J9Amx644xdSd10gt3eIS0dcGE2j4POhZld+bl3eAesfpL2WegLRr57+8rny66G3NK/YB9AgA5uhP+SC5gCaL3GfuL7nctovi7pfynRA+LNYv6AdMB0ABCmnJ3/cDl7vvmsYADZbv35uDZ660wQIbIL9X9eDlIPeiMAw818+AVu1Sv29hBoXwDOcYJ378O6uWEIGAAPkroMTic0Aan76B9Ovdd9V/t/G1B1q2PPvDAZRv+xQA9AgXBRdAW6ID1Otfm3Ng5+enEGBGUfeL7R4IfPHh7WLYhs2QdEm/gOWrX8MaYPTH5f3V0uVqONWgZoCzQGXUA/Dus5YWmClAhwN0AGkL0qBISsD4wClvTngKdIsFGADwvrWkrxKfl98Mes3QhareNy6GLHsW9l9FQHVwZf4tfph/liZAXrGseJ77j5n27bRF9oKhHcBBcOL73dc24dMr07+2Eqt3uZ//MP38+O8NSE/uPv8+AT6v4r6vu8/r9SvfvtPtJ4Bg61ddu+/U+/EPuPA7ka/Wfl79e2r9TsRbWXxewZ82nzbLLfktrd5ewAu7j4zzEV3ufin18Du0guOrAuTVErMZcP03HnxfAsjw1gKAAotfebFb6HQE8PIkAhCAL+Vv83ypsze8+QBC85v6fzYEIOdf4/WNr8CtsgdnB0vTeAs/LbPWon4Xvnwuhzz/8FKCjPtvprOFj4olkbtlngMlA/qvPgmf395Bcfn8+2GXmwA++qAGFpr7Bp6rV2AEzVYSjkulPCnkz4D3jbqXDH+H2IWZXmE3WCzp53pR/XWSW3q/31HC13AhkK+Ld/6oHP0nLPME8AWfACksM+dvOOedxXrQmIT909mL3oCBwdYQ8CGwYAi7f6ZUH079H3U4PT+4+acVGwKUzrvfluMbzy59xm9Q4zUFQOh9EIMPq1cmA5UK9F/CsyCO22VPuvpTXZ5k+PWVDP+o0JM1f8uX702Me3siDGDKT7dPq7Nx5P/y1AxM0cAVXjWB9fekrcqlEQHKtF3/p8d/a9z/ePYFdE/LcUH1eTnywxsyg3cwbH1YfZubgNFvk+xyQlgOxcvnn5eZbcnT55blA9gD3r5t+vYPMV748rc/6AUUe8I9IM1F1nclvy+tnrPeYgIQ3b/+08SvL6AmXBAC960q3oYFsByg48duaZfWADTA4eD7a3mDe//OGPG2tYtd0MuCvZQfIK6/QUKfIvBtiMBb3PUpL/C3LoVEERoRYEUERxs0jFwYD7eYT21hP3R9xA83CAHkveLD16UdTBZ1Fl2AFz4CiAm/3waXgjc7XvVenPRtannW/as5v754OApW7tHuQL++dmsI9vAt4c2MDbV46HQZnde6ZBGe52lFIQWXsWQDJmPNuzf5B0s4VL5hTWYtXtltzB1pZHtQCyGqFRI7kifC2wV9H/ubnbATSzZ/YPkM+Viho4+E5YhSvjIsNugGdE5FG01jxeoFfFZH0ojVqaqS+3SwjwmGoBC8Xosdnu/nNhZJWfUfa2fmd350izOZv+oyd8G5ghe9oj0wGjyP/lWFc0m0rpVoYxMJBdZ9OvaRzcxrzuN9iBA0QydyCC1QajhWDMPlmGwfqUSUvfm68xJVIyFYPpShec0jWZG3bsIMkZ3KV8TA5OPFScgKPuJC59+uTAAZnqTMuzlnbu11jTY5VhZHvTumOU6dUooKInOgOMO/lzCybjctUmyyu48whbqTI1Ep0ANkz6avJ2pFRFPJU/Qj6kS0AmOAWstkMCncTBIqdXxsNexyEhyO1jHuLKDXTVSaCqZuWpqpBcXPQ/KRceiMxm1EsHC2veWWicel3x83npcqcroj2LHP8ROSd5DSPrxN6Ws37kGK9YE5bZKZQ7oDU8aRfKJbzujqEdcCG6Wzs5Zf71nidlPdK7wwutC8tzRGuMk+Tc9mQxnBg0EZpDdb6KGyYZGZdidyW428VEmSGGfhTO53mOjQG6jLRq6TquHChDn8SE16jbj2Bgd/1OvWiQnJVDFH3zW74Dwf1ZM1DP2k4gZ1z3RCYh/dFWMY4zIYBJ2JVL6umhST4K1axaSmgD6qQc66HPv+jrhuZYiPWwSdEl/bhKJQ6+rDcje6c4jn6+kQTe1dxvcxb6VCRsBodhZyR0ha04173t3BtSaQV2UY5vpyCJgxtzZ1d26mAsGbzUwfxK3WT6MO8bXZ7ElMlFFuLUUJL/CTfIJuLanr3aFMkm2MsdfuxJrmAWZIaiimIUgyyCeU61qha9Qp9vmQCSBpcg7uNuhQTxu64dXzCdvK6fbUmB2PjvxEoiYGl5CslOh4LWxIG9X9Zooi04bUHOXnQYwekvhQ6c2QXa6Z0Wyre243t1uCuFjRZ3HZUuF1pGP2eN0T/BYbHhufdqFJonPozAaNn/ispCtVffLyntnMvrQptpxr1HKuhaKdXdjmqAmoQpk5jaD78hKtt6rK+wiNVRyK7roCo64z7rMqDV/ta7GVuccmJM1ip4Zsu75IC7xbOk7uKirkK1V7qLYh7opozK5RUUQxtneniAg7Qov2UyztclmGeXZtj6gVdHe3Egpkv42MoCSGdrIKe8RTcTfd7H2v1ibPons6ibt+dzDQCnP2Mr1f14V25aHcbIqWQGmT1t2OMtPJuEol6oqaPh0TLd5CVCtbBC4MeEzsYm1fmO18GRGbSbZ0NUU1VYQK6N3PhEw5EG8+VHU2VLmgNds7dJx5Qun4VKtSRmYwcaH0ootPh9sho339+MC299lnSgOm+Fvk4NP4oAbz1o6Y3yL13Yk7mDlGOSEw3CY/AZ8rvnJSWeUKzRjJKaxH9y4onKYzkxaludaUwnET0lKtbio4NWxdN/b8idjJfJu3d14Jim5sEdgqNpy4t1NITu5ZvW/KCen1hrYtUgniAJvgO+bB1GHsuvomIJV6os75Ra1xKSGsAjOYjCIxIpTzPXNQwjm1OCc37ix06LRLIV4E9h6eyU2V22cRgbjQOlTSZar08aRhOluFDZG23NZ3GHU/QTJPjZKciHsXEnMBYPcmc4JKkRIjl7nT+lIeprtZUGZv18ix2GEyrTLqISbb7FgrWyg71Mn2gLf2nD/2FT5jdXXA9tTBFeKZuw4HQt5dmaPmXh6XSHNksxMdPD7Tj1giEFw7F4i4tonmiI+03ArJDSt45XEZOjuZrnetOvQPh1Ye/dDsoW2qqHnKSu72SoV7DILu5i0Pj1nm72475LRZp0arz+pGda/icJp0/EGTKEGuu1D194wzEw2VgyjuDxXvriFqY9/XbiQP1v2OidH67rYyOgXFOT/t/IwkN+qJb7S+SMcAkR8bZz6LOq5a0q2RBPWGEKg4sOzFAnDBNESOJg/N84grb1Z7+UDi+6ncMeSe1RLOtSB25NWMFMuHDZ3ndOxiHd/zcnVU6PUjONVxhPGeseMLWk0rmePgVIVv0yQm9l6/BEHN49OxS1JVr7z4zlzoh9qT91lVm+pSbzoYiVo8th4wiRw65yBxN3F/Bqy/77G942i7dR108aRrY5zsrHumHOW77bdjd/cOl80AhxJXsBsu7VlzcJSCKnER2cBcvDGmCplYDhXKaBr5mhE9eXM+U7IzS+aDHlXH3HH07InXq1DeDzZaq2gmYzAlpea4VuwLuz3z/TgeCppZPw478pIeIZ2Hex56dOfTpkv8WWogOpWRLAITwuTcq80j34xsWIX7ehrlqzBZOgcbsVKM992WrjdDwdG8KQ4acYP20IO0j9mtLfn73uLaW73Db16dk6d7ZhcyPMvbZDYdYd+OD12bAj3ijWN2JxPpeE6FRxHUR5vWaRvfxXJJKYONPwzA3ZZBS3y6Owv7S601qUTh9uYU5v65n27+wyLqXHvQKtW4mcViB9BWGLEU2lwB7dykCrOGx8zpkqNwghk3RNsI9LQLSHgKPKhu6uuVSy4JYRCKf5eYvb7Ws8OJ83eCeN+0uwMWdJsIyxJFnArBr6a60azzeevk5O061/aoKqYo8bwwVE0pCuekr5IOY9jUTR5UNXNDeqYpDYFwGYI5Vqajzsh7lXUb67q1EjdpTore2zCUozaGH7dHJkRqtG6jPkmUGM1vB7+9hhFBY2ffc89mJOhjVoV6UNZkaKcxMcgixsxXb3Kvza0RhuFm6jdQb7rQWqIGn7BxNvQzNGY7XpKZqAbZwojXopTDmI+FiobxXNZ4ZeCdq4Iw5MjzTs6qm9PgNvsLxsRnzqJ3DbmHWvFaPo4X0b/kOm/xkKbwzHWK/FhijJ2abWC7p3nXs0VBImN6mDbr46PSOfYyhyV7KUnlUcPaNVPM3iARcaox0aR2Ww1ndpexFRPJuVbrc6FU7ISZ+LU1AtpGzCBdIxiUaR4HIhxcx2wsjVZFKNX1dBHLqtN5Xu+PaGU0IO6nc5aJmz4wtIa4RGV6lCyzr6U5N7hS2l6zbC9ysaT7Lq1IhDFIU1g06XBdYxd9w3t3RYTMFLr5t21i75izVVz6zc5qxYZMw7Mi6Pa9k50cTvwhkOA76d9lmbH3Fdz1yl6jD2YhqQy3l/dr6wwJ0xXmME4z8JGAG8qbOukUOyMUK2XiPRjrUBgG6m+GecxtwpQUanJJQbHLU+Lfe7TVYMxzdt7WBmNFsLscIragkV2wU8bi5nr0vjPSho7aJkk75s6YCH+eBu00THUQemygj7GP0oPy8IsxrdscmQj/4uUkhToWWRHC5Rp1LIrPscwRB0k+BDQGH7i+IaTtoJ5unsvqA0TD1nRZJ6MIlzTIvBPXbxhih7ODtK1x8hZKGcEgt/qc95fzSYEPuFEnhwpMHjLeoLNPUaaGtpVH2b1w7C7UbtakkwPh5NhdBhfdgWHn5mYXZ7eN78KGXo/e3t8KliDHSMVKRO63s3WLyjGx2ZHNqlKEc5GIpGHQ0sBqSHS2FGOrpfQ2b0zuoTTbKDXCnbBOYSu/m3RRD25wsC73SX/k5TCcTgHaQQUJOzCSVT59Ibrt2TBU/2Cr1XTU5/SsiMa2mjVkbfadQ597Wuas2iYTmU7VWaljQM3XW3IK+B0tyj7fXqSDPZh4Woy4DdgQd1JGYzxDEF3SUhB7c/aVgkUraJgHwEeVpF3bo304FYQy7Chj54ij0sCml51ty8kvHF/xpuWNeWYqyrjd6IEc1IJP8RLVDilJhHdAbjPuYsxJ0g4Wd2hGtzQt1jjehB4lEncE4ydLd0fBU7a5Q3tDbwZSQKnwqfZ8MhFVxA14Jo81WITj/tGkV+keP0btTKzPdjANEDwW2wfpGhrhkDj2SNkN1NrKsDnZOoFp/jlgmqLSmWPecOIpg8L7LrXoK+9FwZRxet5Uahdfzuf1Q72a2pAE0eBAoS8OOXyMOP1s7mI8ci65w6emT1yCfUdCdZAxAVad6xHd985EbZqzI297/7IVqgpHaz0J7wd4rqukRwWGMgpHCEFfcz/LruDXbb8zbfIh86S5pmGQgWLX39ZrDLv3PN+ShIFf9p1wuPIbLBr12+GIhERzV8gzhtrobYwPeXNA+ThnGOeRlo2w1fOjbA3TbjMf6JKhr6EqZEcHNBzOeEQvogfQ0+6O8sUip9I47JoaJ/CLmdpCjEByaWNAVzmurtxESWuSC90yr8/zniDTlL6CRud+Tk9xeHMmcdRPkIq7if0Ya/IRGgoYKSTpEhjnERltaxOQDDpM07BltmxvGBEYryYHtr2TLyT5lfVUR/I3ehNXqWY6Fk36/HC1qAtNx8z+vsb3Nw3041N02ItSHhI7SLmFt12F2FvvJnNZy1lXvYZt25AnEd/NQ0NTh7h3cg02N9N+2gu+v3Zms9S7K6n6nM5alSW0OuTNs83ccdy+uE2BXBxnX+jViS2t0It7SrCHzOalQOEhxKyidqJc+3ENZap7CI3NtM4AB+GE2UOp89rDPm070HGr+A2Mf2cqzI9Dcqw0LLi2FekKa3u+j6fSk3uBQiKngMi6sddSochq4Rb4CZ1IImnIGOsvTkRgKNyp7NZu6wpiiDmORrGOT00Ai5Q17be1bSnJtnTUvti6p7YOTec+1KlLbxPEp9iCaeUUq+VHpFFgin3InSRr1XGPIgFzrytHuCWzHd+EQVyvqT4iLaq7ymPah819PdlrF47bqlJqH14H474/s/ax1vOHqGo2nF1U4RAHmxMTZizVBhB/wpNRKmG9LutR3WpFlprBgycZ/pB2Wb4Xoi5LMaRC+PTSmsYR8gMeTHbuve0r9TJyZ21rcMntLG/uI1IoJwcXJjGGxjVRrxmchyR4iLxohw3SiT0YE6FRp5DaWs4cTDSP+OOFR7f5Njg4xzGeDcWaymSNKNMQJua9KA/4Fq86LEGms82WKWnXDo5njQpXuKGVsL8O425AKwZs5jIaPmSAqyEMfXhdr6bu9pAchLhpz4FzjM6SYXld4V6G9OrYtrtvfMvh4x6/9fGG6tosuvvVvXMmlilxkGdQEEdJPvAjpvVTouNjZhitITIuS1OqClIa14/Ojk7htOCxDYbW3lxoCnKOo0JgmxuHnfabSODZNAYYLMrbypsyAiXq7WWS9n1wEB4i1junS3he67nxWFOGukfwBoawtunWvrzR/OtOgWRpj8R3JHdMU8On7sZg81GO+BEXe6mb1ojLd41wK5PCI2v7eN4w3A0Zo4u4OcOItZVi76ak4swW1b3OfCwB/ZpEFteLOJcKXcf2kcwePO5cbPsYKII1b7Eb0gqhFbNJilMO7W/JA0E6veOdLUhNuu5hTZg+2QrxwEgBC91mxGMweZnF3W3YhpWS6Jw2F1fmw6RxiFMBi5kgVQHPHn3bdI53UIEO5Fxu0s2vortHUs3J0fZZCqFgHjOORiKnZEgzOlRIeHk25htUjArXIsdD6Cit9TCv3Z099WFAoXaGt8hjJgIMpyxjcqlGiAI83J7sqNrmHveQ7qfeRqEQZy/cRJLk0QojNyVSWfXqnpBPWyRB7XuI3Rqqog0rulF0Dea1YkJt4mHYbcXJ0SZT3ALM6ZFxq/1JNEPYCCXKCnQhNZWguUKavg/K7f4AOsA0Gi9IVLDQVadaT5vGACvQvXMQzo+uRm+wdm8JJ24ZUqgoKcDhPdzpdyHKJ9+hw0FCrwx53Eg6gBBevsVljuKFFsfrA69UTXSKjDiVHiI3+GtGr2PQZSZ9uokMRj2JNMQeO3jAhogXuyGjMgXrzt48jA9WawpM8ROyJGuikAbDDrfnI0Gf2rbZq5O222Vz3ICV5zW8V/sxiIeTIqWP09nZpdAAhchhzQkb7wwiEu2to7HxHCSqiUTp5fFYk7Ard2zrbXiJvLt3z2rb1FYwxw1UwZOQR05qVX0RxindHP2tHrF1f3VgNrgevfReXfTbo6fqDsbwmxWhhvWIzkzvGuLQkffGZRr+fN4UDKVGl4HwzP38oDf5vYVvR/xMmpqYu/ta2jlw84AI83bPhnMPK3JBig+yw7Xzo9+080m9BCVqDb2geUNIZMKVg5r92aTWabHOyZohIOSw89TpMXfj1h3xg8mcWhG0KjMtRBtWqvbWjbyrECDZbXAN6DsNFTi221Y2655UYHubrK1TcSEiorB83BjMXcNOcJT7w/YxlIMNH4MqhdnOJRqZOwakk1HbuLJavXIrztqcUveuQOeB0olwtDuzYGavH25+3yIZiyHCDsGOWZ/SCr+7PpS2vahXbL/N50j1hZ4tVO0wHoThcrZv52R8JJwO0+sdMfn0Xq6mUOHyCxF6RwROFKWdBF2KOMJGhY6Er9stgo/2Rtvk+7tvaVRyg9hci8B4GzV4ehcJbDabhjhbtnXx1gfowEJC64f7u5yr2N3jBHvbjls0tE9JQArsoGbOyBqmDiGu3OZSw96agvJApiCULHcPkM8Ntt49rg1mtltXGaU782hEdwi2KJwHaIAldrKG3Li1xWkzJtSgi+K4eegYgxEk3AwFhmhERD44KMCtmUsnFWUUyTjQTGM9cHgz6gGtc2R+vmgC7iMBmOlxSRrSMlR6kTYnhL/PhZ+47DFu3UtyI/09pinild3gFHYgciaAcfWMXOvuYK3tOxRH7Xw+qKS/oVDYRQYxKlCXmVn8wioWcbdvHhL7j/1BeST2rc654HS8yRVoiXA88JEUHag1k6LKzGzQpD+pI87dt4VxDkVMF+5rMrBNVAMTXB/Fmnzn/RCqUZKmQrPYTmvuSNP0X//68uFleTb69pD4f/LbtOUh0v+z51Wvj53ef2nyfNIXusHn51mf/0fa/O3DS+snQJfXJ3FdPtzeHmz9w3O4j//iNwXLxvn1R17vD3NfH5737m35tfNLUgZD17fz167Kn78uATu8oVt+JNktv6P1wftvH1B+Owt8dv3ns8evffU1SLq66paLSbn8biQMFiXevt7enkp+eAlmEI/E774iOPY1bOvFyLefKQDbkE+bT8jL3/8vI8RxGLYuAAA= -->
