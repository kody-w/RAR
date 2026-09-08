---
name: "rar-cowork-cookbook-pipeline-risk-and-next-best-actions-review"
description: "Reviews your Dynamics 365 Sales opportunities for risk signals (stalled deals, dropped engagement, quiet activity logs, slipped close dates), cross-checks email and meeting activity, and returns an interactive HTML pipel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_risk_and_next_best_actions_review", "rar_sha256": "e6c9b0ec39565cd659f56d5efb94f9d57ce0b414cc26992f58cebba5a554567e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
