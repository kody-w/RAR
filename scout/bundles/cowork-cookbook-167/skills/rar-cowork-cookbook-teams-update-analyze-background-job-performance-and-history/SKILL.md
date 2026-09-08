---
name: "rar-cowork-cookbook-teams-update-analyze-background-job-performance-and-history"
description: "Summarizes background job performance and history from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_background_job_performance_and_history", "rar_sha256": "bda4d994056efc225622f60431b096f13e9377f95fb60bdf9e818c0582a974a7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
