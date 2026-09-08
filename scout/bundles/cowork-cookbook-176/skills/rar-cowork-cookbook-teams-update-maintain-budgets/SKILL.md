---
name: "rar-cowork-cookbook-teams-update-maintain-budgets"
description: "Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_maintain_budgets", "rar_sha256": "87620539f124bb008d69cca52befc87c03c4aec89a3155a6ade8c402cf7c748a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_maintain_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_maintain_budgets_agent.py` and in the RCI capsule.

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

Maintain budgets Teams Channel Update — Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-maintain-budgets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 87620539f124bb00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_maintain_budgets_agent.py` first:

```bash
python3 teams_update_maintain_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_maintain_budgets_agent.py   # or on stdin
python3 teams_update_maintain_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain budgets Teams Channel Update — Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_maintain_budgets',
    "version": '3.0.3',
    "display_name": 'Maintain budgets Teams Channel Update',
    "description": 'Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-maintain-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-maintain-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '964a95d31b6aea8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/maintain-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-maintain-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-maintain-budgets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of maintain budgets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-maintain-budgets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads maintain budgets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': "Draft a Teams update on maintain budgets in USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-maintain-budgets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on maintain budgets status from D365 ERP, saved as files rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMaintainBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMaintainBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-maintain-budgets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMaintainBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
