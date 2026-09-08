---
name: "rar-cowork-cookbook-teams-update-develop-product-portfolio"
description: "Summarizes develop product portfolio status from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus an Adaptive Card JSON file with KPIs, status indicators, and quick-action"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_portfolio", "rar_sha256": "56eac961bf70da3615a0000a39e9bf2525a9f13cc97d309b54be8c18d735a693", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
