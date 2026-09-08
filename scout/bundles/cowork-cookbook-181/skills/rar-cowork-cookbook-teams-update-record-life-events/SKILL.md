---
name: "rar-cowork-cookbook-teams-update-record-life-events"
description: "Summarizes record life events from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post (2-sentence summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_life_events", "rar_sha256": "b6c15ab6014ddb7a39d5bd0cc81b70ee9ec6d5ab42c4ad55e01dd63550d67708", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
