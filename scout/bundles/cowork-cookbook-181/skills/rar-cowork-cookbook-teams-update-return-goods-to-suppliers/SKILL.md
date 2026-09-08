---
name: "rar-cowork-cookbook-teams-update-return-goods-to-suppliers"
description: "Summarizes return goods to suppliers status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs and quick-action buttons; does not post it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_return_goods_to_suppliers", "rar_sha256": "bc0c3e3de720e61f41b616a2971fb08f504fc441bd932a9d961cda518ba5f571", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
