---
name: "rar-cowork-cookbook-stand-up-an-account-plan-board"
description: "Move from a scattered account plan to a structured working board the full account team can run against."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_an_account_plan_board", "rar_sha256": "b21eefb05b5ed5f1cb631b5ba79e0c2b8f179c1d0e46b6d1d23b0e49665946d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "monday_com"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_an_account_plan_board_agent.py` and embedded as the fenced Python below (sha256 b21eefb05b5ed5f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_an_account_plan_board_agent.py` first:

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
    "version": '2.0.0',
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
