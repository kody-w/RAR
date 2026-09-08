---
name: "rar-cowork-cookbook-report-develop-campaign-themes-and-messages"
description: "Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_campaign_themes_and_messages", "rar_sha256": "0b984421b805237f302f2d42d71d2998ef16f76eb19ae17cb4490cee66c82877", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_campaign_themes_and_messages`. The original RAPP
agent is preserved byte-for-byte in `report_develop_campaign_themes_and_messages_agent.py` and in the RCI capsule.

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

Develop campaign themes and messages Summary Report — Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
    "output_filename": {
      "description": "Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 0b984421b805237f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_campaign_themes_and_messages_agent.py` first:

```bash
python3 report_develop_campaign_themes_and_messages_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_campaign_themes_and_messages_agent.py   # or on stdin
python3 report_develop_campaign_themes_and_messages_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop campaign themes and messages Summary Report — Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_campaign_themes_and_messages',
    "version": '3.0.3',
    "display_name": 'Develop campaign themes and messages Summary Report',
    "description": 'Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-campaign-themes-and-messages',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '11c7817c9b272270',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-develop-campaign-themes-and-messages', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop campaign themes and messages stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop campaign themes and messages for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-campaign-themes-and-messages-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop campaign themes and messages records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of develop campaign themes and messages activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a develop campaign themes and messages summary report for USMF for the latest posted period as an Excel file.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-data-modification Excel summary of develop campaign themes and messages activity with totals, breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopCampaignThemesAndMessages(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopCampaignThemesAndMessages'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-develop-campaign-themes-and-messages-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopCampaignThemesAndMessages().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVrLmX9G8N2JsX6oKhFjrRkcMiwAhoQWxCFwdZXYQq1gFHv/3OUh6y3Z39Z3rmfk0qgUB5+SeT2YKfn1zujYu67fPb+fAKRaik2VJHNQLp/AXXDmUdQoOZeqCfwuvLNo6cbu2rJu3D29+0Hh1UrVJWYDtbJdkfrNwFnXg+B/LIhsXTZfnTj2CK1VZt4syXPhBH2RltfCcvHKSqFi0cZAHzYMbODZONJ94bdIn7bgI6zJf8GPh5InXLFYEvhD++5lTFmEJ5FtESR8UiyyInGwRFO28YSZTlU0bgENQJ6X/YVF2bdW1C2fmsVjfvSBbzEo99BmSNl6cn0J+WPBB6yTZhwcRrayWyKKJg6BtPgFVgzsQOAuat88///3DWwK+v33+9c3LnAZcelMf+vFP3biXatpDM6bwlZdegEzmFBFYX43A5AU4B0ICXXJwyQ/CxevsxybIwg+Lf//3dHDqqPnp85di8fp8eZv/qN3Dbou2dB6qek7luEkGDPBpwWSDMzbA4m1XF7M3GuCxIvr03Pk7JeCDv833fnwy+RQF7Y9f3koggjP788vbTwtg5C9vdTd//zRTqX786VNWDkH940+/02k69xp47UwMSP3p6+v8RRYs/H1pEi6+no9r7sWrDrykCgDxP+g3f56iv8i9TPL1ufjHsvqw+D7lWZ+/AXmfMekCut8nC2wAdr59upZJ8eOLR12CQHIKL/jxp39F1osDL82Spv0v0f35STgGiQCs9TLJTx8e7vv7Anrp9o3mv2ZbgYD5K5qA5e/svhnqX9F+ePYfSGdJAfLv3ZffJfe9DdDfFj//S93+sw0fFuGXNz7IQCbXjpsFnxe/PkLk5x/83y/+8PffAOn/LZlz2dXeg8LX3CmSMGjar19//qF5XP7h7z//0FUgigMn/9rV2fdofs+uDz5/suBr1Y9/3gv460ValEOx+JZDi1/L6r/Vv31aGE6W+L9fbz4v/piJ8wdazEq8M32a4A/Z2ABZ/2DHn95+AxhUAG0673Eb4Me//dtCSby6bMqwXZw9gHoL4OA2yYNZeC1OmgX4O6NGDWCqbhJg2Nc6EP+zh2eJAUL/8j+8B+p/9F6oDz/R++sLur++Q/fXJ3R/BXD59R26f/m0ALAHkCOJkgLAssocj18KcKdoZ/ZVHTRB3QPIcsc2+Agy++P8ZZEUi1/+ApevD4KfqvGXB1YnTzRUuc2MhE2XBZ9mnc0YVIenhh6A/uAeeB3glZUeECxMAJh/ALZoyqwHSDrbp0mTLFv4CcAaUOCexQTY8PNM7JdffnGdJv5SPKF7tXhWvgYGC76Js/j4EWgYZkkUt1+KwIvLxQ+//vbD4n8u/rNdD+IzjyMoJi8PAQnl82G/ABnX5WAZcB5wN4CTh4d+/e1lZ0CmAKUa+DMJk+C5GURsGvjvRj9LzEcUJxZuAIwNDJ3PRgb1YJG0nxabcPFN3leNnitGDAooKNRVUPhB4Y2AqgPU+WbJomwXDQjLJgQ1s2uCB9df3Np5iJiD1HfaXxYKdwT1qczAf7OYj0Vgc1kkwPzfQuJ5HRCpf2gW7DuJT4v9HKOLyqmdKq6dF4/QefplLv6v7YC4syiC4Usxl+RgNtUjYZ7mAYuAZbyXSz/OPgctDKj2hd+8836sceYqqj2qaf2laF7J4NSzKzxQHADTqEv8uUT8xyukmrjsMv9hPyDpTOnlBf/llUcM8v+VdufVgCyeXcTiS4ciS2zx/287NRuGEUV1LTLaml+s95pqPR0295ezY58t6UPksn4m5+89zjuOvcP5lyJLQPTV4388Vz7c/FrzhMiuBgqojPqgD2IMOGym+0iBOaTrek4e50vxXjeA0IsHSIIoAHgB8mkO43eG8913SWMACvP57z3EI2Rqf1YbhPmi6twMhGAYBL7reCmQavbnu5NBPgSzH4c48eI/aTW7ALga0F8AIRKQmKC2fPqG5c+776L/aeOzVZq3PNrIDmRx/SAA5AhmAWeHzK4C4rXPdh7o+flBBKiRV+2suwvyCGj6vBjUwa1LmqSdMfNp16AC0P1xPj41na8G9wqkDjDWM0g+PVNqRpscNEJABhCvIMPypACNATDKywgPgk4+4wPA31fn+qT4uPxSKHjk4VzR3jfOisx75ibhGdxOMf4RRrTvhQmgl88rHnz/MdK+cZtpz1DaADgEHN/vPruJT8+G4NlxLN7pfv6neenHvzZSPUq8/ucA+LyI27ZqPsPwsyy/V+VPAMjgp6zNq0J/fKHBx3c0+PhEg4+A78d3NPgTi6f2nxd/Tcw/kXilyefF8hPyCZlv7V5h9voAq3AfWesjNt/9UqjB74gL2Jc5iLPZhyNoCb6Vx/cloEZGNQAksPhZLpu5yg6gsD/qA1DvS/HHuJ/zDpSfIprjtCn/gAePPgHkwNN/38oYuFW0gLc/95pRME96jyxpgrfPRZdlH94AWAZ/ZcKba1Y+R3kzD4ggnwBwtknwOHOBnKkP8virD6K4aJ6t26//MEfz3+49ou7bJqBS8Cn6NFdmp27nUvcB6NEGUTmjLehkKrDl0daBxaD+AGHasZqFf46Ac9P4gK17+89MD48vTvbpBdvNH3PhVevmWv+HlH3aG9jZAzp+WPhAlGauzcDes/pzujtN+lDiu7I8Ks3XZ6X5jhXm8vSnYjQ3Es/C50SPDH/ZQz8rwncZfGuf/5m6CXqUmaBffp7L9YcX8IEjGHmAWd+nF6DWa558/AhQdGBU/3menGZPP7bMX8AecPi26dsvI27w9vfvyfVAx69zXD6j6x+l+4ey+r7wpe9fSPaPKIISHxH8I4p9umfN/btmelb2f5bi+MfCPxvr2X4kE+iB/CB0ugzkU1s+YiGfW0YQEHNJ/FPDsHB6EE0zQH+HN2D+KCygPM9m/d1fv1utfAyfDzEzp33+VvLrG0gwB8Sb80qx1/QClgMc/tjM/RkM4AgwBOdP4AD3/m/mmhepJnZAMw1oIS5NYRi6dCkER1dkuELQEPUx1CeXPkrTVBAuiZAkAndJO8GS9FwMoxEvCAjCo1CKJAG9JxJ9nfvRZBZvlg1Y5SMAs+D32+CS/9LrqcdstG9j1Kz/Sz2ALgQGVkpYs2GeHw6mly6Mke69vkAXhLpng9lVgpugKa7RY30RSGHlenumUOOgQsxBMJOttM61Sk/EE4Q7l/N0iqFIo9OCKDRlEtaZ2pEbDSetO7+OEpsivIMGwR7qmhQ5sbk7ns+2s9vup7Q0blmZTburf0o08cBqd7SjDgcKzSfOAmg7Xof63EvHHqb547bV1/nB2oonSyMVBD1VrXo3cmNn6ZQmrQci1g2i9pLcVF1Ps/cRstq2uySZaGprkBQNF5VDSgp3Gyc980bByrzYyk+OnmrJegwIY5ec7tYtGb3kRt2obWpsHOxaSOPWTg5d0wn3FHVMzOgujmvqyZSf7FuuceoezyBPkU43KNvtdFjk7zQU7loK94+rCYHXFAQHYYgGS4gykUa1zVwGklpZ0DXWxmXNXWaKfb8bMGNLsBlk2YdkLHR5NAcxMUrdPFC1suKqdZeL1poxMkNnyZaCQq9PT/hlGzX5DYmD/hwzHZfqowhsZ3BotmvEoZO3ghHn61Q3L7mwzOnLDln2Is73phN2vsA2ueCcz3F+jmoLNBKMAtWqs0ka+zReSk2VL1FiuPKIjKNR7eC6tWqzDtETsRUShLWjk3zBujUWN0WAHODjgfJHJ64MY5fnnCZbmu6Y950UEabMr8Vbzgr8aTOS8ikh6jWb+woD33uq2qD9Kd7FZ9SJye3puLS3t+XulthmMW2DHWmfoMDqEV0iN7Z+Eq1o4PPmzl2cCpE1O9aOE6Omre0K5xvFX5OVdrh7zGEfIyk33cSrwcC3amXVirhshOguF6lGIXA8MCd0kq2wMkCMlcJmaPl1vtzpW2RfnxiBGJ1luDynJ0IP8kzoGuVG5qvDrdue1zsQetNkQGI5NWqlZs7xSo0W3MXeENNBdIWWccfJVuFt8hOyOyY9IvJn2EFbSm7tLA96e9SL9XpUyAmDxsnKYkOmrAmnnRanCPAPHOkEdbIJgqyt3XkTdRGUfZJZVzyRYxjj4UEKYCV3shCREvt+KFYIDGvLgG/JbWadw9g8mSZfu8P2vvGN7n5iuR1XmReoOe05b2fcUv40mCwVn0ekQOFYlJK9qqdqRDhqumoFYmL91Ljc6oO0bFlkDLYKiq5vjn27nALZBLQrMeBaU98GUskPG6YL+9OZCxK5YV1vp62DkxVcj7FgioGG5/4amqwcv64SeTi7mB+Kd2NfWERzibZ1RvGVrLEE57EOdjyN7e7cqJvCE3C+EiAcr6VzEO97pg51GXKUXLbQgdS28Kqckn0+NcXRJTzb7fAqjM/5Eb0bXOadTBcdLOI8xWc+8ZNuGyFIGZrMSc7jNU3Y+aYIz11DKPop4w52hoj24CXbM5UeDb1SdcXaxh0O1SgPZ4Xd2GrMxOW6oTrJa2I1hjlQE+pzda9GB1ehOt3Lic7VsogECCqcqqKOWEnRd+JWUGo07im6xLwyTVPd3sih5kF41cD5SXVi3VZhrUH20Ga/MkWKMsgcJjhTWetj7w/Ha3xN1TByr1QxGChs5YHoLKtEpPnkupc3S0rvrJwTCFWFRAHl9nu1dThy4yfp9V4aTlbjSwO2EUWEvSUeM5K+GmBhqY5e0RVqGt720ebWXbgBXt6nSCGzVplAU3kWi1hiRPrg9RvZF7ats8cl9WgEh97r4aHAy1WQqS2fqHvGu69ZXsRy/LLnpyJP5vqsadQEab6NKavzde0dszUj4bVeGHzRs3aKH+/usWdVS92QyIHDFWa4RuvsIA6Ix+AWBhrlKtmToVn7JM7GrL0ZVSaaNnF54xAvL07qersO1oNFpltP1Ip+h0anjDmzPF8UjXHbljuOY8/sgSSzYKB49eBuWQGVXQvWbldfcESUvmUhA92HMhWdmEKXO5IjWpNbOogKGxYKyajXNlNsy0Ka3BVOPftwUFwIWO4nfMQxy4Y2Ck6LmZnomOU1k2aTglQryoncUcp5T6/gU7IRV7zWluo9QtsyVLEJYDY70RO0UzEkOErXjmyqA3XIpmliqMy8M5wkqrv0xHs9E2m7cwHgxjirhslB/NXlqVJeCpprD1xndxt3I5kUapyye5cwBxE6jZDEJqVrMJdxy/BExojEmYFMuVSSaOSkTLAbp8p1tHWyeBXHEuH4MMrkaNocRVKn16t9taK9TF1d78XOPlTsmch4MdzXohFmbefBW1RFxbqYqP14tEdZ6jBoexuZsrRS2jG267buJo3jqHq3T+WDJq5li8MtzhrW1w0X5gnexJYFKwk7EpzM0ljDMRx1JFfGDS+siDxz14SgwvQYV5POpo6CpZg4+ANS787HXbnJCHPCW3rQTxvMGDYn96KGpRGIzNZklMNW2BYn/GpynBy5lLmVqNKUiyivVdzDhdhihFxuz9leHu16U8IZ1A93eXNbnVnbuWwkhN1chiMcHAcnERJqnWZW5UsOUiq8vY6bTi+ZzIN328yxD5IAisLZU4f4zvF5ru2MjA71GWvQwUTv0fayLi30BBGkcmmSQd4leHngFaK2Sbk4WdGFon1nE3ut5FS94VyiSbgkjZMny11cBQeDUpLS0dzBZJjyeggcqOJ0REfSzf0kUs5qgq6qvirHlIU3cXOpd1vsDOlLs2+iU4hTFxYATZWf9MZuhhu113ayl3ACfywB79y8uamyWVO7SBkdXuxICbliLrZn5CVbrJp+ddIUj6XvjqNQ7lVvgo7RlHPXpRuaDo1MyKFiOXoNpjDKjhrRMBR0VDypET7WN4huN+1Jdt1zeBb07bmR8BwKCgHHbLJB4aja+BjhdM4WYi98nx4jZ2/mwb122ThNr153UlmnNJhiwm6GkjauEfWbBkuateuzcp10idFQPcF0Dp+4amQym6Hz2mytpZwHuMk3YJzxMpkGKa7XlhGl1BY3bZ4fBva2MW11OHDypeo2tL2Zyl6iSLWNN5GDainmgn6g5zWcgU7tgd5OQSGi2FJCxIFJt7LLNfGm0vMrfLbQ6CjVR21vChkf+ns0hMMCNdT2LPAtUWD3LaemcIjQbasXsRnhlyMWr0HrqAt0GtGDCF3YlSHzu8qHAg8rl4fwnGmHVGa4q5+iwlnmzSQdTkgd69itQjf6Muc2LUC63YYBnbToHbcR2w39zk5jNFzuaMDhNFpaX9bSquFTe2MVUXIRE39g7eU1ucndenB3Qx1kUrDebfqmXdJGjLXdaPAeeS7ZTghKQ97dCMw0txud57hdB+r4NYoZBl6zmGdkh2K3P18mTunvpjlN5kjx7nYyEnSPiKuaLnjhonFkGcCHC0kNWG7iLHEKuOt9XRn7sAPDDp6GKRXkVxaDIUVaDXioqSSMHJOQZDj8di5aG0eI6Z4YR80xWJihZYFhUHbgT/S+JrrzfXNkg8p0EW5t3JlGtJfHxG/xfVK4xrEWXeG2PGatcAEdUawXArTC5BQ7yOOVE+u9d1MpUGpBd++yWZVU3dZAqiAnrGZ1HDE1uo5hXGnjUPAb1FSuu41PT4QqVQEj3uKOsUcsO+mQr5M+6Edca+cmo8KN3tIQrJ2GwlBi7HrqzK38/AK7hlpJa7S/rlGpOu7lVY9F2+0QUEh1OiVL49YqHk2o+zYeQb/ZVvopzOt+RIuY2zbZeNnhKolqenkvw/M4jie1CIjTfVPKCARaYXWggmNpiRfCUPXG1Gm91cHYtDwQKG+e92Oirs/wiHeMk+PDxuwDXNqJ13PKX1km3Cz33Ijowyq0SDCvsNxBqQbuqPAuGntLHxpRHNOpzbrZX4Fbkx131M8Ty+zc0CPOgeqFxS7WEhetA1wTEGcf6RAVTwwuAAQ4M6hJIOfRR1LQkaC3oW5M/KCgIRmuN+rtoBLx2Id5TELy6t5b0qbUKUdeIwfbdseLxOM3lEKkCwqB5p2hSg+ZsAq1i22uNxZ+iK6WGCm7FjSx25VIWwJbhAJqu75H7UbGY4tiJ0mWKa1TaN8soVOEsubWO7IC4w0Eo+pDuGav9m3c1kodW3RdqjlRNgbpRvWaEfC9eiwlmT17VSk6Fjlpu+00l8IElhPFz6sbRabRMYR037HqEgNtD3MCs2GorSbFCTBc3pn3M8JgWLSLNhnLSWiUQrzjlUyfp6g1wc5SoXzhMnC1xFplaZy6Hd8hRzDZ6OzVOwGRK5c+nMTQJLDL5Wi1cJGyWX4oEujeba0yMpVbuhy6itFhae1xV/pI6NcMxbcqdVbXoOgJh2653zfjVffi5cpFSQ7FN9O9vK/OtoRepvuNULi8TDHpxioaaL32RL6/JpEihbVUREMlSgyU9AoXlk6/5m1WYujt0tSCFWieRjQ3d2x+4pdr0uC1A8wVzMXBQG25Ee2q3t4KJ5ycLRhDnZVk9eWlCM5s2iWJ1vV0pNGTQBZjhlDFCBnjskWks7OJkHyUeGyKPD7ClmcUd2pVXR2yplfMHCbjsdmnELOjyx6nUbu+HPWp0cQOwqhdSlZ0ue8KQzJIIruerHAvmr2TQ+NxIw9NQm88REUaT6NrVlJbwT9IFohhwxPI7QrubnUi5QgRw9I+7WTcIDJbWN1luDQw86a49nWNr+S6mWRZDdc7ob6gHN8WWcysZcfViCXlSxKWETg8tEV1JwKiJJndsDl00eTRdaIfT9AR8kZymdcX/95M7iq8V9RuQPy4ZzVPc9rb3QFocwkFGO6OPcTBptIUcg7QCMau8NVgOwWXWt+gg5gytntkQ6h2vOscI/EhDXRxV+3IOD6t6J4XcqudEKhLKD/m5ATHW7K+nu53idpLG9CbnA8sbuEwkluwWJvZzTHdA52pza462y12PAxL52AWCjkeyJ3X4tH1qgD7u4EnXEf4Gu7vm1UVrvwzfRxNnjkt23KCJ6jrOljz5DVpUssWY9cQ6WpyykBNfA72BmNrgypMCkSofQdvczmo9/ZyeUdcptCQc1uuVjISlrc60IqlBdtxDOc+I2SskjOCkvMxTRMYQTbTMRFzLiLa+mJuiHF9KEExhl3FbH1zhPd0aVd3LTLN1Y27S9ph7FVoGjtoAAOHGOZVPpEjDvp4zJQqbiWyUs1pHeg0zhQlsoQJlxs+6bgo5Y7mwSrqenk/reKL3l5ypwHj6AqP11I+yiU3oNv1vheHxpSamINFUU89tMEh7DCxMtL3/FnYn6FavhCNxN8xmipWYbiVyt7gmO5yT1KyoznPlS8RSOZawEdFovgInupbOsAIKnl9PiXIsYWYvnd0rYikO768D5f9RV1tAjeRa1DG4rKzU5ugVoW2PTSkXnRWi8XRJV9ZzpbqpjDc+z5njvqyXtWcrI9Fct1iBAMNe8kdXB/TDCPg74edNXlB7pM3/ErNv//vXYtMTodJyn3HOfon40SXlzW6NG1cxmsfumRuEo+ieAsFaYN1ZmkHPTTcvXvA3Pa3eKQdADJgsAzORziC7HPqLdNQwLwNdCU3/c1Q6x1P2pCS9N7A4hFaN6TdXrFVraF4wNpHZ4njUH8IAnJbQ1crXuXQkbzsOt27VOxpquGwA2FqM72JQmuOdWnUSWm0F7cEaGPIUIqPqwt1Q2kaEaLLlujXVHbdQ9l91KE9xepJIsOMC11zRq6H/V5B6T6+qmCINZylNAm3bm9hW8FH3Lad1CteXeSwv0gMnGyPHm13Rw3eHCI3SnGVtTV8d+OD3r8eGnFwrkqLuuZRBeP7sY+ZpI10xPLTnGZ1R6VDdA1zrHcpbgKnhBijd0lJjR4bxyWuJwdl2qDdSHXJlF4AxPLrKFQL07x72DFJV9IZTHDkRfTJLsqNuKw3dLHS77kGOzc6IdGiJQnOZjxYmOQOl+O9eooO925goKV9aRNSwgjldmx4NdseSZI+YbDd+yKahVl2Cgr23PbOxbbh6oAYG/ESirHUXVNCEUS6y0nHwK0pq20Tdb3JOBSg/TJkh817f5hkie7Me+7q4h70pccD7oqgfBHTvr3fClCRc3M66kFrmlXHpZ2fhoftZnCUa7oJQc1vhyWVDIeoXXpN1p8LzuHErAxSjEc1TBDOOzx3Tk3cXsxrteFH3h8w/OodERt0f9tlHxLtoBN7VzsaUn49kt6VrSEFHm8ZFnod7h2swyHUUaeLVgCCNrbFINfePpFYLAsshmhXuAfJ6sIn6xTSogr7uTuwmdWbuXcN2qrd+RZ5JzO8I7SVkd3dLXYUst6YVsqRP8jeEl+p4jbUjdXKPqyDm9rYywSzTG0jdlXiCMv2foXA1Jbg1LhBjxNfLa/LMgiW5N7z5DDtzqjCILp8VdADwLTV4dDuUijAZFeycFYdT4rX9DS3PnP0iZBLqSDC2mOwPdcO4Z5uUpQMzOMh0y28mLQ7GLelGpYUDyBrRxNMGMXIXmgU34ITDNvdjueeajc14XbyjkTvKxzNLr5m9wpNXHvaNhK4pSAPRrnU2cMlwrYEXdMcjikiFqwnvsUFcdWmTa+PtwNxc5adUozA1FE3QVJiVWAGFQrXmbRadNpBCvg+zDrcJK9oO10nTeyFI3XnzW53H4cTBC17GuWsY7BuAoK+IJNJECuuXvlUhiDI/ZiSEYPgUhTJpxaWKxAYFldeOX2JrCE9QzXHk9S7v5wu10tU6oqkBHSq0DnCW5Gr8+oQCjJ04jau6BaXYit5+3XQh6To8j1HhtUKtvpluWf5UDoeu73SkjcDP2wL7xRk0dUPyIwS/G14sDg+gFNE9u+701RyuRT3R7rrHAzkd78GoxfOEAD20r4l1j16U7cRxdyuIXXyL1qKW8GdxGShB0CLke51cCmGEBKS3y15hmH+9vbh7fcHeW//Jy+xzQ97/p89V3o+Hnp/F+XxsDJw/M8PXp//j6T7+4e32kuAbM8nak3WRa8HUv/wPO3jX3gwORMan2+LvT+Rfj5ub51ofsf6LSn8rmnr8WtTZo/3U8AOt2vmtzGb+YVdDxz/+Az2yfvt8YTbC6r2a1t+zZ06DeZrSTG/dRL4idMGr9Po9aTxw5v/eh/q64rAvwZ1NSv8eqkB6Ln6hHxavf32vwByqIywJi8AAA== -->
