---
name: "rar-cowork-cookbook-map-an-account-strategy-on-a-miro-board"
description: "Builds a Miro account strategy board for a named customer by reviewing your recent emails, meetings, and CRM notes to map stakeholders, deal stages, initiatives, and priorities, plus a tracking table."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_an_account_strategy_on_a_miro_board", "rar_sha256": "dc55a6e8a40313301d3fe086859a991f0bd935bde3216411f147073435d24a1b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "miro"]}
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
