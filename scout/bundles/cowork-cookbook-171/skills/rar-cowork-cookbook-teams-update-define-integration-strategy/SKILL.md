---
name: "rar-cowork-cookbook-teams-update-define-integration-strategy"
description: "Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_integration_strategy", "rar_sha256": "61d15394933902260ea8879fb9cb5e549bd78e805725fb41cce17de476f69446", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_integration_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_integration_strategy_agent.py` and in the RCI capsule.

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

Define integration strategy Teams Channel Update — Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Initiative or workstream to summarize, e.g. define integration strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 61d1539493390226…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_integration_strategy_agent.py` first:

```bash
python3 teams_update_define_integration_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_integration_strategy_agent.py   # or on stdin
python3 teams_update_define_integration_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define integration strategy Teams Channel Update — Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_integration_strategy',
    "version": '3.0.3',
    "display_name": 'Define integration strategy Teams Channel Update',
    "description": 'Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-integration-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-integration-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a418da66cfe0f73a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-integration-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-integration-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'topic': 'Initiative or workstream to summarize, e.g. define integration strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define integration strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-integration-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define integration strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.', 'example_request': "Draft a Teams update on our define integration strategy status for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Initiative or workstream to summarize, e.g. define integration strategy.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update with an Adaptive Card on define integration strategy status from D365 ERP data, saved for manual review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineIntegrationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineIntegrationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'Initiative or workstream to summarize, e.g. define integration strategy.', 'type': 'string'}},
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
    print(TeamsUpdateDefineIntegrationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
