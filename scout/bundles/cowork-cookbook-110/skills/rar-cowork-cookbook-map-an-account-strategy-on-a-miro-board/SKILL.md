---
name: "rar-cowork-cookbook-map-an-account-strategy-on-a-miro-board"
description: "Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_an_account_strategy_on_a_miro_board", "rar_sha256": "dc55a6e8a40313301d3fe086859a991f0bd935bde3216411f147073435d24a1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/map_an_account_strategy_on_a_miro_board`. The original RAPP
agent is preserved byte-for-byte in `map_an_account_strategy_on_a_miro_board_agent.py` and in the RCI capsule.

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

Map an account strategy on a Miro board — Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table.

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
  Upstream entry : https://coworkcookbook.com/recipes/map-an-account-strategy-on-a-miro-board
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
    "customer_name": {
      "description": "The account or customer the strategy board is being built for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_an_account_strategy_on_a_miro_board_agent.py` and embedded as the fenced Python below (sha256 dc55a6e8a4031330…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_an_account_strategy_on_a_miro_board_agent.py` first:

```bash
python3 map_an_account_strategy_on_a_miro_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_an_account_strategy_on_a_miro_board_agent.py   # or on stdin
python3 map_an_account_strategy_on_a_miro_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map an account strategy on a Miro board — Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table.

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
  Upstream entry : https://coworkcookbook.com/recipes/map-an-account-strategy-on-a-miro-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/map_an_account_strategy_on_a_miro_board',
    "version": '3.0.3',
    "display_name": 'Map an account strategy on a Miro board',
    "description": 'Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'miro'],
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
        "upstream_slug": 'map-an-account-strategy-on-a-miro-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/map-an-account-strategy-on-a-miro-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4f840d6a74947e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/map-an-account-strategy-on-a-miro-board', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A Miro account strategy board - stakeholders, deal stages, key initiatives, and strategic priorities visualized in one place - paired with a tracking table the team can update as the strategy evolves.'], 'confidence': 1.0, 'deliverable': 'A Miro account strategy board - stakeholders, deal stages, key initiatives, and strategic priorities visualized in one place - paired with a tracking table the team can update as the strategy evolves.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The account or customer the strategy board is being built for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand. A Miro account strategy board - stakeholders, deal stages, key initiatives, and strategic priorities visualized in one place - paired with a tracking table the team can update as the strategy evolves.', 'expected_output': 'A Miro account strategy board - stakeholders, deal stages, key initiatives, and strategic priorities visualized in one place - paired with a tracking table the team can update as the strategy evolves.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': "I'm building out the account strategy for [Customer Name] and want to visualize it for the account team. Review my recent emails, meetings, and CRM notes to identify key stakeholders, deal stages, strategic priorities, and outstanding initiatives.\n\nThen build a Miro board that maps the account strategy as a structured framework - stakeholders, deals, initiatives, and priorities - with frames, shapes, and clear labels.\n\nAdd a tracking table beneath the map summarizing each initiative with owner, status, and next step.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Miro account strategy board - stakeholders, deal stages, key initiatives, and strategic priorities visualized in one place - paired with a tracking table the team can update as the strategy evolves.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table.', 'example_request': 'Map the account strategy for Contoso on a Miro board with a tracking table for the account team.', 'inputs': [{'description': 'The account or customer the strategy board is being built for.', 'name': 'customer_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need an account strategy for a specific customer visualized on a Miro board with an initiative tracking table for the account team.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class MapAnAccountStrategyOnAMiroBoard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapAnAccountStrategyOnAMiroBoard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The account or customer the strategy board is being built for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(MapAnAccountStrategyOnAMiroBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
