---
name: "rar-cowork-cookbook-teams-update-analyze-financial-statements"
description: "Summarizes financial statement analysis from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; art"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_financial_statements", "rar_sha256": "0ccf19307767552686d84fff02d54ec6b64c9bddddfaed7aa6a4a6b1097394f5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
