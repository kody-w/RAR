---
name: "rar-cowork-cookbook-teams-update-develop-service-catalogs"
description: "Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_service_catalogs", "rar_sha256": "c414eb29e7a559720e339602524387459c0457cc9eb0a378229e28b2a2659f2e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_service_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_service_catalogs_agent.py` and in the RCI capsule.

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

Develop service catalogs Teams Channel Update — Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-service-catalogs-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to summarize, e.g. USMF.",
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
      "description": "The subject area to summarize, e.g. develop service catalogs.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 c414eb29e7a55972…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_service_catalogs_agent.py` first:

```bash
python3 teams_update_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_service_catalogs_agent.py   # or on stdin
python3 teams_update_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Teams Channel Update — Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_service_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop service catalogs Teams Channel Update',
    "description": 'Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33960c44efc7c73c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-service-catalogs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to summarize, e.g. USMF.', 'topic': 'The subject area to summarize, e.g. develop service catalogs.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop service catalogs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-service-catalogs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop service catalogs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action', 'example_request': "Draft a Teams post and Adaptive Card on develop service catalogs status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 F&SCM legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The subject area to summarize, e.g. develop service catalogs.', 'name': 'topic'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-service-catalogs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams update on develop service catalogs status in D365 F&SCM, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopServiceCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopServiceCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-service-catalogs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The subject area to summarize, e.g. develop service catalogs.', 'type': 'string'}},
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
    print(TeamsUpdateDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
