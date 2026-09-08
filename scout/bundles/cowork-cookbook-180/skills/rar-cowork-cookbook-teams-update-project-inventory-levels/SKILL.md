---
name: "rar-cowork-cookbook-teams-update-project-inventory-levels"
description: "Summarizes current project inventory levels from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_project_inventory_levels", "rar_sha256": "ee0428e14b34ed5664b4953ed58012e12370f08be102eca5f0b46b87e4a03416", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
