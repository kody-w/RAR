---
name: "rar-cowork-cookbook-scheduled-brief-react-to-supply-chain-signals"
description: "Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals", "rar_sha256": "60e6296bccb08a3e96db08701a538313df701f95d76ab66c3acc465a01a802bb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_react_to_supply_chain_signals_agent.py` and in the RCI capsule.

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

React to supply chain signals Scheduled Email Brief — Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 60e6296bccb08a3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_react_to_supply_chain_signals_agent.py` first:

```bash
python3 scheduled_brief_react_to_supply_chain_signals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_react_to_supply_chain_signals_agent.py   # or on stdin
python3 scheduled_brief_react_to_supply_chain_signals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
React to supply chain signals Scheduled Email Brief — Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals',
    "version": '3.0.3',
    "display_name": 'React to supply chain signals Scheduled Email Brief',
    "description": 'Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-react-to-supply-chain-signals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd8167964c2bc16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/react-to-supply-chain-signals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-react-to-supply-chain-signals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where react to supply chain signals stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on react to supply chain signals for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads react to supply chain signals, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary.', 'example_request': "Give me the USMF supply chain morning brief for the ops owner and draft the email — don't send it.", 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly supply chain morning brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReactToSupplyChainSignals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReactToSupplyChainSignals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefReactToSupplyChainSignals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
