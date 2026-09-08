---
name: "rar-cowork-cookbook-teams-update-route-loads"
description: "Summarizes current route loads status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_route_loads", "rar_sha256": "d0eaadf617aeaae66cfa643bd7e780824943a05a31f3ebba21484a8014aeed48", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
