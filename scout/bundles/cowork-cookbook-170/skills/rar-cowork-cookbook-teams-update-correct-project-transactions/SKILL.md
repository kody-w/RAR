---
name: "rar-cowork-cookbook-teams-update-correct-project-transactions"
description: "Summarizes correct project transactions from Dynamics 365 ERP for a legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_project_transactions", "rar_sha256": "d4a99bfd77700f70955c24fe19f7892966690850aaa81e709cb3f846fa927fa6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
