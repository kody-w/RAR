---
name: "rar-cowork-cookbook-teams-update-launch-new-products"
description: "Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_launch_new_products", "rar_sha256": "1915f2d562734435a63daee12197cbd5166184616dbca1d2e62d08515ef2fbaf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_launch_new_products`. The original RAPP
agent is preserved byte-for-byte in `teams_update_launch_new_products_agent.py` and in the RCI capsule.

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

Launch new products Teams Channel Update — Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-launch-new-products-2026-05-24-card.json.",
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
    },
    "topic": {
      "description": "The initiative or area to report on, e.g. launch new products.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 1915f2d562734435…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_launch_new_products_agent.py` first:

```bash
python3 teams_update_launch_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_launch_new_products_agent.py   # or on stdin
python3 teams_update_launch_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch new products Teams Channel Update — Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-launch-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_launch_new_products',
    "version": '3.0.3',
    "display_name": 'Launch new products Teams Channel Update',
    "description": 'Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post',
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
        "upstream_slug": 'teams-update-launch-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-launch-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d5e47bb148ebded',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/launch-new-products'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-launch-new-products', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-launch-new-products-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The initiative or area to report on, e.g. launch new products.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of launch new products. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-launch-new-products-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads launch new products, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post', 'example_request': "Draft a Teams update on launch new products for USMF from D365 and save an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or area to report on, e.g. launch new products.', 'name': 'topic'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-launch-new-products-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on new product launch status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateLaunchNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateLaunchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-launch-new-products-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or area to report on, e.g. launch new products.', 'type': 'string'}},
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
    print(TeamsUpdateLaunchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
