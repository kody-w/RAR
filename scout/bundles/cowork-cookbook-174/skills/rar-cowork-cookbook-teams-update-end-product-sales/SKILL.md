---
name: "rar-cowork-cookbook-teams-update-end-product-sales"
description: "Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_end_product_sales", "rar_sha256": "1e360cb0935f1d7d3a609c22d87ae0b78e1ea7c8d3a86465d596ade809257764", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_end_product_sales`. The original RAPP
agent is preserved byte-for-byte in `teams_update_end_product_sales_agent.py` and in the RCI capsule.

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

End product sales Teams Channel Update — Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-end-product-sales-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize sales for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 1e360cb0935f1d7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_end_product_sales_agent.py` first:

```bash
python3 teams_update_end_product_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_end_product_sales_agent.py   # or on stdin
python3 teams_update_end_product_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
End product sales Teams Channel Update — Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_end_product_sales',
    "version": '3.0.3',
    "display_name": 'End product sales Teams Channel Update',
    "description": 'Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an',
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
        "upstream_slug": 'teams-update-end-product-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-end-product-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dac6c61128493a28',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/end-product-sales'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-end-product-sales', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-end-product-sales-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize sales for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of end product sales. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-end-product-sales-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads end product sales, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an', 'example_request': "Draft a Teams channel update on end product sales for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize sales for (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-end-product-sales-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on end product sales status from D365 F&SCM, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEndProductSales(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEndProductSales'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-end-product-sales-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize sales for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateEndProductSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
