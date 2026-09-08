---
name: "rar-cowork-cookbook-teams-update-set-product-prices"
description: "Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_product_prices", "rar_sha256": "381cb95d16eba43565a602713f4fa133a75a1e9b58909ac2956076a2e653426b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_product_prices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_product_prices_agent.py` and in the RCI capsule.

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

Set product prices Teams Channel Update — Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-product-prices
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-set-product-prices-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 381cb95d16eba435…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_product_prices_agent.py` first:

```bash
python3 teams_update_set_product_prices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_product_prices_agent.py   # or on stdin
python3 teams_update_set_product_prices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set product prices Teams Channel Update — Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-product-prices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_product_prices',
    "version": '3.0.3',
    "display_name": 'Set product prices Teams Channel Update',
    "description": 'Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-set-product-prices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-product-prices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06c4114b7f0377c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/set-product-prices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-set-product-prices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-set-product-prices-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of set product prices. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-set-product-prices-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set product prices, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted', 'example_request': "Draft a Teams update on set product prices for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-set-product-prices-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on set product prices status from D365 ERP data, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateSetProductPrices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetProductPrices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-set-product-prices-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateSetProductPrices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
