---
name: "rar-cowork-cookbook-teams-update-define-research-and-development-approach"
description: "Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_research_and_development_approach", "rar_sha256": "3019476fdc92487baa6e1f886cc453fa425a6feaeb7721463205d645212419d6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_research_and_development_approach`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_research_and_development_approach_agent.py` and in the RCI capsule.

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

Define research and development approach Teams Channel Update — Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-research-and-development-approach-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 3019476fdc92487b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_research_and_development_approach_agent.py` first:

```bash
python3 teams_update_define_research_and_development_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_research_and_development_approach_agent.py   # or on stdin
python3 teams_update_define_research_and_development_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define research and development approach Teams Channel Update — Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_research_and_development_approach',
    "version": '3.0.3',
    "display_name": 'Define research and development approach Teams Channel Update',
    "description": 'Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-research-and-development-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-research-and-development-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf8aff8f4992fc80',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/define-research-and-development-approach'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-define-research-and-development-approach', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-research-and-development-approach-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define research and development approach. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-research-and-development-approach-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define research and development approach, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio', 'example_request': 'Draft a Teams update on our define research and development approach status in USMF with an Adaptive Card.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-research-and-development-approach-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on define research and development approach status from D365 ERP data, saved for review rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineResearchAndDevelopmentApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineResearchAndDevelopmentApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-research-and-development-approach-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineResearchAndDevelopmentApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
