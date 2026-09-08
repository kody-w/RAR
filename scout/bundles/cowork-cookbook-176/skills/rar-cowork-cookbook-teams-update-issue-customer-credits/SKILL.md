---
name: "rar-cowork-cookbook-teams-update-issue-customer-credits"
description: "Summarizes issue customer credits from the Dynamics 365 ERP plugin for a legal entity and saves a draft Teams channel post (markdown) plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_customer_credits", "rar_sha256": "07def25f39cf5898c577dcdfbfe02602bf1368769b5161652fa49f2c6140a3e9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
