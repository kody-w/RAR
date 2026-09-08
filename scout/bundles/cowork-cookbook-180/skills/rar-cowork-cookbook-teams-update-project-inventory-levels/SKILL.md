---
name: "rar-cowork-cookbook-teams-update-project-inventory-levels"
description: "Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_project_inventory_levels", "rar_sha256": "ee0428e14b34ed5664b4953ed58012e12370f08be102eca5f0b46b87e4a03416", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_project_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `teams_update_project_inventory_levels_agent.py` and in the RCI capsule.

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

Project inventory levels Teams Channel Update — Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-project-inventory-levels-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 ee0428e14b34ed56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_project_inventory_levels_agent.py` first:

```bash
python3 teams_update_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_project_inventory_levels_agent.py   # or on stdin
python3 teams_update_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Teams Channel Update — Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_project_inventory_levels',
    "version": '3.0.3',
    "display_name": 'Project inventory levels Teams Channel Update',
    "description": 'Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p',
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
        "upstream_slug": 'teams-update-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4501975faef2762',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-project-inventory-levels-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of project inventory levels. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-project-inventory-levels-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads project inventory levels, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p', 'example_request': "Draft a Teams update on project inventory levels for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-project-inventory-levels-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on project inventory levels from D365 F&SCM, drafted as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProjectInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProjectInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-project-inventory-levels-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
