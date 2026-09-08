---
name: "rar-cowork-cookbook-teams-update-govern-projects"
description: "Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_govern_projects", "rar_sha256": "7dcc344a00d1bdd3767f8c88f0d6ec55a004b467e12f7816bd5a6e62c4481baf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_govern_projects`. The original RAPP
agent is preserved byte-for-byte in `teams_update_govern_projects_agent.py` and in the RCI capsule.

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

Govern projects Teams Channel Update — Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-govern-projects-2026-05-24-card.json.",
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
    "project_scope": {
      "description": "The project area to report on, e.g. govern projects.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_govern_projects_agent.py` and embedded as the fenced Python below (sha256 7dcc344a00d1bdd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_govern_projects_agent.py` first:

```bash
python3 teams_update_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_govern_projects_agent.py   # or on stdin
python3 teams_update_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Teams Channel Update — Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_govern_projects',
    "version": '3.0.3',
    "display_name": 'Govern projects Teams Channel Update',
    "description": 'Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd44c8662774c852',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-govern-projects-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'project_scope': 'The project area to report on, e.g. govern projects.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of govern projects. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-govern-projects-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads govern projects, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing', 'example_request': "Draft a Teams post and Adaptive Card on govern projects status in USMF from D365 — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The project area to report on, e.g. govern projects.', 'name': 'project_scope'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-govern-projects-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on govern projects status from D365 ERP data, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateGovernProjects(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateGovernProjects'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-govern-projects-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_scope': {'description': 'The project area to report on, e.g. govern projects.', 'type': 'string'}},
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
    print(TeamsUpdateGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
