---
name: "rar-cowork-cookbook-teams-update-react-to-supply-chain-signals"
description: "Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_react_to_supply_chain_signals", "rar_sha256": "ee37600e9ab3a312fe27fbddbc69a0285e9fd8169cc50fd1f71193123786e50b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_react_to_supply_chain_signals`. The original RAPP
agent is preserved byte-for-byte in `teams_update_react_to_supply_chain_signals_agent.py` and in the RCI capsule.

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

React to supply chain signals Teams Channel Update — Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-react-to-supply-chain-signals-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 ee37600e9ab3a312…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_react_to_supply_chain_signals_agent.py` first:

```bash
python3 teams_update_react_to_supply_chain_signals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_react_to_supply_chain_signals_agent.py   # or on stdin
python3 teams_update_react_to_supply_chain_signals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
React to supply chain signals Teams Channel Update — Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_react_to_supply_chain_signals',
    "version": '3.0.3',
    "display_name": 'React to supply chain signals Teams Channel Update',
    "description": 'Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-react-to-supply-chain-signals',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b45dd675ff8a3432',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/react-to-supply-chain-signals'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-react-to-supply-chain-signals', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-react-to-supply-chain-signals-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of react to supply chain signals. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-react-to-supply-chain-signals-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads react to supply chain signals, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.', 'example_request': "Draft a Teams update on supply chain signals for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 F&SCM legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-react-to-supply-chain-signals-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on supply chain signals from D365, with an Adaptive Card for triage; it saves files rather than posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReactToSupplyChainSignals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReactToSupplyChainSignals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-react-to-supply-chain-signals-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReactToSupplyChainSignals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
