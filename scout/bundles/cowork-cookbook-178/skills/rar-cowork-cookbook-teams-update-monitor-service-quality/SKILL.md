---
name: "rar-cowork-cookbook-teams-update-monitor-service-quality"
description: "Summarizes monitor service quality from Dynamics 365 F&SCM for a legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action buttons; nothing i"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_service_quality", "rar_sha256": "5b51652c621199a9743f3b5985a94d560de007e16eded6b5af1158f2f5a907fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
