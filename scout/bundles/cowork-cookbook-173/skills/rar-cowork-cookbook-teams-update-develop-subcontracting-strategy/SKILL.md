---
name: "rar-cowork-cookbook-teams-update-develop-subcontracting-strategy"
description: "Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_subcontracting_strategy", "rar_sha256": "e9a07c14970fdafd137ba2df32fa783df9ef1cef134861f98dc9966956fd82c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_subcontracting_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_subcontracting_strategy_agent.py` and in the RCI capsule.

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

Develop subcontracting strategy Teams Channel Update — Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-develop-subcontracting-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 e9a07c14970fdafd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_subcontracting_strategy_agent.py` first:

```bash
python3 teams_update_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_subcontracting_strategy_agent.py   # or on stdin
python3 teams_update_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Teams Channel Update — Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_subcontracting_strategy',
    "version": '3.0.3',
    "display_name": 'Develop subcontracting strategy Teams Channel Update',
    "description": 'Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.',
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
        "upstream_slug": 'teams-update-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b8db67804334eb8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-develop-subcontracting-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop subcontracting strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-subcontracting-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop subcontracting strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it.', 'example_request': "Draft a Teams update on our subcontracting strategy status from D365 USMF, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-develop-subcontracting-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on develop subcontracting strategy status from D365 F&SCM, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopSubcontractingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopSubcontractingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-develop-subcontracting-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
