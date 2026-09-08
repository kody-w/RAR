---
name: "rar-cowork-cookbook-teams-update-start-production"
description: "Summarizes start production status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_start_production", "rar_sha256": "0c8666ca62fb3fad20c8a54fb729726fc9e58caaea7f80d912f814225b98eeb8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
