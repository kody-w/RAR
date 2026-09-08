---
name: "rar-cowork-cookbook-teams-update-sell-product-subscriptions"
description: "Summarizes sell product subscriptions status from the Dynamics 365 ERP plugin for a legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_sell_product_subscriptions", "rar_sha256": "272fe17bc35bdc826347503abbd5263479483dd724b91b9bb6d2ad89c90971b9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
