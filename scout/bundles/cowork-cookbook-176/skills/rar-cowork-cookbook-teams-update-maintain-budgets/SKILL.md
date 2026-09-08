---
name: "rar-cowork-cookbook-teams-update-maintain-budgets"
description: "Summarizes maintain budgets status from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_maintain_budgets", "rar_sha256": "87620539f124bb008d69cca52befc87c03c4aec89a3155a6ade8c402cf7c748a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
