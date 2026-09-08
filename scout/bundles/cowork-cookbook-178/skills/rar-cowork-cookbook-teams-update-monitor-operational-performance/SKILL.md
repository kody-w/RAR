---
name: "rar-cowork-cookbook-teams-update-monitor-operational-performance"
description: "Summarizes operational performance from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_operational_performance", "rar_sha256": "c9a10e282f98797375ae0317bbff6d7ef6b132726228b5eb0478f9e584c0960e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
