---
name: "rar-cowork-cookbook-teams-update-allocate-headcount-to-business-units"
description: "Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_headcount_to_business_units", "rar_sha256": "b2fa38a21ec0e2acdaf400b3f04e5b23482380ae98d20287e755ae4f59aaeef8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_headcount_to_business_units`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_headcount_to_business_units_agent.py` and in the RCI capsule.

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

Allocate headcount to business units Teams Channel Update — Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-allocate-headcount-to-business-units-2026-05-24-card.json.",
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
    },
    "scope": {
      "description": "Optional adjustment to the scope of the headcount allocation summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 b2fa38a21ec0e2ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 teams_update_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 teams_update_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Teams Channel Update — Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_headcount_to_business_units',
    "version": '3.0.3',
    "display_name": 'Allocate headcount to business units Teams Channel Update',
    "description": 'Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
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
        "upstream_slug": 'teams-update-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cd52cb92532c995',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-allocate-headcount-to-business-units-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'scope': 'Optional adjustment to the scope of the headcount allocation summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of allocate headcount to business units. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-allocate-headcount-to-business-units-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate headcount to business units, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams post and Adaptive Card on headcount allocation to business units for USMF — save, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-allocate-headcount-to-business-units-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional adjustment to the scope of the headcount allocation summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update and Adaptive Card on headcount allocation status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAllocateHeadcountToBusinessUnits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateHeadcountToBusinessUnits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-allocate-headcount-to-business-units-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional adjustment to the scope of the headcount allocation summary.', 'type': 'string'}},
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
    print(TeamsUpdateAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
