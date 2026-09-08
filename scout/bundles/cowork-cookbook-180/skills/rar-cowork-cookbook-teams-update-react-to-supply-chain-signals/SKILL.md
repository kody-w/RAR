---
name: "rar-cowork-cookbook-teams-update-react-to-supply-chain-signals"
description: "Summarizes supply chain signal status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_react_to_supply_chain_signals", "rar_sha256": "ee37600e9ab3a312fe27fbddbc69a0285e9fd8169cc50fd1f71193123786e50b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
