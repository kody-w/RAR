---
name: "rar-cowork-cookbook-teams-update-measure-frontline-worker-service-performance"
description: "Uses the Dynamics 365 ERP plugin for a given legal entity to summarize frontline worker service performance and save two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action butto"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_frontline_worker_service_performance", "rar_sha256": "5fba9cbcf9669c9b9d4398e5bd741dfb812527236ae3b5d5a7809cd48e0b0d98", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
