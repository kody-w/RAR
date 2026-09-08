---
name: "rar-cowork-cookbook-teams-update-list-open-positions"
description: "Summarizes open positions from Dynamics 365 F&SCM for a given legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_list_open_positions", "rar_sha256": "6822ef779d8f4a37bb8870c76f2f91d3f867b9baa1cb926006b05bf7ad45f5a9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
