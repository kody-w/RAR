---
name: "rar-cowork-cookbook-teams-update-monitor-operational-performance"
description: "Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_operational_performance", "rar_sha256": "c9a10e282f98797375ae0317bbff6d7ef6b132726228b5eb0478f9e584c0960e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_operational_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_operational_performance_agent.py` and in the RCI capsule.

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

Monitor operational performance Teams Channel Update — Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-monitor-operational-performance-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (recipe default: USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 c9a10e282f987973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_operational_performance_agent.py` first:

```bash
python3 teams_update_monitor_operational_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_operational_performance_agent.py   # or on stdin
python3 teams_update_monitor_operational_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor operational performance Teams Channel Update — Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_operational_performance',
    "version": '3.0.3',
    "display_name": 'Monitor operational performance Teams Channel Update',
    "description": 'Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-operational-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-operational-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aee5ce3079983509',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-operational-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-monitor-operational-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-monitor-operational-performance-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (recipe default: USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of monitor operational performance. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-monitor-operational-performance-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor operational performance, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;', 'example_request': "Draft a Teams update on operational performance for USMF and save the Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 F&SCM legal entity to report on (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-monitor-operational-performance-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on D365 operational performance, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMonitorOperationalPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorOperationalPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-monitor-operational-performance-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMonitorOperationalPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
