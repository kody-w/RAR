---
name: "rar-cowork-cookbook-teams-update-measure-and-analyze-procurement-spend"
description: "Summarizes procurement spend status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend", "rar_sha256": "be00ce87940bcc4473b5ccceb16493edbc7742dacbb69a7f6bd88df47dfe9a21", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
