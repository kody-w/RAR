---
name: "rar-cowork-cookbook-teams-update-process-customer-returns-and-exchanges"
description: "Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_returns_and_exchanges", "rar_sha256": "3cea613cb2031c5442470857d5e9dd7ab66650429396c82dbdefae1e93b833c7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Teams Channel Update — Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
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
    "as_of_date": {
      "description": "Date used in the update and card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 3cea613cb2031c54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 teams_update_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 teams_update_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Teams Channel Update — Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_returns_and_exchanges',
    "version": '3.0.3',
    "display_name": 'Process customer returns and exchanges Teams Channel Update',
    "description": 'Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cd8ed83e01be9bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the update and card filename, e.g. 2026-05-24.', 'card_filename': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process customer returns and exchanges. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-customer-returns-and-exchanges-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process customer returns and exchanges, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams update on customer returns and exchanges for USMF as of 2026-05-24, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on customer returns/exchanges status with an Adaptive Card of KPIs and quick-action buttons.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessCustomerReturnsAndExchanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerReturnsAndExchanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
