---
name: "rar-cowork-cookbook-teams-update-implement-corrective-and-preventative-actions"
description: "Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions", "rar_sha256": "882c873f20eb47851eb8fb072f56edf6324cd5ca06e73874074fcf09252afb17", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_implement_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Implement corrective and preventative actions Teams Channel Update — Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-implement-corrective-and-preventative-actions-2026-05-24-card.json.",
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
    },
    "output_location": {
      "description": "Where artifacts are saved, default Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 882c873f20eb4785…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_implement_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_implement_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_implement_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_implement_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement corrective and preventative actions Teams Channel Update — Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions',
    "version": '3.0.3',
    "display_name": 'Implement corrective and preventative actions Teams Channel Update',
    "description": 'Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-implement-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34f83687444aaa4d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/implement-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-implement-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-implement-corrective-and-preventative-actions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_location': 'Where artifacts are saved, default Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of implement corrective and preventative actions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-implement-corrective-and-preventative-actions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement corrective and preventative actions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n', 'example_request': "Draft a Teams update on corrective and preventative actions for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-implement-corrective-and-preventative-actions-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Where artifacts are saved, default Documents/Cowork/output/ in OneDrive.', 'name': 'output_location'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update and Adaptive Card on corrective/preventative action status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateImplementCorrectiveAndPreventativeActions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateImplementCorrectiveAndPreventativeActions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-implement-corrective-and-preventative-actions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_location': {'description': 'Where artifacts are saved, default Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(TeamsUpdateImplementCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
