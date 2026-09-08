---
name: "rar-cowork-cookbook-catch-up-on-follow-ups-i-owe"
description: "Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_follow_ups_i_owe", "rar_sha256": "8dff5b43009f4cf83bac27a39927c7bbeeaf9a574ecc359c0eaebf9fe11edf41", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_follow_ups_i_owe`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_follow_ups_i_owe_agent.py` and in the RCI capsule.

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

Catch up on follow-ups I owe — Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review.

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
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
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
    },
    "time_period": {
      "description": "The meeting window to review, e.g. last week.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_follow_ups_i_owe_agent.py` and embedded as the fenced Python below (sha256 8dff5b43009f4cf8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_follow_ups_i_owe_agent.py` first:

```bash
python3 catch_up_on_follow_ups_i_owe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_follow_ups_i_owe_agent.py   # or on stdin
python3 catch_up_on_follow_ups_i_owe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on follow-ups I owe — Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review.

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
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_follow_ups_i_owe',
    "version": '3.0.3',
    "display_name": 'Catch up on follow-ups I owe',
    "description": "Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'catch-up-on-follow-ups-i-owe',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6e671423d8bb688',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/catch-up-on-follow-ups-i-owe', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A list of un-re-engaged contacts with a drafted, personalized follow-up for each.'], 'confidence': 1.0, 'deliverable': 'A list of un-re-engaged contacts with a drafted, personalized follow-up for each.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'time_period': 'The meeting window to review, e.g. last week.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Close the loop on every contact you met but never circled back to. A list of un-re-engaged contacts with a drafted, personalized follow-up for each.', 'expected_output': 'A list of un-re-engaged contacts with a drafted, personalized follow-up for each.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "Write follow-ups for every contact I met last week that I haven't re-engaged.\n\nCompare my calendar attendees against my email and Dynamics 365 activity history to find who I've gone quiet on, then draft a personalized follow-up for each - grounded in what we discussed. Hold them as drafts for my review.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A list of un-re-engaged contacts with a drafted, personalized follow-up for each.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review.", 'example_request': "Draft follow-ups for everyone I met last week that I haven't circled back to yet.", 'inputs': [{'description': 'The meeting window to review, e.g. last week.', 'name': 'time_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to catch up on owed follow-ups from recent meetings and needs draft emails per contact, held for review rather than sent.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CatchUpOnFollowUpsIOwe(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnFollowUpsIOwe'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'time_period': {'description': 'The meeting window to review, e.g. last week.', 'type': 'string'}},
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
    print(CatchUpOnFollowUpsIOwe().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
