---
name: "rar-cowork-cookbook-pipeline-risk-and-next-best-actions-review"
description: "Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_risk_and_next_best_actions_review", "rar_sha256": "e6c9b0ec39565cd659f56d5efb94f9d57ce0b414cc26992f58cebba5a554567e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pipeline_risk_and_next_best_actions_review`. The original RAPP
agent is preserved byte-for-byte in `pipeline_risk_and_next_best_actions_review_agent.py` and in the RCI capsule.

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

Pipeline risk and next-best-actions review — Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel

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
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_risk_and_next_best_actions_review_agent.py` and embedded as the fenced Python below (sha256 e6c9b0ec39565cd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_risk_and_next_best_actions_review_agent.py` first:

```bash
python3 pipeline_risk_and_next_best_actions_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pipeline_risk_and_next_best_actions_review_agent.py   # or on stdin
python3 pipeline_risk_and_next_best_actions_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pipeline risk and next-best-actions review — Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel

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
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pipeline_risk_and_next_best_actions_review',
    "version": '3.0.3',
    "display_name": 'Pipeline risk and next-best-actions review',
    "description": 'Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel',
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
        "upstream_slug": 'pipeline-risk-and-next-best-actions-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77ab3f01e53025f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/pipeline-risk-and-next-best-actions-review', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: An interactive HTML pipeline dashboard covering at-risk deals, stalled opportunities, and recommended next-best-actions per opportunity - grounded in real CRM data and customer engagement signals.'], 'confidence': 1.0, 'deliverable': 'An interactive HTML pipeline dashboard covering at-risk deals, stalled opportunities, and recommended next-best-actions per opportunity - grounded in real CRM data and customer engagement signals.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads. An interactive HTML pipeline dashboard covering at-risk deals, stalled opportunities, and recommended next-best-actions per opportunity - grounded in real CRM data and customer engagement signals.', 'expected_output': 'An interactive HTML pipeline dashboard covering at-risk deals, stalled opportunities, and recommended next-best-actions per opportunity - grounded in real CRM data and customer engagement signals.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "It's the start of the week and I need to know where my pipeline stands. Pull my current opportunities from Dynamics 365 Sales and look for the patterns that signal risk: deals that have stalled, opportunities where engagement has dropped off, accounts where the activity log has gone quiet, and anything that's slipped on close date.\n\nFor each opportunity you flag, cross-check against my recent emails, meetings, and CRM activity notes to ground the risk read in real signals - not just stage data. Then for every flagged deal, recommend a specific next-best-action that the seller can run this week. Tie the recommendation to what's happening on the account - the email that hasn't been answered, the meeting that didn't get scheduled, or the stakeholder who's gone dark.\n\nBuild it as an interactive HTML pipeline dashboard I can walk into my 1:1 with - include at-risk deals, recommended actions, and the engagement signals driving the call-outs.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'An interactive HTML pipeline dashboard covering at-risk deals, stalled opportunities, and recommended next-best-actions per opportunity - grounded in real CRM data and customer engagement signals.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel', 'example_request': 'Review my pipeline for at-risk deals and build me an HTML dashboard with next-best-actions for my 1:1.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use at the start of the week or before a pipeline 1:1 when you need to know which deals are at risk and what to do about each one.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PipelineRiskAndNextBestActionsReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PipelineRiskAndNextBestActionsReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(PipelineRiskAndNextBestActionsReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
