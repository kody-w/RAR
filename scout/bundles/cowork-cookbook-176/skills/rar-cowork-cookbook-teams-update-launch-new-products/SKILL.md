---
name: "rar-cowork-cookbook-teams-update-launch-new-products"
description: "Summarizes launch-new-products status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; does not post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_launch_new_products", "rar_sha256": "1915f2d562734435a63daee12197cbd5166184616dbca1d2e62d08515ef2fbaf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
