---
name: "rar-cowork-cookbook-commit-risk-review"
description: "Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/commit_risk_review", "rar_sha256": "6f2d5a4c82acf16a473bcecec558c602ba7d92320adb6cda936c9c1ba32fb59c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/commit_risk_review`. The original RAPP
agent is preserved byte-for-byte in `commit_risk_review_agent.py` and in the RCI capsule.

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

Commit risk review — Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda

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
  Upstream entry : https://coworkcookbook.com/recipes/commit-risk-review
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
    "crm_pipeline_snapshot": {
      "description": "CRM Pipeline Snapshot spreadsheet (or a connected Dynamics 365 Sales environment) containing the opportunities to review.",
      "type": "string"
    },
    "deal_owner": {
      "description": "The seller whose owned opportunities should be reviewed.",
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
    "quarter_close_period": {
      "description": "The quarter whose closing deals should be included, with its deadline date.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commit_risk_review_agent.py` and embedded as the fenced Python below (sha256 6f2d5a4c82acf16a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commit_risk_review_agent.py` first:

```bash
python3 commit_risk_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commit_risk_review_agent.py   # or on stdin
python3 commit_risk_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Commit risk review — Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda

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
  Upstream entry : https://coworkcookbook.com/recipes/commit-risk-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/commit_risk_review',
    "version": '3.0.3',
    "display_name": 'Commit risk review',
    "description": 'Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'commit-risk-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/commit-risk-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f894e03ab8f3993',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/commit-risk-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PowerPoint', 'Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A one-page PowerPoint risk summary, a targeted follow-up email per at-risk deal, and a CRM update file with risk flags and dated follow-up tasks'], 'confidence': 1.0, 'deliverable': 'A one-page PowerPoint risk summary, a targeted follow-up email per at-risk deal, and a CRM update file with risk flags and dated follow-up tasks', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'crm_pipeline_snapshot': 'CRM Pipeline Snapshot spreadsheet (or a connected Dynamics 365 Sales environment) containing the opportunities to review.', 'deal_owner': 'The seller whose owned opportunities should be reviewed.', 'quarter_close_period': 'The quarter whose closing deals should be included, with its deadline date.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated. A one-page PowerPoint risk summary, a targeted follow-up email per at-risk deal, and a CRM update file with risk flags and dated follow-up tasks', 'expected_output': 'A one-page PowerPoint risk summary, a targeted follow-up email per at-risk deal, and a CRM update file with risk flags and dated follow-up tasks', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "It's the end of the quarter and I need to know which of my Commit deals are at risk before the deadline. Review all opportunities I own that are closing this quarter and marked Commit in the attached CRM snapshot [or Dynamics 365 Sales]. Cross-check each against customer engagement signals in emails, meetings, and shared documents.\n\nCreate a one-page PowerPoint slide summarizing the at-risk deals and the specific reason each is flagged. Then draft a targeted follow-up email for each at-risk deal that directly addresses the risk detected.\n\nNow create a CRM update file for the at-risk opportunities - flag the risk on each affected deal and add follow-up tasks with due dates so nothing slips before close.\n\nAttach: [CRM Pipeline Snapshot.xlsx]", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A one-page PowerPoint risk summary, a targeted follow-up email per at-risk deal, and a CRM update file with risk flags and dated follow-up tasks'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda', 'example_request': "Which of my Commit deals closing this quarter are at risk? Here's my CRM pipeline snapshot.", 'inputs': [{'description': 'CRM Pipeline Snapshot spreadsheet (or a connected Dynamics 365 Sales environment) containing the opportunities to review.', 'name': 'crm_pipeline_snapshot'}, {'description': 'The seller whose owned opportunities should be reviewed.', 'name': 'deal_owner'}, {'description': 'The quarter whose closing deals should be included, with its deadline date.', 'name': 'quarter_close_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call at quarter-end when you need to identify which of your Commit deals are at risk, with follow-ups drafted and CRM updates prepared for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CommitRiskReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommitRiskReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'crm_pipeline_snapshot': {'description': 'CRM Pipeline Snapshot spreadsheet (or a connected Dynamics 365 Sales environment) containing the opportunities to review.', 'type': 'string'}, 'deal_owner': {'description': 'The seller whose owned opportunities should be reviewed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quarter_close_period': {'description': 'The quarter whose closing deals should be included, with its deadline date.', 'type': 'string'}},
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
    print(CommitRiskReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
