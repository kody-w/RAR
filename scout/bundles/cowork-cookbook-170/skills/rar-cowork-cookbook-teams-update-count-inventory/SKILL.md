---
name: "rar-cowork-cookbook-teams-update-count-inventory"
description: "Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_count_inventory", "rar_sha256": "99c20dc846548ce8ffbe8876028735c3c2e930060f0f65ea1e4f48968522a057", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_count_inventory_agent.py` and in the RCI capsule.

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

Count inventory Teams Channel Update — Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-count-inventory-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize count inventory for (recipe default: USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_count_inventory_agent.py` and embedded as the fenced Python below (sha256 99c20dc846548ce8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_count_inventory_agent.py` first:

```bash
python3 teams_update_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_count_inventory_agent.py   # or on stdin
python3 teams_update_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Teams Channel Update — Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_count_inventory',
    "version": '3.0.3',
    "display_name": 'Count inventory Teams Channel Update',
    "description": 'Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a2133f65c1bf627e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-count-inventory-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize count inventory for (recipe default: USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of count inventory. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-count-inventory-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads count inventory, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams post and Adaptive Card on count inventory status for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize count inventory for (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-count-inventory-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on count inventory status, with KPIs and quick-action buttons, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCountInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCountInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-count-inventory-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize count inventory for (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
