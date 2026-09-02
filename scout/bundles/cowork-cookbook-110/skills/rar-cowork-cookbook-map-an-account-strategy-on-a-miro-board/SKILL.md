---
name: "rar-cowork-cookbook-map-an-account-strategy-on-a-miro-board"
description: "Turn an account strategy conversation into a visual map the team can rally around - without spending an afternoon assembling it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_an_account_strategy_on_a_miro_board", "rar_sha256": "aa47cf2ec553677f627d7881519ddb7e2e76b24417e8002aba8f4242f82a4908", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "map_an_account_strategy_on_a_miro_board_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/map-an-account-strategy-on-a-miro-board:cf549e1e830cb73786d2a44c7f0e8b4f77aba39d25ec8930e2d6ded800d61705", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/map_an_account_strategy_on_a_miro_board`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `map_an_account_strategy_on_a_miro_board_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
