---
name: "rar-cowork-cookbook-teams-update-list-open-positions"
description: "Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_list_open_positions", "rar_sha256": "6822ef779d8f4a37bb8870c76f2f91d3f867b9baa1cb926006b05bf7ad45f5a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_list_open_positions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_list_open_positions_agent.py` and in the RCI capsule.

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

List open positions Teams Channel Update — Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-list-open-positions
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-list-open-positions-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 6822ef779d8f4a37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_list_open_positions_agent.py` first:

```bash
python3 teams_update_list_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_list_open_positions_agent.py   # or on stdin
python3 teams_update_list_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
List open positions Teams Channel Update — Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-list-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_list_open_positions',
    "version": '3.0.3',
    "display_name": 'List open positions Teams Channel Update',
    "description": 'Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-list-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-list-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f287af6dadc5c6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/list-open-positions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-list-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-list-open-positions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of list open positions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-list-open-positions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads list open positions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on open positions for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-list-open-positions-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on open positions status from D365 ERP data, with an Adaptive Card artifact saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateListOpenPositions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateListOpenPositions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-list-open-positions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateListOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
