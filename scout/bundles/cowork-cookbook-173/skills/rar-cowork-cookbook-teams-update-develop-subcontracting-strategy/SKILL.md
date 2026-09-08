---
name: "rar-cowork-cookbook-teams-update-develop-subcontracting-strategy"
description: "Summarizes subcontracting strategy status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_subcontracting_strategy", "rar_sha256": "e9a07c14970fdafd137ba2df32fa783df9ef1cef134861f98dc9966956fd82c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
