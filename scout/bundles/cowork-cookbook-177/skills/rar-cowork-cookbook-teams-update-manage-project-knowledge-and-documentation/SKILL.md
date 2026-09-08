---
name: "rar-cowork-cookbook-teams-update-manage-project-knowledge-and-documentation"
description: "Summarizes project knowledge and documentation status from Dynamics 365 ERP for a legal entity and saves a Teams-ready markdown channel post plus an Adaptive Card JSON file for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation", "rar_sha256": "c4d6b8013cccddd04d1c06a967a2b71dd2bb0db70adf76fe75ca73f9db21b71d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
