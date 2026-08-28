---
name: "rar-cowork-cookbook-stand-up-an-account-plan-board"
description: "Move from a scattered account plan to a structured working board the full account team can run against."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_an_account_plan_board", "rar_sha256": "9882d87bfef631551b86c41c9571b269eaeed4b819186a650d46a60dda549210", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stand_up_an_account_plan_board`. The original RAPP
agent is preserved byte-for-byte in `stand_up_an_account_plan_board_agent.py` and in the RCI capsule.

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

Stand up an account plan board — Move from a scattered account plan to a structured working board the full account team can run against.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_an_account_plan_board_agent.py` and embedded as the fenced Python below (sha256 9882d87bfef63155…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_an_account_plan_board_agent.py` first:

```bash
python3 stand_up_an_account_plan_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_an_account_plan_board_agent.py   # or on stdin
python3 stand_up_an_account_plan_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up an account plan board — Move from a scattered account plan to a structured working board the full account team can run against.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_an_account_plan_board',
    "version": '2.0.1',
    "display_name": 'Stand up an account plan board',
    "description": 'Move from a scattered account plan to a structured working board the full account team can run against.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-an-account-plan-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-an-account-plan-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b54c1bf96f15e534',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stand-up-an-account-plan-board', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class StandUpAnAccountPlanBoard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpAnAccountPlanBoard'
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
    print(StandUpAnAccountPlanBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
