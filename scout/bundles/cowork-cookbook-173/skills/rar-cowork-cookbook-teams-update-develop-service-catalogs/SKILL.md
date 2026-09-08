---
name: "rar-cowork-cookbook-teams-update-develop-service-catalogs"
description: "Summarizes develop service catalogs status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_service_catalogs", "rar_sha256": "c414eb29e7a559720e339602524387459c0457cc9eb0a378229e28b2a2659f2e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
