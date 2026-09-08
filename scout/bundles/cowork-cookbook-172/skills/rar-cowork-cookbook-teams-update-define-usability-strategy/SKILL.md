---
name: "rar-cowork-cookbook-teams-update-define-usability-strategy"
description: "Summarizes define usability strategy status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_usability_strategy", "rar_sha256": "ba48be0d6a1dc14975d2f9b5aa50eb029f3d817000e34df86f8d0a6f3386b34d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
