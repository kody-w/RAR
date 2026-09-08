---
name: "rar-cowork-cookbook-teams-update-report-production-output"
description: "Summarizes report production output from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_production_output", "rar_sha256": "c8d590fac3d3867e3037134c3e83474ab22eaa593d14ff9d7509afd59f1cd0f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
