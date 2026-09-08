---
name: "rar-cowork-cookbook-teams-update-define-research-and-development-approach"
description: "Summarizes the state of the define research and development approach in Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON with KPIs, status indicators, and quick-actio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_research_and_development_approach", "rar_sha256": "3019476fdc92487baa6e1f886cc453fa425a6feaeb7721463205d645212419d6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
