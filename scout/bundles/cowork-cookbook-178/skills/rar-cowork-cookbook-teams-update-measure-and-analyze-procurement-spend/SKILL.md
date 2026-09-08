---
name: "rar-cowork-cookbook-teams-update-measure-and-analyze-procurement-spend"
description: "Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend", "rar_sha256": "be00ce87940bcc4473b5ccceb16493edbc7742dacbb69a7f6bd88df47dfe9a21", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_and_analyze_procurement_spend_agent.py` and in the RCI capsule.

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

Measure and analyze procurement spend Teams Channel Update — Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
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
    "card_filename": {
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-measure-and-analyze-procurement-spend-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 be00ce87940bcc44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 teams_update_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 teams_update_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Teams Channel Update — Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend',
    "version": '3.0.3',
    "display_name": 'Measure and analyze procurement spend Teams Channel Update',
    "description": 'Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cf9cd3051fffbe9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-measure-and-analyze-procurement-spend-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of measure and analyze procurement spend. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-measure-and-analyze-procurement-spend-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads measure and analyze procurement spend, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it.', 'example_request': "Draft a Teams post and Adaptive Card on procurement spend for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-measure-and-analyze-procurement-spend-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on procurement spend, with an Adaptive Card saved for manual review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureAndAnalyzeProcurementSpend'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-measure-and-analyze-procurement-spend-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjxprmX9GcjhjbTVWJXaJu3IhBCCFAIAkQCLkcZfZ9XwR4/N8nkVSL7/Xtbkf3p1HVOZIg8813fZ43T/Lbm9W1YVG/fXxTPStfcFaaRqFXL6zcXTDFvagT8FYkNvhZOEXe1pHdtUXdvL17c73GqaOyjYp8nt5lmVVHk9csyrpwutrLvLxdNKUHJDWt1XbNwq+LbLEdcyuLnGaBkcRi979VRlr4BVhwEUS9ly9SL7DSBZgateNDi9pruzpvwAAgP3GLe77QPCtrFk5o5bmXLsqiaRdlCuQDA2jXAhr13oKxanchqEd54Uept7hHbbgQT3zzkFl1kZO8t5xZ9wUwqC3y5m8LtwDK50X7lBi1H4CR3mBlZeo1bx9//uXdWwQ+v3387c1JrQZcensocildq/Ukz2qA0XTu0rmVjpN3+uYFdXYCEJZaeQBmlSNweQ6+l14NTM/AJdfzF69vPzZe6r9b/Pu/J3erDpqfPn7KF6/Xp7f5n9Llizb0Fm1hNa3nLhyrtOwoBf76sKDTuzU23/msARHLgw/Pmd8kFeXi7/O9H5+LfAi89sdPbwVQwZp98untpwWIyae3ups/f5illD/+9CEt7l7940/f5DSdHXtOOwsDWn/4/Pr+EgsGfhsa+YvP6ollXmvVnhOVHhD+nX3z66n6S9zLJZ+fg38syneLP5c82/N3oO8zJ20g98/FAh+AmW8f4iLKf3ytURcg76zc8X786V+JdULPSdKoaf9Lcn9+Cg49ywXeernkp3eP8P2ygF62fZX5r5ctQcL8FUvA8C/LfXXUv5L9iOw/iE6jHFTAl1j+qbg/mwD9ffHzv7TtP5rwbuF/ett6KajX2rJT7+Pit0eK/PyD++3iD7/8DkT/p2LUoqudh4TPmZVHvte0nz///EPzuPzDLz//0JUgi0G9fu7q9M9k/plfH+v8wYOvUT/+cS5Y/5In+YxNX2to8VtR/q/69w8L3Uoj99v15uPi+0qcX9BiNuLLok8XfFeNDdD1Oz/+9PY7QKIcWNM9AGwGon/7t4UUOXXRFH67UJ2iaxcgwG2UebPyWhg1C/B/Ro3aA35tIuDY1ziQ/3OEZ40Lf/Hr/3EeqP/eeaH+sp0x7nP3ALnP2RPlPgMQBT8PnPv8Hdx/fsD9rx8WGlipqKMgAmMWCn06fcqtYOaDaKYHr/HqHiCXPbbee1Dg7+cPiyhf/PrXF/v8kPuhHH99IHv0xEaF4WdcbLrU+zB7wAgBtTztdQBLeIPndGDJtHCAfjNBNO+AZ5oiBczRzt5qkihNF24EkAfQ3YuJuvzjLOzXX3+1rSb8lD+BHFs8ebBZggFf1Vm8fw8M9dMoCNtPueeExeKH337/YfF/F//RrIfweY0TIJhXvICGDx4D9dfNdoNQguADcHnE67ffX+4GYnJA3CC6kR95z8kgfxPP/eJ7dU+/RwlyYXvA58DfWVnULWCHmeoWvL/4qi9YdL4180c4U6HrzZ72cmcEUi1gzldPzmzZgCRt/PHdomu8x6q/2rX1UDEDQGC1vy4k5gTYqkjBr1nNxyAwucgj4P6vmfG8DoTUPzSLzRcRHxbynLGL0qqtMqyt1xq+9YzL3Dm8pgPh1iL37p/ymaYfKfIon6d7wCDgGecV0vePpsApQM+Su82XtR9jrJlTtQe31p/y5lUaVj2HwgFUARYNusidCeNvr5RqwqJL3Yf/gKazpFcU3FdUHjn46hAeqfRK5z9plZ69DfPqbZ69xeJTh8IIvvj/sceaPUNznMJytMZuF6ysKeYzYnO7OZv37FBnVWcbHtX5reX5Amtf0P1TnkYg/erxb8+RD8VeY56ICbzmAkhSHvJBkoGIzXIfNTDndF3P1WN9yr/QyDvglgdmAjsAYICCmvP4y4Lz3S+ahgAV5u/fWopHztRzvOcqXJSdnYIc9D3PtS0nAVrVcx2/wgsKwptr+h5GTvgHq+ZYgbwD8hdAiQhUJgjRh6/Q/rz7RfU/THx2TvOUR1fZgTKuHwKAHt6s4ByqOXBAvfbZ3QM7Pz6EADOysp1tt0EhAUufF73aA7FtonYGzadfvRJA+Pv5/WnpfNUbSlA7wFmgQsoOePdRUzPcZKAvAjoAWAEllkU56BOAU15OeAi0shkgAAC/EvMp8XH5ZZD3KMSZ4L5MnA2Z58w9w7MKrHz8Hke0P0sTIC+bRzzW/cdM+7raLHvG0gbgIVjxy91nc/Hh2R88G5DFF7kf/2n79ONf22E9GP/yxwT4uAjbtmw+LpdPlv5C0h8Aki2fujZPwn7/5ND3Lw59D1Z7/wKd999hx/sHdvxhpacTPi7+mrZ/EPGqlo8L5AP8AZ5vHV7Z9noB5zDvN+Z7fL77KVe8b8gLli8ykG5zKEfQIXylyS9DAFcGNQAwMPhJm83MtndA8A+eAHH5lH+f/nP5zTAWzOnaFN/BwqNfAKXwDONXOgO38has7c4daODNu8BHsTTe28e8S9N3bwBcvb+++5sZLJtTvpm3kCAIoL9rI+/xDdSu+3lW6in6t3/YXO9ed75m3p9AsAWEzaz4buF9CD4s/noWvEdhlHwPE+9R/P2sz4e4AeQJFG/Hcjb3uZWcm88H3g3tP+t5fHyw0g+LrQewNW2+L6IXS85dwne1/owQiIwD/PFuMavbzKwOnDG7asYJqwGFByz/U10eXPb5yWX/rNB2JsA/0N3cJTw98HLURZV2fyr5a//9z2IN0NbMktzi48zw715QCd7Bnund4uv2B9jz2pA+/paQd2Cv//O89ZrT4TFl/gDmgLevk77+acX23n75J72AYg/8BSw2y/qm5LehxWPLNpsARLfPvzD89gZSzwLetV7J9+r5wXAAV++buY9ZgnIFi4Pvz8IC9/4HdgMviU1ogd4TiLQ9GHa89YrCYdtxcHyF2YTjOJ6NkDiFAWJ0ViscdS3HtknKWvmk7a7Xro+vXN+jLBQB8p4F+3lu36JZy1lF4Jz3oOa9b7fBJfdl3tOc2XdfNx+zG15W/vZmkzgYuccbnn6+mCWF2EtjZY+b/fIKQ8PN3KlWdKnS6byrYm13vN5GVe4d7mp3USHVEtOOgr+TEu3eWRcH2Z7OIVQoVNITmZtkyu5onK4iRF27Lc3Wyeo4dX5PpO4RxydP9JJDLqW3zSHq8RHzEScaKYmeJrMSTe24k8m1jonx4O8socjEwXVvIt2ky944+Xg9OfVR8XwFK69tRl54o1Tsw0lG+QSFIxnhgsE++SfF7f1ch5Ys3sDIwDdm1emMELU3cbjLaoFu+b5Ta/EksyZ9qq7mtXINxmRGWDXIREgkLz4om3EnRS2tbqbDaaMsj/2yUlecZEZGV6B8u8wnUo9P8moNIiBMfMHHqsJMYpEE2vIisuItPMGNcI7pspe2MYkX3YQga6e/UhSfEkvIXzUGDK2vY6OUbLrJCDltLsRklgp6Ee+xxFymzgwjr7j1m7N1zVRilLYjX8CXbg3BB4lgiCaR7gU93tXBEBtSmoQIipWjLu3ykW/vF57AEnbZKQFPyEV1PQ9hEnW6SJRbjLWunIAmrn2A3U6cVteLtSyOw2XLSkFyKTdVclQTcn/cEJ0ZxWdm1JnQGTtaORUbZjRKCb6oght1LbITBxsaWZfQu+jgbGj9uL26Z1HpLd/Nro4+kUhpbHNxxyLn9ZVvxki5HC/rPYOXJn83lC6wRtBG82jDcjf4vl1y0BjEFpWwBnu4VXsxdc8Vj4ul4xp5VNmHg6lBDWKXvF+ZpMXQiSCOI1/zroZVrrJLxSHQx/3Aw4Je7e+aoLDeZjWshMjE4EMk4etC3Sx1rRsuu7A2me0mPfEnoux3A31Hp1FqM1Gf0gtTmOhQqKQe7CxuqGkVs9sqJQVVchWnynfHRq8QvXPTPAv4fRNOfRZXYnwc9jsy96wrJOjeod/4Wwmk8/F8WG+8lr9GEbpBmFtzZDRMougG7dGh8qOrrtz2BZqfzbVkb6ee2boajcZeWp0jmBDjANLic9Ky4x1trF0KB4HK3nF1Mg2J5uzIse+oqMf7jM9PPeN77GoiotWlg+4Qc7yRayi3R2N1d3Ix04O6FZoAb3KDCK6Wtqn1sAnPq1Fkerjd1KAWL5VCbBlzf2chqj60PX3qJSsqeWoDU7YwjqFaOwHuuuXdb4sjamPKPrlnhRvFa7Uom73Ki4LVF7vL/n7NA4i42tCKwEUD51o63W/Qzow1SdMicrKlQ6MddvENnTye4qt+f1nKRGXpYjGSPSd7+Vjvw7UE6SblJxJ1AiNaVW1NPq8kPEYN/7KO92djJBH/4OclaalZxU/FyiiWw13RbPdqHqHleFFu/qQuEzU7oaHSpOY5t9FlQcZaeu+yU3hIKtkWeUQcjCV5S4TSV0vrXMPYLYqvpAIJtQ/zbFEcxOLeBKcCuleeKWZ7vb1DwxGtT/tTnlYJjSNu2Vd6K3v2RdtTvtpUmh+yJRYXjYiUXFWbcNxVBFwTYp2F05oqOvWo32/V2fA6Yq015vJ6CdyNY8Z7rYdTSISnPPIgbqsBeOUcyY7o5Zmr1+O0l6aWGGN8de5Rq4sFtu3oXeaZSl8fXZLdivA9c6Q4YCsl3W06K5pE8byuzvzV3Kvcfp1mF4koYJ8buuIO7OnX1EF2SaqZKoEUrvba0AE2T2kwYBqppDciZuWeOQby6OrrfodcRaLAumPsMxABrXKcOmhqh9JxtN9BFk1EnCjKS7G4wP7Jq9cDckV6mrUU6FJRdmzaVwDsA9Tck3VQ3e6meIzXRm3fLwZ7OVJpemVLJozNpNhuTFhqk3Ar1whmU9RqE1FWJl4SXgCGiU1rbEpsrexCPjzGx4IpwlRfjVS1Ls90H9yCQiFELbJH2KEvUeyh5AHd9qoS1M39ELXrQ4eMadpdhM66+9OeVo9qrJ37tj8vg6pO773RJeb9KqfmcYt0hqPDrOUdxAuXkfrS29dLaN3fkcESHN4WuIifbI08iWt9A2mCDDewFw5jGYZXwYp9D4LvEcBleGVJji1VUX73D9jZj5vRP53Spk/PPeahpeESsqZkqAsd5Ihhj3hg4MUBP1pyfDCiYtO0KbI7D83VyD1kT27CquowbYN4MCUc855o1p5GEFA5cDZbJBqvGGjCbQ/CwRG7Q6jrqs+L5UkUKztn9+V9TWmirKYud4xGUeEF4lyDvBhSYY+G8LTCBM1JYSfcs2ufaOUJiS+3fEelnO1ocTu5CSfaibdGnBR3ma1wq4+pnq3bU6TxQRXtzr6S7yQPWw8BGoyYFjudqR4yFTV51imBwOy88dHsXGAbKwHOlVKV7+x03PJpUMKCdao3V3JTk2buom1LdUPHy6zCDMs9Re3NO17J8druc3jbyUOG1mSbRCtdXjPMRt9eld7XY/7CNrTe7TIoum48jT7drLt6u1zSMwYwNTOu4oFtWfmyzcJEtPWJUYLlbuxvZxbXEUWxNoayxpkzSCbU6QPkctBxERVuQrO34OKIlVIkGMp5G93g602JUjOtN7WY4NuBPrE3ShqMpqaOLcLlxyDAqZi+dAI+MuESwXZ9yow8ExEFC3gj24Ig0jB9oshLkXEjrdfRPaw8jZO8wVfgvXKTeNCIbi8NW5Pk/nzn+G0dd5bNyoLO03dVsIRj6qk7D7ak2IuF8/5+3LUnvts6renfEsNGeJakXCJOxYMIYGHF2BKZBkZVXe/+TePELcSVOZ0nW9bgoDPZVLliRxNVjKwXX5j2XC/RK2JqkrUlIxa+4WQ+TiJ5k0JrxQQwgnre1bIj98pSt/sBv+Vl23qQwKPSXQ3SQS/apR2T0YRh9JKETUE85QC0odNhuE+YkC2Lfb2RYkJgB6VZacY52yFd5DKFq9SWGcJZpI6+qDBJHdQwae1F3ZnUsDcYMWJpi1LNgkl1HNdlLGzuO+RMdzG/R6qBydYYud7xXMHYcB6b45Ic+4PAbwaj0larvE+k/TbgvbIk/C3Op16Gx0gSHqO1Xze6EAWBhWowxl+WUkUzN+2Ms9qJbLAblmBuE2zRgguYEa9KWLwS5wllqI4ejgisTfLtjuEatVxLwj3Cd1cDm6hWoVMo2Xt9qxcJMcInHg8aPk2Hnc6oZz/YDmJWd+mVIZFl3zkX9cDruwufgC64aGuEY4TNJWpGJYljHlzAzcs4XvbZyK6zYdzEkHQWj0rakgVGXTkoLxFS9xS2TZQDd86TWpvuENiPVtJpbzPXPQ3zDnbD2YPj87oO4SPVqMLdOclKaN5NMxsZJptW9fGWBa0p4Qw7FCIe+MtE4AK8JU0ud9VrFtucirGuPUhh7TgoqtYd69ntrhuO/UQsqbUVx7uYYPD8jMgEx1lYlaG6i6yJqxThbVB4HL51jTN1yyqOqxC40OsM9m77TQDaR7Xm+OpsJ6F64kdTqJgteckt/lCfKZWkNR0Sws3O2PAW26ryTdcDGD7zQ2gxDnUaQ5NRTak9d8Vh7GuOXJI7RMcyyTgEU7Tay/JYaGm/zocqXBWtsCaQ5RmjPEtgu8SoGgQ02XqL1vaQqCgNHZss3Uj0jlScOyTet9puvUa2WYp7rmoEJq9pxUURBKriHVbM2iNSn89ovWzVoqm6nCXRYgiiC+EMcCvgG2l9oZWMd2vXHJahT4ZKALp1n9QhYinSIk7I9lXYYVWAo3UZTrTQwfIpNiF002hnTDiTx8xWd/DhAm8muckK+na8WylikpeMJAlo2GSBxh9ONzrP2ps9shQaEjdX0QYtO3IuLW9Mxbka7M4Nqy6U88bb6LUi2ozS4fT50B9UOjDLqtVBE0YZGXPggoOplDLWRJDDRkN5VNmwPS+zaOUIpyEoxMRgTgqgwniq422eWFq7bBmDtM7IOlwfmJBNWYUdjOJcynDUFQhiBEJdMFvmcnUlZxUcCbsj7ZyDJo4Bvc/2gMgr69qy5T5o7tBagZFDlgsc6xHhLiHkzep2920XaYZy2aCQbssIdUv5nT2c76gEMfhE0NaQVeqt0r3+4NT6WpNJssyhBm36brJVWWNKxj7sTEjRtZ2a345OkLVjZd0jI1yRmlYmZ7lNad4TIF/Mpxs/gsbEuJmUyJZBKpegWYaH0xTYATzurnpxy73e2Lb7JWjVSogbt3Xajid2g+181+JXxrm6JceKPfUxlASJ24tJS5/WB0TqOBoOzCQ8t22zPUKUF9b2SaYRgRLNiydwQnTBiCnKeMFqIDMQJTgSdlubL64qHMTnZp/piSz34cVr2/2OgsJop6V43wcCtjYYstkEKLtSRgpNGBJnA34E9NYx2dXQ+4yQKs9T4BS/gZ1Oe3SHhhBMR3ZtAz7cGnc4S+RlBR3J9cHIh0zAhHZTFtdwLcqhnWlOtTZMfRWTnIa592pnLS39OiLnXdy7DL60y0mUg/VwGIqeGLDbyjwup0LjIIhcrwK0yOU1ppVu5VLa/TLlpZrWmJL38bjBK//A7JlVqyPBsrU2F/e8kUYAFJ4OtjjafmUObnpyB5isz37KpOQo+6m7WbY9Ii4B1TMua+933sktzqGYrbhCRadm2timUDoZ4d20aCl1IHcpIbud5ESCeusO9ojXdGgmO9cgg9vijqeiV5lcXan2qty3ZrlcXk8+tNnXO8NJQBuHLKFDDlt0g+ytNsT7GjUguEBohSSwyr5dxPPdPQ4mPRgcfQ5BP0Aky+J8lwEYrJKiXSlbp7CNiPeGANpIiWLYfRxvJ/U2mU5r3XbqJE9t5Ub03ZZReJ+bajvWd25f6Mx0WLdEMOVHtVFNzzl2xPIeqo4hWxcXhVt/nQb3JML36BIKYQSBSURVjsBS+0gPpw6Fxxt/2vOXPNZNXIJSwZlOXWITXVImp3TiXNdxuXs6UrvakqnR3ZMXXaz2iLO8hZ03bYP6PPGB4h8C3PaPFdOspBUeCkHB2haGMEyXIeFeiGJ0QuqrDhDWr7ibU56Fg01tzTjMb1hB3QgNgF/Ebk+TNd3WuFO61x0c7qNN3EaCmqqJyg77YTS1dEOHlwDiZXoKu3TXEiTOq0NBXuzMELKSx84jvWmtC7rlI5nOTlnbcNs+7GCCYwsPbYY17i0PCBwn6Y67Cb0/2JCnCTDpeQSRnHan+/WiiNYmL42ViWjxfkNG8pVqLtKRyHU827ty6Kf9MVV1sa6LiSeXDo8zx9IOLSLLPArwhmmYEdHTY5wWnRDcSGfKNevY2Ku+AYSwDvYZYt5UKtwefJlyN8ZoYvU17diVqwyb1HPPtokOOi5DBV+RPR2CmpsaNXVWI9gzNHuxli1z1W1ZbZu7oim7kMNQpsZdLpxN3JDCbbybraYjxxUOlrN4lwU3r0fHYT3WNHtG6B0a55qObukGULgKqaScGBvpFp9t7ChVUCXjWeGXRXWvpnuANYVWWfVSxWUSoVZX2dDQ1kNX6XTNjcMF05r7NPk5VaeYuD8cFHaql26nY3KdxYWHCX4WEVpWHOEdTXko1nX2CTpA5MpGhfoY6GHqjqTVpa6XDtCln6yr3bF8B3jhKNo0d2JRpPd9uxN620KuK9Y6chaOTCMeHeFrdTxInhxRjFutm72jKwjYlg2qTTD8zlCrcHPTiEO19Xo33jVykHI3bY02ELJh1+5pu9Ftusx4XJAhp0ji1XGfLJmjc42rHSP5OGjRo2J9dzZhWBBwwK1IC9s3Tl1ftyqxgR1H3UPG4NwIKPLTsm5Zt0aO66t5PewlLfWwzTU0NEh3V7tr37rZ+oSdleLQYfKwRYWEL7PxiHPL3RbwqM+tKieW1qVniFsYp5J6eZBXBQrXa7JzwP5Cb2tjJe+7ZOVdgpu7tgD3WeTFEuWVC/CgmIb+YKhtg+rthfThrrmkBWdR2FZKfJSwmVt7BslsmDCZNiYnT6WEYlzluWv4tpcoBXRXZoaPKoUKhFPEm2I8nsMlR0XY9jpNNMlg+jgalOgIBW8ZIakF/e4QXHTOT/3CHznEtXbpxqPtfr/nrdvqII+cfG3rlX68bjuklaiLZ7HLkuG5dj35YncNqXF1o7z7WqG0W2pMRLHltweWS+TVYX+iBR6XudtyCYH0dHvkoOVLgo5I8o6ZW1HxWmDE0p6sCxlOLXZYuXDcq2moCbi/S3pkAtmTy4KzsidaMqDy2ovOZaDOB3M6yPe7lKkyKYlIHdvxYQ17mD2NfGwupV3WetR2RENn3Ec2frikEU3JtKkJcQG1DolFweRfbyw1VQ49kGeJD1pqPJ0ZxSQIms8ib3LvDb1tYeskr3N0pdoX7JRJzYTv+NvJiMt1bFhcA5KfOtvwmWRi1BALb1BPDFlj9Wm7FbtqFQGbEwrTMx3TUXtw3GIJGZUPU8t8lJc23Cf2cii2trBEKWYgpey+FrK9PTa73hZujrC7uAiM1E4pJ73TxR03pHvcw0EzOcrurdbBXhq3a3rCSMyx9dG2iMuNCK/RkryFts+ZG0NcLvuLtz2ccj+59rbukfH10rarcijXtCMsmeEKGwydMtg6yxyhDMRIErTrWSGcaymXYONw6CprbeE7ZkjwOC/CfI0G9mVrBaK4DUc/pUdmzG7IalQwRrn2MBR20+ocYSS1RA6UtT0Hy2HSsFirPTyF7LDc8/vSlJBrR3mb3Esn3mW7U+bujkVUlvBG0/Jk6v0aAFeKERTnb6rzEaONclpyoU0UCbKPIORWLhlvd4ddd7sJCd2JCh1DynzvwNDWk8Uz1OYJS9P03//+9u7t29Hk23/jEa35bOZ/7BjoeZrz5UGLx7maZ7kfH2t9/O8o+cu7t9qJgIrP47Am7YLXMdI/HIa9/+tnrLO88flk1Jcz1OeRcmsF8zPGb1Hudk1bj5+bIn08igFm2F0zP4fYPJQG798fHn5v6Lejr7b4XFqzu6N8fsTCc6Pn7flr8DovfPfmvp4S+oyRxGevLmfLX0f3wGDsA/wBe/v9/wFe82X+Ii4AAA== -->
