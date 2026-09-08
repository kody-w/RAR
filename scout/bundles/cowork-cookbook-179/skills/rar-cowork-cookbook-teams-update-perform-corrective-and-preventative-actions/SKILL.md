---
name: "rar-cowork-cookbook-teams-update-perform-corrective-and-preventative-actions"
description: "Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions", "rar_sha256": "221299e93a747ff32da59d2e6fe7d3fc9b023d326a71333c4b93d62b44be36bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
