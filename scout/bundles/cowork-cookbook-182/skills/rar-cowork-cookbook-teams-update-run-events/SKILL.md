---
name: "rar-cowork-cookbook-teams-update-run-events"
description: "Summarizes current run events status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post i"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_run_events", "rar_sha256": "64109ecf21d3d9efe9ceee2621835cddd7db2f36ce53adad9096a0476f4b0283", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
