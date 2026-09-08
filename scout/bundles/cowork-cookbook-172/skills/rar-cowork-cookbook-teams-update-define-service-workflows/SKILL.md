---
name: "rar-cowork-cookbook-teams-update-define-service-workflows"
description: "Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_workflows", "rar_sha256": "26eaa4beb2649e5eb954250b914bca3906341b92f9154d4426356b184f1defa6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_service_workflows`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_service_workflows_agent.py` and in the RCI capsule.

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

Define service workflows Teams Channel Update — Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
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
    "as_of_date": {
      "description": "Date used in the output card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Optional name for the Adaptive Card JSON artifact.",
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
    "topic": {
      "description": "The workstream or process to summarize, e.g. define service workflows.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 26eaa4beb2649e5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_workflows_agent.py` first:

```bash
python3 teams_update_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_service_workflows_agent.py   # or on stdin
python3 teams_update_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Teams Channel Update — Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_service_workflows',
    "version": '3.0.3',
    "display_name": 'Define service workflows Teams Channel Update',
    "description": 'Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52a7913e0bf4166c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the output card filename, e.g. 2026-05-24.', 'card_filename': 'Optional name for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The workstream or process to summarize, e.g. define service workflows.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define service workflows. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-service-workflows-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service workflows, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos', 'example_request': "Draft a Teams update on define service workflows in USMF from D365 and save the Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The workstream or process to summarize, e.g. define service workflows.', 'name': 'topic'}, {'description': 'Date used in the output card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Optional name for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on define service workflows status, with KPIs and quick-action buttons in an Adaptive Card, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineServiceWorkflows(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineServiceWorkflows'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the output card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Optional name for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The workstream or process to summarize, e.g. define service workflows.', 'type': 'string'}},
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
    print(TeamsUpdateDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
