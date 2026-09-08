---
name: "rar-cowork-cookbook-catch-up-on-what-moved-on-my-deals"
description: "Returns a per-deal change readout for your top opportunities, combining Dynamics 365 Sales opportunity state with email, meeting, and Teams signals to show what moved, stalled, or went quiet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_what_moved_on_my_deals", "rar_sha256": "769b58e6036bebeed070fc4d8aa68c74a515a855f4b03b6b5aba91687a292322", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
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
