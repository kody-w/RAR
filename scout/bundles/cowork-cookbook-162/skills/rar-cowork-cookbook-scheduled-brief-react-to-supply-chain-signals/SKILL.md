---
name: "rar-cowork-cookbook-scheduled-brief-react-to-supply-chain-signals"
description: "Builds a supply chain signals morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 impact items, anomalies vs the 7-day rolling average, next actions, an email draft, and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals", "rar_sha256": "60e6296bccb08a3e96db08701a538313df701f95d76ab66c3acc465a01a802bb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
