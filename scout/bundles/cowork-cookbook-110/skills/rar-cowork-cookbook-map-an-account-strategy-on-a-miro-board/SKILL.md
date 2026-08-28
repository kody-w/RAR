---
name: "rar-cowork-cookbook-map-an-account-strategy-on-a-miro-board"
description: "Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_an_account_strategy_on_a_miro_board", "rar_sha256": "027eb1298927352c1fd3f6569dcfedecf1b74c24890f73a439bdf2b0b1d0c4d7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "miro"]}
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

Map an account strategy on a Miro board — Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_an_account_strategy_on_a_miro_board_agent.py` and embedded as the fenced Python below (sha256 027eb1298927352c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_an_account_strategy_on_a_miro_board_agent.py` first:

```bash
python3 map_an_account_strategy_on_a_miro_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_an_account_strategy_on_a_miro_board_agent.py   # or on stdin
python3 map_an_account_strategy_on_a_miro_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map an account strategy on a Miro board — Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Map an account strategy on a Miro board',
    "description": 'Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fed772c3bd49b95d',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class MapAnAccountStrategyOnAMiroBoard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapAnAccountStrategyOnAMiroBoard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
