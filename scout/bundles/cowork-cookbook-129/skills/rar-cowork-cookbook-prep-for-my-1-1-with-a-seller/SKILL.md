---
name: "rar-cowork-cookbook-prep-for-my-1-1-with-a-seller"
description: "Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_my_1_1_with_a_seller", "rar_sha256": "325aea652399b6ceaf43f796c91d412ad302cdb1cd23cf51889cd27634f732fd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_my_1_1_with_a_seller`. The original RAPP
agent is preserved byte-for-byte in `prep_for_my_1_1_with_a_seller_agent.py` and in the RCI capsule.

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

Prep for my 1:1 with a seller — Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard.

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
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
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
    "seller_name": {
      "description": "Name of the seller whose book and 1:1 you are preparing for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_my_1_1_with_a_seller_agent.py` and embedded as the fenced Python below (sha256 325aea652399b6ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_my_1_1_with_a_seller_agent.py` first:

```bash
python3 prep_for_my_1_1_with_a_seller_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_my_1_1_with_a_seller_agent.py   # or on stdin
python3 prep_for_my_1_1_with_a_seller_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my 1:1 with a seller — Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard.

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
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_my_1_1_with_a_seller',
    "version": '3.0.3',
    "display_name": 'Prep for my 1:1 with a seller',
    "description": 'Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-my-1-1-with-a-seller',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-my-1-1-with-a-seller',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40346ffcb10c935c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-my-1-1-with-a-seller', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A structured 1:1 prep brief and an interactive coaching dashboard - showing pipeline, deal movement, win/loss trend, and a focused set of coaching themes ready to work through together.'], 'confidence': 1.0, 'deliverable': 'A structured 1:1 prep brief and an interactive coaching dashboard - showing pipeline, deal movement, win/loss trend, and a focused set of coaching themes ready to work through together.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'seller_name': 'Name of the seller whose book and 1:1 you are preparing for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Walk into every 1:1 with the full picture on your seller's book - and a coaching plan, not just talking points. A structured 1:1 prep brief and an interactive coaching dashboard - showing pipeline, deal movement, win/loss trend, and a focused set of coaching themes ready to work through together.", 'expected_output': 'A structured 1:1 prep brief and an interactive coaching dashboard - showing pipeline, deal movement, win/loss trend, and a focused set of coaching themes ready to work through together.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': 'Prepare me for my 1:1 with [Seller Name]. Pull their pipeline, recent deal movements, activity levels, and win/loss trends from Dynamics 365 Sales, and cross-reference recent emails and meetings for engagement signals.\n\nFirst, give me a structured brief: Where the book stands, the 2-3 deals worth focusing on, and coaching prompts I can raise.\n\nThen build an interactive HTML coaching dashboard I can walk through with them - current pipeline health, the deals that need attention, win/loss patterns, and a focused development theme for the next month.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A structured 1:1 prep brief and an interactive coaching dashboard - showing pipeline, deal movement, win/loss trend, and a focused set of coaching themes ready to work through together.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard.', 'example_request': 'Prep me for my 1:1 with Dana Reyes — pipeline, deal movement, win/loss, and a coaching dashboard.', 'inputs': [{'description': 'Name of the seller whose book and 1:1 you are preparing for.', 'name': 'seller_name'}], 'model': 'claude-opus-5', 'when_to_use': "Call before a manager's 1:1 with a seller when they need a full view of the seller's book plus coaching themes, not just talking points."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PrepForMy11WithASeller(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForMy11WithASeller'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'seller_name': {'description': 'Name of the seller whose book and 1:1 you are preparing for.', 'type': 'string'}},
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
    print(PrepForMy11WithASeller().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
