---
name: "rar-cowork-cookbook-teams-update-measure-frontline-worker-service-performance"
description: "Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_frontline_worker_service_performance", "rar_sha256": "5fba9cbcf9669c9b9d4398e5bd741dfb812527236ae3b5d5a7809cd48e0b0d98", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_frontline_worker_service_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_frontline_worker_service_performance_agent.py` and in the RCI capsule.

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

Measure frontline worker service performance Teams Channel Update — Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-measure-frontline-worker-service-performance-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 5fba9cbcf9669c9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_frontline_worker_service_performance_agent.py` first:

```bash
python3 teams_update_measure_frontline_worker_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_frontline_worker_service_performance_agent.py   # or on stdin
python3 teams_update_measure_frontline_worker_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure frontline worker service performance Teams Channel Update — Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_frontline_worker_service_performance',
    "version": '3.0.3',
    "display_name": 'Measure frontline worker service performance Teams Channel Update',
    "description": 'Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-frontline-worker-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ceb04ed0b1dc9a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/measure-frontline-worker-service-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-measure-frontline-worker-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-frontline-worker-service-performance-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of measure frontline worker service performance. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-measure-frontline-worker-service-performance-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure frontline worker service performance, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto', 'example_request': "Draft a Teams update on frontline worker service performance from D365 USMF, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-frontline-worker-service-performance-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on frontline worker service performance drafted from D365 F&SCM data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMeasureFrontlineWorkerServicePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureFrontlineWorkerServicePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-frontline-worker-service-performance-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMeasureFrontlineWorkerServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
