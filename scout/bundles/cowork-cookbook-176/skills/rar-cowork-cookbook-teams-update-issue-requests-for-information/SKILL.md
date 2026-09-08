---
name: "rar-cowork-cookbook-teams-update-issue-requests-for-information"
description: "Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_requests_for_information", "rar_sha256": "e8740e59b3081f7cc7e183ee9c7f367287b11956501ffa6b8b668dbf33ac893f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_issue_requests_for_information`. The original RAPP
agent is preserved byte-for-byte in `teams_update_issue_requests_for_information_agent.py` and in the RCI capsule.

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

Issue requests for information Teams Channel Update — Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 e8740e59b3081f7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_requests_for_information_agent.py` first:

```bash
python3 teams_update_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_requests_for_information_agent.py   # or on stdin
python3 teams_update_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Teams Channel Update — Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_issue_requests_for_information',
    "version": '3.0.3',
    "display_name": 'Issue requests for information Teams Channel Update',
    "description": 'Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad422a5956ee3307',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of issue requests for information. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-issue-requests-for-information-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue requests for information, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of issue requests for information from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file for review; nothing is posted.', 'example_request': 'Summarize issue requests for information in USMF and draft a Teams post plus an Adaptive Card for me to review.', 'inputs': [{'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update and Adaptive Card on issue request for information status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateIssueRequestsForInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueRequestsForInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-issue-requests-for-information-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
