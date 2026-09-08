---
name: "rar-cowork-cookbook-teams-update-run-events"
description: "Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_run_events", "rar_sha256": "64109ecf21d3d9efe9ceee2621835cddd7db2f36ce53adad9096a0476f4b0283", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_run_events`. The original RAPP
agent is preserved byte-for-byte in `teams_update_run_events_agent.py` and in the RCI capsule.

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

Run events Teams Channel Update — Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
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
      "description": "Filename for the Adaptive Card JSON, e.g. 'teams-update-run-events-2026-05-24-card.json'.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize run events for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_run_events_agent.py` and embedded as the fenced Python below (sha256 64109ecf21d3d9ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_run_events_agent.py` first:

```bash
python3 teams_update_run_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_run_events_agent.py   # or on stdin
python3 teams_update_run_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run events Teams Channel Update — Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_run_events',
    "version": '3.0.3',
    "display_name": 'Run events Teams Channel Update',
    "description": 'Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i',
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
        "upstream_slug": 'teams-update-run-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-run-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92b7672d8f660a27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-events'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-run-events', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': "Filename for the Adaptive Card JSON, e.g. 'teams-update-run-events-2026-05-24-card.json'.", 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize run events for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of run events. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-run-events-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads run events, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i', 'example_request': "Draft a Teams post and Adaptive Card on run events status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize run events for (e.g., USMF).', 'name': 'legal_entity'}, {'description': "Filename for the Adaptive Card JSON, e.g. 'teams-update-run-events-2026-05-24-card.json'.", 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on D365 run events status, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRunEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRunEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': "Filename for the Adaptive Card JSON, e.g. 'teams-update-run-events-2026-05-24-card.json'.", 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize run events for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateRunEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
