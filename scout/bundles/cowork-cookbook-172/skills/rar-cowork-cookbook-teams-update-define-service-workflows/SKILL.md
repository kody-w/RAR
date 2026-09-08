---
name: "rar-cowork-cookbook-teams-update-define-service-workflows"
description: "Summarizes the current state of define service workflows from the Dynamics 365 ERP plugin for a legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file, saved for review and not pos"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_workflows", "rar_sha256": "26eaa4beb2649e5eb954250b914bca3906341b92f9154d4426356b184f1defa6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
