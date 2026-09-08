---
name: "rar-cowork-cookbook-teams-update-route-loads"
description: "Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_route_loads", "rar_sha256": "d0eaadf617aeaae66cfa643bd7e780824943a05a31f3ebba21484a8014aeed48", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_route_loads`. The original RAPP
agent is preserved byte-for-byte in `teams_update_route_loads_agent.py` and in the RCI capsule.

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

Route loads Teams Channel Update — Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-route-loads
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
      "description": "Output filename for the Adaptive Card JSON, e.g., teams-update-route-loads-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to summarize route loads for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_route_loads_agent.py` and embedded as the fenced Python below (sha256 d0eaadf617aeaae6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_route_loads_agent.py` first:

```bash
python3 teams_update_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_route_loads_agent.py   # or on stdin
python3 teams_update_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Teams Channel Update — Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_route_loads',
    "version": '3.0.3',
    "display_name": 'Route loads Teams Channel Update',
    "description": 'Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing',
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
        "upstream_slug": 'teams-update-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '978b62571a87cd14',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g., teams-update-route-loads-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to summarize route loads for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of route loads. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-route-loads-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads route loads, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing', 'example_request': "Draft a Teams post and Adaptive Card on route loads status for USMF — save them, don't post.", 'inputs': [{'description': 'D365 F&SCM legal entity to summarize route loads for (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g., teams-update-route-loads-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on route loads status, with an Adaptive Card for triage, drafted but not posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRouteLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRouteLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g., teams-update-route-loads-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to summarize route loads for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
