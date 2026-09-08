---
name: "rar-cowork-cookbook-teams-update-analyze-financial-statements"
description: "Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_financial_statements", "rar_sha256": "0ccf19307767552686d84fff02d54ec6b64c9bddddfaed7aa6a4a6b1097394f5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_financial_statements_agent.py` and in the RCI capsule.

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

Analyze financial statements Teams Channel Update — Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-analyze-financial-statements-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_financial_statements_agent.py` and embedded as the fenced Python below (sha256 0ccf193077675526…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_financial_statements_agent.py` first:

```bash
python3 teams_update_analyze_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_financial_statements_agent.py   # or on stdin
python3 teams_update_analyze_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze financial statements Teams Channel Update — Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_financial_statements',
    "version": '3.0.3',
    "display_name": 'Analyze financial statements Teams Channel Update',
    "description": 'Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '647643a76e4243d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-financial-statements'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-analyze-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-analyze-financial-statements-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze financial statements. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-financial-statements-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze financial statements, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art', 'example_request': "Draft a Teams update on analyze financial statements for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-analyze-financial-statements-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on analyze-financial-statements status from D365 F&SCM, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeFinancialStatements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeFinancialStatements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-analyze-financial-statements-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
