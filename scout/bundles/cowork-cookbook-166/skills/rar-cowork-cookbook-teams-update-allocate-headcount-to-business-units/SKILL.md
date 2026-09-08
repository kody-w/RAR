---
name: "rar-cowork-cookbook-teams-update-allocate-headcount-to-business-units"
description: "Summarizes headcount allocation to business units from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_headcount_to_business_units", "rar_sha256": "b2fa38a21ec0e2acdaf400b3f04e5b23482380ae98d20287e755ae4f59aaeef8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
