---
name: "rar-cowork-cookbook-map-an-account-strategy-on-a-miro-board"
description: "Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_an_account_strategy_on_a_miro_board", "rar_sha256": "aa47cf2ec553677f627d7881519ddb7e2e76b24417e8002aba8f4242f82a4908", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "miro"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_an_account_strategy_on_a_miro_board_agent.py` and embedded as the fenced Python below (sha256 aa47cf2ec553677f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_an_account_strategy_on_a_miro_board_agent.py` first:

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
    "version": '2.0.0',
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
