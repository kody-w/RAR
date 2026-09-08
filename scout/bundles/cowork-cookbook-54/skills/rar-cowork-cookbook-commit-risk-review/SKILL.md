---
name: "rar-cowork-cookbook-commit-risk-review"
description: "Reviews Commit-stage opportunities you own that close this quarter against email, meeting, and document engagement signals, then returns a one-page PowerPoint risk summary, per-deal follow-up email drafts, and a CRM upda"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/commit_risk_review", "rar_sha256": "6f2d5a4c82acf16a473bcecec558c602ba7d92320adb6cda936c9c1ba32fb59c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
