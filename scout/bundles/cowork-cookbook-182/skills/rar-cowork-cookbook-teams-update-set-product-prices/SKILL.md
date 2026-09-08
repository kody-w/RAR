---
name: "rar-cowork-cookbook-teams-update-set-product-prices"
description: "Summarizes set product prices status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_product_prices", "rar_sha256": "381cb95d16eba43565a602713f4fa133a75a1e9b58909ac2956076a2e653426b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
