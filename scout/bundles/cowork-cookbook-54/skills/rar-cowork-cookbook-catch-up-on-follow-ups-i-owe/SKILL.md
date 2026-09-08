---
name: "rar-cowork-cookbook-catch-up-on-follow-ups-i-owe"
description: "Cross-references calendar attendees with email and Dynamics 365 activity history to identify contacts met recently who haven't been re-engaged, then drafts a personalized follow-up for each and holds them for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_follow_ups_i_owe", "rar_sha256": "8dff5b43009f4cf83bac27a39927c7bbeeaf9a574ecc359c0eaebf9fe11edf41", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
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
