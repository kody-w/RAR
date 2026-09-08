---
name: "rar-cowork-cookbook-teams-update-count-inventory"
description: "Summarizes count inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_count_inventory", "rar_sha256": "99c20dc846548ce8ffbe8876028735c3c2e930060f0f65ea1e4f48968522a057", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
