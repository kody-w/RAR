---
name: "rar-cowork-cookbook-demo-data-scrap-defective-inventory"
description: "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_defective_inventory", "rar_sha256": "a4ab6cb7f77e380029ecbc1c847bbca09df61c85cd75f9d13af86a0a475d3c0d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_scrap_defective_inventory_agent.py` and in the RCI capsule.

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

Scrap defective inventory Demo Data Generator — Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Sandbox D365 legal entity to generate records in (default USMF).",
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
    },
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 a4ab6cb7f77e3800…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_defective_inventory_agent.py` first:

```bash
python3 demo_data_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_defective_inventory_agent.py   # or on stdin
python3 demo_data_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Demo Data Generator — Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_defective_inventory',
    "version": '3.0.3',
    "display_name": 'Scrap defective inventory Demo Data Generator',
    "description": "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd60e18c3a4bfd3a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic scrap defective inventory data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for scrap defective inventory. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-scrap-defective-inventory-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic scrap defective inventory records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo scrap defective inventory records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for scrap defective inventory in a sandbox D365 tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataScrapDefectiveInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapDefectiveInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOb2JblX1HfiujMLNkXBAKBK15EIyZJIAmBAEE6w8k8z4OArPzvfZDutZ2v/Krf6+hPLYctCc7Z815rH6M/XqyuDYv65dOL4ln5grfSNAq9emHl7oIu7kWdgLciscHfhVPkbR3ZXVvUzcuHF9drnDoq26jIwXbey73aar1mgWCL2rPSqGkjZ+F6WbEA66zyo+v5ntNGvfcxynsvB1JGsNApardZRPnCWjRAqV0MCwbFsQX3PxX6uEi9wEoXYHHUjh8WTWsFQEEbetljR75gB8dLF7OZDwv9qG7aDwsH6G/fFn54uFJ7bVfnzcKznHCRe/c3xT81i7KOMgtYknjjK3DKG6ysTL3m5dOvv314icDnl09/vDip1YBLLwzwhrFaS5kdYt792b+7A/anVh6AheUIopqD76VX+0WdgUvA/cXbt58bL/U/LP7935O7VQfNL58+54u31+eX+Y/c5bPxi7awmtZzF45VWnaUgiC8Lqj0bo3NV49A2EBS8uD1ufObpKJc/G2+9/NTyWvgtT9/finKOUsgZZ9fflkUNdBXd/Pn11lK+fMvr2lx9+qff/kmp+nsGPg5CwNWv355+/4mFiz8tjTyF18UiaXfdIEYR6UHhH/n3/x6mv4m7i0kX56Lfy7KD4sfS579+Ruw91l2NpD7Y7EgBmDny2tcRPnPbzrqAmTIyh3v51/+kVgn9JxkLtp/Su6vT8GhZ7kgWm8h+eXDI32/LZZvvn2V+Y/VlqBg/hVPwPJ3dV8D9Y9kPzL7d6LTKAeN8Z7LH4r70Ybl3xa//kPf/rsNHxb+Z9A2KWiT2rJT79Pij0eJ/PqT++3iT7/9CUT/H8UoRVc7DwlfMiuPfK9pv3z59afmcfmn3379qStBFXtW9qWr0x/J/FFcH3r+EsG3VT//dS/Qr+ZJXtzzxdceWvxRlP+j/vN1oQG4c79dbz4tvu/E+bVczE68K32G4LtubICt38Xxl5c/AfjkwJvOedwG+PFv/7Y4Rk5dNIXfLhSn6NoFSHAbZd5s/DWMAIo+IA84AOLaRCCwb+tA/c8Zni0u/MXv/8t5APtH5w3YoRmkv7gA1748kPrLV6T+8hWpf39dXIHooo6CKAeQLFOS9DkHcJy3s9qy9hqv7gFU2WPrfQQd/XH+MKP07/+E9C8PQa/l+PsDraMn+sn0fka+pku919lHPfTyN48cgP3e4Dkd0JEWDjDIjwBqfwC+N0XaA+Sc49EkUZou3Ahgy4NtHkzQ5Z9mYb///rttNeHn/AnV6OJJZg0EFnw1Z/HxI/DMT6MgbD/nnhMWi5/++POnxX8u/rtdD+GzDgmwxltGgIUH5XxagA7rMrBspjwA7Zb7yMgff77FF4gBNLoA+Yv86MlgcycknvsebGVHfUQwfGF7IMggwFlZ1C3A/0XUvi72/uKrvUDpfGtmiLBoWsDEpZe7Xu6MQKoF3PkaybxoAfe2UeMDju0a76H1d7u2HiZmoNWt9vfFkZYAHxUp+Gc287EIbC7yCIT/ayk8rwMhNeDW7buI18VprslFaYECCGvrTYdvPfMCeOh9OxBuzQT9OZ+515tD9WiQZ3iCeciYp4pHSj/OOQdTSQbQ4DlDtO9rrJk1rw/2rD/nzVvxW7X3IH5gyrgIusidKeE/3kqqCYsudR/xA5bOkt6y4L5l5VGDD+ZffC3hxbdRZp4NFvNwsHgbhWZ27RB4tV78/zAbzc5TPC+zPHVlmQV7usrGMynzWDgn7zlJAmMWoDKfDfhtbnnHpneI/pynEaiwevyP58pHKt/WPGGvq0HkZUp+yAd1BJIyy32U+Vy2dT03iPU5f+cC4M3iAXwg0wATQM/MpfqucL77bmkIGn/+/m0uePN5jgco5UXZ2SlIkO95rm05CbCqnlv1LZ2g5r25be9hBCL2vVdzNkC8gPwFMCICzQf44vUrPj/vvpv+l43P8Wfe8hgNO9Cp9UMAsMObDZwzdY9aAFhW+5zCgZ+fHkKAG1nZzr7boFeAp8+LXu1VXdRE7YyLz7h6JYDlj/P709P5qjeUoPRAsEATlB2I7qNtZkTJwHADbAB1Crooi/Jn1b4F4SHQymYMABj7VkNPiY/Lbw55j16bWep94+zIvGcm/oUPTAdXxu+h4vqjMgHysnnFQ+/fV9pXbbPsGS4bAHlA4/vd54Tw+iT55xSxeJf76b8cc37+105CD9pW/1oAnxZh25bNJwh6Uu07074CsIKetjYP1v048+LHf4gBfxH99PrT4l8z7y8i3trj02L1Cr/C8y3xrbzeXiAa9Met8XE93/2cy943NAXqiwzU15y7EdD8V+p7XwL4L6gBJoHFTypsZga9A9J+YD9IxOf8+3qf+w1QSx7M9dkU3+HAYwYAtf/M21eKArfyFuh257kx8Obj2qM7Gu/lU96l6YeXHFTeP3VMm4kom8u6mY93oIHAINZG3uPbAyWGdv741yPu+fHBSl8B1gNESpvvS++NPmb6/K5Dnm4C9xyg4cPCfUAvqErg5qx87i6rAeUKKnV2px3L2f7niW6eAR8Y/+WJ8f/VIOV7UvieDmbge0/L9zzyM6gxq0vbhaocuV9+qPHrSPpf1elgDpglu8WnmRI/vAEPeAfHCMAs7ycC4OfbGe1xos47cPz9dT6NzIF/bJk/gD3g7eumr/+hYHsvv/3ArqcXXwBV5z9Iza64A7gCOPLg1HePv4/CV9cR7MeOvxPll2cR/b2GJ5vOLDtD46NM54UfFt5r8Lr4J3r5IwIj+EcY+4isX4e0GX5gxMNNgNmA+eaIfUvFt4AUj7PabC8IYPv8r4U/XkApW7P2t2J+G/bBcgBxwCKA7BDoeKAQfH/2Jrj3f3MMeBPRhBaYQYEMa23ZuGNv/M3GQwkYRkjPsZ2VQ6w3tu1YMOn6OPiGOe4G80l3hVo+gVuwtd5gLurALpD3bPIv8xgXzWZh5MaHSRLx1ysEdoENyNp1CZzAHWyDwBZpW5iNkZb9bWsS5e6br0/f5kB+PZHMMXlz+Y8XG1/P1bJu9tTzRUPLle0hkD2KN+iGkdEYCGnKluqpTRq60zPkKCNOcIQZMjbt0OsKjkmUs2Dt65RAtuyRguALZFzJg+SiUzNeLutqzO1raRsNTymKfET8c370e4m3m/NxE4jHmLzu5fFgHMeuvERKhKVqZWPXcBJtpTpD7v5WI5fIGQhpcKElkfqTMtgRLJ9lZVqeo3gvXCiRofE9Ulnpic8qjDntCZHd+ktBvCcobfqhuIs35GafbpZYNxWxEadIQXDbxE/taBTglIyD2z5up3vMKp5PhZlYTQqkC3YZaiHnafxZNpiVMq3uMc+GqyirJTpjyf35pJwV7dYGrXwwd/qwdG7HyD0NAeFDt4o8XzXiTuTDUkw2hn/Np2kwlBOX0EbqbbdLTd8oO2HcczfTtasDvd1tMhE/G3miE4UQjUVzxRGYdcTb6eJXBV9XByOLWEOltEDZ2xEpJWUCOXG0hw5ypea30gnysyOTHSW1+VqplWs7Dh4waRmdttzAp0Pglrk+kpx9X/q8ONnwmWiv9KmUqCpHlc3eWO+yVSzwdmpeQzgguvv2WITCxB9YJFE4P7LC01btzaVCdRcWAenb0tpSDIW9uJdapl9NPeNkhaUV8KRst1k/VAfhUuaTK1JBdL2BEGqqHZhL3bPlJqqGu5xfKQmya0E+iRA83kNbu2C5eMOrIhKYqDGtfKJtETUuS8/oYXW3EQx+fVHTStMveugnIZnxysilDXTYYUGG347tio/Eg4ZMxJUQr9du2LBDluxIjSe5oOJdij0rh2EHnU6Yf2mOdbO/52eIjUK43sKcZaonp7rwrUih8aFOUU0YduWZLTq65g6NWWI6Lmu7JN7fimCCouK4MpO10iQ2cWCrdIg8xY8PAkTdbGW7LtrAvWQ2EyTQZASKJW0uKyk8200zCsjtYhFHmZqgM+0yrRZvzSvRnw40Fxm7nYxkG9Ei1IHY5Udk68GHI8SfSHK7iRgXgs9WAsGsImPHmwQjy8Hpt5U21B5VlvjtIjqjoG0ceZSXgWrq6nBSjzqUVy6FOneeg7bekkvPU8DespOsNgx1yrCxQpj4gHTjEAmr/oAgl7XVrSjVVkwB5ijNOyi6zkS861Pw6hwwzl0/hNBuHNgjxJIGhazly3Z/HFCzEbaqeDw0k8TFJTJ4JUSJ0k6HNLw0swN8h0ojYdZ6vSe52gB/L+QNJmnlwAjS3ul3WJ4YnJY3m8HMYmcp0FdVrhyl5nJmyeICm9jIaJj20VxlA3tBDZFhNugeUZr9ntzIJsfHEt7pUihWDb232IILmC11gODrmQ19q9eUiawuykqQDpcBMTX82gfZ/R7boABviYh5e3fYNivuItLMPnTuk4uvTXraLpmbAJ/09jz5QZ+qxNZecXxSO9LuFOq0iRuUMUmdctePNag2B6sNIkjWDKgK+lp0/pHUfQ3GZVcuuOkEqydIdDe3xmmuO1QL9PVFPnHtMqTs0I4zlep8J5rsC8KdEG2K/ENtcKKx1rSIOfPwRNHl8SDRyJriEygKbydTvnF7R8ePe1IvLcdNctic6GanGeZlfdc9nwjqs77xKtD2AqfQVpyVHSi8JVfv/LzktTw9Ushya+adkjjLKBKa1WQ3u1vvn3u0N6d1sO+V1nCO14sdQFEqcBc2Fgu0P3sWq9QVS/iRlIHECYEFG0xqqaLDlNrFdRPVpuVilIZ15G1lR7kjUoQF+QUiD7yqHo2o3g9pKQnUib/GXi/hAe6OZwxWjtalgK+0k9BnqdskR0whOHiZJCKqCq3oNUycKJVCj/y97DEWyEHl6iJH9QqFhQje0LpQaMVWOaA6qdApnfZ469JSAKZ2jkItPN3Eml5jVoMFgtGS1uU0rarM4WDe8kXBUlF4WhJSXGIeatLOQRLFo7qkLWsZ0bUsSCvJMg8dOcZwRnMm2ipHEl13wS5B0xCgtqGS67rbEWXvbw2ItDGvJsQdlNtGLTlZeTHL3I9qMwi2RUKvMKkOMdzxuAM3nrSqKSpeDNb63Q/5c1HZtrS1Iyuy/X3nc5mOqWo8KA0ADw5rTuF+KLU1pLIeA4c9Z8gB6Ih9sgzllcOxy5WTDGJXrqUtui0Fw/MDhQ/a4KKuxLgGtEaQm6M8aRFmIscDy7Quz4sudluuRyK+1MlJ63IoT+Umq0O83RiXbM/JW9+Rd9zRQ+9IgATN7Vo7wUUREwXG9qvpXG0To5A3fofi1MXl1+WkHErVFZmoDKjzpsX7yMxxhlKrllJ9cWuOVU0VXu53NZzGfr1JnAt/0PYgdlwOp1qXxKJ61QUNU4p4fzAYUTDRZanuwkt25fhcNyNks6fve0XFVboKzbEU9j6kDR0k86XKR1tDRhQIGO7s1XZYMtqo9pw17HBtu21PzN2y9/02UY0hIa2xuUeBpmLS5XrUTIoNaFkIaFX2YA1rYLMatxnCbq9GFkY7MS+brXupYiNaBUomChl5wMuWyil/Yoci4sa7aoH2Lr2coclIB4eiqOAwg+Y1Qo3MK4sGBEvJvENoKy0RiiV6DGDZto+wSKii1ytOHtyTDSXuocg4VatoeXW6m+Az4+FIyhVDpaURZvdq5FkyinWanuKSJpiV7ioYR4iisT8h8rlAjAayjuGuWFFlQvjLETrJ1P1+27Cleb3zeNl791UAkxe4yjqih3MK7YCjwdatPAFHNkaeX4rTht4JWVEjky8QDLyjIIJVDwKNntGScPJrW3XMCaIj1R4itwxyIe8vZlQQjbvdVitFPbkIsU9YPZhoQ1TDPbWUXGWfpLnVpBibUWYQe+U6AxMQx08jWtBYIYkH8nZMXMrs3TNgRVTQS4jpe1kjzOXB6DYAVoIC2h+36t70RZK6e2F1uRqhgTGHTdEaaSEudwp2vsK9Ru8DC7nCawOGSkTAxpC6q8lQTV6uD6tVaED364qKTpSoQDw7BL0dHA2kE0ynXYvrwxKCdutJKdrsWpxz+az5xh1Swx4db+OZctoYYyWxzgTAfPlSYaR1WUW3pk6LzvKnIQtd2jx1KidcIvFa5yO1ZbNWoQtfu6as5pmKkDKogy5rak0LK1tx3dXILGt+Z9V646BDi6oRI3RXPNqSKx4ONDaJelBmMBfxt6iktqfAzIUqhLCtc9s6GQeGJUvbqyKTk7lbphWHx2rLnMYm6u29yrAyaQR+HG4IVExwKzq0RLCuiitKiFDJKfccsVIcccYV7mrsLl7JB3aSR0zlYI1eHU+3/YY9qAydFUm7sVjI2beH044ZSPKE5mtTEgt9SV5vO5DHQ4PfRemiaUizOnlVzCUbV1ttcMfRShLOHVs5selZoCf3sFWOPtncNgeJnAbzYOdVyemd4VxNaqAIOVYMmztE52CZCuT+eLoaFz5rRovZ88wRrgb6IPDuiYB390NQuEGulynE3ZX17njXuMBNhGkneLYkwqEt5hDsQUeZV3QxWEn1HtV1dYcvExH2iHN/aNA8aEhoRV/Qfapak1bnNZTlUUoPZD61hAMoESk317BlkDS6JUQ/+gGv+MtAjtHhQvAlz46KBw7diV6drX5XSYFZyo5NBUlbUS7LI1v54lEsa4CTB+VI1hU/UIgMowW/KaVN6q95vfN2u5Fo0TLySutiMo6WYDBLtLR4NBQ1CBrrridweC7UVlkdDsS1Fg5EhY78IFiwv+ttBZrWkHRt8Y3Xu3uhTNwjDGtBxOLFxrqh1wKXqBpRIq/yTkHG6oasFtvo7oJEDbwzZEtlw3C1Lle+YPE2pEV0kF5dv9Z3Yh+WCqaMLZh57ma14fte8NjqrCcpfVpqzJKw/VA+OOySxo/sJJ0bFU1MWCePFjRp4+G6oeJljKbUltqw2wRRiwu2wddHVqRVHGZXiLIb6ONtqd0vAivEE5vo7VEyLlQyJneSGNaEwRFVpXB60VR4eGIOsIvg+HnrnS79TRJ8wi949sRO5kAiGWkVJ4ODB3qfJUiEh/xStmP56MoJF5vW/Vytj5UYnXzc0ltmOHpawjSOuEuQfch2QZ1u+a1zPeBrUm/oc+ppq9vtikiIZMnltZGo8kbDe62SlRXdiPeyJlG6XDusGx2CsWk3unQuyo3ZltdeWxqWxVaoba6hkTejJun0NLlw4hIFA35y3JuIMPRVAcGaGrb18mZkrioto33JDjXMX71VjjdGXOBXlOO99f4OF0Y6XJDJKxlxJ1K7su7O1WBS6j7PYxFnq71z9ekmJnRYrrCGxUFe0/xqVG1uqiG2IQ2fosUIqbHjpMCRhKRtwGkWqpwdRqPVpXSQVLW94PBhpXrBZTrix+UpbvVzvAFzAkKcswmn7e16E+eiwBN66JzuOziwTwUDqmyjKFI8uJtukHWNEDtFDNHmbJyZWq3qtDsxuyOuu0evXZEoE8YtSzIT2bSYi9i1JrITfKtvueOlexPFORy+5lJBkpe+yJhDil7rGJC7ShEdoVGu4RY8FsKm3y0puL+gGsPz/aZVgtv9VnqY1SqQtTzdlkke4JrTZUeKr518hwQjyxInXSXcahQ9DuP3UY/BgUkx685V+sJnTRMH84eOQMuEPt1STLB3dgKXd8LrWkfAmUw89Xzm9EfxvnbC+mL4IzYZVExZOAEGoB5acxCh8UOYmnVfYza086mkOBFi5XroLsWWPQ2qmvYUGQET63lXNMm05NhogxdijEGXO+udD7B+3Hp2wN4L24r23hAst8dE9mw0jplJMSfDaS2TEyZtais3Sg2vatfS+b4yWIQNoJAVtT6+5lx+dOB9MJCGEY5S5h+2t1vV3OzoNk38JFxEFnRV3uXdciMczeN622D9enskNo6ZKXup2Kt5rBnrC5SMzgR1ST30UtX1+cS7ruPyd5Mg2do6kaO7w1VNPNR447cXWNIN93iP2IRa7RNmwJbr9Yg3qRSLV1YmRH21is5NdijrA90jE1ff9KaffIuvHNXgsnZDIcXaQlxc0jsd1Y9GSE2k0iD++SYNei4Qzt7Chz2p7feyWrK9tA28vMf1y1jv9gcqXsUZh8HrdVoribECPOqm8WkVUjUPjpLI1sFMSkcjHukZhMr9PhWUs6i4vsc0yuWgT3krrBmlBPNmt4sxgjzGkyTpXNEY4yXYCLYpHjfs6s52PcwKzSZYO8507u/H89Ki+1N/xi6H2IWb65qAXGy9c09X7gRLWmREaYceB470tml+CjozsHAHaEt3+gq9IsemIIJdtnKmE+kh1tLGcaZNxk6HTs55SJJhm3puYBfKeFqflsW+wntqOXpibiQ1hkcYTnQ7TTxZBrEKWSyczu2Zn7RUlBwW97NsQvdRdlYOHZgTw5EpLuY1wO0hxSFb3E0UTKnKantC03xVYCHlKRLakGVKDfW+kuQ1he0Q2dfwUVFzVF4VqbUOY5RqD219beM1Wl+RyT2ZkoMs/fxaS7tzr+2uzWVC/ZysU1RgN+eBnW7LwSXOVtYz6V2QwqqcKsI/Fgef63vSUDPH9043FDH1lEnzqrN6n8ZJMV6WdQoAN14rUOQqKS3fMki5pATZVusduao1KRNV3CxXXDjJsH6Vjj5jdEXvdtcVedwTowYflxIR2czxwgrmWSYvSnlL415O7xPNWmnfpjK5WZuDTXq3iuJqukoukHii1ZslQ9fN/jD653UhgFbfXgU+nmqiNqxgkqfK3qPn+EwmY41IMrZfE+uEWcPjYLmDshQY2z3UQg3wF2W0OKPL2wq2/K0pYUWN73vGg9pCbqiVhrKZHcQsJ06UKGy28Xy4Q7eItLqXrF0qIzg1xROp3ZXpTPII56fpteO2yqq3b2ZJlh2a7oWbL4QsIt85IWodtM2QlPf8EUlq+5SZVX4lcj1K2oC8dYWZxEtUNCauYuzD0Yz9QpeDTUceEgTD09zfLa+TpJ5bSz90x42UTSebYy39SuFZv7I7BMYI4n462DhpnM5Jz8K0q4e4ElTnTUVeS6yVqKZsrSxUvAT1+N25gZHE8HpbRGoHk72N520S3jSg0j5k1WaC6PoWYuMG21h3woLKZjg6y4oat5dBwHZeNEx3WlEZfAUG2B7p8y1UjvvdEpwGuq2GM2Oe1wZ/6BHIVHLnXCGYa5+dpUhjqLCWOK7XJnQ89/rBVc3VFVaXWHGuz2djWXGNuYqNY3xgYy92VtYaWYMBgkewrt/HJwYeLfdCWjcw7Yyg3fsR+MyzlsAOmb1T3GiE0FZMlt76YO8cK/Dul6PTtOSWFrfnwmWNLZGh45o67+Sa2I1+zcPohtTDaWJiY6SWeJffT2ZRTnXZre59EWL7M2C3CzkGS2Z17QE79GDa6Q8bbIzLVrzAqGZpkNHBJ6g2G8aF8nEH6acgrjfa3Xb6HL10y+0WFe+Sca4PdwRr09U90baTdtXbIdctaKz4jQSVA8fY0lr329vR68z6RmUEaFouw5BNqGsrdZronuthlNE7Nz6H3IbgqZ5xpTxEbj2jC3iI2ulmXePn4tivdiy9GwiLDWQKderdOVldOJnZqiuY9W4cLlvOjhw3lS0OdWnoznmP4eq0di9uc6hMXWC6tZ9SRJLcTHgTaahAQ1ZB+n7Gw/HtdIbw1bI53BtyYHw0Znp3neJWuJYE0bycV3lEekPucLHYBygz6WOuyup9Q1XlOB7QfjXd0GgDQXwfwPudHwgsBu0AJcKKFZvi7qJ0ZyiUJ8+13ADbZmq1dcHxeFidpAC6asuylNwtRVF/e/nwMj/0envC+q/8pmt+UPP/7HnR89HO+882Hs8VPcv99ND16V+y6rcPL7UTAZueT8aatAveHiL93XOxj//Ew71ZwPj8sdT70+PnE+nWCubfEr9Euds1LdDfFOnjpxtgh901848Pm/n3qQ54//7x6FdXXuYfAr4b34Jrz59NPi7PP8vw3MhqvbevwdvzQrB/BJmKnOYLimNfvLqc3X17+g+8RF/hV/Tlz/8NJ3tkfP4tAAA= -->
