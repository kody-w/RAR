---
name: "rar-cowork-cookbook-teams-update-develop-product-portfolio"
description: "Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_portfolio", "rar_sha256": "56eac961bf70da3615a0000a39e9bf2525a9f13cc97d309b54be8c18d735a693", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_portfolio_agent.py` and in the RCI capsule.

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

Develop product portfolio Teams Channel Update — Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-portfolio-2026-05-24-card.json.",
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
    },
    "portfolio_scope": {
      "description": "The product portfolio or area to summarize, e.g. develop product portfolio.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 56eac961bf70da36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_portfolio_agent.py` first:

```bash
python3 teams_update_develop_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_portfolio_agent.py   # or on stdin
python3 teams_update_develop_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product portfolio Teams Channel Update — Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_portfolio',
    "version": '3.0.3',
    "display_name": 'Develop product portfolio Teams Channel Update',
    "description": 'Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action',
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
        "upstream_slug": 'teams-update-develop-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80129e407c75210f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-portfolio'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-portfolio-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'portfolio_scope': 'The product portfolio or area to summarize, e.g. develop product portfolio.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop product portfolio. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-product-portfolio-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product portfolio, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action', 'example_request': "Draft a Teams update on the develop product portfolio from D365 USMF with an Adaptive Card - don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The product portfolio or area to summarize, e.g. develop product portfolio.', 'name': 'portfolio_scope'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-portfolio-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on develop product portfolio status sourced from D365 ERP, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopProductPortfolio(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductPortfolio'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-portfolio-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'portfolio_scope': {'description': 'The product portfolio or area to summarize, e.g. develop product portfolio.', 'type': 'string'}},
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
    print(TeamsUpdateDevelopProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
