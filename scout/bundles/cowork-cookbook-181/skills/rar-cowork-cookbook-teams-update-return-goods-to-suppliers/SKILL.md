---
name: "rar-cowork-cookbook-teams-update-return-goods-to-suppliers"
description: "Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_return_goods_to_suppliers", "rar_sha256": "bc0c3e3de720e61f41b616a2971fb08f504fc441bd932a9d961cda518ba5f571", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_return_goods_to_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_return_goods_to_suppliers_agent.py` and in the RCI capsule.

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

Return goods to suppliers Teams Channel Update — Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
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
      "description": "Date used to label the update and the generated card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Optional output name for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 bc0c3e3de720e61f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_return_goods_to_suppliers_agent.py` first:

```bash
python3 teams_update_return_goods_to_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_return_goods_to_suppliers_agent.py   # or on stdin
python3 teams_update_return_goods_to_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to suppliers Teams Channel Update — Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_return_goods_to_suppliers',
    "version": '3.0.3',
    "display_name": 'Return goods to suppliers Teams Channel Update',
    "description": 'Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-return-goods-to-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70011ab18f02d494',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/return-goods-to-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-return-goods-to-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used to label the update and the generated card filename.', 'card_filename': 'Optional output name for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of return goods to suppliers. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-return-goods-to-suppliers-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads return goods to suppliers, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it.', 'example_request': "Draft a Teams update on return goods to suppliers for USMF with an Adaptive Card - save it, don't post.", 'inputs': [{'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used to label the update and the generated card filename.', 'name': 'as_of_date'}, {'description': 'Optional output name for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a reviewable Teams channel update on return goods to suppliers status, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReturnGoodsToSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReturnGoodsToSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used to label the update and the generated card filename.', 'type': 'string'}, 'card_filename': {'description': 'Optional output name for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReturnGoodsToSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
