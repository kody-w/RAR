---
name: "rar-cowork-cookbook-teams-update-analyze-background-job-performance-and-history"
description: "Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_background_job_performance_and_history", "rar_sha256": "bda4d994056efc225622f60431b096f13e9377f95fb60bdf9e818c0582a974a7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_background_job_performance_and_history`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_background_job_performance_and_history_agent.py` and in the RCI capsule.

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

Analyze background job performance and history Teams Channel Update — Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history
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
      "description": "Filename for the Adaptive Card JSON output, e.g. teams-update-analyze-background-job-performance-and-history-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 bda4d994056efc22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_background_job_performance_and_history_agent.py` first:

```bash
python3 teams_update_analyze_background_job_performance_and_history_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_background_job_performance_and_history_agent.py   # or on stdin
python3 teams_update_analyze_background_job_performance_and_history_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze background job performance and history Teams Channel Update — Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_background_job_performance_and_history',
    "version": '3.0.3',
    "display_name": 'Analyze background job performance and history Teams Channel Update',
    "description": 'Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-background-job-performance-and-history',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd845f5136e5d9013',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/analyze-background-job-performance-and-history'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-analyze-background-job-performance-and-history', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON output, e.g. teams-update-analyze-background-job-performance-and-history-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of analyze background job performance and history. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-analyze-background-job-performance-and-history-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze background job performance and history, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams update on background job performance for USMF and save the Adaptive Card - don't post it.", 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON output, e.g. teams-update-analyze-background-job-performance-and-history-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on D365 background job performance/history, with KPIs and quick-action buttons, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON output, e.g. teams-update-analyze-background-job-performance-and-history-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
