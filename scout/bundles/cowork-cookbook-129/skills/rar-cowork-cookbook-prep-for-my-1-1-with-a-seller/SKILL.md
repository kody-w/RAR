---
name: "rar-cowork-cookbook-prep-for-my-1-1-with-a-seller"
description: "Builds a 1:1 prep brief for a named seller from their Dynamics 365 Sales pipeline, deal movement, activity and win/loss trends plus email/meeting signals, then an interactive HTML coaching dashboard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_my_1_1_with_a_seller", "rar_sha256": "325aea652399b6ceaf43f796c91d412ad302cdb1cd23cf51889cd27634f732fd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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
