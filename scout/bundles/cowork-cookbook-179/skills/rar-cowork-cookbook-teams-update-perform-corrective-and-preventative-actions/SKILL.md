---
name: "rar-cowork-cookbook-teams-update-perform-corrective-and-preventative-actions"
description: "Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions", "rar_sha256": "221299e93a747ff32da59d2e6fe7d3fc9b023d326a71333c4b93d62b44be36bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_perform_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Perform corrective and preventative actions Teams Channel Update — Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-perform-corrective-and-preventative-actions-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 221299e93a747ff3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Teams Channel Update — Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions',
    "version": '3.0.3',
    "display_name": 'Perform corrective and preventative actions Teams Channel Update',
    "description": 'Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '388fe136b3d078e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-perform-corrective-and-preventative-actions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of perform corrective and preventative actions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-perform-corrective-and-preventative-actions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform corrective and preventative actions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on corrective and preventative actions for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-perform-corrective-and-preventative-actions-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update on corrective and preventative action status pulled from Dynamics 365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePerformCorrectiveAndPreventativeActions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePerformCorrectiveAndPreventativeActions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-perform-corrective-and-preventative-actions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
