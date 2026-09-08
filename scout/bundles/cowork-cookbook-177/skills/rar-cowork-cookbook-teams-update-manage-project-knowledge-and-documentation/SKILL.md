---
name: "rar-cowork-cookbook-teams-update-manage-project-knowledge-and-documentation"
description: "Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation", "rar_sha256": "c4d6b8013cccddd04d1c06a967a2b71dd2bb0db70adf76fe75ca73f9db21b71d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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

Manage project knowledge and documentation Teams Channel Update — Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-project-knowledge-and-documentation-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 c4d6b8013cccddd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 teams_update_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 teams_update_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Teams Channel Update — Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation',
    "version": '3.0.3',
    "display_name": 'Manage project knowledge and documentation Teams Channel Update',
    "description": 'Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything.',
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
        "upstream_slug": 'teams-update-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '115dc097e731eb2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-project-knowledge-and-documentation-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage project knowledge and documentation. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-project-knowledge-and-documentation-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project knowledge and documentation, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything.', 'example_request': "Draft a Teams channel update on project knowledge and documentation for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-project-knowledge-and-documentation-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on project knowledge/documentation status from D365 F&SCM, saved as artifacts to review before posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageProjectKnowledgeAndDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-manage-project-knowledge-and-documentation-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
