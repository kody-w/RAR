---
name: "rar-cowork-cookbook-teams-update-govern-projects"
description: "Summarizes govern projects status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_govern_projects", "rar_sha256": "7dcc344a00d1bdd3767f8c88f0d6ec55a004b467e12f7816bd5a6e62c4481baf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
