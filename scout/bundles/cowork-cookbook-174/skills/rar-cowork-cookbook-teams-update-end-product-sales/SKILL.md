---
name: "rar-cowork-cookbook-teams-update-end-product-sales"
description: "Summarizes end product sales from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post an"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_end_product_sales", "rar_sha256": "1e360cb0935f1d7d3a609c22d87ae0b78e1ea7c8d3a86465d596ade809257764", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
