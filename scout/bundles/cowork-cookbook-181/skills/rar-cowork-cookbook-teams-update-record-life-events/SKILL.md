---
name: "rar-cowork-cookbook-teams-update-record-life-events"
description: "Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_life_events", "rar_sha256": "b6c15ab6014ddb7a39d5bd0cc81b70ee9ec6d5ab42c4ad55e01dd63550d67708", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_record_life_events`. The original RAPP
agent is preserved byte-for-byte in `teams_update_record_life_events_agent.py` and in the RCI capsule.

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

Record life events Teams Channel Update — Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-life-events
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-record-life-events-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_life_events_agent.py` and embedded as the fenced Python below (sha256 b6c15ab6014ddb7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_life_events_agent.py` first:

```bash
python3 teams_update_record_life_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_record_life_events_agent.py   # or on stdin
python3 teams_update_record_life_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record life events Teams Channel Update — Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-life-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_record_life_events',
    "version": '3.0.3',
    "display_name": 'Record life events Teams Channel Update',
    "description": 'Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-record-life-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-record-life-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70d5458a5964448f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/record-life-events'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-record-life-events', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-life-events-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of record life events. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-record-life-events-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record life events, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica', 'example_request': "Draft a Teams channel update on record life events for USMF and save the Adaptive Card JSON — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-life-events-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on record life events status from D365 ERP, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRecordLifeEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRecordLifeEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-record-life-events-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateRecordLifeEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
