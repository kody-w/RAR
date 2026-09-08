---
name: "rar-cowork-cookbook-demo-data-source-assets"
description: "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_source_assets", "rar_sha256": "419f1d9d0866b5f3664821868e71c5c3672639a8b979f6897c693fafe6e005fb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_source_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_source_assets_agent.py` and in the RCI capsule.

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

Source assets Demo Data Generator — Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Number of demo source asset records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_source_assets_agent.py` and embedded as the fenced Python below (sha256 419f1d9d0866b5f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_source_assets_agent.py` first:

```bash
python3 demo_data_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_source_assets_agent.py   # or on stdin
python3 demo_data_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Demo Data Generator — Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_source_assets',
    "version": '3.0.3',
    "display_name": 'Source assets Demo Data Generator',
    "description": "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd678a74e8944eb97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo source asset records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic source assets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for source assets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-source-assets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic source assets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo source asset records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo source asset records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training source asset data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataSourceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataSourceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo source asset records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5kXxCTIiopoQEggQEKAQOB0pJnnQUwS8vN/74N0bzpdlX71KqI/tRxODZyz573WPhd+e3GHPqnbl08veuhWi61bFGkStgu3ChZcfa3bHLzVuQf+X/h11bepN/R12718eAnCzm/Tpk/rCmzfhlXYun3YLVBi0YZukXZ96i+CsKwXXT20frhwuy7swTW/boNukVYLd9EBPV59W6wxklhs/rfOKYsijN1iEVZ92k+LH4MwcoeiX5x0ZfPTh0XXuzFQ0Sdh+RBQLfibHxaL2dCHjVHadv2HhQ8s6N8Wfpj/rYDefmirbhG6frKowuubIT90i6ZNS7edFnk4vQK/wptbNkXYvXz6+ZcPLyn4/PLptxe/AOYDP9fAobXbu/rDJ2Z2aQ5G4VYxuNpMIJoV+N6EbVS3JfgJeLB4+/ZjFxbRh8V//md+ddu4++nT52rx9vr8Mv+nDdVs7KKv3a4Pg4XvNq6XFiASrwumuLpT99UNEDuQjCp+fe78Q1LdLP4+X/vxqeQ1DvsfP7/UzZwdkKrPLz8t6hboa4f58+sspfnxp9eivobtjz/9IacbvCz0+1kYsPr1y9v3N7Fg4R9L02jxRVd57k0XCGzahED4N/7Nr6fpb+LeQvLlufjHuvmw+L7k2Z+/A3uf5eYBud8XC2IAdr68ZnVa/fimo63HsHIrP/zxp78S6yehn8/F+j+S+/NTcBK6AYjWW0hAXc4p+GUBvfn2VeZfq21Awfw7noDl7+q+BuqvZD8y+w+ii7QC7fCey++K+94G6O+Ln//St/9uw4dF9Bn0SpGOoO68Ivy0+O1RIj//EPzx4w+//A5E/0sxz1abJXwp3SqNwq7/8uXnH56o8sMvP/8wNKCKQ7f8MrTF92R+L64PPX+K4NuqH/+8F+g/VXlVX6vF1x5a/FY3/6v9/XVhApgL/vi9+7T4thPnF7SYnXhX+gzBN93YAVu/ieNPL78DxKmAN4P/uAzw4z/+Y6Gkflt3ddQvdL8eAIQOAB3LcDbeSFIApQ+gAw6AuHYpCOzbOlD/c4Zni+to8ev/8R+A/tF/A3R4BucvAQCzL89YfnkgdPfr68IA4uo2jdMKYLHGqOrnCgBv1c+qmjbswnYE8ORNffgRdPHH+cOMx7/+hcQvj82vzfTrg1jSJ8ppnDgjXDcU4evsizXD9NNyHyB7eAv9Acgtah8YEaUAkj8AH7u6GAFCzn53eVoUiyAFGAI4aXrIBrH5NAv79ddfPbdLPldPSMYWT7LqYLDgqzmLjx+BN1GRxkn/uQr9pF788NvvPyz+a/Hf7XoIn3WowLu3yAMLd/phvwCdNJRg2cxvAMLd4BH5335/iykQA2hyAfKURumTn+aKz8PgPcC6wHxECXLhhSCwIKhlU7c9wPlF2r8uxGjx1V6gdL40M0FSdz1g2iasgrDyJyDVBe58jWRV94Bo+7SLpg+LoQsfWn/1WvdhYgla2u1/XSicCninLsA/s5mPRWBzXaUg/F/T//wdCGkBcbLvIl4X+7n2Fo3buk3Sum86IveZF8A379uBcHdm38/VTKzhHKpHIzzDE89DxDw1PFL6cc45mDpK0PXPgaF/X+PO7Gg8WLL9XHVvRe624YPVgSnTIh7SYIb+v72VVJfUQxE84gcsnSW9ZSF4y8qjBvVvRpVuMZP9Ymb7xdt4MzPngCJLfPH/ybwz+8xstxq/ZQx+veD3hmY/czFPe3POngPibBwoyGff/TGWvEPPOwJ/rooUFFY7/e258pHBtzVPVBtaEHCN0R7yQfmAXMxyH9U9V2vbzn3hfq7eof4DCNsD10CCARSAVpkr9F3hfPXd0gT0+/z9D9p/83kGBlDBi2bwCpCjKAwDz/VzYFU7d+hbRkGph3O3XpMUROxbr+bsgHgB+QtgRAoKA9DB61f4fV59N/1PG5/TzbzlMfkNoEHbhwBgRzgbOEPWNe0BTrn9c7gGfn56CAFulE0/++6BFnmmdS7fNrwMaZf2Mxw+4xo2AIE/zu9PT+dfw1sDugIEC9R+M4DoPrplBpISzC7ABlCqoHnKtHoW7lsQHgLdcm59AK1vNfSU+Pj5zaHw0WIzCb1vnB2Z98y8voiA6eCX6VuEML5XJkBeOa946P3HSvuqbZY9o2QHkA5ofL/6bLPXJ4e/Ne673E//dHr58d874DxY+fTnAvi0SPq+6T7B8JNJ34n0FWAU/LS1e5Dqx5kCPz7t+/jEkj+Je3r6afHvmfQnEW8t8WmxfEVekfmS/FZSby8QAe4ja3/E56ufKy38AziB+roENTXnawIs/pXl3pcAqotbgEtg8ZP1upksrwBWHjAPgv+5+rbG5x4DLFLFc0129Te9/6B7UO9vkPjORuBS1QPdwTwKxuF87Hp0RBe+fKqGovjwUoFq++vj1kw05Vy/3Xw2A50CBqo+DR/fHnBw6+ePfz6iHh4f3OIV4DqAnqL7tsbe6GGmx29a4ekb8MkHGj4sggfIgvIDvs3K5zZyO1CXoCRnH/qpmY1+nszmWe4B7l+e4P7PBunfssGfeAAg3BV0wnwS/AdO+NuiHADbz1H0HhgRPEfF76r/Omf+s24LkP4sPag/zfz34Q1uwDs4GwBCeR/zgdNvB6/H2bgawJn25/mIMWfhsWX+APaAt6+bvv51wAtffvmOXc+wfgG8XH0nT/uh9ECVASj+azYFlr8X6x8BQomfvhuGd7b88iyqf9T3pNSZamd4fJTtvPDDInyNXxc//EVDf0QRlPyIEB9R/PVWdLcfvqP64SpAa8B5c9T+SMcfQakfh7DZShDE/vk3g99eQG27s8q36n6b4sFyAG4fu3megUHfA4Xg+7NDwbX/6Xz/tq1LXDBogn34ko6WAR0gFEl6RISRJE6hS4qkwtXSJ3yMXKEkRruUR6/oiKTolU/SWORGIRkiCBF5QN6b/HlWS2dTCHoVITSNRvgSRQKQHxQPAiCR9IkViri05xIeQbvfbM3TKnjz7+nPHLyvR405Dm9u/vbikThYKeCdyDxfHAwtvRCFvUk+w2eCTuW49/VLwTdBkfdLc5B791bpLEPhXLA6ewkXN5ss1QfJkWUxVMSk3kCpsOKiRobuTe6MueEYlYv103KwlaN+OKvlXaioe6lus0FR7r0yrUnjWjjShk+DqcRrY4TXG52oRIyD9bN6p1sMumPkUc8IUjyrza0R65rn+L15RaSQDfPQTfiCSSJpTe0KKK/8SDaXCMynMAWpGN7bbYXa09YQ0wa1k0wqTHibRNkAq5aMmGl9LegstcSsR64x74YRk5Ty5a7DZ8lrGjPZDHq7FWNGSLQcb0bKaDfDKXQlnhYPe/2gm7avmWI3ZK0Djzfp7Ie2yiL+cHZIf8xoMqrqzNhDsBqNax7CkdPRqU84X+GOt9n56K5PbORcIunuqsCUoxlGhyfnzdYquYy7Cr6hKXFUNFgbS/WlEGyRdY7c1uGyQ9aR9sjSbJxfUSm73y7xOlFF6MqdoSvt7OudVWTjGNf+zSpSOzNwVrqnK83NesJVsxBC+zUm8xQ8dZoqCiR9puJOOLDEYE9J1VgnPBBVueMNSdS7Sdf2DZ+c8bI2jqa8hx3WErnouCmZOM6s3LwWPN0QaEPTTlWMRidIJ92pY5w27YLPa5/AD5tUv7HNijdNrWMrQiP220mW1+w2UBiYHrqaR0ZYl/Wh09alP0RTnmwQVbCnzb7MIXM4tjSRwtox6pr8xLOiaxb5zjZIdTSTwgfzkooeIXFDbDI50uocNfua5uEDhshxdKOdmu1No7uddkllc2u+DDX1boQCtVu7MKM0q+6mKr4Um2sLXXJnt2NaHdnjnLUKCqvXJCOT5OJkN/t0H/XWcNNyGTduBtIvdzVh+HFE6a2prhWqEA6nAhI7lF/ftBWDJx0qALdz0HUO5tmYepPsWsksz4gP4XaXEOeGHRqi0fa6ea5wjUnqovQuolYjxX6FiaVaQ8kuNjPYUG8HCEroGzvCZaJM6n29qqnqjkG2qnjy1Sn87fIouWGBcDcl3YcY76fBKecDp3YddFJ2UYvt4/XVy0TY7cftVdhRbCvzDSfcj/uyuDaomu3K9HZsjojaQOjR18YTB19z/TgkFFc3nXC04+DqXqoD09rq5jq2qJ1uQzAxsJ6/05jzWg5Qj5sipCvvzOoE3e1tOGLc6ap59HLsjbo0E6iLr+fGljbnMxoHw9YNc1AN8LGdIKqG1tPBvEWgDAEtcVFlalK1uYg5CU8b9io2Tjl1MiEryjKvhYhrlbHish13Sw5ZD2reufpUxJ0dW0ol+MQk8Rlf+zSCsUI1NXsk8WFm34JyEWLe1E0pL9QaNxgdt7WgBLPntIGOd9g/OkutZu0jichlaXSYx5zsEVndBQvtFDdIITLSGzRFJU7elXhoeBRoFOjKsD3tX2pTUXsZIprT0mFlu4p1kVENH3I8JVi1iKlpdYXJCrKHxGBpxlR3FPiVdT3oKQoxzOZ6oacLo4UDG0i1BFWrXXRV8n3HLWufY0GdXKBAmHplV3EN6Okc1jNrvwuKjeifJkWkrMQKKWNCTxk3qubWOx5PSqjikAxZeFRGvsxclvWmDckDqXbXldU5ZJhbpxChQApln5j8pqrD3WREyiEWhLGSh/MQq2lI5mgnurchK0V8tdLzlr1i0SF0eb298PDA7adc30gnF/HXzuUkb9atkQeH8thyGxxVbzATspqvHb3o5turYwSqoJMOyDHztKwR98S2FbXxvFpiwLWyK9rtOkUObIxMG0zAbJ3Pk/UmWNeOvjsDhlm2dp3wau2fklA0B3sUdUKJ+F3qBg7M+Y1yLap6g0swv8r8RnPuHLa0BiY5GoWVxnYbJnhmWjIRdlZs5tatj8sbiZlrOrgNxaRnlUSL0JjlcFTtQGsfjjrEKixROZHWmPVGJas9X2LhTSMNEeo8qxXCO3Wx9/3+el25k7K1YPiEjXAIh/oNhvFIyKDztKYpe7hLRsVcpBCcWeIUEa/M2cnrcF3eAqjljMQBGK0dhfTekcEKCFyvTZNuc8a8qze2zu9YeZfnyLElnQ08ix62Dl9PjV/F3HmHG/J29BuWu08boUEk62hPO+rkr+M1FKnbI1P3LOXsV7raV/sDeqEIJ7E0gbt1AsY54aCeV3YzQ6PFnYazX5p0R27OKhn7N6ZXzJskDvU9LrELHDC7RuwnQuABspPIGPJ5cB/Nru3FvpUVi83OaQHztkBfrYoTWIXGbA2jbqPCc60EsXWPc/eNdE4Rr4Sly82EbeceWNqaNWVwHrq00bWOIG3Uj/CWo+rbjtmox3FMjNS9MG7N3NI09krCLmLukGuMOZmCVNY3DWozB4pPetUxJJR18XA8JYHoB1dobekavJFuAumwLAgr7tpixeYne+qo9lpfp9g8EcPBUEyCkVKWhMbL3dQ9k+gQJ55YCGXYI54nSSP7w9j4x0tmp8tY12WpvO/IZhVnzEg0NqJxhL1VOSc9jUYVhNr9iJw1i1OyVr6grtY1nHe1GKbODuGF6orqzGBKfNI8T0FkSruHlcYbV1sPYoGPGnTr6PeoUSzQTwleDmEt7VLdzI+0bXosy+7EzkzjO3+w1EDbSPw57YI4zXYMkYWXG6jhbbg+cqDiaLSimx0qMbCd7N3wcOM3OMZ2birn2jGsbqvSdldTYJ1Y7368YgfaO1E+d1Rd0c8cf1QPaFtLsqLSMWsXtXzEIywgo4NQ4/6Kkhyt2zpQzoUXnU4uYqiTZ/quXXLcLSlR24k1W/Kx3hyvLB2mWbmTD4jjoaLCYMw2OTt75YTyQZaPx839eLYOJBSIE3fnSpGRNtCpM3TVGxDnWNm5gdNSKicyFUvsMVlKQ23s8e1ut003Va4IabqcnHQUj3IWHO4BImZs6xyMZNQh2SeNy15nueBilsBBbnuhkj6pXIYvEtNQT9E9QWt+5W8yt1ga8qWNx7hawQDf91yKOYe43PHE0szW9HELR7tRzNkJVfMjNQx2XRe6R4gCnKYX1p0GSyd2sLp1N8iuRIkj4Ni4lwYLZ3jdNcXLSCPKaV/gvcQraxjMxzZDsomCYpWsucconGIsnRphT7t7WnL4tl7hp8isA27L9FzOaKii+ZeTsAVt5nPO5q4to7N+0TlY3W/c02Fzu1/vTb9xyNFn5VtIGMwZ6plBdSBJ1kXLNgYmj49RkUwnlVWQq7bW00xO1h7S9EgXS/0999VS3rg3ibycQlXLb0dzPPj9hglddPAvFemEUHrIw6xUDQvrtqcIlmvcPYy7KxQZLE7T2WpDNmp7MAIz2/o9ud6dydXeJGUgMpOX9Q06lzWFo7m7k110U5I6V2vcCndR/bhq0um4lLCA6fwYH3URZcmWz3VU8XjAJ8eWinVauzHVLsjx0/FUOo2ZSggirNog3l0NNwni9tyUaLuUmlhDuastK3y8o3iUM+m6hnE4YHFvV5cbC1fyYalnTbkOIo7nsXgDzmYNXQfjuFFKV5dNy6Xu9yV9NzX1iqtYc6fGe1+h9LgsDHQMKK0rCAYp6QbR1EjyV6wttKeTdZYRaI/g9AkR+dhQYluMJOOwNoQ9mfsFG0Iqblx4btvB6XHXn+krPlzMMdhSZ76jARJf6QN9CnZxqmxX08414iUu5t6Z03Brz0jd9lie5KLicnlAJSiNpJGOfT3rz8UqQRoqwgyU6C2vmFxvv2ab7RLvkmNuZisd8lxaK/bBhLDY3mr4Zd6ayOSv1r0+eRjdKdbd2DbbHhzgbpZNCpSyREebKvebQo7X9W7DXazTzV9ihYoi1Y7XrzFMpit/r0IpWBokG4VFqupUqoiHCMH+Mq6OExHKkIbvLllMXqV8surjjSBrRbhPJ1zxV1MeTsEwnlwKs0zFdngJbpKxGY7SWqXvwniNBbSsD4QZ6/JFxLXDelham6OD5ZsSp7O8oK59XqGCNA53KzN3GXMY9OvJzs1AryvX2vt7d7IYa7++RPhWLdwNOFCHErmFbqfjYXPtDlGcnCZifThu8UuXGz3W7MWDdwnb5EKuWli3lkEanyDNZTainZ2gqnKOUuL1iMHtzFV/7+zguBe6bUrK+5TtpMk4VmZrX4Ld0jNHa8Ruod1KQhCLfE4nHmT5lSy4hZl6p44Wx4KKkU25rADc57WeiM7+1q76I92UNsnnDRkhNyEKbhqb1TdTZsSmmVBe7HrL4Ei3Q7dov3NM2vOte5tR9NFCM3d5xMmmzqzp3OwVBb+rZGm4IYdl94haU0c+NofzpEEaltJJtK3O7eWyu+dlG5dmo6yS8rIpG44UcbayYI1ybIg2mtS+jZZ3NIwtxvgsvUcadOcvo6zsNtHJueqB1wjCDZtow062CCk4vrBeQQIvJHStLkmsTNaI2zLpASWp1Q7D9jgVynTXE+Dc0F4k6t5F2+GAw7JqNKVJLo0irGn6uK5Xa7aQjTaDte0J6S4UIgbS3d3dwLEfWoFzI532SIyrdL/cn+GxwbFuvzYdFVMiht5baL3n+6pgtwcSUQCXcmIDeOEGO/vCX8n69piel21Cr9b2xSZgKFwbHepisUqY+JLFYKcLjyun4Ahob+ZtG+a3jMixntat7RqUEYdwSLzyNdsA1BmgMAyhI8Ty3tYK8mls25EyVWbC930zhKvQMiuSNpm7vcMdwTkB+j2UdleAIozyUxRIQ6iSArNuboeK8GUdZepi7Z1ua0QRcDlPt2vGP9khaSheVrRG3VjhIeiN7kTwdNCzBMq363LKBURKwgLaUlfnLiiDqEToVvEropqO5nJ1UdFrQVK3bsq525aItrBRReCoq1R+lHoYxRjhvtnn03Z9qf08M32iHv27bwhjvlo18jBaVXaIAt/cXAmc5gnrQKemQCLBTjrTARwmfcjHuMOKB1Erj2JVXSm2r5Y7KxB6UHn4JgJHKfpaXxr75E52B3XBFkXUPXW+JERlWut6rbUeAngforctzHryYWvEN6xF77tSxvCLXOgqvz+7eTm5uZgvUzWLr7CGBLLoFHK+jZ3r3UhRnPJPS+Ii8R7p7oemJq5XP6b2kseQ+iU2omnoLKFLwDTgnnIf7XDIV52c1cdKCM0h6fX7SBxV4U6QhFCGMAiWneQJHBqovvWwXZbAwfkimg4KH6+rMjindoCgG8iiyIJBVQwM7ZlMX7NYJO+QtCojcGwhtyvuzp+X+FbzafaqGJhe+pCnFVXQBJUswQpD9OZh2V3NAi6h4bhylbYY7ueDh+p8ch/ZzME5grI3WI2T1yG+UBHs2aWXTNkwen111fduh5gNVcdGWSno0hbI5MTfmkreopZLCycCJEMyRGV/wumtjQ9W7YRjeL35154xN8LxHDSOTYVXRt0JK8pH9No282BT+2KYrcTxYmqyZJDOFtF7/3ojYnQ0g932RnnLdrUawq7sXUrGjFYVRvmEGR04U0cV3RaYxMv7G39vYXewBNXANDyVZKK+nChwJt5tMdpZBVq/Aye+alncqk2hF8S9jcyCPAtNFO534UAwDcx5sOHqhb7i0cv9cI5u8RmkYXQ1/Ho5W50P8Q4C98l9mfUDJnoDtqGgko+c7Q2KBEjr2VJaFwomhvXuJJM3TCTxgJVUvSIajV7hzs2jw3PJ8K005EdY3nOns0vA65W4u0WHXS3Z0cQa0ja7N5CpbHRHJFAs9yptbZWOuQJxyv3Q19fUVrO9zW0LSWsv2LVSa9gXbG9m5bY5733X2zjqyjx35/nvwN7x7jNkPfAKthFESRuYUsPWZ7JG6XLdRWOii9S0vyM1LGSlMMKd0Wq9diadExZfkcxBC9SN3HNH6LsSs2pj6duchY/mHll5eibsCZs0++3qsLwXlF4TunXVWkxRJi0yis65LFnDUZwsqi0tXg30LkcJsqoitdTv6unQu9ZuUPCRzPbOhrf3pXZTottAePfxdj9S+egtU8XVYYNhTbcqRK4mmnYjrkqEYlOUuLjmHjd63PGTS3U/Ybmidx4G1X5zjlpSI08HdwvvLnIIxffoMpwSGgKT4/ZOLQnd8Uwm4Hd5uczTnJ5EIeJluRY2uK9GkEmtsEAimIg0NwEMWiW00iCarj2ElacGMy79cLbuhUD2Uq5UCWXp2FmNDmRwKui9cFJvHpnGUI03sd2gt9zyktipcwfBteZcwtuzM+57r0XF+5FW0OqkWsVqte1ampWpTLduyTZNFKe8IZXfdfRKJ9Rq4Kwbtq2Fjl8Lshwdj+nVuAjanqE0mQgYYV0vhzWh9mWJeXeDuGPrjIcYaKdXVzqom6xqhwIZa5aWDk3dJ5dGoM5lHHa+pJJQOjYYPmVlI1/PpmlFd7PHA6gEI6OcyQVM516yO6EeheKq28c0vllDchkd14YBWMFdjblyEdLLtnFTqEMgkgLn2MEQkCCBtRu07Ihl2Vsdf45pdFedJcz3lnANubVDJFGKuWBQiZRrbsdUuJLMhEj0GykjpaFGSjtOwWXA7xAvRjuYSerUZJm93kfspeK8mhOr9JKmzGhc4Jo+rEPNRIzVsmlEPTzUNHm6I8YxyGVX508CfYUllgAoXhnD7uzXMn3JljRke/rexzy4PZPXirtj/B4OlQONpefmIsRU3RfMygrl5WobXC1lgNa+uvckU9sY644jK1msQvi8j0J5hCkXWh/jAGJqo4I6DsO03WWfdwYr4XfaFlQn3N0SYpPUF7KDkBzHt/CV1Yzd1nZOPMMwf//7y4eX+fbW273Vf/Ww1nxz5v/ZPaLn7Zz3BzMe9xBDN/j00PXpX1ryy4eX1k+BHc+7Xl0xxG83i/7hntfHv7hbN2+ank87vd8eft5n7t14ftL3Ja2CoevbCVhQPB7CADu8oZufEuzmB0l98P7tLc+vJoPPrv+4x/elB7+kXVN34cv8GN/8eEUYpG7//jV+u/sHdk8gB6nffcFI4kvYNrODb3f0gV/YK/KKvfz+fwHYsJoXnS0AAA== -->
