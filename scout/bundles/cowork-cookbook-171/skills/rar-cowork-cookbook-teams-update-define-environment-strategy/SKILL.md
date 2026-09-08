---
name: "rar-cowork-cookbook-teams-update-define-environment-strategy"
description: "Summarizes define-environment-strategy status from Dynamics 365 ERP for a legal entity and returns a Teams channel post in markdown plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_environment_strategy", "rar_sha256": "72f61a658618b3a5c371d19c73a6873170f5379450dafdc99e8c4b4d0ef33cec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
