---
name: "rar-cowork-cookbook-teams-update-update-product-assortments"
description: "Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_product_assortments", "rar_sha256": "80718435c8d1944668576e1d5165fe02dec43c538beb976247de16ab34613e6e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_product_assortments_agent.py` and in the RCI capsule.

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

Update product assortments Teams Channel Update — Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 80718435c8d19446…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_product_assortments_agent.py` first:

```bash
python3 teams_update_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_product_assortments_agent.py   # or on stdin
python3 teams_update_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Teams Channel Update — Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_product_assortments',
    "version": '3.0.3',
    "display_name": 'Update product assortments Teams Channel Update',
    "description": 'Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any',
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
        "upstream_slug": 'teams-update-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44a3f22cf4a8d8bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of update product assortments. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-update-product-assortments-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update product assortments, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes product assortment status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post any', 'example_request': "Draft a Teams post and Adaptive Card on product assortment status in USMF — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on product assortment status from D365 ERP, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateUpdateProductAssortments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateProductAssortments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-update-product-assortments-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
