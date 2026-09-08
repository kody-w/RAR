---
name: "rar-cowork-cookbook-scheduled-brief-issue-requests-for-proposals"
description: "Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_requests_for_proposals", "rar_sha256": "a9748b860dadf493d9045115621fcc1ba0561a39d909c6974ff3f63ea8de51e2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_requests_for_proposals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_requests_for_proposals_agent.py` and in the RCI capsule.

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

Issue requests for proposals Scheduled Email Brief — Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 a9748b860dadf493…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_requests_for_proposals_agent.py` first:

```bash
python3 scheduled_brief_issue_requests_for_proposals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_requests_for_proposals_agent.py   # or on stdin
python3 scheduled_brief_issue_requests_for_proposals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for proposals Scheduled Email Brief — Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_requests_for_proposals',
    "version": '3.0.3',
    "display_name": 'Issue requests for proposals Scheduled Email Brief',
    "description": 'Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-requests-for-proposals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86b5b21c78f0ad6c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-proposals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-issue-requests-for-proposals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where issue requests for proposals stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on issue requests for proposals for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue requests for proposals, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t', 'example_request': 'Give me the 7am brief on issue requests for proposals in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly (e.g. weekday 7am) brief on issue requests for proposals with a drafted email and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefIssueRequestsForProposals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueRequestsForProposals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefIssueRequestsForProposals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
