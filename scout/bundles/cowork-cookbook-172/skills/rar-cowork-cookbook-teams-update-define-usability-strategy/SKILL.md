---
name: "rar-cowork-cookbook-teams-update-define-usability-strategy"
description: "Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_usability_strategy", "rar_sha256": "ba48be0d6a1dc14975d2f9b5aa50eb029f3d817000e34df86f8d0a6f3386b34d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_usability_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_usability_strategy_agent.py` and in the RCI capsule.

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

Define usability strategy Teams Channel Update — Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-usability-strategy
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-usability-strategy-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "The initiative or workstream to summarize, e.g. define usability strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 ba48be0d6a1dc149…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_usability_strategy_agent.py` first:

```bash
python3 teams_update_define_usability_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_usability_strategy_agent.py   # or on stdin
python3 teams_update_define_usability_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define usability strategy Teams Channel Update — Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-usability-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_usability_strategy',
    "version": '3.0.3',
    "display_name": 'Define usability strategy Teams Channel Update',
    "description": 'Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is',
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
        "upstream_slug": 'teams-update-define-usability-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-usability-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8699bad9c6ea8dff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-usability-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-usability-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-usability-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'topic': 'The initiative or workstream to summarize, e.g. define usability strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define usability strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-usability-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define usability strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is', 'example_request': "Draft a Teams update on define usability strategy for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or workstream to summarize, e.g. define usability strategy.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-usability-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on define usability strategy status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineUsabilityStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineUsabilityStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-usability-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or workstream to summarize, e.g. define usability strategy.', 'type': 'string'}},
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
    print(TeamsUpdateDefineUsabilityStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
