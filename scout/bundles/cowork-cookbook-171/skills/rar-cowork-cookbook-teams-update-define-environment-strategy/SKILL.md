---
name: "rar-cowork-cookbook-teams-update-define-environment-strategy"
description: "Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_environment_strategy", "rar_sha256": "72f61a658618b3a5c371d19c73a6873170f5379450dafdc99e8c4b4d0ef33cec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Teams Channel Update — Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-environment-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 72f61a658618b3a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_environment_strategy_agent.py` first:

```bash
python3 teams_update_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_environment_strategy_agent.py   # or on stdin
python3 teams_update_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Teams Channel Update — Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_environment_strategy',
    "version": '3.0.3',
    "display_name": 'Define environment strategy Teams Channel Update',
    "description": 'Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;',
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
        "upstream_slug": 'teams-update-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '773570d3643e092b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-environment-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define environment strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-environment-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define environment strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;', 'example_request': "Draft a Teams update on define environment strategy for USMF from D365 and save the Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-environment-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on define environment strategy status sourced from D365 F&SCM, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineEnvironmentStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineEnvironmentStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-environment-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
