---
name: "rar-cowork-cookbook-teams-update-start-production"
description: "Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_start_production", "rar_sha256": "0c8666ca62fb3fad20c8a54fb729726fc9e58caaea7f80d912f814225b98eeb8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_start_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_start_production_agent.py` and in the RCI capsule.

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

Start production Teams Channel Update — Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-start-production-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_start_production_agent.py` and embedded as the fenced Python below (sha256 0c8666ca62fb3fad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_start_production_agent.py` first:

```bash
python3 teams_update_start_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_start_production_agent.py   # or on stdin
python3 teams_update_start_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Start production Teams Channel Update — Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_start_production',
    "version": '3.0.3',
    "display_name": 'Start production Teams Channel Update',
    "description": 'Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-start-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-start-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34eb25306fb683bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/start-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-start-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-start-production-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of start production. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-start-production-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads start production, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p', 'example_request': "Draft a Teams channel update on start production for USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-start-production-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on start production status, with an Adaptive Card for triage, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateStartProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateStartProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-start-production-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateStartProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
