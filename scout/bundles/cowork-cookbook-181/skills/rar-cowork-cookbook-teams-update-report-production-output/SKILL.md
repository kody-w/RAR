---
name: "rar-cowork-cookbook-teams-update-report-production-output"
description: "Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_production_output", "rar_sha256": "c8d590fac3d3867e3037134c3e83474ab22eaa593d14ff9d7509afd59f1cd0f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `teams_update_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Teams Channel Update — Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-report-production-output-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_production_output_agent.py` and embedded as the fenced Python below (sha256 c8d590fac3d3867e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_production_output_agent.py` first:

```bash
python3 teams_update_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_production_output_agent.py   # or on stdin
python3 teams_update_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Teams Channel Update — Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_production_output',
    "version": '3.0.3',
    "display_name": 'Report production output Teams Channel Update',
    "description": 'Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3309b69370b3f64e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-report-production-output-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of report production output. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-report-production-output-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report production output, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi', 'example_request': "Draft a Teams update on report production output for USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-report-production-output-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on report production output status from D365 ERP, saved as artifacts for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReportProductionOutput(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportProductionOutput'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-report-production-output-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
