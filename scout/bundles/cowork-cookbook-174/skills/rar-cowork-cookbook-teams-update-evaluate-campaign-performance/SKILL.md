---
name: "rar-cowork-cookbook-teams-update-evaluate-campaign-performance"
description: "Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_evaluate_campaign_performance", "rar_sha256": "365ac4254ca0907bf611156456e1ac2692bda2e0adec6b595018296b778736ef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_evaluate_campaign_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_evaluate_campaign_performance_agent.py` and in the RCI capsule.

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

Evaluate campaign performance Teams Channel Update — Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
    "topic": {
      "description": "The process or area to summarize, here 'evaluate campaign performance'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 365ac4254ca0907b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_evaluate_campaign_performance_agent.py` first:

```bash
python3 teams_update_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_evaluate_campaign_performance_agent.py   # or on stdin
python3 teams_update_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Teams Channel Update — Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_evaluate_campaign_performance',
    "version": '3.0.3',
    "display_name": 'Evaluate campaign performance Teams Channel Update',
    "description": 'Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab5a20f8007b6787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'topic': "The process or area to summarize, here 'evaluate campaign performance'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of evaluate campaign performance. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-evaluate-campaign-performance-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads evaluate campaign performance, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes campaign performance from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs and quick-acti', 'example_request': "Draft a Teams update on evaluate campaign performance for USMF with an Adaptive Card - save it, don't post.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': "The process or area to summarize, here 'evaluate campaign performance'.", 'name': 'topic'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want a review-ready Teams channel update on campaign performance status from D365 F&SCM, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEvaluateCampaignPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEvaluateCampaignPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-evaluate-campaign-performance-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': "The process or area to summarize, here 'evaluate campaign performance'.", 'type': 'string'}},
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
    print(TeamsUpdateEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
