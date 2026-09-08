---
name: "rar-cowork-cookbook-scheduled-brief-issue-requests-for-proposals"
description: "Builds a morning brief on issue requests for proposals from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_requests_for_proposals", "rar_sha256": "a9748b860dadf493d9045115621fcc1ba0561a39d909c6974ff3f63ea8de51e2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOi2LrmX7H3jeiqumYmMop540Q0IoMIKJMMlSeymEGZZJChuv57L9SdWXVOndtdt/tTm5Ghwlrv/D7Puzb++uZ2bVLWb5/ftNAtFpybZWkS1gu3CBZ02Zf1FbyVVw/8X/hl0dap17Vl3bx9eAvCxq/Tqk3LAmzfdmkWNAt3kZd1kRbxwqvTMFqUxSJtmi5c1OGtC5u2WURlvajqsiobNwPf6jJf7MbCzVO/WaAEvmDU0+LHLIzdbBEWbdqOC0OT2J8+L9qyWuCLtA3zZuGNizSvXL/9ACwtczdLw2ZxbxZtEi7WHwN3XNQl8ASY4d7D2o3DDw+P6tAv8zwsgjBYFOHQLoAEYH7zYd5YLBqweHYhqN2oXYS5m2ZA66IFzoaDm1dZ2Lx9/vnvH96A7uzt869vfuY2zRw7PwmDLguD7ez0fnZYffnLlvXp3VsgJ3OLGGyoRhD1AnyvwhoEJAeXAhCt17cfmzCLPiz+/d+vvVvHzU+fvxSL1+vL2/xP7YqHq23pNi3wxXcr10szEKxPCyrr3bEBrrZdXczeNCBpRfzpufO7JBDNv833fnwq+RSH7Y9f3kpggjvH5MvbTwuQqS9vdTd//jRLqX786VNW9mH940/f5TSddwn9dhYGrP709fX9JRYs/L40jRZftRNDv3SBbKRVCIT/zr/59TT9Je4Vkq/PxT+W1YfFn0ue/fkbsPdZlh6Q++diQQzAzrdPlzItfnzpqMt7WLiFH/74078SCzLsX7O0af+P5P78FJyEbgCi9QrJTx8e6fv7Yvny7ZvMf622AgXzVzwBy9/VfQvUv5L9yOw/iAY9A1rgPZd/Ku7PNiz/tvj5X/r2n234sIi+vO3CLJ3b1MvCz4tfHyXy8w/B94s//P03IPp/K0Yru9p/SPiau0Uagfb7+vXnH5rH5R/+/vMPXQWqOHTzr12d/ZnMP4vrQ88fIvha9eMf9wL9RnEtyr5YfOuhxa9l9d/q3z4tzgCggu/Xm8+L33fi/FouZifelT5D8LtubICtv4vjT2+/ARAqgDfdE8AAfvzbvy2k1K/LpgTYpfll1y5Agts0D2fj9SRtABI/UKMOQVybFAT2tQ7U/5zh2eIyWvzyP/wH8H/0X8APNe/w9vUB6l8fiP71HdG/gv78+g3Rf/m00IGOsk7jtAAYrlKn05cCIHDRzvqrOmzC+g4wyxvb8CPY+nH+sEiLxS9/Rc3Xh8RP1fjLA9jTJx6q9H7GwgYI+TR7bc6o/vTRB+wWDqHfAWVZ6QPLohTg+QcQjabM7gBL5wg11zTLFkEK0Aaw3Pgkja74PAv75ZdfPLdJvhRP8EYXT/prILDgmzmLjx+Bi1GWxkn7pQj9pFz88OtvPyz+5+I/2/UQPus4AT555QhYKGhHeQF6rgOUBZhzTjgAlEeOfv3tFWggpgB8DTKaRjMJzptBzV7D4D3qGk99RHBi4YUgguHMm2XdztSYtp8W+2jxzV6gdL41c0ZSNu0iCKuZKgt/BFJd4M63SBZlC8iyTZto/LDomvCh9Revdh8m5qD53faXhUSfAEOVDw6tX4wFNpdFCsL/rSae14GQ+odmsX0X8Wkhz1W6qNzarZLafemI3GdeADO9bwfCXUDm/ZdiZuVwDtWjZZ7hAYtAZPxXSj/OOV/MMwBIbPOu+7HGnXlUf/Bp/aVoXu3g1uFjaACmjIu4S4OZJP7jVVJNUnZZ8IgfsHSW9MpC8MrKowb3/9n4821wWDCPaeMxPyy+dMgKxhb/P49Uc2QojlMZjtKZ3YKRddV+ZmyeMufMPgfT2djZvUd3fh9z3qHsHdG/FFkKyq8e/+O58pHn15onSnY1MFCl1Id8UGQgY7PcRw/MNV3Xs7/ul+KdOoB7iwdOgngDwAANNRv+rnC++25pAlBh/v59jHhEpQ7mAIE6X1Sdl4EajMIw8Fz/Cqyq5z5+pRk0RDj3dJ+kfvIHr+ZsgboD8h9JB5kG9PLpG5w/776b/oeNz2lp3vKYJDuQnvohANgRzgbOqevTFqCZ2z6HeuDn54cQ4EZetbPvHmik/MPrYjiXW9qAYnnmFsQ1rAB4f5zfn57OV8OhAr0DggU6pOpAdB89NZdNDmYhYAOAFdBieVqA2QAE5RWEh0A3nwECAPBreH1KfFx+ORQ+GnEmtfeNsyPznnlOeJa+W4y/xxH9z8oEyMvnFQ+9/1hp37TNsmcsbQAeAo3vd58DxafnTPAcOhbvcj//06npx792sHqwvPHHAvi8SNq2aj5D0JOZ34n5E2g96Glr852kPz5g4uMDIz6+Y8SDab9hxB90PN3/vPhrdv5BxKtPPi/gT6tPq/mW+Kqz1wuEhf64tT9i890vhRp+x1ygHqBNO3NCNs4o9E6Q70sAS8Y1AC+w+EmYzcyzPUCXB0OAjHwpfl/4c+MBAiriuVCb8neA8JgUQBM8E/iNyMCtogW6g3nejMNP8zFtNr8J3z4XXZZ9eANYGv6lY95MW/lc5818TJzjHgLODR/fHrAxtPPHPx6hj48PbvZpsQsBRGXN72vxRTYz2f6uZZ7uAjd9oOHDIgBBamZyBO7Oyud2c5vrgyFmt9qxmv14ngjnGfJBCl+fpPDPBv2BRNj/rtHS4g8sAvAQeD+DLji8ul0GQgsuzdzyp8q+TbP/rMkEA8O8Nyg/z9z54QVC4B2cQD4svh0mgIuv492sISw6cHL+eT7IzDF/bJk/gD3g7dumb3+r8MK3v/+ZXT0otH+2SQ2bChDZY05+LAE1V84RD9P7C28frAZq+Mlrj777U8/fe/PPHA+fQ8iT219ZfoQg/BR/WvRheJ259zUCAIZqF2s3/xMtQM0DoQHPzTH5HuzvLpePg9xsEAhR+/y7w69voE5dUDjuq1JfJwGwHADax2aedCDQ1kAh+P5sQHDv/+qM8JLVJC6YS4Ewd7PGSI8kVoEbRNgGDTYrDIdhnEDgyPdhz13hBOyiG3B94xNgcRShEYGGLhmEOBwiQN6zpb/Os0g624dv1tFqs0EiDEZWAShPBAsCkiAJH18jK3fjubiHb1zv+9ZrWgQvp59OzhH9dlyZg/Py/dc3j8DASh5r9tTzRUMb2IPMtafWHmStyCHrW1/zGi3zXHRtHPDOvKTHedYxG4zQsENN0tIo8EyeCs4uz3iJmhpl2evr6uSj03VScMbA7eUKtUlul46qhETHQoKio35CThzUq117SA1xc6azwK35A10xlungVW5eBrEdyxtTGQJDoNJ1zaSjYB4g7nSH4OB+uKSCLNBpDpsVzxHstV1mrpHey3t8a1IE6wxQfw0GHw9ivcaMahkUdqWVrTEyWtNh6L64o2t4IzuEKDV3Nhv3HXx2RdxYMwg8crih72X5fhBYx7W4TPUqHQuTWig0YAXNILhg3HC2VjsqkRI5Q26b/Z5bXc4DfKCUaszC6143CGbIRVthLeFMN8Za3MnqLvZO1ppcnlB0A53QSkN5Yh3dJx6dBj7tWPN8o9WRq/1KOg901dbtxJilMmZkg5VmONju/RCcr2Wnrq6kd1CGkKg4Lz0wS5OzGeqcZcZ23RBRMck454Y3WxQGwm5QQYmtrQmbu9oeL2dfOXh23jC5fLHjKz2SA7ca13iYthgqXTa2u1SgwTpU5+rGxqlq6DQXbvHWmFLjMBppZY93Sj2VW3oIW6k5a4KXhq3Mc7i7HJmW1bt08m9cApgE3pIS2p66aXfnfaRxzyU+qapsNNVtT19Bb+8q25AU9xD2hHjxd6bjsPfDsDfQY07NrWHkntWUI3pdN8rKQNi8tVOWKfFDMRLWHq2CJalat/LU2TeR5q41XU/0VdgUqyy43rLGMXQyZdLzrb1wrj3x+3AZpv61lWlC3wrDTiWuIcxA7TlRbCS+9hUfa6QBXXB17zqXziIULKRwky7d1VC6+DmWXXN7pzXL627nUdSaIy6Kuu2cC/kenO1zaYtNYl14HjMvx8QvEOtsWkfBCuqCiSaWqBDlZpVHKKROW4a0Oma399hiMIkdW0YtZC7ZoRkvokVurg2+z5MijHYD4nKGjupivpWOKg7+J5Kl03Z8lyteGV0NT9uJtC4dN2gNjQ0sDuE6BID+JBUuHCH8Sh2lAh16SIVIXujr1gbd4wliTa32cWVc4DPKctnKlFT8ZgadRu8sot9v6fI0ML6oRDWxc5YUzKZneSdUpn7Hzl6uEUJ9Mkz/1Lp6eyUN5y4J9moybgkJ2qyxFCPe9O7yrihZHGyxbb+kJWXy9WOsW/EVJdAV3uxrR8BPubNygm6QJ75hzqWJ9shSutyco2bd2e1htOOtoR8lgzGYQTkgTpmec5WpV/e9rNzRk1TCxTUNMNZbn5iqOrjXi7hrDzWUVccD4tFjENwbzESjSVsXZs6vhot8LOPWaqlqlfH0yDMT65+T0lG5VnPKS7SRRkaHalCWwnIQbTtjc2UcVpuUPR6S9HawQ6hbDlVnb8N9LcS7dJcpqo77pojTF3ZTDDaOwFWikxCsC9p1s83NJjz514GuWWYKqRLNk+Cw0w6bOi5rVy32WpBk1OkUhct9cIxE1zwqy+OpSFDiiLKmM1VRJG4raZ+kHSfilI7ti3EaqbYP8NTB1ucT4qopL3g2KwbObY+srCVJb1nX0emdRm65rESCrX+Nc30wQH/R1YZYG42z297vAAEUFTbI07Ax3EKAKvisJb2jeAYZWjE23bNkQAdCzRxWiU93+qjLmoEtY4O4yT681nn9Llg6tKyWmsbfLDdW7lN8kRWlx1uBc7S+BDSXcfd9vZYpXVLossiUdeBS6iQb6vV0CQSEYHpTQoXUugwxSaX2TUGbC+0ojK2Ve1u5IHFc1PyWORcMfveQybpHNiOJN7CC30kjl5ciWB6IjI6p0zHY3dNqH+jb5uLoB1u5lfTpkHaqXd7iRt6ze2Z974xNgnGpdaj3O6z2dmvdcPDa0KWAqvuToQDUrMsouCjL4VafV3ezXdmKJTf2cddWiC83uamLnM9dEAcKC2FYLpeEQWV0Up4Um7F41AWgqKZXCNQTth1UYr3jtMoZcTIiTlzG923O8Gs1ARmw+Bp3IvECQeJpIi5EU0j38tbyTiagGQwfXYdfdch+r2Cj4KSUl+BbuzVZrrjAWnm89YrqF5idJcfy5nknip3kwYuoNZ9OtXGTVgo7oClt9Vhw4TKXJ+mMXgoq3UlXNaMJel9KaYKroS5pdtbmBtMcU8m2x9WRU/JoxZV4ArBXcIsDMYmySGqHe0o3buygPkGW+7PO2mbH9+Np3697CCn9KtSn6Txa2xXlZ1kX8gdvXEUs6+x05mAuL8KR2RT9tDtwG293v0K0xl1lV1N93k4aN8pFxUQ6DXWZeonlTtlQQk2FpXAVDmlPU0aDm2vWAiRthUq6L/QCF9cuPVCOGTcDSjk9B4naXS6pFD32PMSzSqdYcV55/Dliz8mBYr3YjpibWCj4zuTOQjpQhWQeDzcGtGpuGYJ/VinQX6wYr/KqM9J2WV/Ckd1fQXEPzrAEag/aPbZ7MoqRlSgTe5V1qk7kV9hWcppsFQrYTl2T5S29SIM/bm/bThNue790uMo2UTny1gemH64kp7S2lkwtLVt3F6Kza2olHW2x7mRTHRLRRcpjMCwVXLq3vHzs6qXF7o9wqzPStGc4urJxqx+FbbW5b22KTn0cr9Oro9u6Hu9c3qgBGtFovSoETIKlQNlbOTn5qXEn0cN5yGgyz9Ryr6ba1VaXfTEdc4HtZXkbc3vL8a19dtwz/OikKTZw24sVXogzJEtawbjJlpCjRJt8ldoMvCeV9oVs8iXk7dVjX4v9rvdGYnJ34aaoOYqajqQk35HBkhNy5TP+bV3e62hnHENsZbLd5SwrdEsEhYP7IediLZocNraTRcItO0i66467za4uBMWVEBP0nYfHV7/IO0XYEYJMF5dldZaM1oPLbt8kYNJS2K0B93VioCE/UdZZjmXH5mycOjhTCPeG7ZpCS4dyJK7vLFrdT/U9GIO7YQuKs3OcQm+Eo2IOcbVnWZ2V6hXKhE0mnkfESfdce93InHzC1tSQKVwp6SeXRJ11MwSqRNN7maa1vi6Vg4mX0IqTb7thOcC6snV7FNY3d/Ikro89Uh0SZNmTUr/NNiUfRlV4y/pzuVT7JeYc6vxEQaMSKJdMvES3a8LCIhRJWLk8RgdYT68CBwbm2mQ1YWem115Z1ckSKyv0Zgz5dW/5SD2kGLVt8anrEsRKU9znHN3xFGPrskopVQeTMBDzxo40xmwHWWV0x1pRHLJNfe18FLVlJYrVzfEIQvQCN9lYdXM7G8SeTMYjvzn0hkRfuYRQKRNmfAkWmGw1VdZxb4/2MoPI637f+m6UHpZdXbBk7MOS6fcekoNR/BpdRdZkfa3gB2/yJQIMymQbLjvWu4GRcEJGmbrQaxYmaS/bIsES3zK6y7aBLN3acwEOVywpOPKBi9ykkXfGuqOONBkbsnaXUvGWhjfJOG0xOlaPXi+InbkKjzA5NLyAlddVBzBj61MRmPhVKW2Go+VajrxXONi58d06v/dnaUX7V2opyR4mrlUi2yz3id5NHNTS5YgnqjWka7EszBRFojjs7q1/tUYBXm2PI7nU3HwtpiUjrZrIXAuivBsL+MoTdYcUtt+rwX11oat9owdXdUJlgu9Z1t4w7inLt3d+h8DCxReHlWMb+zhBS5O+LVeeMRRFkbLVebNPN0xxvmRU1mmAFJD+LnFOJx7y+phObl+o1QVuz4gGwbnlmxlhtbsteyDVqTZRSpXP2j7mzdvaWycbO8a2o5Qr3EVutmLcpWmWI15mwvr5uCU9I0ME9zTR+IaNpZJNaFgjPQT18X2ZZw4BimMrUq3XSjEomjZb631GobV33kEK7bjHMicpodiygltfQ2xtn3AsX152pDcIZ3WYgmmqeRlmAxnV5XZdaqio6/dYxRVTKOOLlR/H+FLJdDpWFWymgljSB9rQ+Y2tFMVd8yS0O7o8mJqobmwvRbOjUxhHuCMGToIdvbNxcoh2HpZ6poQUuERBuooUx4RzjUOrYjih0EmfLHPzvK4IJ9otLxZbHpgqDe9H8kSh6JDnSxqcP857FOcKsR7YgdILuSxpdLdpBl2IkeE02kkUK2tpt46Ck5cELnwz+jV1XzrlfnvYaqLeJ5V/LzxzqeZx78IJxcQRaSw5JkZvsq6BYyTJNFkg1BCsrfGLSzDbfHMiGD0m7mhUs5iGZ2ZHJEkMV8udepMUJx/ijXGXmCtvcoB6klhnAHea98tlqsJqOgyIYF3IYjxZLjL5dx3fKY5haTC0FbADU+cr4qL3HXrq3ebUXOPVmRSIW3CWXZgI3EiY2C2yK87p8t50ouSa5kok2dYKYZxPU+dQbDSYjJCOvTS73iAK1Y2mXl3TUML1AdbApX9yeAY7sp6MrtVbZIUr80AOrgd1PFUil5G8IylpoU7eKuTuOEjuen0Zu6K7NFYdHM9djZ5ZUdfMguvudp6AySKEVTUvj5kTwwjDZMu1U0tZtMwtcrdEtEKPuuse9eTUCnaIGPkWUcSKKU25UIpm0oMppaRiS+DEKSg1eFA617M28OmAXVZnMDERWghG8NywN8uyybMQ19oJ5lx/s91P67pmLa2N1twkd5st7NunpF7XURIXotWi4XHrWdMSW26gHoPsG60UzaRG0CgvuZZX1OLkTfVIZs3ZBWNCOkSq2GpyKZ/ExuQ2tDox+AbzNyvSyvUxSRQC0qnOOFLhPsl29jjwK4nH+GvOTi5J2ktCl6LL+a5jlekc9Y3SeJniyNjxGG8828J2BEWweQE7U3KX/MhOh6b3LikUQoTrdDumna6Ea25GLQ4VqtnwUBjA8BknvIHK7r5yF3EkR8FRtkl2fe56/e3K5VFqt2wBqS22AVOwN4GzQ9Nxd6/J3QQO6Bg3L5vjAbJqogmaHvdxS+9tRd/HaiTGmBeFHd2spTWWCHHVei4K03SXQMlJSC/IBNfWmewE5QaibWBcJiNJM2BDsybDBjBGg+HctsAvjo+QCZRS3bnCFHkTq4dVrqbxKAzhbr/ZSQRVjjelZKlpSHN2AxFYafclYXh5L1dViV97Zts6DLIttTOdQ2nTmHyTyI2iJiLfFpJ95JsRksr1fq3mmo6uXci6jmEYLdf4/ZRRhEm6VNqOxrRBwy0nyzUW2Oi5WeP5dplgAQvDmg0Rzq4LdSuxBATaW+jpoF34miBdA2O4+rZmqHZgYDBN9ytLGo+bwRWq7GQFOXWyzb3S15PXAxww2TLKj/lFxA827G0SJkzUQc3CgIqccNsS8pEUb4f7LtFEavJDM1gfoAuZ8vJd9myoBtM/nweue9qYhrQpLZ5ccQ4u4vWGMTMvTUaOi0Oa32OdWTrhfdkP/hBSN46Ox7U3DcA8KtROULlxij1+23enAdvi/FHVz/mkajyyEuzMxWIdwXoUKQZMrtZ+l5Bo5ZJEfSqik38xILVRoAnit7cMPZ7qxmImsV92+5PsadXtxm9P+bgJ8ua4rrDJR4rbfQ2G2OUIZcj9foyTqgv4wgvY63ojJlJVZysHjvaO6bm1SHEnCVndVdTvJN5zYZNn3COYGJFpJaRHvLgdFS2Uic0hoEmc9x1tHUY8JhxJJWVabVfxsHAowkZeyx2HKRepIt3cC5LxcIimjW9T58a9bUE8V2Vaa6cbtdz5PJ9wWmlgGBknNkZEgxPfBOayMTwBPaZIS9c3a6dttivf16ylOfi2A2lRVtUto+ZW3KzcXmQGo72FOzEFcABgYnMTu14lCBqcyTd4J4bDPgkUO+6Ge68Q6KFIknW+X0sHvhHi9nDyRoiYlku5vaFS3VeHHQxc74gREjjkjNFGZLZMd4RsbixCdOe0B7JxRripvaCzb6i1zLNb1lKT2ZVBdukm0Z7kemfe3Im/+O1E9Z0cFEg56CjEnDVdtMKNZlbhIe/kNApve8ATl+vhNLS2TCIkjRxjGQ+b80UrRpfisjK8YiIK+o9XI9h2MzJuUTOp7FO/kzEc3+lHH+/UgcCbyG0nU0baCu3SibkT/ni6ZQ001Gcs9LtlGJInLlohThd5OuMwjh2v4sihcGwrc9sSvcSnO3qHBMkY8wufCiQHK50Z+4ftpu3E1sBBRa07x0ItduMe9ic+g84jqh7LI+6vQH5OxrH3uo7zBVlvnN1918eri7Jx9yLmmXDokVWQNeYU3+27tLsi66DEPeveWoMk8XdtK3g5ZR+u09WzwqAbKbmtm2WIsR5vb6gdE7s4bjLMvmGJYaUrpxOxMfttT8hePGi8U7WIn3tHx/CJQrb6dLVk69Mu9IMA6WSCiqgBldnrKSjRxDdEuEicjWUEGzk6mhuUXa6RcxhMSltvluk9CByoGCEICbDtTeYgKdwhkc2HWxviJttn9F2Lwwe0Nera3+5bWDfb4bq0oLOxRSPcEfgjEvUk5JqHwJnOt+26D9YphB5QH5SVe3NsGKugXALTinsytR2y3JBRv9uuNfaCoDc6y6fC8m9RgBKmOw7J0HX2pFxDmspolMxzX6jiQyoJuqXouAZm66r3T2J3c0kXY+nhioFpLSlIJPaMnRsfDrtkjLL9SI+5A69HFd2pSrRaJt20VlJ0vYFgcePulBIaJh296HWIZUtvqPg9X7kSbHWbcFuE2bQPmE4yA/ZYplW12ur6dWVtQbkpkHiHyJA0M2rdbJ3ihPcsdEt136kYNs1IlYwvCU7E5q7pkEQVoYu0PMIYedrcLlLI3VcMRVF/+9vbh7f5yevr+el/6Qde8xOa/2cPip7PdN5/pvF4dhi6weeHrs//NfP+/uGt9lNg3PMhWZN18esx0j88Ivv4V57Qz5LG52+p3h8XPx9Ft248/wj5LS2Crmnr8WtTZo8fb4AdXtfMv1ZsZjN98P77h6L/4Nz3515t+bVy5yinxfy7jDBI3TZ8fY1fjxA/vAWvR8FfUQL/GtbV7PbrqT/wFv20+oS+/fa/AAa3jixOLgAA -->
