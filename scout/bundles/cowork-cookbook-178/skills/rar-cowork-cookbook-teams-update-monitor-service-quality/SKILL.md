---
name: "rar-cowork-cookbook-teams-update-monitor-service-quality"
description: "Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_service_quality", "rar_sha256": "5b51652c621199a9743f3b5985a94d560de007e16eded6b5af1158f2f5a907fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_service_quality`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_service_quality_agent.py` and in the RCI capsule.

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

Monitor service quality Teams Channel Update — Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-monitor-service-quality-2026-05-24-card.json.",
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
    "scope": {
      "description": "Optional scope or reporting period for the monitor service quality summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 5b51652c621199a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_service_quality_agent.py` first:

```bash
python3 teams_update_monitor_service_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_service_quality_agent.py   # or on stdin
python3 teams_update_monitor_service_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service quality Teams Channel Update — Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_service_quality',
    "version": '3.0.3',
    "display_name": 'Monitor service quality Teams Channel Update',
    "description": 'Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i',
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
        "upstream_slug": 'teams-update-monitor-service-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-service-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a2933519807f5568',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/monitor-service-quality'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-monitor-service-quality', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-service-quality-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'scope': 'Optional scope or reporting period for the monitor service quality summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of monitor service quality. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-monitor-service-quality-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor service quality, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i', 'example_request': "Draft a Teams update on monitor service quality for USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-service-quality-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional scope or reporting period for the monitor service quality summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on monitor service quality status from D365 ERP data, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMonitorServiceQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorServiceQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-monitor-service-quality-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional scope or reporting period for the monitor service quality summary.', 'type': 'string'}},
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
    print(TeamsUpdateMonitorServiceQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
