---
name: "rar-cowork-cookbook-teams-update-issue-customer-credits"
description: "Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_customer_credits", "rar_sha256": "07def25f39cf5898c577dcdfbfe02602bf1368769b5161652fa49f2c6140a3e9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_issue_customer_credits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_issue_customer_credits_agent.py` and in the RCI capsule.

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

Issue customer credits Teams Channel Update — Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-customer-credits
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
      "description": "Output Adaptive Card JSON filename, e.g. teams-update-issue-customer-credits-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 07def25f39cf5898…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_customer_credits_agent.py` first:

```bash
python3 teams_update_issue_customer_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_customer_credits_agent.py   # or on stdin
python3 teams_update_issue_customer_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue customer credits Teams Channel Update — Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-customer-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_issue_customer_credits',
    "version": '3.0.3',
    "display_name": 'Issue customer credits Teams Channel Update',
    "description": 'Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-issue-customer-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-issue-customer-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c659fa4bdda6fe0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-customer-credits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-issue-customer-credits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output Adaptive Card JSON filename, e.g. teams-update-issue-customer-credits-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of issue customer credits. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-issue-customer-credits-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue customer credits, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on issue customer credits for USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-issue-customer-credits-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on issue customer credits status from D365 F&SCM, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIssueCustomerCredits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueCustomerCredits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-issue-customer-credits-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateIssueCustomerCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
