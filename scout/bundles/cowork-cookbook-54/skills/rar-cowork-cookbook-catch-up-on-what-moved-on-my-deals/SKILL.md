---
name: "rar-cowork-cookbook-catch-up-on-what-moved-on-my-deals"
description: "Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_what_moved_on_my_deals", "rar_sha256": "769b58e6036bebeed070fc4d8aa68c74a515a855f4b03b6b5aba91687a292322", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_what_moved_on_my_deals`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_what_moved_on_my_deals_agent.py` and in the RCI capsule.

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

Catch up on what moved on my deals — Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet.

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
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals
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
    "number_of_deals": {
      "description": "How many top deals to cover (e.g. top 5).",
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
    "time_range": {
      "description": "Period of change to summarize, e.g. since last week.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_what_moved_on_my_deals_agent.py` and embedded as the fenced Python below (sha256 769b58e6036bebee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_what_moved_on_my_deals_agent.py` first:

```bash
python3 catch_up_on_what_moved_on_my_deals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_what_moved_on_my_deals_agent.py   # or on stdin
python3 catch_up_on_what_moved_on_my_deals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on what moved on my deals — Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet.

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
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_what_moved_on_my_deals',
    "version": '3.0.3',
    "display_name": 'Catch up on what moved on my deals',
    "description": 'Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet.',
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
        "upstream_slug": 'catch-up-on-what-moved-on-my-deals',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cc53967cc478a30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/catch-up-on-what-moved-on-my-deals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A per-deal change readout across your top opportunities, fusing CRM movement with communication signals.'], 'confidence': 1.0, 'deliverable': 'A per-deal change readout across your top opportunities, fusing CRM movement with communication signals.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'number_of_deals': 'How many top deals to cover (e.g. top 5).', 'time_range': 'Period of change to summarize, e.g. since last week.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Know what changed across your top deals without reading back through a week of threads. A per-deal change readout across your top opportunities, fusing CRM movement with communication signals.', 'expected_output': 'A per-deal change readout across your top opportunities, fusing CRM movement with communication signals.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "Summarize everything that's changed on my top 5 deals since last week.\n\nPull opportunity state from Dynamics 365 Sales and fuse it with my email, meeting, and Teams signals - what moved, what stalled, and where a customer went quiet. Give me a per-deal readout I can scan in two minutes.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A per-deal change readout across your top opportunities, fusing CRM movement with communication signals.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet.', 'example_request': "Summarize everything that's changed on my top 5 deals since last week.", 'inputs': [{'description': 'How many top deals to cover (e.g. top 5).', 'name': 'number_of_deals'}, {'description': 'Period of change to summarize, e.g. since last week.', 'name': 'time_range'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a seller wants to catch up on changes across their top deals over a recent period without rereading threads.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CatchUpOnWhatMovedOnMyDeals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnWhatMovedOnMyDeals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'number_of_deals': {'description': 'How many top deals to cover (e.g. top 5).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'time_range': {'description': 'Period of change to summarize, e.g. since last week.', 'type': 'string'}},
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
    print(CatchUpOnWhatMovedOnMyDeals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
