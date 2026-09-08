---
name: "rar-cowork-cookbook-teams-update-implement-corrective-and-preventative-actions"
description: "Summarizes corrective and preventative action status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions", "rar_sha256": "882c873f20eb47851eb8fb072f56edf6324cd5ca06e73874074fcf09252afb17", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
