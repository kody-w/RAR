---
name: "rar-cowork-cookbook-teams-update-sell-product-subscriptions"
description: "Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_sell_product_subscriptions", "rar_sha256": "272fe17bc35bdc826347503abbd5263479483dd724b91b9bb6d2ad89c90971b9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_sell_product_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_sell_product_subscriptions_agent.py` and in the RCI capsule.

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

Sell product subscriptions Teams Channel Update — Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-sell-product-subscriptions-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 272fe17bc35bdc82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_sell_product_subscriptions_agent.py` first:

```bash
python3 teams_update_sell_product_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_sell_product_subscriptions_agent.py   # or on stdin
python3 teams_update_sell_product_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell product subscriptions Teams Channel Update — Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_sell_product_subscriptions',
    "version": '3.0.3',
    "display_name": 'Sell product subscriptions Teams Channel Update',
    "description": 'Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted.',
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
        "upstream_slug": 'teams-update-sell-product-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab40c524925b6d43',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/sell-product-subscriptions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-sell-product-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-sell-product-subscriptions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of sell product subscriptions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-sell-product-subscriptions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads sell product subscriptions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted.', 'example_request': "Draft a Teams update on sell product subscriptions for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-sell-product-subscriptions-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on sell product subscriptions status from D365 F&SCM, with KPIs and quick-action buttons, saved for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateSellProductSubscriptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSellProductSubscriptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-sell-product-subscriptions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateSellProductSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
