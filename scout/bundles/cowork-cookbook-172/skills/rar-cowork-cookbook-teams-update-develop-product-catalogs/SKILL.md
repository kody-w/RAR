---
name: "rar-cowork-cookbook-teams-update-develop-product-catalogs"
description: "Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_catalogs", "rar_sha256": "0b10a65613042e335d4bb0a35624b51361d73eaf69d2c0bdeeddc778b9f501c1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_catalogs_agent.py` and in the RCI capsule.

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

Develop product catalogs Teams Channel Update — Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 0b10a65613042e33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_catalogs_agent.py` first:

```bash
python3 teams_update_develop_product_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_catalogs_agent.py   # or on stdin
python3 teams_update_develop_product_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product catalogs Teams Channel Update — Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop product catalogs Teams Channel Update',
    "description": 'Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe',
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
        "upstream_slug": 'teams-update-develop-product-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1feb311f9f4814b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-develop-product-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop product catalogs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-product-catalogs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product catalogs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes product catalog development status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; doe', 'example_request': "Draft a Teams update on develop product catalogs for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on develop product catalogs status from D365 F&SCM, saved as artifacts for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopProductCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-product-catalogs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDevelopProductCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
