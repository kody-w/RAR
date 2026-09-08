---
name: "rar-cowork-cookbook-teams-update-correct-project-transactions"
description: "Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_project_transactions", "rar_sha256": "d4a99bfd77700f70955c24fe19f7892966690850aaa81e709cb3f846fa927fa6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_project_transactions_agent.py` and in the RCI capsule.

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

Correct project transactions Teams Channel Update — Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-project-transactions
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-correct-project-transactions-2026-05-24-card.json.",
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
    "scope": {
      "description": "Optional adjustment to the scope of the correct project transactions summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 d4a99bfd77700f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_project_transactions_agent.py` first:

```bash
python3 teams_update_correct_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_project_transactions_agent.py   # or on stdin
python3 teams_update_correct_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct project transactions Teams Channel Update — Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_project_transactions',
    "version": '3.0.3',
    "display_name": 'Correct project transactions Teams Channel Update',
    "description": 'Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-correct-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '885ac8308ad3fef6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/correct-project-transactions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-correct-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-correct-project-transactions-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'scope': 'Optional adjustment to the scope of the correct project transactions summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of correct project transactions. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-correct-project-transactions-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct project transactions, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons.', 'example_request': "Draft a Teams update on correct project transactions in USMF with an Adaptive Card - save it, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-correct-project-transactions-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional adjustment to the scope of the correct project transactions summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update plus Adaptive Card on correct project transactions status from D365 F&SCM; it saves files and does not post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCorrectProjectTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectProjectTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-correct-project-transactions-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional adjustment to the scope of the correct project transactions summary.', 'type': 'string'}},
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
    print(TeamsUpdateCorrectProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
